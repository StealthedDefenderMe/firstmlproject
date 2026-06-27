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
# When csv content changes hash value also get changes
# Thats why only .dvc files are tracked by git not the csv file because this is reference of data from my local
# Files are getting tracked from the reference: .dvc/cache
# Usually we store this data in remote location instead of local (s3 buckets) No matter how big it is