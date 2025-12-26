x=int(input())
for i in range (x):
    for j in range (x):
       if j==0 or i==x-1 or i==j or i==0 or j==x-i-1 or j==x-1:
         print("*",end=" ")
       else:
         print(" ",end=" ")
    print()