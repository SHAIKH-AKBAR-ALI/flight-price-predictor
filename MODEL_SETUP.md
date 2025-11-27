# Model Setup Instructions

## Large Model Files

Due to GitHub's file size limitations, the trained model files are not included in this repository. 

### Required Model Files:
- `model_artifacts.pkl` (793MB) - Contains trained Random Forest model, scaler, and label encoders
- `Indian Airlines.csv` (dataset)

### Setup Options:

#### Option 1: Train Your Own Model
Run the training notebook:
```bash
jupyter notebook final.ipynb
```

#### Option 2: Download Pre-trained Models
Contact the developer for pre-trained model files:
- **Email:** [your-email@example.com]
- **LinkedIn:** [Your LinkedIn Profile]

#### Option 3: Use Sample Data
For demo purposes, you can use a smaller sample dataset and retrain the model.

### File Structure:
```
flight-price-predictor/
├── app.py                 # Main Streamlit app
├── model_artifacts.pkl    # [REQUIRED] Trained model (not in repo)
├── Indian Airlines.csv    # [REQUIRED] Dataset (not in repo)
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

### Deployment Notes:
- For Streamlit Cloud: Upload model files manually to your deployment
- For local development: Place model files in the root directory
- The app will show error messages if model files are missing