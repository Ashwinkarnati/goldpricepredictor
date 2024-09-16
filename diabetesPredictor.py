import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the diabetes dataset and train the model
diabetes_dataset = pd.read_csv('diabetes.csv')

# Separating the data and labels
x = diabetes_dataset.drop(columns='Outcome', axis=1)
y = diabetes_dataset['Outcome']

# Standardize the data
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)

# Train an SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(x_train, y_train)

# Create the Tkinter UI
def predict_diabetes():
    try:
        # Get user input from the form fields
        input_data = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()),
                      float(entry5.get()), float(entry6.get()), float(entry7.get()), float(entry8.get())]
        # Convert input data to NumPy array and reshape it
        input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

        # Standardize the input data
        std_data = scaler.transform(input_data_as_numpy_array)

        # Make the prediction
        prediction = classifier.predict(std_data)

        # Show the result
        if prediction[0] == 0:
            messagebox.showinfo("Result", "The person is not diabetic")
        else:
            messagebox.showinfo("Result", "The person is diabetic")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers in all fields.")

# Create the main window
window = tk.Tk()
window.title("Diabetes Prediction System")

# Add input fields and labels for the 8 features
tk.Label(window, text="Pregnancies").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Glucose").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

tk.Label(window, text="Blood Pressure").grid(row=2, column=0)
entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)

tk.Label(window, text="Skin Thickness").grid(row=3, column=0)
entry4 = tk.Entry(window)
entry4.grid(row=3, column=1)

tk.Label(window, text="Insulin").grid(row=4, column=0)
entry5 = tk.Entry(window)
entry5.grid(row=4, column=1)

tk.Label(window, text="BMI").grid(row=5, column=0)
entry6 = tk.Entry(window)
entry6.grid(row=5, column=1)

tk.Label(window, text="Diabetes Pedigree Function").grid(row=6, column=0)
entry7 = tk.Entry(window)
entry7.grid(row=6, column=1)

tk.Label(window, text="Age").grid(row=7, column=0)
entry8 = tk.Entry(window)
entry8.grid(row=7, column=1)

# Add a button to make the prediction
predict_button = tk.Button(window, text="Predict", command=predict_diabetes)
predict_button.grid(row=8, column=1)

# Run the GUI
window.mainloop()
