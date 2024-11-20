To run cs412_tsp_approx.py, you can either run the program from the command line without any additional arguments, or utilize the '-s' or '--shuffle' flags.
If you run the program without the flag, the SHUFFLE parameter will default to 20, meaning the order of traversal will be shuffled 20 times prior to testing individual permutations. 
Otherwise, you can pass a specific number to the shuffle parameter to customize the amount of shuffles performed on the graph. 
The assumption is that more shuffles will result in an answer closer to that of the optimal solution. 