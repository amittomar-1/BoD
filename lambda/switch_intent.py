

import time
import logging
import json
import bibot_helpers as helpers
import bibot_userexits as userexits
import count_intent
import top_intent

#
# See additional configuration parameters at bottom 
#

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def lambda_handler(event, context):
    logger.debug('<<BIBot>> Lex event info = ' + json.dumps(event))

    session_attributes = event['sessionAttributes']
    logger.debug('<<BIBot>> lambda_handler: session_attributes = ' + json.dumps(session_attributes))

    config_error = helpers.get_bibot_config()
    if config_error is not None:
        return helpers.close(session_attributes, 'Fulfilled',
            {'contentType': 'PlainText', 'content': config_error})   
    else:
        return switch_intent_handler(event, session_attributes)


def switch_intent_handler(intent_request, session_attributes):
    session_attributes['greetingCount'] = '0'
    session_attributes['resetCount'] = '0'
    session_attributes['finishedCount'] = '0'
    # note: do not alter session_attributes['lastIntent'] here

    if session_attributes.get('lastIntent', None) is not None:
        intent_name = session_attributes['lastIntent']
        if INTENT_CONFIG.get(intent_name, False):
            logger.debug('<<BIBot>> switch_intent_handler: session_attributes = ' + json.dumps(session_attributes))
            logger.debug('<<BIBot>> switch_intent_handler: refirecting to ' + intent_name)
            return INTENT_CONFIG[intent_name]['handler'](intent_request, session_attributes)    # dispatch to the event handler
        else:
            return helpers.close(session_attributes, 'Fulfilled',
                {'contentType': 'PlainText', 'content': 'Sorry, I don\'t support the intent called "' + intent_name + '".'})
    else:
        return helpers.close(session_attributes, 'Fulfilled',
            {'contentType': 'PlainText', 'content': 'Sorry, I\'m not sure what you\'re asking me.'})


INTENT_CONFIG = {
    'Top_Intent':       {'handler': top_intent.top_intent_handler},
    'Count_Intent':     {'handler': count_intent.count_intent_handler}
}

