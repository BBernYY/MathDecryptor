import math
from collections import Counter
def get_simple_theory(a, n):
    
    results = {}
    # Addition - Subtraction
    results["+"] = a + n
    results["-"] = a - n
    # Multiplication - Division
    results["*"] = 1/(a/n)
    results["/"] = a/n
    # Exponent - Square-root
    if a == 1:
        results["**"] = math.log(n)/math.log(a)
    else:
        results["**"] = 1

    return results
def format_results(results):
    out = []
    for i in results:
        for k, v in i.items():
            out.append({
                "type": k,
                "num": v,
                "format": f"a {k} {v}"
                })
    return out
def get_theories(df):
    results = []
    for i in df:
        results.append(get_simple_theory(i[0], i[1]))
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
    



def main(df):
    output = []
    theories = format_results(get_theories(df))
    return sort_theories(theories, len(df))




if __name__ == '__main__': # checks if the code is ran as a file
    print(main([
        [3, 6],
        [6, 12]
    ]))
