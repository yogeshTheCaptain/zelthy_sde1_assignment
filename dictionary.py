import requests

class Dictionary:

    def __init__(self):

        self.word           = input("Word?")
        self.dictionaryDict = {}
        
        
    def getWordMeaning(self):

        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + self.word

        response = requests.request("GET",url )
        r1 = response.json()
        
        
        
        if type(r1) is dict:
            print(r1.get("title"))

        else:

            for i in r1[0]["meanings"] :
                self.dictionaryDict[i['partOfSpeech']] = i['definitions'][0]['definition']


        if self.dictionaryDict.get('noun'):
            print(self.word.capitalize()+". Noun. "+self.dictionaryDict['noun'])
            
        elif self.dictionaryDict.get('transitive verb'):
            print(self.word.capitalize()+". Transitive Verb. "+self.dictionaryDict['transitive verb'])
            
        elif self.dictionaryDict.get('adjective'):
            print(self.word.capitalize()+". Adjective. "+self.dictionaryDict['adjective'])
            
if __name__ == "__main__":


    dict1 = Dictionary()

    dict1.getWordMeaning()