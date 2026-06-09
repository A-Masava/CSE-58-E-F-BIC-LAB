
t=input().strip()
k=int(input())
count={}

for i in range(len(t)-k+1):
    pattern=t[i:i+k]
    count[pattern]=count.get(pattern,0)+1
max_count=max(count.values())
    
for pattern in count:
        if count[pattern]==max_count:
            print(pattern, end=" ")
