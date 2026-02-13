# 🏥 Personal Health Coach – AI Agents Platform

An AI-powered **Personal Health Coach** that analyzes long-term health data, compresses health history using **ScaleDown memory**, detects anomalies, and provides **personalized recommendations** through specialized AI agents.

This project was built as part of a **GenAI Hackathon**, focusing on real-world health monitoring, explainable AI, and scalable architecture.

---

## 🚀 Key Features

### 🧠 AI-Powered Health Intelligence
- **ScaleDown Health Memory**  
  Compresses 12 months of health data by ~80% while retaining medical context.
- **Personalized AI Recommendations** using LLM (Gemini API)

### 🤖 Specialized AI Agents
- 🥗 Nutrition Agent
- 🏃 Exercise Planning Agent
- 😴 Sleep Analysis Agent
- 🎯 Goal-Setting Agent
- 🩺 Doctor Visit Preparation Agent
- 🚨 Anomaly Detection Agent

### 📊 Health Dashboard
- Long-term health summary
- Anomaly alerts
- Progress tracking
- Visual charts for trends
- Responsive UI (mobile + desktop)

---

## 🏗️ System Architecture

Frontend (React + Vite)
|
| REST APIs
v
Backend (FastAPI)
|
|-- ScaleDown Memory Engine
|-- AI Agent Layer
|-- Health Data Loader
|
v
LLM (Gemini API)

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- React Router
- Recharts (Charts)
- CSS (Responsive, Dark UI)

### Backend
- FastAPI
- Python
- REST APIs
- Modular Agent Architecture

### AI / GenAI
- Google Gemini API
- Prompt-based reasoning
- ScaleDown memory compression

---

## 🧩 Project Structure

GenAI-Hackathon/
├── backend/
│ ├── app/
│ │ ├── agents/ # AI Agents
│ │ ├── core/ # LLM integration
│ │ ├── memory/ # ScaleDown logic
│ │ ├── ingestion/ # Health data loader
│ │ ├── routes/ # API routes
│ │ └── main.py
│
├── frontend/
│ ├── src/
│ │ ├── pages/
│ │ ├── components/
│ │ ├── api/
│ │ ├── styles/
│ │ └── App.jsx
│
└── README.md

---

## ⚙️ How It Works

1. **Health Data Ingestion**
   - Simulated wearable health data (steps, sleep, calories, heart rate)

2. **ScaleDown Memory**
   - Converts long-term daily logs into a compressed medical summary

3. **AI Agents**
   - Each agent focuses on one domain (nutrition, sleep, etc.)
   - Uses compressed memory + live data for recommendations

4. **Frontend Dashboard**
   - Displays summary, anomalies, progress, and charts
   - Allows interaction with AI Coach

---

## ▶️ How to Run the Project

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
