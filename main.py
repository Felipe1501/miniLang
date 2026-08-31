# main.py
from lexer import Lexer
from parser_ast import Parser, ProgramNode, AssignNode, ReadNode, WriteNode, IfNode, WhileNode, BinOpNode, NumNode, VarNode

codigo_fonte = """
# Teste Completo da MiniLang
soma := 0;
read x;

while x != 0 do
    if x >= 10 then
        soma := soma + x;
    else
        soma := soma + 1;
        
    read x;
    
write soma;
"""

# Função auxiliar para desenhar a árvore bonita no terminal
def print_ast(node, level=0):
    indent = "  " * level
    if isinstance(node, ProgramNode):
        print(f"{indent}PROGRAMA:")
        for cmd in node.cmds: print_ast(cmd, level + 1)
    elif isinstance(node, AssignNode):
        print(f"{indent}ATRIBUIR (:=):")
        print_ast(node.var_node, level + 1)
        print_ast(node.expr_node, level + 1)
    elif isinstance(node, ReadNode):
        print(f"{indent}READ:")
        print_ast(node.var_node, level + 1)
    elif isinstance(node, WriteNode):
        print(f"{indent}WRITE:")
        print_ast(node.expr_node, level + 1)
    elif isinstance(node, IfNode):
        print(f"{indent}IF:")
        print_ast(node.condition, level + 1)
        print(f"{indent}THEN:")
        for cmd in node.then_cmds: print_ast(cmd, level + 1)
        if node.else_cmds:
            print(f"{indent}ELSE:")
            for cmd in node.else_cmds: print_ast(cmd, level + 1)
    elif isinstance(node, WhileNode):
        print(f"{indent}WHILE:")
        print_ast(node.condition, level + 1)
        print(f"{indent}DO:")
        for cmd in node.cmds: print_ast(cmd, level + 1)
    elif isinstance(node, BinOpNode):
        print(f"{indent}OP({node.op}):")
        print_ast(node.left, level + 1)
        print_ast(node.right, level + 1)
    elif isinstance(node, VarNode):
        print(f"{indent}Var({node.name})")
    elif isinstance(node, NumNode):
        print(f"{indent}Num({node.value})")


if __name__ == '__main__':
    print("Iniciando o Compilador MiniLang...\n")
    lexer = Lexer(codigo_fonte)
    parser = Parser(lexer)
    
    try:
        ast = parser.parse()
        print("✅ SUCESSO! Código compilado sem erros.")
        print("-" * 40)
        print("ÁRVORE SINTÁTICA ABSTRATA (AST) GERADA:")
        print("-" * 40)
        print_ast(ast)
        
    except Exception as e:
        print(f"❌ ERRO FATAL: {e}")