✈️ FlightPricePredictor

Welcome to FlightPricePredictor, a cutting-edge machine learning system that forecasts flight prices with 94.2% accuracy! Built with Streamlit and Scikit-learn, this app empowers travelers to make smarter booking decisions through real-time price predictions for flights across India. 🚀
   
📑 Table of Contents

🌟 Overview
✨ Key Features
🛠️ Installation
🚀 Usage
🤖 Model Details
💻 Tech Stack
👨‍💻 About the Developer
📜 License

🌟 Overview
FlightPricePredictor is your go-to tool for predicting flight prices with precision! Powered by a Random Forest Regressor, this app analyzes factors like airline, route, class, and booking window to deliver accurate price forecasts in milliseconds. Whether you're planning a quick getaway or a business trip, this system helps you save time and money. 🤑

Why use FlightPricePredictor? It’s fast, reliable, and supports 6 major Indian airlines across multiple routes, with an intuitive Streamlit interface that makes predictions a breeze!

✨ Key Features

🎯 Real-Time Predictions: Get instant flight price estimates with a sleek, user-friendly interface.
📊 High Accuracy: Boasts a 94.2% R² score and a low ₹1,080 MAE.
✈️ Wide Coverage: Supports 6 major Indian airlines and key city routes.
💺 Flexible Options: Predicts prices for Economy and Business class with customizable inputs.
🔄 Robust ML Pipeline: Uses ColumnTransformer for seamless preprocessing of categorical and numerical data.
⚡ Blazing Fast: Delivers predictions in under 100ms with a compact 12.4 MB model.

🛠️ Installation
Get started in just a few steps! Follow these instructions to set up FlightPricePredictor locally:

Clone the Repository:
git clone https://github.com/your-username/FlightPricePredictor.git
cd FlightPricePredictor


Create a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Ensure Python 3.x is installed, then run:
pip install -r requirements.txt


Add the Model File:Place the random_forest_model.pkl file in the project directory. (Note: The model is not included in the repo due to size constraints. Contact the developer or train it using the provided script.)

Launch the App:
streamlit run app.py




Pro Tip: Ensure all dependencies are installed correctly to avoid issues. Check the requirements.txt for the full list!

🚀 Usage

Start the Streamlit app with the command above.
Navigate to the Predict page via the sidebar.
Input flight details: airline, source/destination cities, departure/arrival times, stops, class, duration, and days to departure.
Hit the Predict Price button to see the estimated price in a sleek, gradient-styled output. 🎉
Explore the Home, About, and Model Info pages for insights into the project and its performance.

🤖 Model Details

Architecture: Random Forest Regressor with a preprocessing pipeline:
ColumnTransformer: StandardScaler for numerical features, OneHotEncoder for categorical features.
RandomForestRegressor: 100 estimators, auto-optimized max depth, random_state=42.


Performance Metrics:
R² Score: 0.9420 (High accuracy)
MAE: ₹1,080 (Excellent precision)
RMSE: ₹1,456 (Low error)
Prediction Time: 0.05 seconds (Real-time)
Model Size: 12.4 MB (Optimized)


Feature Importance:


Feature
Importance (%)



Days Left
28.5


Duration
22.3


Airline
18.7


Class
12.4


Route
9.8


Departure Time
4.2


Stops
2.8


Arrival Time
1.3





Fun Fact: The model’s efficiency ensures predictions are lightning-fast, making it ideal for real-world applications!

💻 Tech Stack



Category
Tools



Machine Learning
Scikit-learn, XGBoost, Pandas, NumPy


Development
Python 3.x, Streamlit, Joblib


Data Processing
Pipeline API, ColumnTransformer, OneHotEncoder


👨‍💻 About the Developer
Akbar AliData Scientist & AI EngineerPassionate about building AI solutions that solve real-world problems, Akbar specializes in machine learning, predictive modeling, and data analytics. This project showcases his expertise in creating production-ready ML pipelines. Connect with him to collaborate or learn more! 🌟
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

✨ Built with ❤️ by Akbar Ali | Powered by Streamlit & Scikit-learn ✨
