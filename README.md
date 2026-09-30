# SmartFix NLP

## AI-Powered Complaint Analysis and Solution Recommendation System

SmartFix NLP is a Natural Language Processing (NLP) based complaint-management system developed as a Bachelor of Engineering mini project in Artificial Intelligence and Data Science.

The system accepts complaint text in natural language and helps analyze it by identifying the complaint category, recommending a suitable solution, detecting priority and sentiment, suggesting the responsible department, generating a ticket ID, and finding similar complaints. The project also demonstrates additional NLP experiments such as POS tagging, chunking, Named Entity Recognition, Word Sense Disambiguation, and TF-IDF based text similarity.

---

## 📌 Project Overview

Handling customer or organizational complaints manually can be time-consuming. Different complaints may describe the same issue in different words, and important information such as urgency or responsible department may not be immediately clear.

SmartFix NLP provides a simple web-based interface that uses NLP techniques to:

- Analyze complaint text
- Classify complaints into predefined categories
- Recommend a suitable solution
- Detect complaint priority
- Detect basic sentiment
- Suggest the responsible department
- Generate a unique ticket ID
- Find similar complaint text
- Maintain complaint history in the browser
- Display dashboard statistics and insights
- Demonstrate Word Sense Disambiguation

---

## ✨ Key Features

### 1. Complaint Analysis
SmartFix analyzes complaint text and assigns it to one of the predefined categories:

- Machine Problem
- Quality Problem
- Production Delay
- Material Problem
- General Complaint

### 2. Solution Recommendation
After identifying the complaint category, SmartFix displays a suggested action or solution.

### 3. Priority Detection
The system detects complaint priority as:

- HIGH
- MEDIUM
- LOW

The current prototype uses keyword-based priority detection.

### 4. Department Routing
SmartFix suggests the department that can handle the complaint:

| Complaint Category | Suggested Department |
|---|---|
| Machine Problem | Maintenance |
| Quality Problem | Quality Control |
| Production Delay | Production |
| Material Problem | Stores / Materials |
| General Complaint | Customer Support |

### 5. Sentiment Detection
The current prototype performs lightweight rule-based sentiment detection and returns:

- Positive
- Negative
- Neutral

### 6. Ticket Generation
Each analyzed complaint receives a unique ticket ID in the SmartFix interface.

Example:

```text
SF-20260930073421
```

### 7. Text Similarity
The system compares complaint text using:

- TF-IDF vectorization
- Cosine similarity

It returns the most similar complaint from the predefined complaint examples and a similarity percentage.

### 8. Word Sense Disambiguation
SmartFix demonstrates contextual interpretation of the word **bank**.

Examples:

```text
The fisherman sat near the bank of the river.
→ River Bank
```

```text
I deposited money in the bank.
→ Financial Bank
```

### 9. Complaint Dashboard
The frontend dashboard provides:

- Total complaints
- High-priority complaints
- Open complaints
- Resolved complaints
- Category analytics
- Smart insights
- Complaint history
- Status tracking

Complaint history is stored in the browser using `localStorage`.

---

## 🧠 NLP Techniques Used

| Technique | Purpose |
|---|---|
| Text preprocessing | Clean and prepare text |
| TF-IDF | Convert text into numerical features |
| Text classification | Identify complaint categories |
| Cosine similarity | Compare complaint text |
| Sentiment detection | Detect basic sentiment |
| POS tagging | Identify grammatical roles |
| Chunking | Group related words into phrases |
| Named Entity Recognition | Identify named entities |
| Word Sense Disambiguation | Identify word meaning from context |
| Recommendation | Suggest complaint solutions |

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │     User / Staff     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   SmartFix Frontend  │
                    │ HTML + CSS + JS       │
                    └──────────┬───────────┘
                               │ HTTP Requests
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    │      Python          │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌───────────────┐
      │ Complaint   │   │ WSD Module  │   │ Similarity    │
      │ Analysis    │   │             │   │ Module        │
      └──────┬──────┘   └─────────────┘   └───────┬───────┘
             │                                    │
             ▼                                    ▼
      Category / Solution               TF-IDF + Cosine Similarity
             │
             ▼
      Priority / Sentiment /
      Department / Ticket ID
             │
             └──────────────────┐
                                ▼
                       ┌─────────────────┐
                       │ Dashboard /     │
                       │ History / Status│
                       └─────────────────┘
```

---

## 🛠️ Technology Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Scikit-learn

### NLP
- NLTK
- TF-IDF
- Cosine Similarity
- Rule-based NLP logic

### Frontend
- HTML
- CSS
- JavaScript

### Development
- Visual Studio Code
- Git
- GitHub

### Platform
- Windows

---

## 📁 Project Structure

```text
Smart-Fix/
│
├── backend/
│   ├── api/
│   ├── app/
│   │   ├── main.py
│   │   └── __init__.py
│   ├── experiments/
│   │   ├── experiment1_*.py
│   │   ├── experiment2_*.py
│   │   ├── experiment3_*.py
│   │   ├── experiment4_*.py
│   │   ├── experiment5_*.py
│   │   ├── experiment6_pos_tagging.py
│   │   ├── experiment7_chunking.py
│   │   ├── experiment8_ner.py
│   │   ├── experiment9_wsd.py
│   │   └── experiment10_text_similarity.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── .gitignore
└── README.md
```

> The local `venv/` folder should not be committed to GitHub. It is recreated locally from the required Python packages.

---

## 💻 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/PTarmale/SmartFix-NLP.git
cd SmartFix-NLP
```

### 2. Open the backend folder

```powershell
cd backend
```

### 3. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 4. Install required packages

```powershell
python -m pip install fastapi "uvicorn[standard]" scikit-learn nltk
```

If `requirements.txt` is available:

```powershell
pip install -r requirements.txt
```

### 5. Start the FastAPI backend

```powershell
python -m uvicorn app.main:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Open the frontend

In another terminal:

```powershell
cd C:\Users\prach\Smart-Fix\frontend
start index.html
```

Refresh the browser with:

```text
Ctrl + F5
```

---

## 🔌 API Endpoints

### Home

```http
GET /
```

Returns a backend status message.

### Complaint Analysis

```http
POST /api/analyze
```

Example input:

```json
{
  "text": "The conveyor machine has completely stopped"
}
```

The response contains:

- Ticket ID
- Complaint
- Category
- Department
- Priority
- Sentiment
- Confidence
- Recommended solution

### Word Sense Disambiguation

```http
POST /api/wsd
```

Example:

```json
{
  "text": "The fisherman sat near the bank of the river"
}
```

Possible result:

```json
{
  "meaning": "River Bank"
}
```

### Text Similarity

```http
POST /api/similarity
```

Example:

```json
{
  "text": "my machine has stopped working"
}
```

The response contains:

- Input text
- Most similar complaint
- Similarity score

---

## 🧪 Experiments 1–10

| Experiment | Topic |
|---|---|
| 1 | NLP Text Processing |
| 2 | TF-IDF |
| 3 | Text Classification |
| 4 | Sentiment Analysis |
| 5 | Recommendation |
| 6 | POS Tagging |
| 7 | Chunking |
| 8 | Named Entity Recognition |
| 9 | Word Sense Disambiguation |
| 10 | Real-Time Text Similarity Recognizer |

### Experiment 10

The final experiment demonstrates:

```text
TF-IDF + Cosine Similarity
```

Run it from the backend folder:

```powershell
python experiments\experiment10_text_similarity.py
```

---

## 🧾 Current Complaint Categories

### Machine Problem
Examples:
- machine not working
- motor stopped
- conveyor not running
- equipment not working

### Quality Problem
Examples:
- product defective
- product scratches
- poor product quality
- product damaged

### Production Delay
Examples:
- production delayed
- production line late
- delivery late
- production slow

### Material Problem
Examples:
- material missing
- raw material unavailable
- material shortage
- not enough material

---

## 📊 Text Similarity Method

SmartFix converts complaint texts into TF-IDF vectors and then calculates cosine similarity.

```text
Complaint Text
      ↓
TF-IDF Vectorization
      ↓
Numerical Vectors
      ↓
Cosine Similarity
      ↓
Most Similar Complaint
      ↓
Similarity Percentage
```

The current implementation is mainly lexical, so two sentences with similar meaning but very different wording may not always receive a high similarity score.

---

## 📈 Dashboard

The SmartFix dashboard provides:

- Total complaints
- High-priority complaints
- Open complaints
- Resolved complaints
- Category-wise analytics
- Smart insights
- Complaint history
- Status tracking

Complaint history is currently stored locally in browser `localStorage`, rather than in a centralized database.

---

## 🔬 Validation and Testing

### Complaint Analysis

Input:

```text
The conveyor is not running
```

Expected category:

```text
Machine Problem
```

### Quality Complaint

Input:

```text
The product has scratches and poor quality
```

Expected category:

```text
Quality Problem
```

### Production Complaint

Input:

```text
The production line is running late
```

Expected category:

```text
Production Delay
```

### Material Complaint

Input:

```text
We do not have enough raw material
```

Expected category:

```text
Material Problem
```

### WSD

Input:

```text
The fisherman sat near the bank of the river
```

Expected:

```text
River Bank
```

Input:

```text
I deposited money in the bank
```

Expected:

```text
Financial Bank
```

### Text Similarity

Input:

```text
machine is not working
```

The system returns a similar complaint and similarity score.

---

## 🎯 Project Objectives

1. Automate basic complaint analysis.
2. Classify complaints using NLP.
3. Recommend solutions for common complaint categories.
4. Detect complaint priority.
5. Detect basic sentiment.
6. Suggest a responsible department.
7. Generate complaint ticket IDs.
8. Identify contextual word meanings.
9. Find similar complaints.
10. Demonstrate multiple NLP techniques in one integrated project.

---

## ✅ Advantages

- Simple and easy-to-use web interface
- Multiple NLP capabilities in one system
- Fast local processing
- Easy to demonstrate in a viva or project presentation
- Clear and interpretable complaint categories
- Practical experiments connected to one application
- No external API is required for the current prototype

---

## ⚠️ Current Limitations

The current SmartFix implementation is a prototype.

- Complaint categories use predefined examples.
- Complaint classification is not yet trained on a large real-world complaint dataset.
- Sentiment and priority detection are lightweight rule-based modules.
- TF-IDF similarity is mainly lexical rather than deep semantic similarity.
- Complaint history is stored locally in the browser.
- The current prototype is designed for English text.
- Production deployment would require stronger data storage, authentication, monitoring, and evaluation.

---

## 🚀 Future Scope

SmartFix can be further extended with:

- A real complaint dataset
- Machine-learning based complaint classification
- Transformer-based NLP models
- Semantic sentence embeddings
- Multilingual complaint analysis
- Database-backed complaint history
- User authentication and role-based access
- Email and notification alerts
- Automatic department assignment
- Larger analytics dashboards
- Cloud deployment
- Voice-based complaint input
- Feedback-based model improvement

---

## 📸 Screenshots

Recommended screenshots for the repository:

1. SmartFix Home Page
2. Complaint Analyzer
3. Complaint Analysis Result
4. Text Similarity
5. WSD Result
6. Analytics Dashboard
7. Complaint History
8. FastAPI `/docs` page

Example:

```markdown
![SmartFix Home](screenshots/home.png)
![Complaint Analyzer](screenshots/analyzer.png)
![Dashboard](screenshots/dashboard.png)
```

---

## 👩‍💻 Author

**Prachi Ramchandra Tarmale**

Bachelor of Engineering  
Artificial Intelligence and Data Science  
Smt. Indira Gandhi College of Engineering, Ghansoli

Academic Year: **2025–26**

Project Guide: **Prof. Nirosha Uppu**

---

## 📜 Project Type

**BE Mini Project**

**Project Title:**  
**SmartFix NLP – AI-Powered Complaint Analysis and Solution Recommendation System**

---

## ⭐ Acknowledgement

This project was developed as an academic mini project to demonstrate the practical application of Natural Language Processing techniques in complaint management. The project combines multiple NLP experiments into a single application-oriented system.

---

## 📄 License

This repository is intended primarily for academic and educational use.

---

## 🔗 Repository

```text
https://github.com/PTarmale/SmartFix-NLP
```
