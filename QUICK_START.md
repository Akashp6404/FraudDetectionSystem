# 🚀 Quick Start Guide - Phishing & Fraud Detection System

## 🎯 Easiest Method

### Method 1: Start by Double-Clicking (Windows)
In the project folder, double-click the START.bat file.
The browser will open automatically, or you can manually open http://localhost:5000.

### Method 2: Start from Terminal/PowerShell

**Step 1:** Open Terminal/PowerShell in the project folder

- Windows: Right-click inside the folder → **"Open PowerShell here"**
- Or press `Win + R` → type `cmd` → press Enter → `cd "D:\Phishing & Fraud Detection System"`


**Step 2:** Run the following command:
```bash
python app.py
```

**Step 3:** Open the following URL in your browser:
```
http://localhost:5000
```

---

## ✅ Complete Steps:

### 1️⃣ ### Install Dependencies (Only Required Once)
```bash
pip install -r requirements.txt
```
*(If already installed, skip this step.)*

### 2️⃣ Application Run
```bash
python app.py
```

### 3️⃣ Browser Mein Open
```
http://localhost:5000
```

---

## 🎨 ### How to Use the Features:

1. **Dashboard** - `/` - To view the Home page:
2. **Check URL** - `/check-URL` -To check a website URL:
3. **Check Email** - `/check-email` - To check for email fraud: 
4. **Analytics** - `/analytics` - To view statistics:

---

## ⚠️ If You Get an Error:

### Error: "python is not recognized"
**Solution:** `python3` use it:
```bash
python3 app.py
```

### Error: "ModuleNotFoundError"
**Solution:** Install the dependencies:
```bash
pip install flask flask-cors numpy pandas scikit-learn requests tldextract dnspython joblib
```

### Error: "Port already in use"
**Solution:** 
- Stop the running process in the terminal by pressing `Ctrl + C`.
- Or change the port in `app.py` (line 152): `port=5001`

---

## 🛑 How to Stop the Server:

In the Terminal window:
```
Ctrl + C
```

---

## 📱 To Test the System::

1. Open the Browser (Chrome/Firefox/Edge)
2. Type the following in the address bar: `localhost:5000`
3. Press Enter 
4.The Dashboard page will be displayed! 🎉

---

## 💡 Quick Tips:

- ✅ Do not close the terminal window after starting the server.
- ✅ The browser tab will not open automatically; you will need to open it manually.
- ✅ The server will keep running until you press `Ctrl + C`.
- ✅ If port 5000 is already in use, try `localhost:5001`.

---

**Ready! Now just run `python app.py` and open `localhost:5000` in your browser!** 🚀

