from templates.text import TextTemplate
from pogoiv.iv_calculator import IvCalculator

def process(input, data ,sender):
    calc = IvCalculator()
    res = calc.get_ivs("Chansey", "285", "271", "1900", powered=False):
    output = {
        'input': input,
        'output': TextTemplate(res).get_message(),
        'success': True
    }
    return output
