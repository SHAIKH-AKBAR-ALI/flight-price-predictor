# ✈️ AI Flight Price Predictor

A machine learning-powered web application that predicts flight prices using Random Forest algorithm trained on 300K+ Indian flight records.

## 🚀 Live Demo

**Streamlit Cloud:** [https://your-app-name.streamlit.app](https://your-app-name.streamlit.app)

## 📋 Features

- **Real-time Predictions:** Instant flight price predictions
- **Advanced ML:** Random Forest algorithm with 99.1% accuracy
- **Modern UI:** Responsive design with gradient backgrounds
- **Lazy Loading:** Optimized performance with cached model loading
- **Error Handling:** Graceful error handling and user feedback

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **ML:** Scikit-learn, Random Forest
- **Data:** Pandas, NumPy
- **Deployment:** Streamlit Cloud

## 📦 Installation & Local Development

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/flight-price-predictor.git
cd flight-price-predictor

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

### Local Testing
```bash
# Test health endpoint
curl "http://localhost:8501?health=check"

# Test app loads
python -c "import app; print('✓ App imports successfully')"
```

## 🌐 Deployment to Streamlit Cloud

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Set:
   - **Repository:** `YOUR_USERNAME/flight-price-predictor`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click "Deploy"

### Expected URL Pattern
Your app will be available at: `https://flight-price-predictor-[random].streamlit.app`

## 📁 Project Structure

```
flight-price-predictor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── model_artifacts.pkl    # Trained ML model and preprocessors
├── Indian Airlines.csv    # Flight dataset
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## 🔧 Configuration

### Streamlit Settings (`.streamlit/config.toml`)
- Optimized for production deployment
- CORS disabled for security
- Dark theme with custom colors

### Dependencies (`requirements.txt`)
- Pinned versions for stability
- NumPy 1.24.3 (prevents binary compatibility issues)
- Minimal dependencies for faster cold starts

## 🧪 Model Details

- **Algorithm:** Random Forest Regressor
- **Features:** 10 input features (airline, route, timing, class, etc.)
- **Training Data:** 300,000+ Indian flight records
- **Accuracy:** 99.1% R² score
- **Preprocessing:** Label encoding + standard scaling

## 📊 Usage

1. Select flight details (airline, route, timing)
2. Enter trip information (duration, advance booking days)
3. Click "🔮 Predict Flight Price"
4. Get instant price prediction with insights

## 🚨 Troubleshooting

### Common Issues

**App won't start:**
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Model loading errors:**
- Ensure `model_artifacts.pkl` is in repository
- Check file size (should be ~480MB)
- Verify pickle compatibility

**Streamlit Cloud deployment fails:**
- Check repository is public
- Verify all files are committed
- Check Streamlit Cloud logs for errors

### Health Check
Visit `https://your-app.streamlit.app?health=check` to verify deployment.

## 💰 Cost & Limits

### Streamlit Cloud (Free Tier)
- ✅ **Cost:** Free
- ✅ **Apps:** Up to 3 public apps
- ✅ **Resources:** 1 CPU, 800MB RAM
- ✅ **Usage:** Unlimited within fair use

### Removing Deployment
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Find your app
3. Click "Delete app"

## 👨‍💻 Developer

**SHAIKH AKBAR ALI**
- Data Scientist & AI Engineer
- [GitHub](https://github.com/YOUR_USERNAME)
- [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

## 📄 License

MIT License - see LICENSE file for details.

---

⭐ **Star this repo if you found it helpful!**