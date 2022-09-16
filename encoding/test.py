#  print(open('teste_win1252.txt', encoding='cp1252').read())
#  print(open('teste_win1252.txt', encoding='utf-8').read())
print(open('teste_win1252.txt', encoding=None).read()) # pega o encoding padrão da máquina
