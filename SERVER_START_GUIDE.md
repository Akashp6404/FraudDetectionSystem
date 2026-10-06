# 🚀 # Complete Guide to Starting the Server
## Method 1: Easiest Way (Double Click)

### Windows:
1. **START.bat** or **start_server.bat** or **Double-click the file.**
2.The terminal window will open.
3. The server will start automatically.
4.Open `http://localhost:5000` in your browser.

---

## Method 2: **From Terminal/PowerShell**

### Step 1: Open the Terminal.
- Go to the project folder: `D:\Phishing & Fraud Detection System`
- Right-click inside the folder → **"Open PowerShell here"**.
- Or `Win + X` → **Windows PowerShell**

### Step 2: Start the Server
Type the following command in the terminal and press Enter:

```bash
python app.py
```

### Step 3: Check the Success Message.
If everything is working correctly, you will see the following message:

```
Starting Phishing & Fraud Detection System...
Access the web interface at: http://localhost:5000
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Step 4: Open in the Browser
1. **Chrome/Firefox/Edge** Open the Browser
2. Type the following in the address bar: `localhost:5000`
3. Or: `http://localhost:5000`
4. **Enter** Press Enter 

---

## ✅ How to Check if the Server Has Started:

You should see the following in the terminal:
```
Starting Phishing & Fraud Detection System...
Access the web interface at: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

And the website should open in the browser!

---

## ⚠️ Common Problems & Solutions:

### Problem 1: "python is not recognized"
**Solution:**
```bash
python3 app.py
```
Or add Python to the PATH.

### Problem 2: "ModuleNotFoundError: No module named 'flask'"
**Solution:**
```bash
pip install flask flask-cors numpy pandas scikit-learn requests tldextract dnspython joblib
```

### Problem 3: "Address already in use" / Port 5000 busy
**Solution:**
`app.py` Go to **line 152** in the file and change the port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```
Then open `localhost:5001` in the browser.

### Problem 4: In the Browser "This site can't be reached"
**Check:**
- Is the server running in the terminal? (Check the terminal window.)
- Is the port correct? (5000 or 5001?)
- Is the URL Correct? (`localhost:5000` or `127.0.0.1:5000`)

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

