# SimpleLang 👨‍💻
Programming language created by AI and builded on Python.

## What is SimpleLang? 🤔
SimpleLang is a simple programming language created by AI and builded on Python enviroment. It uses Python interpreter for interpreting `.slang` into machine code. You can add your own functions and rules into this programming language by modifying essential files (`lexer.py`, `parser.py`, `interpreter.py`, `simplelang_interpreter`) It's some kind of "AI experiment" and it's completly crazy!

## How to use SimpleLang? ❓
1. Make sure you have installed **Python** on your machine!
2. Create main `program.slang` file in your project folder.
```
x = 5
print(x)
```
4. Add `lexer.py` file.
```
def lexer(input_code):
    tokens = []
    i = 0
    while i < len(input_code):
        char = input_code[i]
        if char.isalpha():
            identifier = ""
            while i < len(input_code) and input_code[i].isalnum():
                identifier += input_code[i]
                i += 1
            if identifier == "print":
                tokens.append(("PRINT", identifier))
            else:
                tokens.append(("IDENTIFIER", identifier))
        elif char.isdigit():
            number = ""
            while i < len(input_code) and input_code[i].isdigit():
                number += input_code[i]
                i += 1
            tokens.append(("NUMBER", number))
        elif char == "=":
            tokens.append(("EQUALS", "="))
            i += 1
        elif char == "+":
            tokens.append(("PLUS", "+"))
            i += 1
        elif char == "(":
            tokens.append(("LPAREN", "("))
            i += 1
        elif char == ")":
            tokens.append(("RPAREN", ")"))
            i += 1
        else:
            i += 1
    return tokens

```
5. Add `parser.py` file.
```
def parse(tokens):
    def parse_assignment():
        identifier = tokens.pop(0)
        if identifier[0] != "IDENTIFIER":
            raise SyntaxError("Expected an identifier")
        equals = tokens.pop(0)
        if equals[0] != "EQUALS":
            raise SyntaxError("Expected '='")
        expr = parse_expression()
        return ("ASSIGNMENT", identifier[1], expr)

    def parse_expression():
        token = tokens.pop(0)
        if token[0] == "NUMBER":
            return ("NUMBER", token[1])
        elif token[0] == "IDENTIFIER":
            return ("IDENTIFIER", token[1])
        elif token[0] == "PLUS":
            left = parse_expression()
            right = parse_expression()
            return ("PLUS", left, right)
        else:
            raise SyntaxError("Invalid expression")

    def parse_print():
        print_kw = tokens.pop(0)
        if print_kw[0] != "PRINT":
            raise SyntaxError("Expected 'print'")
        lparen = tokens.pop(0)
        if lparen[0] != "LPAREN":
            raise SyntaxError("Expected '('")
        identifier = tokens.pop(0)
        if identifier[0] != "IDENTIFIER":
            raise SyntaxError("Expected an identifier")
        rparen = tokens.pop(0)
        if rparen[0] != "RPAREN":
            raise SyntaxError("Expected ')'")
        return ("PRINT", identifier[1])

    ast = []
    while tokens:
        token = tokens[0]
        if token[0] == "IDENTIFIER":
            ast.append(parse_assignment())
        elif token[0] == "PRINT":
            ast.append(parse_print())
        else:
            raise SyntaxError("Unknown statement")
    return ast
```
6. Add `interpreter.py` file.
```
def interpret(ast):
    environment = {}

    def evaluate_expression(expr):
        if expr[0] == "NUMBER":
            return int(expr[1])
        elif expr[0] == "IDENTIFIER":
            if expr[1] in environment:
                return environment[expr[1]]
            else:
                raise NameError(f"Variable '{expr[1]}' is not defined")
        elif expr[0] == "PLUS":
            left = evaluate_expression(expr[1])
            right = evaluate_expression(expr[2])
            return left + right
        else:
            raise SyntaxError("Unsupported expression")

    for node in ast:
        if node[0] == "ASSIGNMENT":
            var_name = node[1]
            value = evaluate_expression(node[2])
            environment[var_name] = value
        elif node[0] == "PRINT":
            var_name = node[1]
            if var_name in environment:
                print(environment[var_name])
            else:
                raise NameError(f"Variable '{var_name}' is not defined")
        else:
            raise SyntaxError("Unsupported statement")

```
7. Add a `simplelang_interpreter` script for running all processes in one click.
```
from lexer import lexer
from parser import parse
from interpreter import interpret

def run_simplelang(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    tokens = lexer(code)

    ast = parse(tokens)

    interpret(ast)

# Running: make sure you replace YOUR_FILE_NAME with name of your .slang file.
if __name__ == "__main__":
    run_simplelang('YOUR_FILE_NAME.slang')

```
Now, you have completed the setup process of SimpleLang. Hope it will be useful! 💖
