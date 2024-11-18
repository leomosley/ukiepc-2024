num_ex = int(input())
parsed = []

for _ in range(num_ex):
    parsed.append(input()) 

hashmap = { "rest": "😎", "leg" : "🦵", "arm": "💪"}

pattern = []

for i, ex in enumerate(parsed):
    if "rest" in ex:
        pattern.append(hashmap["rest"])
    elif "leg" in ex:
        pattern.append(hashmap["leg"])
    else:
        pattern.append(hashmap["arm"])

n = 0
j = 0
for i in range(31):
    if (i % 7  == 0):
        n += 1
        if n > 1: 
            print(f"\n{n} ", end="")
        else:
            print(f"{n} ", end="")

    print(pattern[j], end="")
    
    j += 1
    if j > (num_ex-1):
        j = 0