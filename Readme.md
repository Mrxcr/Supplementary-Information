## Supplementary information for Paper "Robust soft sensor development based on Dirichlet process mixture of regression model for multimode processes"

This file outlines the data sources and the reproducibility of all figures and tables presented paper "Robust soft sensor development based on Dirichlet process mixture of regression model for multimode processes".


This repository contains the source data and the code necessary to reproduce all figures and tables in the manuscript and the supplementary material. This repository includes two directories: `NumericalEx` and `DistillationCol`. The former contains the materials related to the numerical example presented in Section 4 of the manuscript, while the later contains the materials for the industrial application in Section 5. To reproduce the figures and tables, run the script `SuppMaterial/un.sh` from the terminal. Prior to executing the code, several Python packages must be installed, and these dependencies are listed in the `requirements.txt` file. If the script executes successfully, the terminal will display the following information:

```bash
$ bash run.sh
Reproduce figures and tables in paper: Robust soft sensor development based on Dirichlet process mixture of regression model for multimode processes.

1. Numerical example

Simulation Data
Generating Figures F1, F2
Save simulation data at data/simulation.csv.
Save Figure F1 at Figures/Figure F1.png.
Save Figure F2 at Figures/Figure F2.png.

Results of 50 simulation runs
Generating Figures 2 5 and 6
Save Figure 2 at Figures/Figure 2.png.
Save Figure 6 at Figures/Figure 6.png.
Save Figure 5 at Figures/Figure 5.png.

Results of the first simulation run
Generating Figures 3 and 4
Save Figure 3 at Figures/Figure3_GMR.png.
Save Figure 3 at Figures/Figure3_DPMRM.png.
Save Figure 3 at Figures/Figure3_DPIRMRM.png.
Save Figure 3 at Figures/Figure3_DPORMRM.png.
Save Figure 3 at Figures/Figure3_DPR2MRM.png.
Save Figure 4 at Figures/Figure 4.png.

2. Soft sensor modeling for m-diaminobenzene concentration
Generating Figures 7, 8, 9, G1 and Table 1
Save the predicted values for MPD at data/MPD_inversed.csv.


-------------------------Table 1------------------------
GMR on the testing set, RMSE: 114.04, MAE: 90.94
DPMRM on the testing set, RMSE: 110.38, MAE: 92.34
DPIRMRM on the testing set, RMSE: 109.82, MAE: 91.72
DPORMRM on the testing set, RMSE: 100.34, MAE: 79.58
DPR2MRM on the testing set, RMSE: 82.45, MAE: 65.81


Save Figure 7 at Figures/Figure7.png.
Save Figure 8 at Figures/Figure8_2176.png.
Save Figure 8 at Figures/Figure8_1500.png.
Save Figure 9 at Figures/Figure9.png.
Save Figure G1 at Figures/FigureG1.png.

3. Soft sensor modeling for p-diaminobenzene concentration
Generating Figures 10, 11 and Table 2
Save Figure 10 at Figures/Figure10.png.
Save Figure 11 at Figures/Figure11.png.


-------------------------Table 2------------------------
GMR on the testing set, RMSE: 37.48, MAE: 26.44
DPMRM on the testing set, RMSE: 25.59, MAE: 20.83
DPIRMRM on the testing set, RMSE: 19.59, MAE: 14.90
DPORMRM on the testing set, RMSE: 19.27, MAE: 15.46
DPR2MRM on the testing set, RMSE: 17.17, MAE: 12.22
```

Note that HTML files have also been generated for each figure. These files can be opened in a web browser, allowing for interactive exploration of the figures. Detailed descriptions of the supplementary information are provided as follows, which can also be found in the `Readme.md` file.


## Section H.1. Materials for Numerical Example 

The materials corresponding to the numerical example in Section 4 are stored in the `NumericalEx` folder. The structure of this folder is illustrated below:

```
  --- NumbericalEx
  ------ simulation 
  ------------ data
  ------------ Figures
  ------------ generateData.py
  ------------ run.sh
  ------ Result_firstRun
  ------------ data
  ------------ Figures
  ------------ process.py
  ------------ run.sh
  ------ Result_50Runs
  ------------ data
  ------------ Figures
  ------------ process.py
  ------------ run.sh
  ```

The `NumericalEx` folder contains three subfolders: `simulation`, `Result_firstRun`, and `Result_50Runs`. Each subfolder includes a data folder, a Figures folder, and a script named `run.sh`. Running `run.sh` in the terminal will generate the corresponding data and figures, which will be saved in the respective data and Figures folders.
In the `NumbericalEx/simulation` folder, the script `run.sh` can be executed to generate the simulation data used in Section 4 of the manuscript. The resulting data will be saved as `NumericalEx/simulation/data/simulation.csv`, while **Figures F1** and **F2** will be stored in the `NumericalEx/simulation/Figures` folder. Note that multiple simulations can be performed by modifying the random seed in the script `NumbericalEx/simulation/generateData.py`. In this way, we conducted 50 simulations, and the corresponding results from different models are stored in the `NumericalEx/Result_50Runs/data` folder. This folder contains five CSV files, each representing the results of one model across all simulations, including prediction MSE, the estimated number of components, and the estimated model weights. In the `NumericalEx/Result_50Runs` directory, the script `run.sh` can be executed to read the data and generate **Figures 2**, **5**, and **6** in the manuscript.
The `NumbericalEx/Result_firstRun/data` folder contains the results of different models from the first simulation, which are used to generate **Figure 3** and **4** in the manuscript. Within each subfolder of the `NumbericalEx/Result_firstRun/data` folder, there are six *.npy* file. The descriptions of these files are provided below (taking the subfolder `NumbericalEx/Result_firstRun/data/DPR2MRM` as an example):

```
list_com_DPIRMRM.npy: An array recording the component numbers during the training process.
list_idx.npy: A mode ID array indicating which mode a sample belongs to, based on the posterior probability $p(s_{N+1}=c|x_(N+1))$.
mat_epl.npy: An array derived from the predicted covariance matrices, used to draw ellipses for each mode.
mat_epl_true.npy: An array derived from the true covariance matrices, used to draw ellipses for each mode.
mean_pred.npy: An array containing the predicted mean for each mode.
Xt.npy: A two-dimensional array of simulation data.
```

The script run.sh can be executed to read the data in `NumericalEx/Result_firstRun/data` and generate **Figures 3** and **4** in the manuscript.


## Section H.2. Materials for Industrial Applications


The materials corresponding to the industrial applications discussed in Section 5 are stored in the `DistillationCol` folder. The structure of this folder is shown below:

```
  --- DistillationCol
  ------ MPD_softsens
  ------------ data
  ------------ Figures
  ------------ process.py
  ------------ run.sh
  ------ PPD_softsens
  ------------ data
  ------------ Figures
  ------------ process.py
  ------------ run.sh
```

The subfolder `MPD_softsens` and `PPD_softsens` contains materials for Section 5.1 and Section 5.2, respectively. 

  The `MPD_softsens/data` folder contains the following seven csv files:
  ```
  MPD.csv
  MPD_inversed.csv
  train_DPIRMRM.csv
  train_DPMRM.csv
  train_DPORMRM.csv
  train_DPR2MRM.csv
  ```
The `MPD.csv` file saves the m-diaminobenzene predictions along with confidence intervals given by different models on the testing set. Note that the data in `MPD.csv` are pre-normalized. Running the script `DistillationCol/MPD_softsens/run.sh` will perform the reverse normalization, and the resulting data will be saved in `MPD_inversed.csv`. Moreover, **Figures 7**, **8**, **9** and **Table 1** will be reproduced based on the reverse-normalized data in `MPD_inversed.csv`. While a snippet of the predictions on the testing set, within the range of [0, 1500], is presented in the manuscript, the complete results for the full testing set are available in **Figure8_2176.png**.
 The dataset `train_DPMRM.csv`, `train_DPIRMRM.csv`, `train_DPORMRM.csv` and `train_DPR2MRM.csv` record the ELBO value and estimated number of components throughout the training process of the four DPM-based models, respectively. These datasets will be used to generate **Figure 7**. The `df_qq.csv` file contains historical data for four variables: T35111_MPD.PV, TI35112.PV, TI35111a3.PV and TI35111a9.PV, which will be used to generate the normal probability plots in **Figure G1**. 
  The `PPD_softsens/data` folder contains a single CSV file, PPD.csv, which records p-diaminobenzene predictions along with confidence intervals given by different models on the testing set. Running the script `DistillationCol/PPD_softsens/run.sh` will read the data and reproduce **Figures 10**, **11** and **Table 2** in the manuscript.

  Note that the historical data for process and quality variables in `MPD_softsens/data/MPD.csv`, `MPD_softsens/data/df_qq.csv` and `PPD_softsens/data/PPD.csv` were collected from the database of the distribution control system (DCS) of the distillation process.
