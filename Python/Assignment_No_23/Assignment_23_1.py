from multiprocessing import Pool
import os

def EvenSum(No):

    Sum = 0

    for i in range(2, No+1, 2):
        Sum = Sum + i

    print("Process ID :",os.getpid())
    print("Input Number :",No)
    print("Sum of Even Numbers :",Sum)
    print("-------------------------")

def main():

    Data = [1000000,2000000,3000000,4000000]

    Pobj = Pool()

    Pobj.map(EvenSum,Data)

    Pobj.close()
    Pobj.join()

if __name__ == "__main__":
    main()