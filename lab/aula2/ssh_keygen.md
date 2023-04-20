## Como funciona o sistema de chave pública e privada do SSH?

O SSH (Secure Shell) é um protocolo de rede que permite a conexão segura entre dois dispositivos. Para se conectar a um servidor SSH, você normalmente precisa fornecer suas credenciais, como nome de usuário e senha. No entanto, para uma conexão ainda mais segura, o SSH também suporta autenticação baseada em chaves.

A autenticação baseada em chaves usa um par de chaves, uma pública e outra privada, para autenticar o usuário. A chave privada é mantida em segredo no computador do usuário, enquanto a chave pública é compartilhada com o servidor SSH. Quando o usuário se conecta ao servidor SSH, o servidor solicita que o usuário prove sua identidade. O usuário então usa sua chave privada para criar uma assinatura digital, que é enviada ao servidor SSH. O servidor SSH, por sua vez, usa a chave pública correspondente para verificar a assinatura digital e autenticar o usuário.

O processo de autenticação por chave pública e privada é mais seguro do que a autenticação por senha, pois a chave privada é mantida em sigilo e nunca é enviada pela rede. Além disso, a chave pública é apenas usada para autenticar o usuário e não pode ser usada para acessar o computador do usuário.

Para configurar a autenticação baseada em chave pública e privada, o usuário deve criar um par de chaves usando um utilitário como o ssh-keygen. O utilitário gera um par de chaves, uma pública e outra privada, que são salvas no diretório ~/.ssh/. A chave pública deve ser adicionada ao servidor SSH que o usuário deseja acessar, enquanto a chave privada deve ser mantida em segredo no computador do usuário.

Aqui está um exemplo de como gerar um par de chaves usando o ssh-keygen:

```$ ssh-keygen -t rsa -b 4096```

Esse comando cria um par de chaves RSA de 4096 bits e armazena a chave privada no arquivo ~/.ssh/id_rsa e a chave pública no arquivo ~/.ssh/id_rsa.pub.
