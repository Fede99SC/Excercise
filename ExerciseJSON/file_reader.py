import random, json

class FileReader:

    @staticmethod
    def read_json():
        with open('jsontest.json') as j:
            data = json.load(j)
        return data

    def add_humidity(self,data):
        humidity = random.randint(0, 200)
        with open('jsontest.json', 'w') as j:
            dictiornary = {"NAME": data.get("NAME"), "TEMPERATURE": data.get("TEMPERATURE"),
                           "HUMIDITY": humidity}
            j.write(json.dumps(dictiornary))

    def check_temperature(self):
        data = self.read_json()
        if data.get('TEMPERATURE') > 10:
            self.add_humidity(self, data)
        else:
            print("The Temperature isn't > 10")