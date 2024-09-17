# Gold Price Predictor
This project is a simple Gold Price Prediction tool built using a Random Forest Regressor. The model is trained on historical data, and the app includes a Graphical User Interface (GUI) built using Python's tkinter library. The user can input relevant economic data, such as stock indices, oil prices, and exchange rates, to predict the future price of gold.

Features
Predict the price of gold based on key economic indicators:
S&P 500 Index (SPX)
Crude Oil Prices (USO)
Silver Prices (SLV)
EUR/USD Exchange Rate
Simple GUI for easy data input and prediction.
Random Forest model for prediction.
Requirements
Before running the project, ensure that you have the following Python libraries installed:

numpy
pandas
scikit-learn
tkinter (comes pre-installed with Python)
matplotlib (optional, for plotting)
seaborn (optional, for enhanced visualizations)
You can install these dependencies using the following command:

bash
Copy code
pip install numpy pandas scikit-learn matplotlib seaborn
Dataset
The dataset used in this project is the "Gold Price Data" CSV file. It contains various economic indicators (such as stock prices and exchange rates) and their corresponding gold prices. Make sure you have the file gld_price_data.csv in the project directory.

How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/Ashwinkarnati/goldpricepredictor.git
Navigate to the project directory:

bash
Copy code
cd goldpricepredictor
Ensure the dataset is available:

Place the gld_price_data.csv file in the project directory.
Run the Python script:

bash
Copy code
python goldpricepredictor.py
Use the GUI:

Input values for SPX, USO, SLV, and EUR/USD in the fields provided.
Click on "Predict Gold Price" to view the predicted gold price based on the input data.
Project Structure
plaintext
Copy code
├── gld_price_data.csv        # Dataset file containing gold prices and economic indicators
├── goldpricepredictor.py   # Main script containing the machine learning model and UI code
├── README.md                 # Documentation for the project
GUI Example
The GUI is designed for simple and intuitive input. Here’s a visual representation of the interface and how to use it:

Interface Layout
less
Copy code
--------------------------------------------
|  SPX (S&P 500 Index): [Enter Value]      |
|  USO (Crude Oil Prices): [Enter Value]   |
|  SLV (Silver Prices): [Enter Value]      |
|  EUR/USD Exchange Rate: [Enter Value]    |
|------------------------------------------|
|             [Predict Gold Price]         |
--------------------------------------------
How to Use the GUI
Input Fields:

SPX (S&P 500 Index): Enter the value of the S&P 500 Index.
USO (Crude Oil Prices): Enter the current crude oil price.
SLV (Silver Prices): Enter the current silver price.
EUR/USD Exchange Rate: Enter the current EUR/USD exchange rate.
Predict Button:

Click the "Predict Gold Price" button to make a prediction based on the input values.
Prediction Output:

A message box will display the predicted gold price based on the inputs provided.
How It Works
Model Training:
The model is trained using a Random Forest Regressor.
The training dataset includes features like:
Stock prices (SPX)
Oil prices (USO)
Silver prices (SLV)
Exchange rates (EUR/USD)
The target variable is the price of gold (GLD).
Prediction:
The trained model makes predictions based on user input in the GUI.
The user enters values for SPX, USO, SLV, and EUR/USD, and the model returns the predicted gold price.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code.