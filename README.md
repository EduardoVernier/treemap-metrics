# Caching metrics
for d in $(cat tvcg-datasets.txt); do echo $d; time python3 Main.py cache-metrics $d; done;

# Star scatter
python3 Main.py scatter $(cat tvcg-datasets.txt)

# Matrices
python3 Main.py matrix $(cat tvcg-datasets.txt)