""" r+ (aberto para leitura e escrita) """
file = open('teste.txt', 'r+')

print(file.read())
file.write('Olá jovens')
