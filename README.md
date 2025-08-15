# 🦠 covid19-outcome-chatbot
A Python Flask web app that predicts COVID-19 patient outcomes (recovered or deceased) based on input data.  
This chatbot uses trained machine learning models stored in `.rar` format to stay within GitHub's size limits.

----------
## 📂 Project Structure
covid19-outcome-chatbot/
│
├── static/ # CSS, images
├── templates/ # HTML templates
├── app.py # Main Flask application
├── deaths_model.rar # Compressed model for death prediction
├── recovered_model.rar # Compressed model for recovery prediction
└── .gitattributes # Git attributes config

----------------
## ⚙️ How to Run
### 1️⃣ Install Requirements
Make sure you have **Python 3.8+** installed.
Install Flask and any other dependencies:
```bash
pip install flask pandas scikit-learn


### 2️⃣ Extract Models

The trained models are compressed as .rar files to avoid GitHub's 100 MB limit.
Before running the app, extract them in the same folder as app.py:
- deaths_model.rar → deaths_model.pkl
- recovered_model.rar → recovered_model.pkl
- You can use WinRAR or 7-Zip.

### 3️⃣ Run the App
From the project folder:
python app.py

### 4️⃣ Open in Browser
Once the server starts, open:
http://127.0.0.1:5000/

--------------

## 🛠 Features
 - Web-based chatbot interface
 - Predicts COVID-19 outcome based on user input
 - Uses machine learning models trained on real datasets
 - Responsive design (works on desktop & mobile)
--------------
## 📸 Screenshot
![Chatbot Screenshot](screenshots/covid19-outcome-chatbot.png)

-------------

## 📌 Notes
 - The .rar files are only for storage convenience.
 - If you retrain models, save them as .pkl and compress them again before pushing to GitHub.
 - For deployment, make sure the .pkl files are extracted on the server.



