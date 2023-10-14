#importacao do módulo sys
import sys 

#chamada de variaveis
sequencia = sys.argv[1].upper()
num_1 = sys.argv[2]
num_2 = sys.argv[3]
num_3 = sys.argv[4]
num_4 = sys.argv[5]
num_5 = sys.argv[6]
num_6 = sys.argv[7]

#criacao de uma lista para verificacao se a string passada pelo usuario é somente de bases nitrogenadas
lista_bases_nitrogenadas = ["A","T","C","G"]

#verifica se foi passado o número de argumentos corretos
if len(sys.argv) != 8:
    print("Usage: <DNA> <n1> <n2> <n3> <n4> <n5> <n6>")
    sys.exit(1)

#verifica se a sequencia é formada apenas por bases nitrogenadas
for i in set(sequencia):
    if i not in lista_bases_nitrogenadas:
        print("Você deve passar uma sequencia de DNA!")
        sys.exit(1)

#verifica se os argumentos passados são numericos e os transforma para o tipo inteiro
if num_1.isdigit() and num_2.isdigit() and num_3.isdigit() and num_4.isdigit() and num_5.isdigit() and num_6.isdigit() :
    num_1, num_2, num_3, num_4, num_5, num_6 = int(num_1), int(num_2), int(num_3), int(num_4), int(num_5), int(num_6)
else:
    print("Você deve digitar apenas números inteiros")
    sys.exit(1)


#verifica se os numeros passados estão dentro dos ranges certos
if num_1 < 1 or num_2 > len(sequencia) or num_3 < 1 or num_4 > len(sequencia) or num_5 < 1 or num_6 > len(sequencia):
    print("Os números n1, n2, n3, n4, n5 e n6 estão fora dos limites da sequência de DNA.")
    sys.exit(1)


#extrai a primeira sequencia entre os codons 1 e 2
extracao_1 = sequencia[num_2 : num_3 - 1]

#extrai a segunda sequencia entre os codons 3 e 4
extracao_2 = sequencia[num_4 : num_5 - 1]

#faz a extracao dos 3 codons
cds_1 = sequencia[num_1 - 1 : num_2]
cds_2 = sequencia[num_3 - 1 : num_4]
cds_3 = sequencia[num_5 - 1 : num_6]

#exibe na saida a concatenacao dos 3 codons caso as exigencias forem feitas
if extracao_1.startswith("GT") and extracao_1.endswith("AG") and extracao_2.startswith("GT") and extracao_2.endswith("AG"):
    print(cds_1 + cds_2 + cds_3)