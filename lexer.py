# lexer.py
from enum import Enum, auto

class TokenType(Enum):
    IF = auto()
    THEN = auto()
    ELSE = auto()
    WHILE = auto()
    DO = auto()
    READ = auto()
    WRITE = auto()
    
    ID = auto()     
    NUM = auto()     
    
    ASSIGN = auto()  
    OP_ARIT = auto()
    OP_REL = auto() 
    SEMI = auto()   
    
    EOF = auto()     
    ERROR = auto()  

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', Linha:{self.line}, Col:{self.column})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        
        self.line = 1
        self.column = 1

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None  
        else:
            self.current_char = self.text[self.pos]
            self.column += 1

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.text):
            return None
        return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
                self.column = 0 
            self.advance()

    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def number(self):
        result = ''
        start_line = self.line
        start_column = self.column
        
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            
        return Token(TokenType.NUM, int(result), start_line, start_column)

    def _id(self):
        result = ''
        start_line = self.line
        start_column = self.column
        
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        RESERVED_KEYWORDS = {
            'if': TokenType.IF,
            'then': TokenType.THEN,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'do': TokenType.DO,
            'read': TokenType.READ,
            'write': TokenType.WRITE
        }

        token_type = RESERVED_KEYWORDS.get(result, TokenType.ID)
        return Token(token_type, result, start_line, start_column)

    def get_next_token(self):
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char.isalpha():
                return self._id()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == ':':
                start_col = self.column
                if self.peek() == '=':
                    self.advance() 
                    self.advance() 
                    return Token(TokenType.ASSIGN, ':=', self.line, start_col)
                
                self.advance()
                return Token(TokenType.ERROR, ':', self.line, start_col)

            if self.current_char == '=':
                start_col = self.column
                if self.peek() == '=':
                    self.advance(); self.advance()
                    return Token(TokenType.OP_REL, '==', self.line, start_col)
                self.advance()
                return Token(TokenType.ERROR, '=', self.line, start_col) # MiniLang usa := para atribuição

            if self.current_char == '!':
                start_col = self.column
                if self.peek() == '=':
                    self.advance(); self.advance()
                    return Token(TokenType.OP_REL, '!=', self.line, start_col)
                self.advance()
                return Token(TokenType.ERROR, '!', self.line, start_col)

            if self.current_char == '<':
                start_col = self.column
                if self.peek() == '=':
                    self.advance(); self.advance()
                    return Token(TokenType.OP_REL, '<=', self.line, start_col)
                self.advance()
                return Token(TokenType.OP_REL, '<', self.line, start_col)

            if self.current_char == '>':
                start_col = self.column
                if self.peek() == '=':
                    self.advance(); self.advance()
                    return Token(TokenType.OP_REL, '>=', self.line, start_col)
                self.advance()
                return Token(TokenType.OP_REL, '>', self.line, start_col)

            if self.current_char in ('+', '-', '*', '/'):
                token = Token(TokenType.OP_ARIT, self.current_char, self.line, self.column)
                self.advance()
                return token

            if self.current_char == ';':
                token = Token(TokenType.SEMI, ';', self.line, self.column)
                self.advance()
                return token

            erro_char = self.current_char
            linha_erro = self.line
            col_erro = self.column
            self.advance()
            return Token(TokenType.ERROR, erro_char, linha_erro, col_erro)

        return Token(TokenType.EOF, 'EOF', self.line, self.column)