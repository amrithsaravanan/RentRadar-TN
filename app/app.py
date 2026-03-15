import streamlit as st
import pandas as pd
import joblib
import os
import time
import plotly.express as px

st.set_page_config(page_title="RentRadar TN | Home", page_icon="🏠", layout="wide")

# --- Custom CSS (Soft Bright Theme) ---
st.markdown("""
    <style>
    /* Soft Bright Theme */
    :root {
        --primary: #5AB2FF; 
        --secondary: #A0E9FF; 
        --accent: #FF9F66; 
        --bg: #F8FAFC;
    }
    .stApp { background-color: var(--bg); }
    
    /* --- THE DROPDOWN FIX --- */
    /* Forces the dropdown menus to be clickable and sit above other elements */
    div[data-baseweb="select"], div[data-baseweb="select"] > div {
        cursor: pointer !important;
        pointer-events: auto !important;
        z-index: 99 !important;
    }
    .stSelectbox, .stMultiSelect {
        position: relative;
        z-index: 99 !important;
    }
    /* ------------------------ */

    /* Modern Card Container */
    .listing-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #EDF2F7;
        transition: transform 0.3s ease;
    }
    .listing-card:hover { transform: translateY(-5px); }
    
    /* Custom Headers */
    .title-text {
        font-weight: 800;
        background: linear-gradient(90deg, #5AB2FF, #FF9F66);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Load Model & Data ---
@st.cache_resource
def load_assets():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, 'models', 'tn_rent_model.pkl')
    data_path = os.path.join(base_dir, 'data', 'tn_rental_data.csv')
    
    model = joblib.load(model_path) if os.path.exists(model_path) else None
    df = pd.read_csv(data_path) if os.path.exists(data_path) else pd.DataFrame()
    return model, df

model, df = load_assets()

# --- Header ---
st.markdown("<h1 class='main-header'>RentRadar Tamil Nadu</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Discover intelligent rental insights across the state.</p>", unsafe_allow_html=True)

# --- Tabs for Dashboard vs Prediction ---
tab1, tab2 = st.tabs(["🔮 AI Price Predictor", "📊 Market Dashboard"])

with tab1:
    st.markdown("### 🏡 Property Details")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        city = st.selectbox("City", ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore", "Thanjavur", "Hosur"])
        bhk = st.number_input("BHK", min_value=1, max_value=5, value=2)
        sqft = st.number_input("Square Feet", min_value=300, max_value=5000, value=1000, step=100)
    
    with col2:
        prop_type = st.selectbox("Property Type", ["Apartment", "Independent House", "Villa"])
        furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Furnished"])
        parking = st.radio("Parking Available?", ["Yes", "No"], horizontal=True)
        
    with col3:
        distance = st.slider("Distance to City Center (km)", 0.0, 20.0, 5.0, 0.5)
        asking_price = st.number_input("Landlord's Asking Rent (₹)", min_value=3000, value=15000, step=500)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    _, btn_col, _ = st.columns([1, 1, 1])
    with btn_col:
        analyze_btn = st.button("Calculate True Market Value", use_container_width=True)
        
    if analyze_btn and model:
        with st.spinner("Analyzing Tamil Nadu market trends..."):
            time.sleep(1)
            
        input_df = pd.DataFrame({
            'City': [city], 'BHK': [bhk], 'Sqft': [sqft], 
            'Property_Type': [prop_type], 'Furnishing': [furnishing], 
            'Parking': [parking], 'Distance_to_Center_km': [distance]
        })
        
        predicted_rent = model.predict(input_df)[0]
        diff = predicted_rent - asking_price
        
        st.divider()
        res1, res2, res3 = st.columns(3)
        res1.metric("Asking Rent", f"₹{asking_price:,.0f}")
        res2.metric("AI Estimated Rent", f"₹{predicted_rent:,.0f}", delta=f"₹{diff:,.0f} Variance")
        
        with res3:
            if diff > 1000:
                st.success("✨ **Great Deal!** Below market value.")
                st.balloons()
            elif diff < -1000:
                st.error("⚠️ **Overpriced.** Negotiate down.")
            else:
                st.info("🤝 **Fair Price.** Matches market rates.")

with tab2:
    if not df.empty:
        st.markdown("### 🗺️ Tamil Nadu Rental Map")
        # Interactive Map
        fig_map = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="Rent", size="Sqft",
                                    color_continuous_scale=px.colors.sequential.Teal, size_max=15, zoom=6,
                                    hover_data=["City", "BHK", "Property_Type"],
                                    mapbox_style="carto-positron")
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)
        
        st.divider()
        st.markdown("### 📈 Market Trends")
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Avg Rent by City
            avg_rent = df.groupby('City')['Rent'].mean().reset_index().sort_values('Rent', ascending=True)
            fig_bar = px.bar(avg_rent, x='Rent', y='City', orientation='h', title="Average Rent by City (₹)",
                             color='Rent', color_continuous_scale=px.colors.sequential.Mint)
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col_chart2:
            # Rent vs Sqft
            fig_scatter = px.scatter(df, x="Sqft", y="Rent", color="City", title="Rent vs. Square Footage",
                                     opacity=0.6, trendline="ols")
            st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Data not found. Please run the data generation script.")
        