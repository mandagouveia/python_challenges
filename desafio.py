import argparse

#Sessão que cria os parâmetros e atribui as ações a cada um deles
parser = argparse.ArgumentParser(description='Criando e manipulando o arquivo .txt')
parser.add_argument('-l','--criararquivo', help='Cria arquivo .txt', action='store_true')
parser.add_argument('-t','--inserirtexto', type=str, help='Adiciona texto ao arquivo')
parser.add_argument('-d', '--inserirnum', type=int, help='Insere número ao arquivo')
args = parser.parse_args()

#Texto padrão do arquivo
texto = ['Os números abaixo serão multiplicados pelo valor repassado via parâmetro -d:', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Criando o arquivo .txt
if args.criararquivo: 
    with open('desafiopython.txt', 'w', encoding='utf-8') as arquivo:
        for valor in texto:
            arquivo.write(str(valor) + '\n')

#Inserindo texto no arquivo .txt
if args.inserirtexto:
    with open('desafiopython.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
    with open('desafiopython.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.writelines(args.inserirtexto + '\n')
        arquivo.writelines(conteudo[1:11])

#Inserindo número no arquivo .txt
if args.inserirnum:
    with open('desafiopython.txt', 'r', encoding='utf-8') as arquivo:
        conteudo2 = arquivo.readlines()
    with open('desafiopython.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(conteudo2[0])
        for count in range(10):
            arquivo.writelines("%d x %d = %d \n" %(count, args.inserirnum, args.inserirnum*(count)))
