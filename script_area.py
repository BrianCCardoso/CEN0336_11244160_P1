import sys #importação do módulo sys para aquisição dos valores utilizados no script

#aquisicao dos valores do numero a e b 
num_a = sys.argv[1] 
num_b = sys.argv[2]

if len(sys.argv) != 3:
    print("Usage: <n1> <n2>")
    sys.exit(1)

if num_a.isdigit() and num_b.isdigit(): # o script verfica se os valores passados são compostos por apenas número
    num_a = int(num_a) #transforma o valor anteriormente do tipo str em int, caso a condicao seja verdadeira
    num_b = int(num_b)
    if num_a < 500 and num_b < 500: # verifica se ambos os número são menores que 500
        area = (num_a * num_b) / 2 # caso a condição seja verdadeira, realiza o cálculo da área
        print(f"A área do triângulo retângulo com lados a = {num_a} e b = {num_b} é {area} ")
    else:
        print("Os valores de ambos os catetos devem ser menor que 500") #caso os valores sejam maiores que 500, pede para rodar novamente o programa
else:
    print("Rode novamente o programa, os dados inseridos devem ser números inteiros <cateto a> <cateto b>") #pede para rodar novamente o programa caso não seja inserido números

