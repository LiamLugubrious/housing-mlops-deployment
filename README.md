```bash

# Housing Price Prediction - Web App Deployment

This project demonstrates a simple machine learning deployment using Gradio. 
It uses a pre-trained linear regression model to predict housing prices based on user input.

## Files Included

- `Housing.csv`: The original dataset used to train the model.
- `model.pkl`: The trained linear regression model (created during the lab).
- `app.py`: The Gradio app for real-time prediction through a web interface.

## How to Use

1. **Clone the repository**:
git clone https://github.com/LiamLugubrious/housing-mlops-deployment.git,
then, cd housing-mlops-deployment


2. **Install required libraries**:
pip install gradio pandas joblib scikit-learn

3. **Run the application**:
python app.py

4. The Gradio web interface will create a URL that you can use in your browser where you can enter:
- Area (in square feet)
- Number of bedrooms
- Number of bathrooms

and get a predicted house price.
5 **Qutting the Server/Application**
If using CMD press Crtl+C!

## Purpose

This is part of my assignment, which builds on the previous lab I did
by using the trained model we got from the lab and creating a user interface
for making live predictions. It is part of an introduction to using MLOps pipeline.
