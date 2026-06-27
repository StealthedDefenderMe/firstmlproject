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