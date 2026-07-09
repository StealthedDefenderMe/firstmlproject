## End to end data science project

## setup.py
# Used to make a package of the application.
# This contains all the information about the package as well. e.g. : Author, version
# This package can be pulled on pypi too (open source)
# or you can say overall basic information of the application is seen in setup.py


# T2
# Here we'll write a code to create folder structure in python
# Pipeline -
# Training pipeline : follow lifecycle of DS, read data, model train & ready. EDA, feature engineering, model training and evaluation & deployement
# Prediction pipeline : i/p => model => o/p

# In training pipeline below components are included
# Data source (mySQL, mongoDB)
# Data injection: Read from database & train_test_split
# data tansformation: for EDA & feature engineering. (Handling of missing, duplicate, outliers values, EDA, feature selection)
# Model Trainer: Multiple models to train
# Model monitoring: Tool => Evidently AI (Open source tool) + CI/CD pipeline with GitHubActions

# T6
# here we will see how to track data using DVC (Data version control): Open Source
# Data could be huge so it'd be impossible to track it using git, so dvc
# data could be saved in different db or hadoop
# Only for development purpose (pip install dvc)
# We'll only track files from artifacts
# Why dvc? To track records in your .csv file
# Commands : 
<!-- dvc init -->
<!-- dvc add <path to file (artifacts.raw.csv)> --> 
# a folder cannot be tracked by both dvc & git, make sure folder is removed from git tracking.
# After this only .dvc files from the artifacts folder will be committed to git not original csv files
# Whenever dvc tracks any file it creates md5 with respect to content of the file which is hash value
# To work as said above run 2nd command again
# When csv content changes hash value also get changes
# Thats why only .dvc files are tracked by git not the csv file because this is reference of data from my local
# Files are getting tracked from the reference: .dvc/cache
# Usually we store this data in remote location instead of local (s3 buckets) No matter how big it is

# T7 
# Based on EDA & model trainigs
# Install ipykernel for using notebook

# T7
# Everything will be in pipeline format (Data Trasnformation)
# DT is more about feature engineering. Here we'll check everythign as T6 but in pipeline format


# T10
# To integrate mlflow tracking getting included
# No matter how many times model trains with new data i should be knowing the r2_score & experiment & track model performance
# To check its accuracy and evaluation metrics
# Track all above things we use mlflow
# mlFlow is open source platform for entire machine learning lifecycle
# There is one public repository "dagshub"
# Here we'll connect that specific repository & through that we'll track this repository
# By using the URL we can clearly track the how model is performing with respect to every model training

# mlFlow tracking details (Keep this in .env variable only)
# MLFLOW_TRACKING_URI=https://dagshub.com/StealthedDefenderMe/firstmlproject.mlflow
# MLFLOW_TRACKING_USERNAME=StealthedDefenderMe
# MLFLOW_TRACKING_PASSWORD=4b56e764a67aba0f491ab04b86df49ccc7423c39
# python script.py