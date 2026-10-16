
# 📝 Quiz App  
An interactive multi‑category quiz application built with **Streamlit**, featuring dynamic question rendering, progress tracking, session state management, and a clean sidebar‑driven user experience.

---

## 🚀 Features

- **Three quiz categories:** HTML, Python, and SQL  
- **Five questions per quiz**, each with multiple‑choice options  
- **Session state tracking** for:
  - Current question  
  - Score  
  - Answer status  
  - Completed quizzes  
- **Dynamic UI updates** using Streamlit’s rerun model  
- **Progress bar** showing quiz advancement  
- **Correct/incorrect feedback** after each question  
- **Restart Quiz** and **Reset All Progress** controls  
- **Sidebar navigation** with quiz selector and completed quiz list  
- **Automatic quiz reset** when switching categories  

---

## 📦 Technologies Used

- **Python 3.x**  
- **Streamlit** for UI and state management  
- **Datetime** for simple timestamp logging  

---

## 📁 Project Structure

```
quiz_app.py        # Main Streamlit application
README.md          # Project documentation
```

---

## ▶️ Running the App

Install Streamlit if you haven’t already:

```bash
pip install streamlit
```

Run the application:

```bash
streamlit run quiz_app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧠 How It Works

The app uses **Streamlit’s session_state** to maintain quiz progress across reruns.  
Key design choices include:

- Initializing all state variables at startup  
- Resetting quiz progress when the user switches categories  
- Using unique widget keys to avoid duplicate element errors  
- Separating sidebar UI from main quiz logic for predictable behavior  

---

## 📌 Future Enhancements (Optional)

- Add difficulty levels  
- Add a “Review Answers” mode  
- Add timed quizzes  
- Add user scoring history  
- Add animations or custom themes  

---

## 📄 License

This project is for educational use. You may modify or extend it as needed.

