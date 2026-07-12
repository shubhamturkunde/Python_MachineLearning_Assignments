from multiprocessing import Pool
import os

def Factorial(No):

    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i

    print("Process ID :",os.getpid())
    print("Input Number :",No)
    print("Factorial :",Fact)
    print("-------------------------")

def main():

    Data = [10,15,20,25]

    Pobj = Pool()

    Pobj.map(Factorial,Data)

    Pobj.close()
    Pobj.join()

if __name__ == "__main__":
    main()