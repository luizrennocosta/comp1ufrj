#!/bin/bash

# select a random number from 1 to 100000
random_num=$((1 + RANDOM % 100000))

# create a folder with the random number as title
mkdir $random_num

# create a file named "read_me.txt" inside the folder and write some text into it
echo "Revele os arquivos escondidos usando 'ls -a'" > ./$random_num/read_me.txt

# write descriptions of the listed Linux commands in the "read_me.txt" file
echo "Aqui estão alguns comandos comuns do Linux e suas descrições:" >> ./$random_num/read_me.txt
echo "" >> ./$random_num/read_me.txt
echo "ls - lista o conteúdo do diretório" >> ./$random_num/read_me.txt
echo "cd - muda o diretório de trabalho atual" >> ./$random_num/read_me.txt
echo "pwd - imprime o diretório de trabalho atual" >> ./$random_num/read_me.txt
echo "man - exibe a página do manual para um comando" >> ./$random_num/read_me.txt
echo "cat - concatena e exibe arquivos" >> ./$random_num/read_me.txt
echo "vim - um poderoso editor de texto" >> ./$random_num/read_me.txt
echo "ssh - shell seguro, usado para login remoto em um servidor" >> ./$random_num/read_me.txt

# create a hidden file named "hidden.txt" inside the folder
echo "Use pwd para saber o diretório atual" > ./$random_num/.hidden.txt

# create the folder structure '04/04/2020'
mkdir -p "$random_num/.04/04/2020"

# download an image from a specific URL to the innermost folder
wget -q -P "$random_num/.04/04/2020/" https://raw.githubusercontent.com/luizrennocosta/comp1ufrj/main/lab/1/toriel.jpg

# print the randomly generated number on the screen
echo "O seu número gerado aleatoriamente é $random_num"