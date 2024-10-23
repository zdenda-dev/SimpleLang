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
