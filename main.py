n = input("Digite um número:")
n = int(n)
contador = 0
a = 2
while contador != n:
   b = 2
   primo = True 
   while b < a:
      if a % b == 0 and a != b:
         primo = False 
         break
      b = b + 1 
   if primo:
      contador += 1
      print(a)
   a = a + 1

