import random

def data():
    dzien = random.randint(1, 30)
    miesiac = random.randint(1,12)
    rok = random.randint(2025,2027)
    if dzien < 10:
        dzien = '0' + str(dzien)
    if miesiac < 10:
        miesiac = '0' + str(miesiac)
    return f'{dzien}.{miesiac},{rok}'

