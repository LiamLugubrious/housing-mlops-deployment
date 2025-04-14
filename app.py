import gradio as gr
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("model.pkl")

# Define prediction function
def predict_price(area, bedrooms, bathrooms):
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })
    prediction = model.predict(input_data)
    return f"${prediction[0]:,.2f}"

# Create Gradio interface
demo = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Bathrooms")
    ],
    outputs="text",
    title="Housing Price Predictor",
    description="Enter the features to estimate the housing price."
)

# Launch the app
demo.launch()
