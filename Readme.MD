# MiniComp - Compilador Front-End MiniLang

Projeto didático desenvolvido para a disciplina de Compiladores. O objetivo é implementar o front-end de um compilador para a linguagem hipotética **MiniLang**.

Este repositório contém a implementação completa do **Analisador Léxico**, do **Analisador Sintático Preditivo LL(1)** e a geração da **Árvore Sintática Abstrata (AST)**.

> **Nota sobre a linguagem de implementação:** Conforme permitido na especificação do projeto, o desenvolvimento foi feito em **Python 3**. Essa escolha simplificou o gerenciamento de memória na construção da Árvore Sintática Abstrata e permitiu um código mais limpo por meio da técnica de Descida Recursiva.

## 📂 Estrutura do Projeto

* `lexer.py`: Contém o **Analisador Léxico (Scanner)**. Responsável por ler o código-fonte, ignorar espaços e comentários, classificar palavras-chave, variáveis, números e operadores, gerando um fluxo de *Tokens*.
* `parser_ast.py`: Contém o **Analisador Sintático Preditivo LL(1)** e as classes da **AST**. Utiliza a técnica de *Descida Recursiva* (Recursive Descent) para validar a gramática livre de contexto (já fatorada e sem recursão à esquerda) e montar a árvore em memória, garantindo a precedência matemática correta.
* `main.py`: Arquivo principal do projeto. Contém um código-fonte MiniLang embutido para testes, orquestra a chamada do Lexer e do Parser, e possui uma função para imprimir a árvore sintática gerada visualmente no terminal.

## 🚀 Como Executar

Certifique-se de ter o Python 3 instalado na sua máquina. Não há dependências externas.

1. Abra o terminal na pasta raiz do projeto.
2. Execute o arquivo principal:

```bash
python main.py