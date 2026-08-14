# TechSolutions — Módulo de Inscrições em Eventos

Sistema desenvolvido para gerenciar inscrições em eventos acadêmicos da **Universidade Inovação**, permitindo validar a elegibilidade dos alunos, controlar vagas e calcular descontos em ingressos.

## 📋 Sobre o projeto

Este projeto faz parte de uma atividade prática de **Qualidade de Software (QA)**, na qual o objetivo é analisar e testar o módulo de inscrições do aplicativo de eventos da TechSolutions.

O sistema deve garantir que as regras de negócio sejam respeitadas antes que uma inscrição seja realizada.

### Regras de negócio

* Alunos com **menos de 16 anos** não podem se inscrever.
* O cupom `ALUNO10` concede **10% de desconto** no valor do ingresso.
* O número de vagas disponíveis não pode ficar negativo.

## ⚙️ Funcionalidades

### Validação da inscrição

A função `validar_inscricao()` verifica:

* Idade mínima do aluno.
* Disponibilidade de vagas.
* Permissão ou negação da inscrição.

### Cálculo do ingresso

A função `calcular_valor_ingresso()` aplica o desconto de 10% quando o cupom `ALUNO10` é utilizado.

Por exemplo:

```text
Valor do ingresso: R$ 100,00
Desconto: 10%
Valor final: R$ 90,00
```

O material também apresenta a correção de um defeito em que o sistema subtraía R$ 10,00 do ingresso em vez de aplicar 10% de desconto. A implementação corrigida utiliza `valor_base * 0.9`.

### Checkout

A função `realizar_checkout()` integra as validações e o cálculo do ingresso:

1. Valida a inscrição.
2. Calcula o valor do ingresso.
3. Reduz uma vaga disponível.
4. Retorna o status da operação, o valor pago e as vagas restantes.

## 🧪 Testes

O projeto utiliza conceitos de **testes funcionais e não funcionais**, além dos diferentes níveis da pirâmide de testes.

### Testes funcionais

Verificam **o que o sistema faz**, como:

* Validar a idade mínima.
* Verificar disponibilidade de vagas.
* Aplicar corretamente o cupom `ALUNO10`.
* Emitir certificados com os dados corretos.
* Filtrar eventos corretamente.

### Testes não funcionais

Verificam características de **como o sistema funciona**, como:

* Tempo de carregamento.
* Segurança dos dados.
* Capacidade de suportar acessos simultâneos.
* Confiabilidade e usabilidade.

## 🔺 Níveis de teste

O projeto aborda quatro níveis principais:

| Nível               | Objetivo                                               |
| ------------------- | ------------------------------------------------------ |
| **Unitário**        | Testar funções ou métodos isoladamente                 |
| **Integração**      | Verificar a comunicação entre módulos                  |
| **Sistema**         | Testar a aplicação completa                            |
| **Aceitação (UAT)** | Validar se o sistema atende às necessidades do cliente |

Por exemplo, testar `validar_inscricao()` isoladamente corresponde a um **teste unitário**.

## 🐛 Análise de defeitos

Durante a atividade de QA, é importante diferenciar:

**Erro → Defeito/Bug → Falha**

* **Erro:** engano humano cometido durante o desenvolvimento.
* **Defeito/Bug:** problema existente no código.
* **Falha:** comportamento incorreto observado durante a execução.

Um exemplo analisado no projeto é o cálculo incorreto do desconto do cupom `ALUNO10`.

### Antes da correção

```python
valor_final = valor_base - 10
```

Essa implementação subtraía apenas R$ 10,00, independentemente do preço do ingresso.

### Depois da correção

```python
valor_final = valor_base * 0.9
```

Dessa forma, o sistema aplica corretamente o desconto de 10%.

## 🛠️ Tecnologias

* **Python**
* Teste de mesa
* Execução manual de scripts
* Conceitos de QA e testes de software

O material propõe a utilização de Python/JS para validação das regras de negócio.

## 🚀 Como executar

1. Tenha o **Python 3** instalado.
2. Salve o código do módulo em um arquivo `.py`.
3. Execute o arquivo pelo terminal ou por uma IDE, como VS Code ou IDLE.
4. Realize testes utilizando diferentes idades, quantidades de vagas, valores de ingresso e cupons.

Exemplo:

```python
resultado = realizar_checkout(
    idade=18,
    vagas=10,
    valor_base=100,
    cupom="ALUNO10"
)

print(resultado)
```

Resultado esperado:

```text
{
    "sucesso": True,
    "mensagem": "Inscrição realizada!",
    "valor_pago": 90.0,
    "vagas_restantes": 9
}
```

## 📚 Objetivo de QA

O principal objetivo dos testes é aumentar a **confiança na aplicação**, garantindo que suas funcionalidades estejam de acordo com os requisitos e evitando problemas para os usuários e para a organização responsável pelo sistema.

## 📄 Contexto

**Projeto:** Aplicativo de Gestão de Eventos Acadêmicos
**Empresa:** TechSolutions
**Cliente:** Universidade Inovação
**Área:** Qualidade de Software / QA
**Linguagem utilizada no módulo:** Python

---

**Projeto acadêmico — Análise e Testes de Software**
