import re  # regular expression - RegEx

address = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'


# 5 dígitos + hífen (opcional) + 3 dígitos

expression = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
search = expression.search(address)  # match
if search:
    cep = search.group()
    print(cep)
