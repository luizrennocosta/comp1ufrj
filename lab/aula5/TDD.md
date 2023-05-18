# Test-Driven Development

O Test-Driven Development (TDD), ou Desenvolvimento Orientado a Testes, é uma metodologia de desenvolvimento de software que coloca os testes como ponto central do processo. Com o TDD, os testes são escritos antes do código de produção e guiam o desenvolvimento do software.

O TDD segue um ciclo repetitivo composto por três etapas principais: "Red-Green-Refactor" (Vermelho-Verde-Refatorar). Vamos entender cada uma delas:

1. **Red (Vermelho)**: Nesta etapa, você escreve um teste automatizado que falha. O teste deve refletir um requisito ou comportamento que ainda não foi implementado.

2. **Green (Verde)**: Na etapa Verde, você escreve a quantidade mínima de código necessário para fazer o teste passar. O objetivo é fazer o teste passar corretamente, não se preocupando com a qualidade ou eficiência do código.

3. **Refactor (Refatorar)**: Após o teste estar passando, você pode refatorar o código para melhorar sua qualidade, legibilidade e eficiência, mantendo os testes passando o tempo todo. O refatoramento é uma etapa importante para eliminar duplicação de código, melhorar a estrutura e garantir que o código esteja bem organizado.

O TDD traz diversos benefícios, como:

- **Código mais confiável**: Como o código é constantemente testado, há uma maior confiança na sua qualidade e funcionalidade.
- **Maior clareza dos requisitos**: Ao escrever testes antes do código, você precisa entender claramente o que é esperado do software, o que ajuda a definir os requisitos de forma mais precisa.
- **Facilidade de manutenção**: Os testes atuam como uma garantia de que as alterações no código não quebrarão o funcionamento existente. Isso facilita a manutenção e evolução do software ao longo do tempo.
- **Design mais modular**: O TDD incentiva a separação de responsabilidades e a criação de código modular, facilitando a compreensão e reutilização.

Algumas práticas e metodologias importantes dentro do TDD incluem:

- **Testes unitários**: Os testes devem ser pequenos, focados em testar uma unidade de código isoladamente, como uma função ou método específico.
- **Testes automatizados**: Os testes devem ser executados automaticamente, sem intervenção manual, para garantir que sejam repetíveis e rápidos.
- **Testes de aceitação**: Além dos testes unitários, os testes de aceitação devem ser criados para verificar se o sistema como um todo atende aos requisitos e comportamentos esperados.
- **Refatoração contínua**: O refatoramento é uma etapa fundamental para melhorar a qualidade do código, garantindo que seja legível, eficiente e bem estruturado.
- **Iteração e feedback rápido**: O ciclo de desenvolvimento no TDD é rápido, permitindo obter feedback imediato sobre o código e os testes, o que facilita a identificação e correção de problemas.

É importante ressaltar que o TDD não é uma metodologia que elimina a necessidade de outros tipos de testes, como testes de integração, testes de sistema ou testes de desempenho. O TDD foca


# Exemplo Prático

Passo 1: Red (Vermelho)

Escrevemos um teste que represente o comportamento esperado da função. O teste deve falhar inicialmente, pois a função ainda não está implementada.

```python
import pytest

def test_verificar_par():
    assert verificar_par(3) == False
```

Passo 2: Green (Verde)

Agora, escrevemos a quantidade mínima de código necessário para fazer o teste passar. Nesse caso, implementamos a função `verificar_par` para retornar `True` se o número for par e `False` caso contrário.

```python
def verificar_par(numero):
    return numero % 2 == 0
```

Passo 3: Refactor (Refatorar)

Após o teste estar passando, podemos refatorar o código para melhorar sua qualidade, legibilidade e eficiência. Neste exemplo simples, não há muito o que refatorar, mas vamos adicionar um novo teste para garantir o funcionamento correto da função.

```python
def test_verificar_par():
    assert verificar_par(3) == False
    assert verificar_par(4) == True
```

Agora, podemos executar o teste utilizando o pytest para garantir que a função esteja corretamente implementada:

```
$ pytest
```

O pytest executará os testes e fornecerá o resultado:

```
============================= test session starts ==============================
...
collected 2 items

test_example.py ..                                                         [100%]

============================== 2 passed in 0.01s ===============================
```

Ambos os testes passaram com sucesso, o que indica que a função `verificar_par` está implementada corretamente.