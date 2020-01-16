# Valida cpf

from validate_docbr import CPF
#CNH/ CNPJ/ CNS/ TITULO ELEITORAL

cpf = CPF()

#validar CPF
cpf.validate("012.345.678-90")  # True
cpf.validate("012.345.678-91")  # False


#Gerar novo documento
new_cpf_one = cpf.generate()  # "01234567890"
new_cpf_two = cpf.generate(True)  # "012.345.678-90"

#Mascara para documento
cpf_me = "01234567890"

# Mascara o CPF
cpf.mask(cpf_me)  # "012.345.678-90"