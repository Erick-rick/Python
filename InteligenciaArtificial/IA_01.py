import iaml
import os

#inicialização
ai = iaml.Kernel()

#abre o arquivo principal da AIML(que faz referencias aos outros)
ai.learn('std-startup.xml')

#faz com que os outros arquivos da AIml sejam carregados
ai.respond('load aiml b')

while (1==1):
    frase = raw_input('Fale algo em ingles:')
    print("Bot : %s"%ai.respond(frase))
