import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Configure page
st.set_page_config(
    page_title="Flight Price Predictor",
    page_icon="✈️",
    layout="wide"
)

@st.cache_resource
def load_model_artifacts():
    """Lazy load model artifacts only when needed"""
    try:
        with open('model_artifacts.pkl', 'rb') as f:
            artifacts = pickle.load(f)
        return artifacts['model'], artifacts['scaler'], artifacts['label_encoders'], artifacts['feature_order']
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None, None, None

@st.cache_data
def load_dataset():
    """Load dataset with caching"""
    try:
        df = pd.read_csv('Indian Airlines.csv')
        return df.loc[:, ~df.columns.str.contains('^Unnamed')]
    except Exception as e:
        st.error(f"Error loading dataset: {str(e)}")
        return None

# UI loads immediately - no model loading here
st.title("✈️ Flight Price Predictor")
st.markdown("Get instant flight price predictions using AI")

# Load dataset for dropdowns (lightweight)
df = load_dataset()
if df is None:
    st.stop()

# Input form
col1, col2 = st.columns(2)

with col1:
    airline = st.selectbox("Airline", df['airline'].unique())
    source_city = st.selectbox("Source City", df['source_city'].unique())
    departure_time = st.selectbox("Departure Time", df['departure_time'].unique())
    stops = st.selectbox("Stops", df['stops'].unique())

with col2:
    flight = st.selectbox("Flight Code", df['flight'].unique())
    destination_city = st.selectbox("Destination City", df['destination_city'].unique())
    arrival_time = st.selectbox("Arrival Time", df['arrival_time'].unique())
    class_type = st.selectbox("Class", df['class'].unique())

duration = st.number_input("Duration (hours)", min_value=0.5, value=2.0, step=0.5)
days_left = st.number_input("Days Left", min_value=1, value=7)

# Prediction button with lazy loading
if st.button("🔮 Predict Price"):
    with st.spinner('Loading AI model...'):
        # Model loads only when button is clicked
        model, scaler, label_encoders, feature_order = load_model_artifacts()
        
        if model is None:
            st.error("Failed to load model")
            st.stop()
    
    # Safe encoding function
    def safe_encode(value, column):
        try:
            return label_encoders[column].transform([value])[0]
        except:
            return -1
    
    # Prepare input
    input_data = {
        'airline': safe_encode(airline, 'airline'),
        'flight': safe_encode(flight, 'flight'),
        'source_city': safe_encode(source_city, 'source_city'),
        'departure_time': safe_encode(departure_time, 'departure_time'),
        'stops': safe_encode(stops, 'stops'),
        'arrival_time': safe_encode(arrival_time, 'arrival_time'),
        'destination_city': safe_encode(destination_city, 'destination_city'),
        'class': safe_encode(class_type, 'class'),
        'duration': duration,
        'days_left': days_left
    }
    
    input_df = pd.DataFrame([input_data], columns=feature_order)
    input_df[['duration', 'days_left']] = scaler.transform(input_df[['duration', 'days_left']])
    
    # Predict
    with st.spinner('Predicting...'):
        try:
            prediction = model.predict(input_df)[0]
            st.success(f"### Predicted Price: ₹{prediction:,.2f}")
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

st.markdown("---")
st.markdown("**AI-powered flight price prediction**")