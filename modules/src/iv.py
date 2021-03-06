from templates.text import TextTemplate
from pogoiv.iv_calculator import IvCalculator

def process(input, data ,sender):
    calc = IvCalculator()
    if data is not None:
        pogodata = data.split(' ')
        res = calc.get_ivs(pogodata[1].encode("utf-8"), pogodata[2].encode("utf-8"), pogodata[3].encode("utf-8"), pogodata[4].encode("utf-8"), pogodata[5].encode("utf-8"))
    else:
        res = "Invalid data input!\n"
        res += "e.g check \"Chansey\" 285 271 1900 False"
    output = {
        'input': input,
        'output': TextTemplate(str(res)).get_message(),
        'success': True
    }
    return output
