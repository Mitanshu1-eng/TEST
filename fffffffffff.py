#5 
#abcd xyzfwegwr jfk kfn ijk

n = int(input())
k=0
words = list(map(str,input().split()))

for word in words:
    #word = abcd
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
