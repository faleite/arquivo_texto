from string import ascii_letters

file = open('teste.txt', 'a')

#  file.write('Continuando o arquivo')
#  file.writelines('\nContinuando o arquivo')

for x in ascii_letters:
    #  file.writelines(x)
    #  file.write(x)
    file.write('\n{}'.format(x))
