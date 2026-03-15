# 🏙️ RentRadar TN | AI Real Estate Valuation Engine

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0+-green.svg)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-informational)

**RentRadar TN** is a modern **AI-powered data science dashboard** designed to analyze and predict rental prices across major cities in **Tamil Nadu, India**.

The system uses **Machine Learning (XGBoost Regression)** to estimate the fair rental price of a property based on key features such as **BHK, Square Footage, Property Type, and Distance from the City Center**.

Whether you're evaluating an apartment in **Chennai**, a villa in **Coimbatore**, or an independent house in **Madurai**, RentRadar can tell you if the landlord's price is a **Steal, Fair, or Overpriced**.

---

# ✨ Key Features

### 🔮 AI Rent Predictor

Predicts the **fair market rent** of a property using a trained **XGBoost Regression model**.

Inputs include:

* BHK
* Square Footage
* Property Type
* Distance to City Center
* City

---

### 🗺️ Geospatial Analytics

Interactive **Plotly Mapbox visualization** showing rental clusters across Tamil Nadu.

Users can explore:

* Rent distribution
* Property locations
* City-wise rental density

---

### 📊 Market Analytics Dashboard

Dynamic visualizations built using **Plotly** including:

* Average Rent by City
* Rent vs Square Footage
* Price per Square Foot Trends
* Property Type Distribution

---

### 🎨 Modern UI/UX

The dashboard is built using **Streamlit** with:

* Soft bright color theme
* Glassmorphism containers
* Smooth UI layout
* Interactive filters and widgets

---

# 🗂️ Project Architecture

This project follows structured **data science project architecture**.

```
rent-radar-tn/
│
├── app/                  # Streamlit dashboard frontend
│   └── app.py
│
├── data/                 # Tamil Nadu rental datasets (.csv)
│
├── models/               # Trained XGBoost models (.pkl)
│
├── notebooks/            # EDA and model training notebooks
│
├── src/                  # Core python modules
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   └── model_training.py
│
├── .streamlit/           # Streamlit theme configuration
│   └── config.toml
│
├── requirements.txt      # Python dependencies
│
└── README.md             # Project documentation
```

---

# 📊 Dataset

The dataset contains **synthetic and cleaned rental listings from major Tamil Nadu cities**.

### Cities Included

* Chennai
* Coimbatore
* Madurai
* Tiruchirappalli (Trichy)
* Salem
* Tiruppur
* Erode
* Vellore
* Hosur
* Thanjavur

### Dataset Features

| Feature            | Description                              |
| ------------------ | ---------------------------------------- |
| City               | City where the property is located       |
| Area               | Locality within the city                 |
| BHK                | Number of bedrooms                       |
| Square Feet        | Size of the property                     |
| Property Type      | Apartment / House / Villa                |
| Furnishing         | Furnished / Semi-Furnished / Unfurnished |
| Parking            | Parking availability                     |
| Distance to Center | Distance from city center                |
| Rent               | Monthly rent price (target variable)     |

---

# 🤖 Machine Learning Model

### Model Used

**XGBoost Regressor**

XGBoost was chosen because it performs well for **tabular data regression problems** and handles feature interactions effectively.

### Model Pipeline

Data Collection
→ Data Cleaning
→ Feature Engineering
→ Train/Test Split
→ Model Training
→ Model Evaluation
→ Model Serialization (.pkl)

### Evaluation Metrics

| Metric   | Description                |
| -------- | -------------------------- |
| RMSE     | Root Mean Squared Error    |
| R² Score | Model accuracy measurement |

---

# 📈 Dashboard Insights

The application provides key rental market insights such as:

* City-wise average rent comparison
* Rent vs square feet correlation
* Rental density maps
* Property type distribution
* AI-based rent prediction

These insights help users **understand rental trends across Tamil Nadu**.

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/rent-radar-tn.git
cd rent-radar-tn
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# 🚀 Run the Application

Start the Streamlit dashboard:

```
streamlit run app/app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 📸 Dashboard Preview

### Market Analytics Dashboard

(Add screenshot here)

### AI Rent Prediction Tool

(Add screenshot here)

### Rental Heatmap

(Add screenshot here)

---

# 🚧 Future Improvements

Planned improvements include:

* Real rental data integration from property APIs
* Deep learning rent prediction models
* District-level Tamil Nadu analytics
* Time-series rental trend forecasting
* Cloud deployment (AWS / Streamlit Cloud)

---

# 🧑‍💻 Author

Amrith S S

Data Science | Machine Learning | AI Applications

GitHub: https://github.com/amrithsaravanan

---

# 📜 License

This project is licensed under the **MIT License**.
