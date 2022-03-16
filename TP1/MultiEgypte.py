def Egypt():
   A = int(input("Entrer un nombre: "))
   B = int(input("Entrer un autre nombre: "))
   S = 0
   while A != 0:
      if A % 2 == 1:
         S = S+B
      A = A//2
      B = B+B
   return(S)

print(Egypt())

