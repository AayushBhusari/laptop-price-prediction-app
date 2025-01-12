import streamlit as st
import pandas as pd
import pickle

st.title('Laptop Price Prediction App')

# Inputs
brand = st.selectbox('Brand', ['MSI', 'Acer', 'Razer', 'Other'])
cpu = st.selectbox('CPU', ['AMD', 'Intel', 'Other'])
gpu = st.selectbox('GPU', ['Intel', 'AMD', 'Nvidia', 'Other'])
device_type = st.selectbox('Type', ['Workstation', 'Ultrabook', 'Gaming', 'Notebook', 'Other'])
memory_type = st.selectbox('Memory Type', ['Flash', 'HDD', 'SSD', 'Notebook', 'Other'])
weight = st.number_input('Weight', min_value=0.0, format="%.2f")
cpu_frequency = st.number_input('CPU Frequency', min_value=0.0, format="%.2f")
ram = st.number_input('Ram', min_value=0, step=1)
screen_height = st.number_input('Screen Height', min_value=0, step=1)
screen_width = st.number_input('Screen Width', min_value=0, step=1)

# Function to prepare input
def prepare_model_input(brand, cpu, gpu, device_type, memory_type, weight, cpu_frequency, ram, screen_height, screen_width):
    columns = [
        'MSI', 'AMD_CPU', 'Intel_CPU', 'Intel_GPU', 'AMD_GPU', 'Acer', 'Weight', 'Flash',
        'Razer', 'Workstation', 'Ultrabook', 'Nvidia_GPU', 'Gaming', 'HDD', 'CPU Frequency',
        'SSD', 'Notebook', 'Screen Height', 'Screen Width', 'Ram'
    ]
    data = {col: 0 for col in columns}

    # Map brand
    if brand == 'MSI':
        data['MSI'] = 1
    elif brand == 'Acer':
        data['Acer'] = 1
    elif brand == 'Razer':
        data['Razer'] = 1

    # Map CPU
    if cpu == 'AMD':
        data['AMD_CPU'] = 1
    elif cpu == 'Intel':
        data['Intel_CPU'] = 1

    # Map GPU
    if gpu == 'Intel':
        data['Intel_GPU'] = 1
    elif gpu == 'AMD':
        data['AMD_GPU'] = 1
    elif gpu == 'Nvidia':
        data['Nvidia_GPU'] = 1

    # Map device type
    if device_type == 'Workstation':
        data['Workstation'] = 1
    elif device_type == 'Ultrabook':
        data['Ultrabook'] = 1
    elif device_type == 'Gaming':
        data['Gaming'] = 1
    elif device_type == 'Notebook':
        data['Notebook'] = 1

    # Map memory type
    if memory_type == 'Flash':
        data['Flash'] = 1
    elif memory_type == 'HDD':
        data['HDD'] = 1
    elif memory_type == 'SSD':
        data['SSD'] = 1

    # Numeric features
    data['Weight'] = weight
    data['CPU Frequency'] = cpu_frequency
    data['Ram'] = ram
    data['Screen Height'] = screen_height
    data['Screen Width'] = screen_width

    return pd.DataFrame([data])

# Prepare input
input_df = prepare_model_input(brand, cpu, gpu, device_type, memory_type, weight, cpu_frequency, ram, screen_height, screen_width)
st.dataframe(input_df)

# Load the scaler and model
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

if st.button('Predict Price'):
    try:
        # Scale the input
        input_scaled = scaler.transform(input_df)
        # Predict the price
        pred = model.predict(input_scaled)
        st.write(f'The predicted price is €{pred[0]:.2f} which equals to ₹{pred[0] * 83.0:.2f}')
        st.write(f'This Model was Trained on European Data, so may not perform that well according to Indian Market')
    except Exception as error:
        st.error(f"An error occurred: {error}")
