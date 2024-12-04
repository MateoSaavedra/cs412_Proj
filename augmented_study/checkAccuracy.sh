python genGraph.py

echo "Starting Abby's Code now"

# Run Abby code 6 times
python ../approx_solution/cs412_tsp_approx.py < graph > abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50

echo "Starting Mateo's code now"
python ../exact_solution/cs412_tsp_exact.py < graph > mateo.txt

echo "Run Complete"

# I keep Abby and Mateo's files separate so that I can keep track of things
cat abby.txt mateo.txt > results

echo "Plotting Results"

python plotResults.py < results
