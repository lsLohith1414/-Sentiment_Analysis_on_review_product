# 📝 Sentiment Analysis Web App

This project is an **end-to-end Sentiment Analysis System** that classifies customer reviews into **Positive**, **Neutral**, or **Negative** sentiments using a **Machine Learning model**.  
It includes both a **FastAPI backend** for prediction and a **Streamlit web interface** for user interaction and visualization.

---

## 🚀 Project Overview

The goal of this project is to automate the process of analyzing text data (such as product reviews or user feedback) and determining the overall sentiment behind it.  
This project demonstrates how **Machine Learning**, **FastAPI**, and **Streamlit** can work together to create a real-world NLP web application.

---

## 🧠 Key Features

✅ Real-time sentiment prediction for customer reviews  
✅ Interactive and clean Streamlit interface  
✅ REST API built using FastAPI  
✅ Displays probability distribution for each sentiment class  
✅ Modular and easy-to-extend architecture  
✅ Trained ML model integrated for instant predictions

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit |
| **Backend API** | FastAPI |
| **Machine Learning** | Scikit-learn |
| **Language** | Python |
| **Libraries** | Pandas, NumPy, Requests, Joblib |
| **Visualization** | Streamlit Charts |

---

## 📁 Project Structure

Sentiment-Analysis-App/
│

├── app.py # FastAPI backend

├── streamlit_app.py # Streamlit frontend app

├── prediction/

│ └── review_prediction.py # Model loading and prediction logic

├── models/

│ └── sentiment_model.pkl # Trained ML model

├── requirements.txt # Dependencies

└── README.md # Documentation