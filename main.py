import math
from collections import Counter
def get_simple_theory(a, n ,types=["+", "-", "*", "/", "**"]):
    
    results = {}
    # Addition - Subtraction
    results["+"] = n - a
    results["-"] = a - n
    # Multiplication - Division
    results["*"] = 1/(a/n)
    results["/"] = a/n
    # Exponent - Square-root
    results["**"] = math.log(n)/math.log(a)
    out = []
    for k, v in results.items():
        if k in types:
            out.append({
                "type": k,
                "num": v,
                "format": f"a {k} {v}"
                })
    return out


def get_theories(df):
    results = []
    for i in df:
        for ii in get_simple_theory(i[0], i[1]):
            results.append(ii)
    return results

def sort_theories(values, total_list_length):
    rangedlist = []
    for i in values:
        rangedlist.append(i['format'])
    result = [item for items, c in Counter(rangedlist).most_common() for item in [items] * c]
    out = {}
    for i in result:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    for k, v in out.items():
        out[k] = round(v/total_list_length, 3)*100
    return out
    

def theory_web(*steps):
    theories = [get_simple_theory(steps[0], steps[1])]
    for i in range(len(steps)-1):
        theories.append(get_simple_theory(steps[i], steps[i+1]))
    print(theories)

def main(df):
    for i in df:
        if 1 in i:
            df.remove(i)
    output = []
    theories = get_theories(df)
    return sort_theories(theories, len(df))




if __name__ == '__main__': # checks if the code is ran as a file
    # print(main([
    #     [3, 6],
    #     [6, 12]
    # ]))
    print(theory_web(3, 2, 10, 8, 101, 55))
