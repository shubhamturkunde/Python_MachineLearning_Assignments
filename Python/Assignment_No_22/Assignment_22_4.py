from multiprocessing import Pool
import time

def PowerSum(No):

    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i ** 5)

    return Sum

def main():

    Data = [1000000,2000000,3000000,4000000]

    Start = time.time()

    Pobj = Pool()

    Result = Pobj.map(PowerSum,Data)

    Pobj.close()
    Pobj.join()

    End = time.time()

    for i in range(len(Data)):
        print("Sum for",Data[i],"=",Result[i])

    print("Execution Time :",End-Start)

if __name__ == "__main__":
    main()