import matplotlib.pyplot as plt


def main():
    numGraphs = 4
    abbyRuns = 6 # how many times we run over a data set for each graph
    abbyNums = []
    xAxis = [i for i in range(abbyRuns)]

    for i in range(numGraphs):
        graphNumsA = []
        for _ in range(abbyRuns):
            num = float(input())
            graphNumsA.append(num)
            # flush input
            input()
            input()
        abbyNums.append(graphNumsA)
    
    num = float(input()) # grab Mateo's number
    # mateoNums = [num for _ in range(abbyRuns)]
    
    fig = plt.figure()
    # ax = fig.add_axes(xAxis)
    bp =  plt.boxplot(abbyNums)
    print(abbyNums)
    plt.show()

    # plt.plot(xAxis, abbyNums, label="Approx Results")
    # plt.plot(xAxis, mateoNums, label="Exact Results")
    # plt.legend()
    # plt.show()
    plt.savefig("comparisonPlot")



if __name__ == "__main__":
    main()