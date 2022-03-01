
def syracuse(N):
    u = N
    n=0
    while(u!=1): 
        if u%2==0: 
            u = u//2 
        else:
            u = 3*u+1
        n += 1
    return n

print(syracuse(int(input("n = "))))