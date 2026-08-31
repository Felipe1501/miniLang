# MiniComp - Compilador Front-End MiniLang

Projeto didático desenvolvido para a disciplina de Compiladores. O objetivo é implementar o front-end de um compilador (Analisador Léxico, Analisador Sintático Preditivo LL(1) e Árvore Sintática Abstrata - AST) para a linguagem hipotética **MiniLang**.

A MiniLang é uma linguagem imperativa simples que possui variáveis globais, números inteiros não negativos, comandos de atribuição, leitura (`read`), escrita (`write`), condicionais (`if-then-else`) e laços de repetição (`while-do`).

## 📂 Estrutura do Projeto

Até o momento, o projeto possui os seguintes arquivos:

* `lexer.py`: Contém o Analisador Léxico (Scanner), responsável por ler o código-fonte, ignorar espaços/comentários e gerar os Tokens.
* `main.py`: Arquivo principal que contém um código MiniLang de teste e executa o compilador.

> **Nota:** Os arquivos referentes ao Analisador Sintático (`parser_ast.py`) e aos autômatos no JFLAP serão adicionados nas próximas etapas.

## 🚀 Como Executar

O projeto foi desenvolvido em **Python 3**. Para rodar o analisador léxico, basta executar o arquivo principal:

1. Abra o terminal na pasta do projeto.
2. Execute o comando:

```bash
python main.py