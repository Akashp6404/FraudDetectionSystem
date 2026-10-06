# 🚀 Quick Start Guide - Phishing & Fraud Detection System

## 🎯 Easiest Method

### Method 1: Double Click se Start (Windows)
1. Project folder mein **START.bat** file ko **double-click** karein
2. Browser mein khud khol lein ya manually `http://localhost:5000` open karein

### Method 2: Terminal/PowerShell se

**Step 1:** Project folder mein terminal/PowerShell khol lein
- Windows: Folder mein right-click → "Open PowerShell here"
- Ya `Win + R` → type `cmd` → Enter → `cd "D:\Phishing & Fraud Detection System"`

**Step 2:** Ye command run karein:
```bash
python app.py
```

**Step 3:** Browser mein ye URL open karein:
```
http://localhost:5000
```

---

## ✅ Complete Steps:

### 1️⃣ Dependencies Install (Ek baar karna hai)
```bash
pip install -r requirements.txt
```
*(Pehle se installed hai to skip karein)*

### 2️⃣ Application Run
```bash
python app.py
```

### 3️⃣ Browser Mein Open
```
http://localhost:5000
```

---

## 🎨 Features Use Karne Ka Tarika:

1. **Dashboard** - `/` - Home page dekhne ke liye
2. **Check URL** - `/check-url` - Website URL check karne ke liye
3. **Check Email** - `/check-email` - Email fraud check karne ke liye  
4. **Analytics** - `/analytics` - Statistics dekhne ke liye

---

## ⚠️ Agar Error Aaye:

### Error: "python is not recognized"
**Solution:** `python3` use karein:
```bash
python3 app.py
```

### Error: "ModuleNotFoundError"
**Solution:** Dependencies install karein:
```bash
pip install flask flask-cors numpy pandas scikit-learn requests tldextract dnspython joblib
```

### Error: "Port already in use"
**Solution:** 
- Terminal mein running process ko `Ctrl + C` se stop karein
- Ya `app.py` mein port change karein (line 152): `port=5001`

---

## 🛑 Server Stop Karne Ka Tarika:

Terminal window mein:
```
Ctrl + C
```

---

## 📱 Test Karne Ke Liye:

1. Browser open karein (Chrome/Firefox/Edge)
2. Address bar mein type karein: `localhost:5000`
3. Enter press karein
4. Dashboard page dikhega! 🎉

---

## 💡 Quick Tips:

- ✅ Server start hone ke baad terminal window band mat karein
- ✅ Browser mein automatically tab open nahi hoga, manually open karna hoga
- ✅ Server running rahega jab tak `Ctrl + C` na press karein
- ✅ Agar port 5000 use hai, to `localhost:5001` try karein

---

**Ready hai! Ab bas `python app.py` run karein aur browser mein `localhost:5000` open karein!** 🚀

