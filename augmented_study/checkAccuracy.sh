python genGraph.py

echo "Starting Abby's Code now"
python ../approx_solution/cs412_tsp_approx.py < graph > abby.txt

echo "Starting Mateo's code now"
python ../exact_solution/cs412_tsp_exact.py < graph > mateo.txt

echo "Run Complete"

echo "Plotting Results"

## generate a lot of different graphs
## show how they differ