# Notas da Aula - Fluxo de Trabalho do Git

## Introdução ao Fluxo de Trabalho do Git

O fluxo de trabalho do Git é uma sequência de etapas e práticas recomendadas para colaboração e gerenciamento de código usando o Git como sistema de controle de versão. Ele define como os desenvolvedores trabalham juntos, gerenciam branches, fazem commits e mesclam alterações. Existem vários fluxos de trabalho do Git, mas aqui vamos abordar o fluxo de trabalho básico com branches principais.

## Fluxo de Trabalho Básico com Branches Principais

1. **Criação do Repositório**: Inicie um repositório Git em seu projeto usando `git init` ou clone um repositório existente usando `git clone <url-do-repositório>`.

2. **Criação de um Branch Principal**: Geralmente, é criado um branch principal chamado "main" ou "master" que contém o código principal do projeto.

3. **Criação de um Branch de Recurso**: Crie um novo branch a partir do branch principal para trabalhar em um recurso específico. Use o comando `git branch <nome-do-branch>` para criar o branch e `git checkout <nome-do-branch>` para alternar para ele.

4. **Trabalhando no Branch de Recurso**: Faça as alterações necessárias no código, adicione novos arquivos, modifique os existentes e teste suas alterações.

5. **Adição das Alterações ao Stage**: Use `git add <arquivo>` para adicionar as alterações ao ambiente de staging. Você pode adicionar arquivos individualmente ou usar `git add .` para adicionar todas as alterações.

6. **Commit das Alterações**: Faça o commit das alterações preparadas no ambiente de staging usando `git commit -m "Mensagem do Commit"`. Certifique-se de fornecer uma mensagem descritiva que resuma as alterações feitas.

7. **Atualização do Branch Principal**: Antes de mesclar suas alterações no branch principal, é uma boa prática atualizá-lo para incorporar quaisquer alterações feitas por outros colaboradores. Use `git checkout main` para alternar para o branch principal e `git pull origin main` para obter as alterações mais recentes.

8. **Mesclagem das Alterações**: Com o branch principal atualizado, alterne de volta para o seu branch de recurso usando `git checkout <nome-do-branch>` e, em seguida, use `git merge main` para mesclar as alterações do branch principal em seu branch de recurso.

9. **Resolução de Conflitos**: Se houver conflitos durante a mesclagem, o Git indicará os arquivos em conflito. Abra esses arquivos em um editor de texto e resolva manualmente as diferenças. Após a resolução, adicione as alterações ao stage e faça o commit novamente.

10. **Teste e Revisão**: Teste suas alterações no branch de recurso para garantir que tudo funcione corretamente. Além disso, é uma prática recomendada solicitar a revisão de colegas antes de prosseguir.

11. **Mesclagem do Branch de Recurso (feature)**: Após revisar e testar, alterne para o branch principal (`git checkout main`) e use `git merge <nome-do-branch>` para mesclar o branch de recurso no branch principal.

12. **Envio para o Repositório Remoto**: Finalmente, envie suas alterações para um repositório remoto usando `git push origin main`. Isso tornará as alterações disponíveis para outros colaboradores.

## Conclusão

O fluxo de trabalho do Git com branches principais permite que você trabalhe de forma colaborativa e gerencie alterações de código de maneira eficiente. Com a criação de branches de recurso, commits adequados e mesclagens corretas, você pode controlar o desenvolvimento do projeto e manter um histórico claro de alterações. É importante praticar esse fluxo de trabalho para se familiarizar com os conceitos e aproveitar os benefícios que o Git oferece.