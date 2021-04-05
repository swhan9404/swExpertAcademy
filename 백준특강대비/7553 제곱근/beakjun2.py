s=input()
i=int(s)
r=int(10**(len(s)//2))
while r*r!=i:
    print(r, r+ i//r)
    r=(r+i//r)//2
print(r)