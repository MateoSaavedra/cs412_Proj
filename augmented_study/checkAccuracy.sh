echo 8 | python genGraph.py

echo "Testing with 8 vertices"
echo "Running Approximate Solution"

# Run Abby code 6 times
python ../approx_solution/cs412_tsp_approx.py < graph > abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50

echo "Running Exact Solution"
python ../exact_solution/cs412_tsp_exact.py < graph > mateo.txt

echo "Run Complete"
##############################################################################
echo 10 | python genGraph.py

echo "Testing with 10 vertices"
echo "Running Approximate Solution"

# Run Abby code 6 times
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50

echo "Running Exact Solution"
python ../exact_solution/cs412_tsp_exact.py < graph >> mateo.txt

echo "Run Complete"
##############################################################################
echo 12 | python genGraph.py

echo "Testing with 12 vertices"
echo "Running Approximate Solution"

# Run Abby code 6 times
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50

echo "Running Exact Solution"
python ../exact_solution/cs412_tsp_exact.py < graph >> mateo.txt

echo "Run Complete"
##############################################################################
echo 14 | python genGraph.py

echo "Testing with 14 vertices"
echo "Running Approximate Solution"

# Run Abby code 6 times
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50
python ../approx_solution/cs412_tsp_approx.py < graph >> abby.txt -s 50

echo "Running Exact Solution"
python ../exact_solution/cs412_tsp_exact.py < graph >> mateo.txt

echo "Run Complete"

# I keep Abby and Mateo's files separate so that I can keep track of things
cat abby.txt mateo.txt > results

echo "Plotting Results"

python plotResults.py < results

echo "Plot saved to comparisonPlot.png"
