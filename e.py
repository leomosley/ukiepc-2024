n = int(input())
sequence = [int(i) for i in input().split()]


def sub_sequences(s):
    subs = [[] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if subs[i]:
                if sequence[j] >= subs[i][-1]:
                    subs[i].append(s[j])
            else:
                subs[i].append(s[j])
    
    return subs

subs = sub_sequences(sequence)
costs = { i: 0 for i in range(n) }

for i, sub in enumerate(subs):
    
    count = 0
    x = 0
    j = 0
    while x < len(sub):
        if sub[x] == sequence[j]:
            if count > 0:
                costs[i] += count ** 2
                count = 0
            j += 1
        else:
            count += 1
        x += 1
        
    if count > 0:
        costs[i] += count ** 2

print(costs)