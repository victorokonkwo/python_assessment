import pytest
import json
from src.transformation  import Transformation

test_data = {
    "attributes": [],
    "message": {
        "user": "Apamieye",
        "cities_visited":[
            "Abuja",
            "Lagos",
            "Port Harcourt"
        ]
    }
}

json_object = json.dumps(test_data)

with open('data/test_data_array.json', 'w') as f:
    f.write(json_object)



@pytest.fixture
def transformer():
    """ Returns a Transformation object"""
    data = 'data/test_data_array.json'
    return Transformation(data)

def test_check(transformer):
    """  Test check method for string_list"""
    assert transformer.check() == ["String", "Enum"]
    
def test_tag(transformer):
    """ Test tag in string_list """
    assert transformer.tags() == ["user", "cities_visited"]

def test_descriptions(transformer):
    """ Test descriptions in string_list"""
    assert transformer.descriptions() == {
        'user': 'This contains information relating to user',
 'cities_visited': 'This contains information relating to cities_visited',
    }





