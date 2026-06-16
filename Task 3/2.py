pattern= input().strip()
text=input().strip()
d=int(input())
k=len(pattern)
ans=[]

for i in range(len(text)-k+1):
    mismatch=0
    for j in range(k):
        if text[i+j]!=pattern[j]:
            mismatch=mismatch+1
    if mismatch<=d:
        ans.append(i)
        
print(*ans)
