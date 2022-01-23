def solve_hectoc(expressions_with_parantheses):
    results = []
    for expr in expressions_with_parantheses:
        try:
            replaced_expr = expr.replace('^', '**')
            solve = eval(replaced_expr)
            if solve == 100:
                results.append(expr)
        except:
            pass

    if len(results) == 0:
        print("\nThere are no possible results for your number")
        print("\n--------------------------------------------------------------------------------")
    else:
        
        print(f'\nFor you number there are {len(results)} possible results!\n\nFollowing mathematical expressions are possible:')
        for result in results:
            #printing_result += result + "; "
            print(f'\n {result}')
        
        print("\n--------------------------------------------------------------------------------")
