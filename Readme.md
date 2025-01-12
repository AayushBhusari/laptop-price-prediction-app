# Laptop Price Prediction App

The **Laptop Price Prediction App** is a web-based application built with **Streamlit** that helps predict laptop prices based on various hardware and configuration parameters. Users can input details such as brand, CPU, GPU, weight, screen size, and more to get an estimated price for a laptop.

---

## Features

- **Predict Laptop Price**: Input laptop specifications (brand, CPU, GPU, weight, etc.) to get an estimated price.
- **Interactive User Interface**: A simple and user-friendly interface built with Streamlit.
- **Real-time Prediction**: Get instant predictions as you submit laptop configuration details.
- **Model-Based Predictions**: The app uses a pre-trained Random Forest model to predict laptop prices.
- **Scalable Input**: Easily handle multiple features and user input types (categorical, numerical).
- **Error Handling**: Clear error messages to guide users in case of invalid input.

---

## Future Improvements

- **Improved Model**: Upgrade to a more advanced machine learning model for better predictions.
- **Additional Features**: Add more laptop features such as battery life, brand reputation, etc.
- **Multi-Region Support**: Implement region-based predictions (e.g., different pricing for various countries).
- **Model Explainability**: Display model predictions with explanations on feature importance.

---

## Installation

Follow these steps to set up the Laptop Price Prediction App on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/laptop-price-prediction.git
   cd laptop-price-prediction
   ```

2. **Install Dependencies**:
   The app requires `Streamlit`, `pandas`, `sklearn`, and `pickle`. Install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Model Files**:
   Make sure to download the pre-trained model and scaler files (`model.pkl` and `scaler.pkl`). You can get them from the releases section or the project’s Google Drive link.

4. **Run the App**:
   Start the Streamlit app using the following command:

   ```bash
   streamlit run app.py
   ```

5. **Access the App**:
   Once the app is running, open your browser and go to:
   ```
   http://localhost:8501
   ```

---

## Usage

After running the app, you'll be able to input laptop specifications such as brand, CPU, GPU, weight, and screen size. Press **"Predict Price"** to get an estimated price for the laptop.

### Example Steps:

1. **Select Brand**: Choose from the available brands (e.g., MSI, Acer, Razer).
2. **Select CPU**: Choose from available CPUs (e.g., AMD, Intel).
3. **Select GPU**: Choose the laptop’s GPU (e.g., Intel, AMD, Nvidia).
4. **Enter Numerical Details**: Input weight, CPU frequency, screen dimensions, and RAM.
5. **Click "Predict Price"**: See the predicted price displayed instantly.

---

## Examples

### Example 1: Predicting Price

1. **Input**:

   - Brand: MSI
   - CPU: AMD
   - GPU: Intel
   - Device Type: Workstation
   - Memory Type: Flash
   - Weight: 2.5 kg
   - CPU Frequency: 3.6 GHz
   - RAM: 16 GB
   - Screen Height: 1080 px
   - Screen Width: 1920 px

2. **Output**:
   - The predicted price is $1200.50

### Example 2: Input Error Handling

If you input an invalid weight (e.g., a negative value), the app will display an error message and prompt you to correct the input.

---

## Contributing

Contributions to the Laptop Price Prediction App are welcome! If you have suggestions for new features or improvements, please submit an issue or pull request on GitHub.

- **Bug Reports**: If you encounter any bugs, please open an issue with details on how to reproduce it.
- **Feature Requests**: Suggest new features or enhancements by submitting a feature request.
