# This transformation script transforms the json data 
# and transforms it to a designed schema pattern.

import json

class Transformation:
    """ Transformation class information.
    This class handles actions performed by a student.
    This class handles actions performed on a json dataset and then
    it maps the data to a desired schema.
    The possible pipeline steps includes loading the data, checking and mapping relevalant data structures,
    padding the tags and descriptions, and lastly saving the file
    Once it has been mapped, it is saved as a new json file in a schema folder.

    Usage:

    data = {
        {
            "attributes": [],
            "message": {
                "user_name" : "Ali",
                "school_attended" : ["Uniport", "FUTO] 
            }
        }
    }

    import transformation

    transformer = transformation.Transformation(data)
    transformer.check()

    >>> ['Enum', 'String']

    transformer.tags()

    >>> ["user_name", "school_attended"]

    transformer.save("data.json")

    """

    def __init__(self, file_path):
        self.data = file_path

    def load_data(self):
        """Load json data.
        
        Load the json data and processes the data so as to return a list of the data for further preprocessing

        :return: List of attributes and values

        :rtype: List
        
        """
        with open(self.data) as file:
            data_file = json.load(file)
            new_file = []

            for key in data_file:
                if key == 'message':            # filter the message key of the json data.
                    new_file.append(data_file[key]) # extract all the json data of the key "message".


            file.close()  

        self.attributes = [attr for attr in new_file[0]]  # filter the attributes and assign it to a list
        
        return new_file          # returns extracted message attributes

    
    def check(self):
        """ Checks the data structures.
        
        Checks the data structures and map the data stucture where appropriate.
        
        :return: List of mapped data structure

        :rtype: List
        """

        check = []
        new_data = self.load_data()[0]           # load json data
        for attr in new_data :
            if isinstance(new_data[attr], str):             
                check.append('String')
            elif isinstance(new_data[attr], bool):
                check.append('Boolean')
            elif isinstance(new_data[attr], dict):
                check.append('Object')

            elif isinstance(new_data[attr], int):
                check.append('Integer')

            elif isinstance(new_data[attr], list):
                if new_data[attr]:                               # if attributes is not empty
                
                    if isinstance(new_data[attr][0], str):
                        check.append('Enum')                    # store it as enum
                        
                    elif isinstance(new_data[attr][0], dict):
                        check.append('Array')   
                else:                                           # if attributes is empty store it as List
                    check.append('List')

            else:
                pass

        return check
    
    def tags(self):

        """ Filter tags.
        
        Filter tags from the json data which are the attributes and map appropriately.


        :return: List of tags

        :rtype: List
        """
        tags = []
        new_data = self.load_data()[0]
        for attr in new_data:
            if isinstance(new_data[attr], dict):                  # if attributes data is a dictionary
                tags.append(list(new_data[attr].keys()))          # extract all the attributes and store it in the tags variable

            else:
                tags.append(attr)                                 # else store only the attributes name

        return tags


    def descriptions(self):
        
        """ Construct Descriptions.

        Design descriptions from tags and json attributes respectively.

        return: a dictionary of tags and their relevant descriptions
        
        rtype: dict
        """

        tags = self.tags()
        descriptions = {}
        for describe, tag in zip(self.attributes, tags):   # map attributes and tags
            if isinstance(tag, list):
                descriptions[describe] = f'This contains information relating to {describe} and it has the following attributes: {tag}'  
            else:
                descriptions[describe] = f'This contains information relating to {describe}'

        return descriptions   # description explaining what is in the tags/attributes

    
    def save(self, file_name):
        """ Saving Files.

        Saving Files as json data.

        param file_name: the path to save the file with the file name.

        :type file_name: str
        
        :return: Saves the file with the file name provided
        
        :rtype: file object
        """

        file = {}
        data = self.load_data()[0]
        for i, attr in enumerate(self.attributes):               # Design file schema using type, tags, descriptions and required
            file[attr] = {"type": self.check()[i],
                          "tag": self.tags()[i],
                          "description": self.descriptions()[attr],
                          "required": False}
        
        json_object = json.dumps(file, indent = 4)   # Dump file data as a json object with indentation

        with open(file_name, 'w') as file:
            file.write(json_object)                  # Open and write json object as a json file passing in the desired file_path.

        return file




