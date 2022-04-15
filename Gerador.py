import random

print("Gerador de Senhas")

caract = 'abcdefgihjklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ1234567890!@#$%¨&*()-=_+'

qtSenhas = int(input('Quantas senhas serão geradas? '))
qtDigitos = int(input('Quantos caracteres em cada senha? '))

print('\nSenhas Geradas: ')

for pwd in range(qtSenhas):
    senhas = ''
    for c in range(qtDigitos):
        senhas += random.choice(caract)
    print(senhas)
