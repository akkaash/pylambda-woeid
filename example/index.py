"""
API handler module
"""
import json
import os
import logging
import requests


WORLDWIDE_RESPONSE_BODY = {'woeid': 1}
RESPONSE_HEADERS = {'Content-Type': 'application/json'}
WORLDWIDE_RESPONSE = {
    'statusCode': 200,
    'body': json.dumps(WORLDWIDE_RESPONSE_BODY),
    'headers': RESPONSE_HEADERS
}


def make_api_call(query):
    """
    Builds api object
    """
    base_url = "https://query.yahooapis.com/v1/public/yql"
    params = {'q': query, 'format': 'json'}
    req = requests.get(url=base_url, params=params)
    return req.json()


def get_woeid(city, country_code):
    """
    query Yahoo and get WOEID
    """
    query = 'select woeid from geo.places where text="%s" and placeTypeName.code=7' % (city)
    if country_code is not None:
        query += ' and country.code="%s"' % (country_code)
    api_response = make_api_call(query)
    response_count = api_response['query']['count']
    if response_count > 1:
        return api_response['query']['results']['place'][0]['woeid'] # get the first response
    elif response_count == 1:
        return api_response['query']['results']['place']['woeid']


def handler(event, context):
    """base handler for api request"""
    query_string_parameters = event['queryStringParameters']
    city = None
    country_code = None

    if 'city' in query_string_parameters:
        city = query_string_parameters['city']
    else:
        return WORLDWIDE_RESPONSE

    if 'countryCode' in query_string_parameters:
        country_code = query_string_parameters['countryCode']
    else:
        country_code = 'US'

    body = None

    try:
        woeid = get_woeid(city, country_code)
        body = {'woeid': woeid}
    except Exception as e:
        body = WORLDWIDE_RESPONSE_BODY
    if body is None:
        body = WORLDWIDE_RESPONSE_BODY
    
    return {'statusCode': 200,
            'body': json.dumps(body),
            'headers': RESPONSE_HEADERS}
