import spacy
import json

# Load the small English model
nlp = spacy.load('/opt/en_core_web_sm-2.1.0')

def get_entities(text):

    print('Calling DetectEntities')
    return_string = ""
    
    #evaulate the text
    doc = nlp(text)
    
    for token in doc:
        # print(token.text, token.ent_type)
        if token.ent_type != 0:
            return_string += token.text.upper() + " "
        else:
            return_string += token.text + " "
    
    return_string = return_string[:-1]
    
    return_dict = {
        'writeable': return_string,
        'syntax': doc.to_json()
    }

    print(return_dict)
    
    return return_dict
    
def get_syntax(text):
    
    print('Calling DetectSyntax')
    return_string = ""
    
    #evaluate the text
    doc = nlp(text)
    
    #iterate over the tokens for the nouns
    for token in doc:
        # Print the text and the predicted part-of-speech tag
        # print(token.text, token.pos_)
        
        if (token.pos_ == "NOUN"):
            # print(token.text)
            return_string += token.text.upper() + " "
        else:
            return_string += token.text + " "
        
    return_string = return_string[:-1]
    
    return_dict = {
        'writeable': return_string,
        'syntax': doc.to_json()
    }

    print(return_dict)
    
    return return_dict