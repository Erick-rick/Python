largura= float(input( 'Largura da parede :'))
altura = float(input( 'Altura da parede :'))

area = largura * altura
tinta = area/2

print('A parede tem a dimensão de {}x{}, sua área é de {:.2f}m2 \n Para pintar a parede precisará de {}L de tinta.'.format(largura, altura, area, tinta))


