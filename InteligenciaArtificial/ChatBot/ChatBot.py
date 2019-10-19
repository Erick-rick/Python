from chatterbot.treiners import ListTrainer

from chatterbot import ChatBot
from chatterbot import corpus


bot = ChatBot('T bot')

conversa =['Oi', 'Ola', 'Tudo bem?', 'Tudo ótimo', 'Como você esta?' ,'Bem e você?']

bot.set_Trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta= input('User :')
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence)> 0.5:
        print('T Bot: ', resposta)
    else:
        print('T Bot: ainda não sei responder esta pergunta')