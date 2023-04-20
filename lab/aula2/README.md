#

Olá! O conteúdo da segunda aula é uma continuação da aula1, onde o principal foco é a familiarização com o terminal e Linux-based OSes.

# Objetivo
    - Familiarização do aluno com Linux
      - Interação com arquivos e pastas
      - ssh
        - Chave publica/privada 
      - vim
    - Arquivos de configuração
      - .bashrc
      - .ssh/config
      - .ssh/authorized_keys

------------------------
# Roteiro

1. acessar o servidor com a conta de teste para ssh `ssh-teste-123`
2. criar um arquivo com o nome do seu usuário (ex: luiz.renno)-> isso vai ser usado para criar sua conta no servidor do lipe
3. depois da conta estar criada, acesse e redefina a senha **imediatamente** (comando `passwd`) 
4. volte para sua maquina local, fora do servidor, e crie seu par de chaves ssh
5. coloque sua chave publica no servidor no arquivo `~/.ssh/authorized_keys`
6. em sua maquina local, edite o arquivo `~/.ssh/config` e coloque configurações de acesso ao servidor do lipe (hint: arquivo `/home/readme` no servidor)
------------------------


## Comandos usados:
- **ls**: O comando ls é utilizado para listar os arquivos e diretórios presentes no diretório atual ou em um diretório especificado. Por exemplo, o comando "ls" lista os arquivos e diretórios presentes no diretório atual e o comando "ls /pasta" lista os arquivos e diretórios presentes na pasta "pasta".

- **cd**: O comando cd é utilizado para mudar de diretório no sistema. Por exemplo, o comando "cd pasta" muda o diretório atual para a pasta "pasta" e o comando "cd .." volta um nível no diretório atual.

- **mkdir**: O comando mkdir é utilizado para criar novos diretórios no sistema. Por exemplo, o comando "mkdir pasta" cria uma nova pasta chamada "pasta" no diretório atual. Se for necessário criar diretórios aninhados, é possível utilizar a opção "-p". Por exemplo, o comando "mkdir -p pasta/subpasta" cria uma pasta "pasta" e uma subpasta "subpasta" dentro dela.

- **vim**: O comando vim é um editor de texto avançado que é frequentemente utilizado por programadores e desenvolvedores. Ele é capaz de editar arquivos de texto de qualquer tamanho e possui recursos como destaque de sintaxe, autocompletar e busca e substituição. Para editar um arquivo com o vim, basta digitar "vim nome_do_arquivo" no terminal.

- **ssh**: O comando ssh é utilizado para conectar-se a um servidor remoto de forma segura. Ele é frequentemente utilizado por administradores de sistemas e desenvolvedores para acessar servidores e executar tarefas remotamente. Por exemplo, o comando "ssh usuario@servidor.com" conecta-se ao servidor "servidor.com" com o nome de usuário "usuario".


# Próxima Aula

Para a próxima aula, veremos padrões de projetos de código, como organizar seu código tanto dentro do arquivo quanto fora, regras de CleanCode e boas práticas de programação para um código mais limpo, legível e reproduzível.

Um exemplo para os interessados: https://raw.githubusercontent.com/ioccc-src/winner/master/2013/cable2/cable2.c