
import logging
import json
import bibot_helpers as helpers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    logger.debug('<<BIBot>> Lex event info = ' + json.dumps(event))

    session_attributes = event['sessionAttributes']

    if session_attributes is None:
        session_attributes = {}

    logger.debug('<<BIBot>> lambda_handler: session_attributes = ' + json.dumps(session_attributes))

    return hello_intent_handler(event, session_attributes)


def hello_intent_handler(intent_request, session_attributes):
    session_attributes['resetCount'] = '0'
    session_attributes['finishedCount'] = '0'
    # don't alter session_attributes['lastIntent'], let BIBot remember the last used intent

    askCount = helpers.increment_counter(session_attributes, 'greetingCount')
    
    # build response string
    if askCount == 1: response_string = "Hello! How can I help?"
    elif askCount == 2: response_string = "I'm here"
    elif askCount == 3: response_string = "I'm listening"
    elif askCount == 4: response_string = "Yes?"
    elif askCount == 5: response_string = "Really?"
    else: response_string = 'Ok'

    return helpers.close(session_attributes, 'Fulfilled', {'contentType': 'PlainText','content': response_string})   

