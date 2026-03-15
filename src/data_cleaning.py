import pandas as pd

def clean_listings(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans raw apartment listings, dropping invalid rows in O(N) time."""
    # Drop rows missing crucial price or target variables
    df = df.dropna(subset=['price', 'bedrooms', 'bathrooms', 'latitude', 'longitude'])
    
    # Fast filtering of absurd outliers (e.g., $0 rent or 50 bedrooms)
    df = df[(df['price'] > 100) & (df['price'] < 15000)]
    df = df[(df['bedrooms'] < 10) & (df['bathrooms'] < 10)]
    
    # Ensure types are optimized
    df['price'] = df['price'].astype('float32')
    df['bedrooms'] = df['bedrooms'].astype('int8')
    
    return df