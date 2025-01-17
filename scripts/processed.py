from sklearn.preprocessing import LabelEncoder

def encode_features(df, features):
    """
    Applies LabelEncoder to a set of columns in a DataFrame.

    Parameters:
    df (DataFrame): The DataFrame containing the data to be encoded.
    features (list): List of column names to be encoded.

    Returns:
    DataFrame: The DataFrame with the encoded columns.
    """
    le = LabelEncoder()
    for col in features:
        df[col] = le.fit_transform(df[col])
    return df