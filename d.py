n = int(input())

arr = []
for _ in range(n):
    inp = input()
    arr.append([int(i) for i in inp.split(" ")])

directions = [{ "n" : 0, "e": 0, "s": 0, "w": 0 } for _ in range(n)]

def split_even(d, y):
    z = y / 4
    d["n"] += z
    d["e"] += z
    d["s"] += z
    d["w"] += z
    
    return d

#def add_to_min(d, y):
   # m, mKey = d["n"], "n"
   # for key in d:
       # if d[key] < m:
           # m, mKey = d[key], key

   #d[mKey] += y

    #return d

def split_half(d, y, p):
    if p == 0:
        d["n"] += y /2
        d["s"] += y /2
    else:
        d["e"] += y /2
        d["w"] += y /2
    
    return d

def find_dif(d):
    return max([abs(x) for x in d.values()])

for i, (p, r, y) in enumerate(arr):

    directions[i]["n"] = (r / 2)
    directions[i]["e"] = (p / 2)
    directions[i]["s"] = directions[i]["n"] - r
    directions[i]["w"] = directions[i]["e"] - p

    vals = directions[i].values()
    s = sum(vals)

    d1 = split_even(directions[i].copy(), y)
     #d2 = add_to_min(directions[i].copy(), y)
    d3 = split_half(directions[i].copy(), y, p)

    d1m = find_dif(d1)
     #d2m = find_dif(d2)
    d3m = find_dif(d3)

    mn = min(d1m, d3m)

    if d1m == mn:
         split_even(directions[i], y)
    # elif d2m == mn:
         #add_to_min(directions[i], y)
    else:
         split_half(directions[i], y, p)

for d in directions:
    print(" ".join(str(i) for i in d.values()))