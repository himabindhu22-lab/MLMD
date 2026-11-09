#preprocessing.py
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import make_classification
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.model_selection import train_test_split
def create_pipeline():
  #Define which features are numeric vs categorical
  numeric_features=['age','income']
  categorical_features=['city','occupation']
#preprocessing for numerical data (impute missing,then scale)
numeric_transformer=Pipeline(steps=[('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler())
                                   ])
#preprocessing for categorical data(impute missing, then one-hot encode)
categorical_transformer=Pipeline(steps=[('imputer',SimpleImputer(strategy='constant',fill_value='missing')),('onehot',OneHotEncoder(handle_unknown='ignore'))
                                       ])
#combine into a single ColumnTransformer preprocessor= ColumnTransformer(transformers=[('num',numeric_transformer,numeric_features),('cat',categorical_transformer,categorical_features)
])
  return preprocessor
if_name_=="-main_":
 print("Preprocessing pipeline template ready.")
