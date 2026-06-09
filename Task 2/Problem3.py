
dna=input()

result= ""

for ch in dna:
    if ch=='A':
        result+='T'
    elif ch=='T':
        result +='A'
    elif ch=='C':
        result +='G'
    else:
        result +='C'
print(result[::-1])
