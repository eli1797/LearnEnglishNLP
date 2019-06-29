import boto3
import json
import nlp



def lambda_handler(event, context):
    
    #Log and view the JSON event
    print('event:' + json.dumps(event))
    
    to_return = "Failed to processes text"
    
    #get the comprehend service from amazon
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    #extract the text from the event
    text = "It is raining today in Seattle"

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
        print("Failure to parse JSON for text")
        print(e)

    #process the text with the appropriate nlp type
    if type == "noun":
        to_return = nlp.get_syntax(text)
    else:
        to_return = nlp.get_entities(text)
    
    print("To Return: " + to_return)
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin" : "*", 
            "Access-Control-Allow-Credentials" : True
        },
        'body': json.dumps(to_return)
    }

