fLine = input()
sLine = input()
tLine = input()


n, k, p = map(int, fLine.split(" "))
m = int(sLine)
pre_done = tLine

im = False

hashmap = { str(i+1): 0 for i in range(k)}

string = pre_done

for c in pre_done.split(" "):
    hashmap[c] += 1

def check_valid(string: str):
    for i, c in enumerate(string.split(" ")):
        prev = string.split(" ")[i+1:i+p]
        if c in prev:
            return False
    else:
        return True

def check_can_use(string: str, c:str):
    if c in string[:p]:
        return False
    return True

def sort_hashmap(h: dict[str, int]) -> dict[str, int]:
    sorted_values = sorted(h.values())
    temp = h.copy()
    new = {}

    for val in sorted_values:
        for key in temp:
            if temp[key] == val:
                new[key] = val
                temp.pop(key)
                break
    
    return new


if not im:
    if k < p and n >= p:
        print("impossible")
        im = True

if not im:
    if not check_valid(pre_done):
        print("impossible")
        im = True

if not im:
    while len(string.split(" ")) < n:
        s = sort_hashmap(hashmap)

        for c in s:
            if check_can_use(string, c):
                string += f" {c}"
                hashmap[c] += 1
                break

    print(string)  