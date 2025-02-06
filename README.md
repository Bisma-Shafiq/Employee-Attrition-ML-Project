# Employee Attrition Prediction Flask App

## Overview
This Flask web application predicts whether an employee is likely to leave or stay in the company based on user input. The prediction is made using a pre-trained Random Forest Classification model.

## Features
- User-friendly web interface
- Takes employee-related inputs via a form
- Uses a trained machine learning model to predict attrition
- Displays prediction results on the webpage

## Installation
### Prerequisites
Ensure you have Python installed along with the required dependencies.

### Clone the Repository
```bash
git clone https://github.com/your-repo/employee-attrition-flask.git
cd employee-attrition-flask
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`.

## Usage
1. Open the web application in your browser.
2. Enter the required employee details.
3. Click the "Predict" button.
4. View the prediction result on the screen.

## Model Details
The app uses a `RandomClassModel.pkl` file which is a pre-trained Random Forest Classification model. Ensure the model file is in the project directory.

## File Structure
```
/employee-attrition-flask
│── app.py               # Flask application
│── templates/
│   ├── index.html       # Frontend template
│── static/              # CSS/JS files (if needed)
│── randomClassModel.pkl # Trained model
│── requirements.txt     # Required Python libraries
│── README.md            # Project documentation
```

## Dependencies
- Flask
- NumPy
- Pickle

## Future Enhancements
- Improve the UI/UX design
- Expand dataset for better predictions
- Deploy the model on a cloud platform

## License
This project is open-source and available for modifications and improvements.

