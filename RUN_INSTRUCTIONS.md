# 🚀 Phishing & Fraud Detection System - Run Instructions

## Step-by-Step Guide to Run the Project

### Step 1: Install Python Dependencies

Open terminal/PowerShell in the project folder and run:

```bash
pip install -r requirements.txt
```

If you encounter any errors, try the following:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 2: Run the Application

Run the following command in Terminal/PowerShell in the project folder:

```bash
python app.py
```

Or, if you want to use Python 3:
```bash
python3 app.py
```

### Step 3: Access in Browser

Browser mein ye URL open karein:

```
http://localhost:5000
```

Ya

```
http://127.0.0.1:5000
```

### Step 4: Test the System (Optional)

You can run the test script in a separate terminal window:

```bash
python test_system.py
```

---

## Complete Command Sequence

```bash
# 1. Navigate to project directory
cd "D:\Phishing & Fraud Detection System"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python app.py

# 4. Open browser and go to:
# http://localhost:5000
```

---

## Common Issues & Solutions

### Issue 1: ModuleNotFoundError
**Solution:** 
```bash
pip install flask flask-cors numpy pandas scikit-learn requests tldextract dnspython joblib
```

### Issue 2: Port already in use
**Solution:** 
- Change the port in `app.py`. (line 152): `app.run(debug=True, host='0.0.0.0', port=5001)`
- Or, stop the running process in the terminal.

### Issue 3: Virtual Environment
**If you want to use a virtual environment:**

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
```

---

## Features After Running

1. **Dashboard** - `/` - Home page with statistics
2. **Check URL** - `/check-url` - Analyze URLs for phishing
3. **Check Email** - `/check-email` - Analyze emails for fraud
4. **Analytics** - `/analytics` - View analytics and statistics
5. **API Endpoints** - `/api/check-url` and `/api/check-email`

---

## Quick Test

Open the browser and try the following:

1. Dashboard page: http://localhost:5000
2. URL Check: http://localhost:5000/check-url
3. Email Check: http://localhost:5000/check-email
4. Analytics: http://localhost:5000/analytics

---

## Stop the Server

Press `Ctrl + C` in the terminal to stop the server.

---

## Project Status

✅ Flask Application  
✅ URL Analyzer  
✅ Email Analyzer  
✅ ML Model  
✅ Web Interface  
✅ API Endpoints  
✅ Analytics Dashboard  

**Project ready to run!**

