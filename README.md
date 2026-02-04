# Phishing & Fraud Detection System

A comprehensive system to detect phishing websites and fraudulent emails using machine learning and heuristic analysis.

## Features

- **🔗 URL Analysis**: Advanced URL phishing detection with ML-powered analysis
- **📧 Email Analysis**: Comprehensive email fraud detection with pattern recognition
- **🤖 Machine Learning Model**: AI-powered detection using Random Forest classifier
- **🎨 Modern Web Interface**: Beautiful, responsive UI with animations and interactive elements
- **📊 Analytics Dashboard**: Real-time statistics and performance metrics
- **⚡ Real-time Detection**: Fast analysis with detailed risk scoring (0-100)
- **🔍 Feature Breakdown**: Detailed analysis of detection factors
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **🌐 RESTful API**: Complete API for integration with other systems

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

```bash
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

### Using the API

```bash
# Check URL
curl -X POST http://localhost:5000/api/check-url -H "Content-Type: application/json" -d '{"url": "https://example.com"}'

# Check Email
curl -X POST http://localhost:5000/api/check-email -H "Content-Type: application/json" -d '{"email": "email content here"}'
```

## Project Structure

```
├── app.py                 # Main Flask application with routes
├── url_analyzer.py        # URL phishing detection module
├── email_analyzer.py      # Email fraud detection module
├── ml_model.py            # Machine learning model (Random Forest)
├── test_system.py         # Test script for system validation
├── models/                # Saved ML models directory
├── static/
│   ├── css/
│   │   └── style.css      # Advanced CSS with animations
│   └── js/
│       └── main.js        # JavaScript for interactivity
├── templates/             # HTML templates
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Dashboard/Home page
│   ├── check_url.html     # URL checking interface
│   ├── check_email.html   # Email checking interface
│   ├── result.html        # Results display page
│   └── analytics.html     # Analytics dashboard
└── requirements.txt       # Python dependencies
```

## How It Works

1. **URL Analysis**: Extracts features from URLs (domain age, SSL certificate, suspicious keywords, etc.)
2. **Email Analysis**: Analyzes email content, headers, and links
3. **ML Model**: Uses trained classifier to predict if content is phishing/fraudulent
4. **Risk Score**: Provides a risk score (0-100) for the analyzed content

## License

MIT License

