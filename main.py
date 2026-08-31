# main.py
from lexer import Lexer, TokenType

codigo_fonte = """
# Programa de teste MiniLang
soma := 0;
read x;

while x != 0 do
    if x >= 10 then
        soma := soma + x;
    else
        soma := soma + 1;
        
    read x; # lê o próximo valor
    
write soma;
"""

def testar_lexer():
    print("--- INICIANDO ANÁLISE LÉXICA ---")
    lexer = Lexer(codigo_fonte)
    
    while True:
        token = lexer.get_next_token()
        print(token)
        
        if token.type == TokenType.EOF:
            break
            
        if token.type == TokenType.ERROR:
            print(f">>> ERRO LÉXICO DETECTADO: '{token.value}' na Linha {token.line}, Coluna {token.column}")

if __name__ == '__main__':
    testar_lexer()