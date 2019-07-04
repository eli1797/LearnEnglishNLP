import json
import nlu

def lambda_handler(event, context):
    
    #Log and view the JSON event
    print('event:' + json.dumps(event))
    
    to_return = "Failed to processes text"

    #extract the text from the json event
    text = ''
    try:
        text = event['queryStringParameters']['text']
    except Exception as e:
        print("Failure to parse JSON for text")
        print(e)
    
    #extract the nlp type the user wants from the event
    type = "noun"
        
    try:
        type = event['queryStringParameters']['type']
    except Exception as e:
        print("Failure to parse JSON for type")
        print(e)

    #process the text with the appropriate nlp type
    if type == "noun":
        to_return = nlu.get_syntax(text)
    else:
        to_return = nlu.get_entities(text)
    
    
    
    print("To Return: " + str(to_return))
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin" : "*", 
            "Access-Control-Allow-Credentials" : True
        },
        'body': json.dumps(to_return)
    }
 