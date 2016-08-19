from templates.text import TextTemplate


def process(input, sender):
    help = '''Hi %s! I'm Espurr, your personal assistant.\nTell me things like the following:\n
  - define a superhero\n  - iron man 2 movie plot\n  - tell me a joke\n  - wiki html\n  - anything you want book\n  - random quote\n  - usd to eur rate\n
I'm always learning, so do come back and say hi from time to time!\nHave a nice day.''' % (sender)
    help += '\nTell me things like:'
    help += '\n  - define comfort'
    help += '\n  - iron man 2 movie plot'
    help += '\n  - tell me a joke/quote/fact'
    help += '\n  - wiki html'
    help += '\n  - anything you want book'
    help += '\n  - usd to eur rate'
    help += '\n  - death note anime'
    help += '\n  - time in seattle'
    help += '\n  - songs by linkin park'
    help += '\n  - shorten google.com'
    help += '\n  - weather in london'
    help += '\n  - videos of sia'
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
