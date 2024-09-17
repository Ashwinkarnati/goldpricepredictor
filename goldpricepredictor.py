import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset and train model
gold_data = pd.read_csv("gld_price_data.csv")  # Load the gold price dataset from a CSV file
x = gold_data.drop(['Date', 'GLD'], axis=1)    # Drop 'Date' and 'GLD' columns, keeping only feature columns
y = gold_data['GLD']                           # 'GLD' column is the target variable (gold price)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)  # Split data into training and testing sets

# Train the Random Forest Regressor model
regressor = RandomForestRegressor(n_estimators=100)  # Initialize Random Forest Regressor with 100 trees
regressor.fit(x_train, y_train)                      # Train the model on the training data

# Function to make predictions based on user input
def predict_gold_price():
    try:
        # Get user inputs from the entry fields and convert them to float
        spx = float(entry_spx.get())           # Get SPX input (S&P 500 Index) and convert to float
        uso = float(entry_uso.get())           # Get USO input (Crude Oil Prices) and convert to float
        slv = float(entry_slv.get())           # Get SLV input (Silver Prices) and convert to float
        eur_usd = float(entry_eur_usd.get())   # Get EUR/USD exchange rate and convert to float

        # Prepare the input values as a NumPy array and reshape it to match model input format
        input_values = np.asarray([spx, uso, slv, eur_usd]).reshape(1, -1)
        
        # Make prediction using the trained Random Forest model
        prediction = regressor.predict(input_values)
        
        # Display the predicted gold price in a message box
        messagebox.showinfo("Prediction", f"Predicted Gold Price: ${prediction[0]:.2f}")

    except ValueError:
        # If there is a problem with the user input (e.g., non-numeric values), display an error message
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Creating UI using tkinter
root = tk.Tk()                   # Initialize the main window of the tkinter application
root.title("Gold Price Predictor")  # Set the title of the window

# Labels and entry fields for the input parameters
tk.Label(root, text="SPX (S&P 500 Index)").grid(row=0, column=0, padx=10, pady=10)  # Label for SPX
entry_spx = tk.Entry(root)       # Entry field for SPX input
entry_spx.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="USO (Crude Oil Prices)").grid(row=1, column=0, padx=10, pady=10)  # Label for USO
entry_uso = tk.Entry(root)       # Entry field for USO input
entry_uso.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="SLV (Silver Prices)").grid(row=2, column=0, padx=10, pady=10)  # Label for SLV
entry_slv = tk.Entry(root)       # Entry field for SLV input
entry_slv.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="EUR/USD Exchange Rate").grid(row=3, column=0, padx=10, pady=10)  # Label for EUR/USD
entry_eur_usd = tk.Entry(root)   # Entry field for EUR/USD input
entry_eur_usd.grid(row=3, column=1, padx=10, pady=10)

# Button to trigger the prediction process
predict_button = tk.Button(root, text="Predict Gold Price", command=predict_gold_price)  # Button to predict gold price
predict_button.grid(row=4, column=0, columnspan=2, pady=20)  # Position the button and set some padding

# Run the tkinter event loop
root.mainloop()  # Start the tkinter main loop to display the window and wait for user interaction
