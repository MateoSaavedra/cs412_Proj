To run cs412_tsp_approx.py, you can either run the program from the command line without any additional arguments, or utilize the '-s' or '--shuffle' flags.
If you run the program without the flag, the SHUFFLE parameter will default to 50, meaning the order of traversal will be shuffled 50 times prior to testing individual permutations. 
Otherwise, you can pass a specific number to the shuffle parameter to customize the amount of shuffles performed on the graph. 
The assumption is that more shuffles will result in an answer closer to that of the optimal solution. 

to run test_cases/graph_generator.py, you can run the program from the command line and enter the amount of graphs desired as the first line of input. Different test case files will then be generated (with v ranging from 4 to 10) and labeled as "test{x}.txt" with x being the number in the sequence of test graphs generated-1. The final 1 test case will generate a graph of 1010 vertices for stress testing purposes. 