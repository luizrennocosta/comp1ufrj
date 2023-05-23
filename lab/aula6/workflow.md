# Notas da Aula - Fluxo de Trabalho do Git com Branches de Development e Pull Requests

## Introdução ao Fluxo de Trabalho do Git com Branches de Development e Pull Requests

O fluxo de trabalho do Git com branches de development e pull requests é uma abordagem colaborativa para o desenvolvimento de software que permite que as equipes trabalhem em paralelo em diferentes recursos e integrem as alterações de forma controlada. Ele envolve a criação de um branch de development para o desenvolvimento contínuo de recursos e o uso de pull requests para revisar e integrar as alterações ao branch principal. Aqui estão as etapas para trabalhar com esse fluxo de trabalho:

## Fluxo de Trabalho com Branches de Development e Pull Requests

1. **Criação do Repositório**: Inicie um repositório Git em seu projeto usando `git init` ou clone um repositório existente usando `git clone <url-do-repositório>`.

2. **Criação do Branch Principal**: Geralmente, é criado um branch principal chamado "main" ou "master" que contém o código estável do projeto.

3. **Criação do Branch de Development**: Crie um novo branch de development a partir do branch principal usando `git branch development` e `git checkout development`.

4. **Trabalho no Branch de Development**: Realize o desenvolvimento contínuo de recursos, correções de bugs e outras melhorias no branch de development. Faça alterações, adicione novos arquivos, modifique os existentes e teste suas alterações.

5. **Adição das Alterações ao Stage**: Use `git add <arquivo>` para adicionar as alterações ao ambiente de staging. Você pode adicionar arquivos individualmente ou usar `git add .` para adicionar todas as alterações.

6. **Commit das Alterações**: Faça o commit das alterações preparadas no ambiente de staging usando `git commit -m "Mensagem do Commit"`. Forneça uma mensagem descritiva que resuma as alterações feitas.

7. **Envio das Alterações para o Repositório Remoto**: Envie o branch de development para o repositório remoto usando `git push origin development`.

8. **Criação do Pull Request**: Acesse a plataforma de hospedagem do repositório (como GitHub ou GitLab) e crie um novo pull request para o branch de development recém-enviado. Forneça uma descrição clara das alterações, detalhes sobre os recursos desenvolvidos e solicite a revisão dos colegas.

9. **Revisão do Pull Request**: Os colegas de equipe revisam o código, fornecem feedback, fazem perguntas e sugerem alterações. Conforme necessário, o autor do pull request faz alterações adicionais no branch de development e envia novos commits.

10. **Integração do Pull Request**: Após a revisão e aprovação, o pull request é mesclado no branch de development. Isso pode ser feito pelo autor do pull request ou por um mantenedor do repositório. Durante a mesclagem, pode ser necessário resolver conflitos.

11. **Atualização do Branch Principal**: Periodicamente, o branch principal (como "main" ou "master") é atualizado com as alterações do branch de development. Isso é feito alternando para o branch principal (`git checkout main`) e usando `git merge development` para mesclar as alterações do branch de development.

12. **Implantação do Branch Principal**: Após mesclar as alterações do branch de development no branch principal, o código está pronto para ser implantado em produção ou em outro ambiente de destino.

![alt](images/git-workflow-release-cycle-2feature.png)

## Conclusão

O fluxo de trabalho do Git com branches de development e pull requests é uma maneira eficiente de colaborar no desenvolvimento de software em equipe. Ele permite que diferentes recursos sejam desenvolvidos simultaneamente em branches separados, enquanto o branch principal permanece estável. O uso de pull requests facilita a revisão de código, a discussão entre os membros da equipe e o controle das alterações integradas no branch principal. Ao praticar esse fluxo de trabalho, você pode garantir uma integração suave das alterações e manter um histórico claro e organizado do desenvolvimento do projeto.