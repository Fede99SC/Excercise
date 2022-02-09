import requests

class WebRequestor:

    def write_file(self):
        r = requests.get("https://wwww.bing.com")
        with open("myfile.txt", 'w') as f:
            f.write(str(r.content))
