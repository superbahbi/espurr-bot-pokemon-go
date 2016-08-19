from templates.text import TextTemplate


def process(input, data ,sender):
    output = {
        'input': input,
        'output': TextTemplate(data).get_message(),
        'success': True
    }
    return output
