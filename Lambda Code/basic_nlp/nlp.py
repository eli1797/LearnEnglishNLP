import boto3
import json

#get the comprehend service from amazon
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

def get_entities(text):

    print('Calling DetectEntities')
    json_reponse = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    print("JSON Response: " + str(json_reponse))
    
    py_dict = json.loads(json_reponse)
        
    to_return = text
    
    # print(py_dict)
    
    # overwrite the string 
    for ent in py_dict["Entities"]:
        # print("Ent: " + str(ent))
        substring = ent["Text"]
        # print(ent["Text"])
        to_return = to_return.replace(substring, substring.upper())
           
    return to_return
    
def get_syntax(text):
    
    print('Calling DetectSyntax')
    json_reponse = json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
    print("JSON Response: " + str(json_reponse))
    
    py_dict = json.loads(json_reponse)
        
    return_string = ""
    
    print(py_dict["SyntaxTokens"])
            
    for word in text.split():
        usedflag = False
        for cur in py_dict["SyntaxTokens"]:
            if word == cur["Text"] and (cur["PartOfSpeech"]["Tag"] == "NOUN" or cur["PartOfSpeech"]["Tag"] == "PROPN"):
                print(f'{word} is a Noun')
                return_string += word.upper() + " "
                usedflag = True
                break
        if not usedflag:
            return_string += word + " "
    
    return_string = return_string[:-1]
    
    return_dict = {
        'writeable': return_string,
        'syntax': py_dict["SyntaxTokens"]
    }

    
    print(return_dict)
    
    return return_dict
