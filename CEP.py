import pycep_correios
from pycep_correios
from pycep_correios.exceao import CEPInvalido

cep = int(input('Digite seu CEP (sem -) :'))

endereco = pycep_correios.consultar_cep(cep)

try:
   #cep = '00000000'
   endereco = pycep_correios.consultar_cep('000000000')

except CEPInvalido as exc:
    print(exc)

print(endereco['end', 'bairro', 'cidade', 'uf', 'cep'] )