import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Car Price Prediction",page_icon='car.png')
st.title("Car Price Prediction App")
st.write("Enter car details below to predict the price:")

# Load trained model
with open('rfmodel.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the original dataset to get options for dropdowns
df = pd.read_csv('Copied_Car_Price_Prediction.csv')

# Get unique 
car_models = sorted(df['Model'].unique())  
fuel_types = sorted(df['Fuel Type'].unique())
transmissions = sorted(df['Transmission'].unique())  

with st.container(border=True):
    col1, col2 = st.columns(2)
    
    # Left column
    selected_model = col1.selectbox("Select Car Model:", car_models)  
    engine_size = col1.slider("Engine Size (liters):", min_value=1.0, max_value=5.0, step=0.1)
    fuel_type = col1.radio("Fuel Type:", fuel_types)
    
    # Right column
    mileage = col2.number_input("Mileage (km):", min_value=100)
    transmission = col2.selectbox("Transmission:", options=transmissions)
    car_age = col2.number_input("Car Age (years):",min_value=5)

models_list = list(df['Model'].unique())
models_list.sort()
fuels_list = list(df['Fuel Type'].unique())
fuels_list.sort()
trans_list = list(df['Transmission'].unique())
trans_list.sort()

c1, c2, c3 = st.columns([1.6, 1.5, 1])

if c2.button('predict_price'):
    input_values = [(models_list.index(selected_model), engine_size, mileage, 
                    fuels_list.index(fuel_type), trans_list.index(transmission), car_age)]
    
    out = model.predict(input_values)
    st.info(f"💰 Estimated Price: ₹ {out[0]}")
