import config
import os
import requests
import sys
from src import *
from templates.text import TextTemplate


def search(input, data, sender):
    data = sys.modules['modules.src.' + input].process(input, data, sender)
    if data['success']:
        return data['output']
    else:
        if 'error_msg' in data:
            return data['error_msg']
        else:
            return TextTemplate('Something didn\'t work as expected! I\'ll report this to my master.').get_message()