echo Reproduce figures and tables in paper: "Robust soft sensor development based on Dirichlet process mixture of regression model for multimode processes".
echo

cd ./NumericalEx
echo 1. Numerical example
echo
echo Simulation Data
cd ./Simulation
bash run.sh

echo
echo Results of 50 simulation runs
cd ../Result_50Runs
bash run.sh

echo
echo Results of the first simulation run
cd ../Result_firstRun
bash run.sh

echo
cd ../../DistillationCol/MPD_softsens
echo 2. Soft sensor modeling for m-diaminobenzene concentration
bash run.sh

echo
cd ../PPD_softsens
echo 3. Soft sensor modeling for p-diaminobenzene concentration
bash run.sh