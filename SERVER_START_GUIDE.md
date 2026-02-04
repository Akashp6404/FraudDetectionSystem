# 🚀 Server Start Karne Ka Complete Guide

## Method 1: Easiest Way (Double Click)

### Windows:
1. **START.bat** ya **start_server.bat** file ko **double-click** karein
2. Terminal window open hoga
3. Server automatically start ho jayega
4. Browser mein `http://localhost:5000` open karein

---

## Method 2: Terminal/PowerShell se

### Step 1: Terminal Khol Lein
- Project folder mein jaayein: `D:\Phishing & Fraud Detection System`
- Folder mein **right-click** → **"Open PowerShell here"**
- Ya `Win + X` → **Windows PowerShell**

### Step 2: Server Start Karein
Terminal mein ye command type karein aur Enter press karein:

```bash
python app.py
```

### Step 3: Success Message Dekhein
Agar sab kuch sahi hai, to ye message dikhega:

```
Starting Phishing & Fraud Detection System...
Access the web interface at: http://localhost:5000
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Step 4: Browser Mein Open Karein
1. **Chrome/Firefox/Edge** browser khol lein
2. Address bar mein type karein: `localhost:5000`
3. Ya: `http://localhost:5000`
4. **Enter** press karein

---

## ✅ Server Start Ho Gaya Check Kaise Karein:

Terminal mein ye dikhna chahiye:
```
Starting Phishing & Fraud Detection System...
Access the web interface at: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

Aur browser mein website open ho jani chahiye!

---

## ⚠️ Common Problems & Solutions:

### Problem 1: "python is not recognized"
**Solution:**
```bash
python3 app.py
```
Ya Python ko PATH mein add karein

### Problem 2: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask flask-cors numpy pandas scikit-learn requests tldextract dnspython joblib
```

### Problem 3: "Address already in use" / Port 5000 busy
**Solution:**
`app.py` file mein line 152 pe jayein aur port change karein:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Phir browser mein `localhost:5001` open karein

### Problem 4: Browser mein "This site can't be reached"
**Check:**
- Terminal mein server running hai? (check terminal window)
- Port sahi hai? (5000 ya 5001?)
- URL sahi type kiya? (`localhost:5000` ya `127.0.0.1:5000`)

### Problem 5: Server start hota hai but kuch error aata hai
**Solution:**
1. Terminal window close mat karein
2. Error message ko carefully read karein
3. Dependencies install karein: `pip install -r requirements.txt`

---

## 🛑 Server Stop Karne Ka Tarika:

Terminal window mein:
```
Ctrl + C
```

---

## 📱 Complete Example:

```bash
# 1. Terminal khol lein (Project folder mein)
cd "D:\Phishing & Fraud Detection System"

# 2. Dependencies check (optional)
pip install -r requirements.txt

# 3. Server start
python app.py

# 4. Browser mein open karein
# http://localhost:5000
```

---

## 💡 Tips:

1. ✅ Terminal window open rakhein jab tak server use karna hai
2. ✅ Server running rehna chahiye, terminal band mat karein
3. ✅ Browser automatically nahi khulta, manually open karna padta hai
4. ✅ Agar port 5000 use hai, to 5001 try karein

---

## 🎯 Quick Checklist:

- [ ] Python installed hai? (`python --version`)
- [ ] Project folder mein hain? (`cd "D:\Phishing & Fraud Detection System"`)
- [ ] Dependencies install hui hain? (`pip install -r requirements.txt`)
- [ ] Server start kiya? (`python app.py`)
- [ ] Browser mein URL open kiya? (`localhost:5000`)
- [ ] Terminal window open hai? (Server running ke liye)

---

**Agar abhi bhi problem hai, to terminal mein jo error aaya hai, wo share karein!** 🚀

