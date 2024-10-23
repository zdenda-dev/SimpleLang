def lexer(input_code):
    tokens = []
    i = 0
    while i < len(input_code):
        char = input_code[i]
        if char.isalpha():  # Proměnná nebo klíčové slovo
            identifier = ""
            while i < len(input_code) and input_code[i].isalnum():
                identifier += input_code[i]
                i += 1
            if identifier == "print":
                tokens.append(("PRINT", identifier))
            else:
                tokens.append(("IDENTIFIER", identifier))
        elif char.isdigit():  # Číslo
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
            i += 1  # Přeskočíme mezery a neznámé znaky
    return tokens
