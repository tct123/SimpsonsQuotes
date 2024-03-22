import requests
class Wrapper:
    def __init__(self):
        self.url = "https://thesimpsonsquoteapi.glitch.me/quotes"
    def getdata(self):
        r = requests.get(url=self.url)
        erg = r.json()[0]
        return erg
if __name__=="__main__":
    k = Wrapper()
    print(k.getdata()["quote"])