n = int(input())
k=0
words = input().split()  # No need for map since input is already space-separated strings

for word in words:
    seen = []
    for ch in word:
        if ch not in seen:
            seen.append(ch)
    if len(seen) == len(word):
        c=list(word)
        d=list(word)
        c.sort()
        if c==d:
            k+=1
print(k)