word1 = input()
word2 = input()

hashmap= {}

if len(word1) < len(word2):
    first = word1
    second = word2
else:
    first = word2
    second = word1

for char in set(i for i in first):
    hashmap[char] = first.count(char)

for char in set(i for i in second):
    c = second.count(char)
    if char in hashmap:
        if c > hashmap[char]:
            hashmap[char] = c
    
    else:
        hashmap[char] = c

ans = []
for char in hashmap:
    ans.append(char * hashmap[char])

print("".join(ans))