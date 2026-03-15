import numpy as np
import pandas as pd

def vectorized_haversine(lat1: pd.Series, lon1: pd.Series, 
                         lat2: float, lon2: float) -> pd.Series:
    """
    Calculates the great-circle distance between two points on the Earth surface.
    Fully vectorized with Numpy for blazing fast execution.
    """
    # Earth radius in kilometers
    R = 6371.0 

    # Convert degrees to radians
    lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
    lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Haversine formula
    a = np.sin(dlat / 2.0)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

def engineer_features(df: pd.DataFrame, city_center_lat: float, city_center_lon: float) -> pd.DataFrame:
    """Generates new predictive features."""
    df = df.copy()
    
    # Calculate distance to downtown (Highly predictive for rent price)
    df['dist_to_center_km'] = vectorized_haversine(
        df['latitude'], df['longitude'], city_center_lat, city_center_lon
    )
    
    # Feature crossing: Value metrics
    df['beds_to_baths_ratio'] = df['bedrooms'] / (df['bathrooms'] + 0.1) # Add 0.1 to avoid div by zero
    
    return df