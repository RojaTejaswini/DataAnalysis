import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

def clean_dataset(df, scale_numeric=True, encode_categorical=True):
    """
    Cleans a pandas DataFrame step by step:
    - Handles missing values
    - Fixes data types
    - Removes duplicates
    - Standardizes text columns
    - Handles outliers (IQR method for numeric cols)
    - Scales numeric data (optional)
    - Encodes categorical data (optional)
    
    Returns a cleaned DataFrame.
    """
    
    df = df.copy()  # Avoid modifying original
    
    # 1. Handle Missing Values
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    
    # 2. Fix Data Types
    for col in df.select_dtypes(include="object").columns:
        try:
            df[col] = pd.to_datetime(df[col], errors="ignore")
        except:
            pass
    
    # 3. Remove Duplicates
    df = df.drop_duplicates()
    
    # 4. Standardize Text Columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip().str.lower()
    
    # 5. Handle Outliers (numeric cols via IQR)
    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]
    
    # 6. Scale Numeric Data
    if scale_numeric:
        scaler = StandardScaler()
        for col in df.select_dtypes(include=["int64", "float64"]).columns:
            df[col + "_scaled"] = scaler.fit_transform(df[[col]])
    
    # 7. Encode Categorical Data
    if encode_categorical:
        le = LabelEncoder()
        for col in df.select_dtypes(include="object").columns:
            df[col + "_encoded"] = le.fit_transform(df[col])
    
    return df
