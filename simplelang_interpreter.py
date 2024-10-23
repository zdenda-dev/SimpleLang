from lexer import lexer
from parser import parse
from interpreter import interpret

def run_simplelang(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    # Krok 1: Lexikální analýza
    tokens = lexer(code)

    # Krok 2: Syntaktická analýza
    ast = parse(tokens)

    # Krok 3: Interpretace
    interpret(ast)

# Spuštění: Předáme cestu k souboru SimpleLang jako argument
if __name__ == "__main__":
    run_simplelang('program.slang')