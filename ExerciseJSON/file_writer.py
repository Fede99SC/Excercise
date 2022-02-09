import uuid, json

class FileWriter:

    @staticmethod
    def write_json():
        with open("myfile.json", 'w') as myfile:
            myjson = {"ID": str(uuid.uuid4())}
            myfile.write(json.dumps(myjson))
