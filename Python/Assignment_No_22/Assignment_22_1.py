from multiprocessing import Pool

def SumSquare(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + (i * i)

    return Sum

def main():

    Data = [1000000,2000000,3000000,4000000]

    Pobj = Pool()

    Result = Pobj.map(SumSquare,Data)

    Pobj.close()
    Pobj.join()

    print(Result)

if __name__ == "__main__":
    main()