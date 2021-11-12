import pytest
import json
from src.transformation  import Transformation

test_data = {
    "attributes": [],
    "message": {
        "user": "Joshua",
        "age": 27
    }
}

json_object = json.dumps(test_data)

with open('data/test_string_int.json', 'w') as f:
    f.write(json_object)




@pytest.fixture
def transformer():
    """ Returns a Transformation object"""
    data = 'data/test_string_int.json'
    return Transformation(data)


def test_check(transformer):
    """  Test check method"""
    assert transformer.check() == ["String", "Integer"]
    
def test_tag(transformer):
    """ Test tag method"""
    assert transformer.tags() == ["user", "age"]

def test_descriptions(transformer):
    """ Test description method"""
    assert transformer.descriptions() == {
        'user': 'This contains information relating to user',
 'age': 'This contains information relating to age',
    }