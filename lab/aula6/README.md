# Notas da Aula sobre Git

## Introdução ao Git

O Git é um sistema de controle de versão distribuído usado para rastrear mudanças em arquivos e coordenar o trabalho entre várias pessoas. Ele permite que desenvolvedores trabalhem em um projeto simultaneamente e mesclam suas alterações de forma eficiente. O Git é amplamente utilizado na indústria de desenvolvimento de software e se tornou uma habilidade essencial para os desenvolvedores.

Existem muitos recursos no GitHub para o aprendizado do Git no geral, e da plataforma do Github. Alguns links relevantes:

-  https://github.com/skills/introduction-to-github#welcome
- [Cheat Sheet](https://training.github.com/downloads/github-git-cheat-sheet.pdf)
- [Interactive Cheat Sheet](https://ndpsoftware.com/git-cheatsheet.html#loc=index;)
## Conceitos Básicos

- **Repositório**: Um repositório é uma coleção de arquivos e seu histórico. Pode ser local ou remoto (em um servidor).

- **Commit**: Um commit representa uma imagem instantânea de um repositório em um ponto específico no tempo. Ele registra as alterações feitas nos arquivos.

- **Branch**: Um branch é uma linha separada de desenvolvimento dentro de um repositório. Ele permite o trabalho paralelo em diferentes recursos ou correções de bugs.

- **Merge**: O merge combina as alterações de diferentes branches em um único branch.

- **Remote**: Um remote é um repositório armazenado em um servidor ou localização diferente. Ele permite a colaboração entre vários desenvolvedores.

## Configurando o Git

1. Instalar o Git: Baixe e instale o Git a partir do site oficial (https://git-scm.com) com base no seu sistema operacional.

2. Configurar o Git:
   - Definir seu nome: `git config --global user.name "Seu Nome"`
   - Definir seu email: `git config --global user.email "seu.email@exemplo.com"`

## Comandos Básicos do Git

1. `git init`: Inicializa um novo repositório Git no diretório atual.

2. `git clone \<url-do-repositório>`: Cria uma cópia local de um repositório remoto.

3. `git add \<arquivo>`: Prepara as alterações de um arquivo para o próximo commit.

4. `git commit -m "Mensagem do Commit"`: Cria um novo commit com as alterações preparadas.

5. `git status`: Verifica o status do repositório, incluindo arquivos modificados, preparados e não rastreados.

6. `git diff`: Mostra as diferenças entre as alterações atuais e o último commit.

7. `git log`: Exibe o histórico de commits do branch atual.

8. `git branch`: Lista todos os branches do repositório.

9. `git branch <nome-do-branch>`: Cria um novo branch.

10. `git checkout <nome-do-branch>`: Alterna para um branch diferente.

11. `git merge <nome-do-branch>`: Mescla as alterações do branch especificado no branch atual.

12. `git remote add <nome-remoto> <url-remoto>`: Adiciona um repositório remoto.

13. `git pull <nome-remoto> <nome-do-branch>`: Obtém e mescla as alterações de um repositório remoto.

14. `git push <nome-remoto> <nome-do-branch>`: Envia os commits locais para um repositório remoto.

## Exemplos de Fluxos de Trabalho no Git

### Criando um Novo Branch de Recurso

1. Criar um novo branch: `git branch branch-recurso`

2. Alternar para o novo

 branch: `git checkout branch-recurso`

3. Fazer alterações nos arquivos.

4. Preparar e fazer commit das alterações: `git add <arquivo>` e `git commit -m "Mensagem do Commit"`

### Mesclando Alterações de um Branch de Recurso

1. Alternar para o branch onde você deseja mesclar as alterações: `git checkout main`

2. Mesclar o branch de recurso: `git merge branch-recurso`

3. Resolver quaisquer conflitos que possam surgir.

4. Fazer commit das alterações de mesclagem: `git commit -m "Mesclar branch-recurso"`

### Colaborando com Repositórios Remotos

1. Clonar um repositório remoto: `git clone <url-do-repositório>`

2. Criar um novo branch para o seu trabalho: `git branch meu-branch`

3. Alternar para o novo branch: `git checkout meu-branch`

4. Fazer alterações, prepará-las e fazer commit: `git add <arquivo>` e `git commit -m "Mensagem do Commit"`

5. Obter as alterações mais recentes do repositório remoto: `git pull origin meu-branch`

6. Mesclar as alterações do branch remoto no seu branch: `git merge origin/branch-remoto`

7. Resolver quaisquer conflitos que possam surgir.

8. Enviar seu branch para o repositório remoto: `git push origin meu-branch`

Essas são algumas informações importantes sobre o Git, incluindo comandos e fluxos de trabalho comuns. Lembre-se de que a prática é essencial para aperfeiçoar suas habilidades com o Git.

Mais detalhes sobre os fluxos de trabalho (workflows) utilizando Pull Requests podem ser vistos em [workflow.md](workflow.md)