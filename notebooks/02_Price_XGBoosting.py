import pandas as pd
import joblib
import os
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'tn_rental_data.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'tn_rent_model.pkl')

print("--- Training Tamil Nadu Rental Model ---")
df = pd.read_csv(DATA_PATH)

X = df.drop(columns=['Rent', 'Latitude', 'Longitude']) # Exclude coords from model, keep for map
y = df['Rent']

numeric_features = ['BHK', 'Sqft', 'Distance_to_Center_km']
categorical_features = ['City', 'Property_Type', 'Furnishing', 'Parking']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', XGBRegressor(n_estimators=150, max_depth=5, learning_rate=0.1, random_state=42))
])

pipeline.fit(X, y)

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"🚀 SUCCESS: TN Model saved at {MODEL_PATH}")