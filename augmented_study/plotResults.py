import matplotlib.pyplot as plt


def main():
    abbyRuns = 6
    abbyNums = []
    xAxis = [i for i in range(abbyRuns)]
    for _ in range(abbyRuns):
        num = float(input())
        abbyNums.append(num)
        # flush input
        input()
        input()
    
    num = float(input()) # grab Mateo's number
    mateoNums = [num for _ in range(abbyRuns)]
    

    plt.plot(xAxis, abbyNums, label="Approx Results")
    plt.plot(xAxis, mateoNums, label="Exact Results")
    plt.legend()
    plt.show()
    plt.savefig("comparisonPlot")



if __name__ == "__main__":
    main()