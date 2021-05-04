import json


def hello(event, context):
    input=event['queryStringParameters']['type']
    if input==1:
        output=1
    else:
        output=2
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input":output
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response