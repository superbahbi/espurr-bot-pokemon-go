import config
import os
import requests
import sys
from src import *
from templates.text import TextTemplate

def search(input, sender):
    intent, entities = process_query(input)
    if intent is not None:
        data = sys.modules['modules.src.' + intent].process(input, entities, sender)
        if data['success']:
            return data['output']
        else:
            if 'error_msg' in data:
                return data['error_msg']
            else:
                return TextTemplate('Something didn\'t work as expected! I\'ll report this to my master.').get_message()
    else:
        return TextTemplate('I\'m sorry; I\'m not sure I understand what you\'re trying to say sir.\nTry typing "help" or "request"').get_message()