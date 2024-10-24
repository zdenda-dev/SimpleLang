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
