#importando os módulos do chatbot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import os

import speech_recognition as sr

bot = ChatBot('Sexta-Feira')
bot.set_trainer(ListTrainer) #Definir treinamento

for _file in os.listdir('chats'): # percorrer todos os arquivos da pasta chats
    lines = open('chats/' + _file,'r').readlines() # ler linhas

    bot.train(lines)

"""
r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)

    while True:
        audio = r.listen(s)
        speech = r.recognize_google(audio, language = 'pt')

        print('Você disse: ', speech)
        print('Bot: ', bot.get_response(speech))"""