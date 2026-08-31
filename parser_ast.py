# parser_ast.py
from lexer import TokenType

# --- NÓS DA AST ---
class ASTNode: pass

class NumNode(ASTNode):
    def __init__(self, token):
        self.value = token.value

class VarNode(ASTNode):
    def __init__(self, token):
        self.name = token.value

class BinOpNode(ASTNode):
    def __init__(self, left, op_token, right):
        self.left = left
        self.op = op_token.value
        self.right = right

class AssignNode(ASTNode):
    def __init__(self, var_node, expr_node):
        self.var_node = var_node
        self.expr_node = expr_node

class ReadNode(ASTNode):
    def __init__(self, var_node):
        self.var_node = var_node

class WriteNode(ASTNode):
    def __init__(self, expr_node):
        self.expr_node = expr_node

class IfNode(ASTNode):
    def __init__(self, condition, then_cmds, else_cmds):
        self.condition = condition
        self.then_cmds = then_cmds
        self.else_cmds = else_cmds

class WhileNode(ASTNode):
    def __init__(self, condition, cmds):
        self.condition = condition
        self.cmds = cmds

class ProgramNode(ASTNode):
    def __init__(self, cmds):
        self.cmds = cmds


# --- O PARSER LL(1) ---
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, expected_type=None):
        if expected_type:
            msg = f"Esperava {expected_type.name}, mas encontrou '{self.current_token.value}'"
        else:
            msg = f"Token inesperado '{self.current_token.value}'"
        raise Exception(f"Erro Sintático na Linha {self.current_token.line}, Col: {self.current_token.column} -> {msg}")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_type)

    def parse(self):
        return self.parse_program()

    def parse_program(self):
        return ProgramNode(self.parse_cmd_list())

    def parse_cmd_list(self):
        cmds = []
        inicios_validos = (TokenType.ID, TokenType.READ, TokenType.WRITE, TokenType.IF, TokenType.WHILE)
        while self.current_token.type in inicios_validos:
            cmds.append(self.parse_cmd())
        return cmds

    def parse_cmd(self):
        t = self.current_token.type
        if t == TokenType.ID: return self.parse_assign()
        elif t == TokenType.READ: return self.parse_read()
        elif t == TokenType.WRITE: return self.parse_write()
        elif t == TokenType.IF: return self.parse_if()
        elif t == TokenType.WHILE: return self.parse_while()
        else: self.error()

    def parse_assign(self):
        var_node = VarNode(self.current_token)
        self.eat(TokenType.ID)
        self.eat(TokenType.ASSIGN)
        expr_node = self.parse_expr()
        self.eat(TokenType.SEMI)
        return AssignNode(var_node, expr_node)

    def parse_read(self):
        self.eat(TokenType.READ)
        var_node = VarNode(self.current_token)
        self.eat(TokenType.ID)
        self.eat(TokenType.SEMI)
        return ReadNode(var_node)

    def parse_write(self):
        self.eat(TokenType.WRITE)
        expr_node = self.parse_expr()
        self.eat(TokenType.SEMI)
        return WriteNode(expr_node)

    def parse_if(self):
        self.eat(TokenType.IF)
        condition = self.parse_expr()
        self.eat(TokenType.THEN)
        then_cmds = self.parse_cmd_list()
        else_cmds = []
        if self.current_token.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            else_cmds = self.parse_cmd_list()
        return IfNode(condition, then_cmds, else_cmds)

    def parse_while(self):
        self.eat(TokenType.WHILE)
        condition = self.parse_expr()
        self.eat(TokenType.DO)
        cmds = self.parse_cmd_list()
        return WhileNode(condition, cmds)

    def parse_expr(self):
        node = self.parse_arit()
        if self.current_token.type == TokenType.OP_REL:
            op_token = self.current_token
            self.eat(TokenType.OP_REL)
            node = BinOpNode(node, op_token, self.parse_arit())
        return node

    def parse_arit(self):
        node = self.parse_termo()
        while self.current_token.type == TokenType.OP_ARIT and self.current_token.value in ('+', '-'):
            op_token = self.current_token
            self.eat(TokenType.OP_ARIT)
            node = BinOpNode(node, op_token, self.parse_termo())
        return node

    def parse_termo(self):
        node = self.parse_fator()
        while self.current_token.type == TokenType.OP_ARIT and self.current_token.value in ('*', '/'):
            op_token = self.current_token
            self.eat(TokenType.OP_ARIT)
            node = BinOpNode(node, op_token, self.parse_fator())
        return node

    def parse_fator(self):
        token = self.current_token
        if token.type == TokenType.NUM:
            self.eat(TokenType.NUM)
            return NumNode(token)
        elif token.type == TokenType.ID:
            self.eat(TokenType.ID)
            return VarNode(token)
        else:
            raise Exception(f"Erro Sintático: Esperava Número ou Variável, encontrou '{token.value}'")