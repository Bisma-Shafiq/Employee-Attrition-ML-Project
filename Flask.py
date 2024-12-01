from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("randomClassModel.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = [
            float(request.form['satisfaction_level']),
            float(request.form['last_evaluation']),
            int(request.form['number_project']),
            int(request.form['average_monthly_hours']),
            int(request.form['time_spend_company']),
            int(request.form['Work_accident']),
            int(request.form['promotion_last_5years']),
            int(request.form['Department']),
            int(request.form['salary'])
        ]
        
        # Make prediction
        prediction = model.predict([data])[0]
        
        # Interpret the prediction
        result = "The employee is likely to leave." if prediction == 1 else "The employee is likely to stay."
        return render_template('index.html', result=result)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(debug=True)
