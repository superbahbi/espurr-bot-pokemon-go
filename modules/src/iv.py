from templates.text import TextTemplate
from pogoiv.iv_calculator import IvCalculator

def process(input, data ,sender):
    calc = IvCalculator()
    pogodata = data.split(' ')
    res = calc.get_ivs(pogodata[0], pogodata[1], pogodata[2], pogodata[3], pogodata[4])
    output = {
        'input': input,
        'output': TextTemplate(str(res)).get_message(),
        'success': True
    }
    return output
