import json
import datetime
import logging


def handler(event, context):
    queryStringParameters = event['queryStringParameters']
    print(queryStringParameters)
    if (queryStringParameters is None):
        return {
            'statusCode': 500
        }
    return {'statusCode': 200,
            'body': json.dumps(queryStringParameters),
            'headers': {'Content-Type': 'application/json'}}
