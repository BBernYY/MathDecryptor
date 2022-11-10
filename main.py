import math
def get_simple_theory(a, n):
    
    results = []
    # Addition - Subtraction
    results.append(f"a + {n - a}")
    results.append(f"a - {a - n}")
    # Multiplication - Division
    results.append(f"a / {a / n}")
    results.append(f"a * {1/(a/n)}")
    # Exponent - Square-root
    results.append(f"a**{math.log(n)/math.log(a)}")

    return results
def get_theories(df):
    results = []
    for i in df:
        for ii in get_simple_theory(i[0], i[1]):
            results.append(ii)
    return results

def check_theory(theory, a, b):
    return eval(theory.replace("a", str(a))) == b

def main(df):
    
    theories = get_theories(df)
    for i in theories:
        if theories.count(i) >= len(df):
            theory = i
            break
    
    return theory




if __name__ == '__main__': # checks if the code is ran as a file
    print(main([
        [2, 16],
        [88, 59969536]
    ]))
