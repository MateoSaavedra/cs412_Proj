import matplotlib.pyplot as plt


def main():
    numGraphs = 4
    abbyRuns = 6 # how many times we run over a data set for each graph
    abbyNums = []
    mateoNums = []
    startingSize = 6 # this is the number of vertices in the first graph
    xAxis = [startingSize + (i * 2) for i in range(numGraphs)]

    # Get approximate data
    for i in range(numGraphs):
        graphNumsA = []
        for _ in range(abbyRuns):
            num = float(input())
            graphNumsA.append(num)
            # flush input
            input()
            input()
        abbyNums.append(graphNumsA)
    
    # Get exact data
    for i in range(numGraphs):
        num = float(input()) # grab Mateo's number
        mateoNums.append(num)
        input() # skip the next input
    
    plt.figure()
    plt.boxplot(abbyNums, positions = xAxis)
    plt.plot(xAxis, mateoNums)
    plt.title("Comparison of the Aproximate vs Exact Solutions (TSP)")
    plt.xlabel("Graph Size (# of Vertices)")
    plt.ylabel("Shortest Path Length")
    plt.show()
    plt.savefig("comparisonPlot")



if __name__ == "__main__":
    main()