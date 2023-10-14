#Mostra a pasta atual que o usuário está
echo "Diretório atual"
pwd

#Gera uma lista detalhada do diretório home e imprime no arquivo lista_Home.txt
ls -l "$HOME" > lista_HOME.txt

#Imprime a data no momento
echo "Data atual:"
date