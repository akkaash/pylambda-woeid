import json
import datetime
import logging


def handler(event, context):
    logging.info(event)
    logging.info(context)
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(event),
            'headers': {'Content-Type': 'application/json'}}
