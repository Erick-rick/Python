import requests

r = request.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=aaffd4776bf1eb6b3003b92c9a98ff2d5b129218')
print(r.response.content)

alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

mensagemCriptografada = ""

chave = input("Por favor, entre a chave: ")

chave = int (chave)

for char in mensagem:

    if char in alfabeto:

        posicao = alfabeto.find(char)

        novaPosicao = (posicao + chave) % 26

        mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]

    else:

        mensagemCriptografada = mensagemCriptografada + char

print("Sua mensagem criptografada é:" , mensagemCriptografada)