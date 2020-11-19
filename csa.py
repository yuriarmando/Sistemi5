#YURI ARMANDO
import random
import logging

def control_input(input_num):
   
    return sympy.numprimo(input_num)
def lcm(p, q):
   if p > q:
      maggiore = p
   else:
       maggiore = q
   while(True):
       if((maggiore % p == 0) and (maggiore % q == 0)):
           lcm = maggiore
           break
       maggiore += 1

   return mcm
def chooseC(m):
    while (True):
        c = random.range(2, m)

        if (euclide(c, m) == 1):
            return c


def euclide(c, m):
    if (m == 0):
        return c
    else:
        return euclide(c, c % m)
def Euclidean_Algorithm(a, b):

    if a!=b:
        #.....
        if a > b:
            a = a-b
        else:
            b = b-a
    else:

        return a
def main():
    while True:

        num1 = int(input("Inserisci un numero : "))
        num2 = int(input("Inserisci il secondo numero : "))

        if control_input(num1) != True:
            logging.error(f"Numero non primo")
        elif control_input(num2) != True:
            logging.error(f"Numero non primo")
        else:
    return



if __name__ == "__main__":
    main()