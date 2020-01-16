import pycep_correios

meu_cep = '37.503-003'

if pycep_correios.validar_cep(meu_cep):
    print('O CEP %s é valido!' %meu_cep)
else:
    print('CEP %s não é valido!'%meu_cep)


##Formatar CEP
'''from pycep_correios import formatar_cep

meu_cep = '37.503-003'

try:
    cep_formatado = formatar_cep(meu_cep)
    print('O CEP %s formatado : %s' %(meu_cep, cep_formatado))
except ValueError as exc:
    print('Erro ao formatar CEP')'''