from multiprocessing import Pool
import os

def EvenCount(No):

    Count = 0

    for i in range(2, No+1, 2):
        Count = Count + 1

    print("Process ID :",os.getpid())
    print("Input Number :",No)
    print("Even Number Count :",Count)
    print("-------------------------")

def main():

    Data = [1000000,2000000,3000000,4000000]

    Pobj = Pool()

    Pobj.map(EvenCount,Data)

    Pobj.close()
    Pobj.join()

if __name__ == "__main__":
    main()