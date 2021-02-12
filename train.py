import pandas as pd
import numpy as np
import argparse
import os
import joblib

from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core.run import Run

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data_path = "https://raw.githubusercontent.com/eparamasari/ML_Engineer_ND_Capstone/main/data/heart_failure_clinical_records_dataset.csv"
ds = TabularDatasetFactory.from_delimited_files(data_path)

# Saving model for current iteration
run = Run.get_context()

# Cleaning data
x_df = ds.to_pandas_dataframe().dropna()

y_df = x_df.pop("DEATH_EVENT")

# Splitting data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x_df, y_df, test_size=0.3, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test) 

def main():
    # Adding arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=int, default=20, help="The number of trees in the forest")
    parser.add_argument('--min_samples_split', type=int, default=2, help="The minimum number of samples required to split an internal node")
    
    args = parser.parse_args(args=[])
    
    run.log("The number of trees in the forest:", np.int(args.n_estimators))
    run.log("The minimum number of samples required to split an internal node:", np.int(args.min_samples_split))
    
    model = RandomForestClassifier(n_estimators=args.n_estimators, random_state=42, min_samples_split=args.min_samples_split).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("accuracy", float(accuracy))

    #Saving model for current iteration, including the value for n_estimators and min_samples_split in filename
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/model.pkl')

if __name__ == '__main__':
    main()