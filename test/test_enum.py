import pytest
import json
from src.transformation  import Transformation

test_data = {
    "attributes": [],
    "message": {
        "cities_visited":[
            "Abuja",
            "Lagos",
            "Port Harcourt"
        ],
        "countries_visited": [{
            "France": ["Paris"],
            "USA": ["Texas", "California", "Washington"],
            "Nigeria": ["Abuja", "Kano", "Ibadan"]
        }],

        "childrens_age": []
    }
}


json_object = json.dumps(test_data)

with open('data/test_enum.json', 'w') as f:
    f.write(json_object)

@pytest.fixture
def transformer():
    """ Returns a Transformation object"""

    data = 'data/test_enum.json'
    return Transformation(data)


def test_check(transformer):
    """ Test check method"""
    assert transformer.check() == ["Enum", "Array", "List"]
    
def test_tag(transformer):
    """ Test tag method"""
    assert transformer.tags() == ["cities_visited", "countries_visited", "childrens_age"]

def test_descriptions(transformer):
    """ Test descriptions method"""
    assert transformer.descriptions() == {
        "cities_visited": 'This contains information relating to cities_visited',
        "countries_visited": 'This contains information relating to countries_visited',
        "childrens_age": 'This contains information relating to childrens_age'
    }

