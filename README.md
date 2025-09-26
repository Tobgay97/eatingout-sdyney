echo "# Predictive Modelling of Eating-Out (Sydney)

## Setup
conda install -c conda-forge pandas numpy scikit-learn matplotlib plotly geopandas pyspark -y

## Run
Open notebooks in Jupyter and execute cells.

## Expected Results
- Part A: EDA summaries & plots
- Part B: Regression MSE and Classification metrics (Precision/Recall/F1)
- Part B(4) PySpark: MSE + Confusion Matrix, Precision/Recall/F1

" > README.md

git add README.md
git commit -m "Add README"
git push
