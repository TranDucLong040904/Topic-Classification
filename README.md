<div align="right">
  <a href="README.md"><img src="https://img.shields.io/badge/English-blue?style=flat-square&logo=github&logoColor=white&labelColor=000080" alt="English"></a>
  <a href="README.vi.md"><img src="https://img.shields.io/badge/Tiếng_Việt-red?style=flat-square&color=C90000" alt="Tiếng Việt"></a>
</div>

# 📰 Topic Classification - Vietnamese Text Classifier

![Banner](docs\assets\banner.png)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

![Repo Size](https://img.shields.io/github/repo-size/TranDucLong040904/topic-classification?style=flat-square&label=Size&color=orange)
![Last Commit](https://img.shields.io/github/last-commit/TranDucLong040904/topic-classification?style=flat-square&label=Last%20Commit&color=blue)
![Stars](https://img.shields.io/github/stars/TranDucLong040904/topic-classification?style=flat-square&color=yellow)

</div>

---

## 📖 Introduction

**Topic Classification** is an AI-powered web application that automatically classifies Vietnamese text into **10 predefined topics** with high accuracy (85-92%). Built using **Naive Bayes** algorithm and **TF-IDF** vectorization, the system efficiently organizes news articles, social media posts, and various text content.

**Key Highlights:**
- 🎯 **10 Topics:** Sports, Economy, Entertainment, Technology, Education, Health, Law, News, Science, Culture
- ⚡ **Real-time:** Classification results in seconds
- 💾 **History:** Save and review past classifications
- 🌓 **Dark Mode:** Modern UI with light/dark theme
- 📱 **Responsive:** Optimized for desktop, tablet, and mobile

---

## 📑 Table of Contents

- [Introduction](#-introduction)
- [About the Author](#-about-the-author)
- [Technology Stack](#-technology-stack)
- [Key Features](#-key-features)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Model Details](#-model-details)
- [Demo Screenshots](#-demo-screenshots)
- [API Documentation](#-api-documentation)
- [Roadmap](#-roadmap)
- [License](#-license)
- [References](#-references)

---
## 👨‍💻 About the Author

The project is developed and maintained by:

| Avatar | Information | Contact |
| :---: | :--- | :--- |
| <img src="docs/assets/github-avatar.png" width="80" height="80" style="border-radius:50%; object-fit:cover;"/> | **Tran Duc Long** | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/TranDucLong040904)<br>[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:22010139@st.phenikaa-uni.edu.vn) |

## 🛠️ Technology Stack

<details>
<summary><b>Click to view technology details</b></summary>

### Backend
| Component | Technology | Version |
|-----------|------------|---------|
| **Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | `3.0.0` |
| **ML Library** | ![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white) | `1.3.2` |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | `3.11` |
| **Algorithm** | **Multinomial Naive Bayes + TF-IDF** | - |
| **Additional** | ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat-square&logo=numpy&logoColor=white) | - |

### Frontend
| Component | Technology | Version |
|-----------|------------|---------|
| **CSS Framework** | ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-%2338B2AC.svg?style=flat-square&logo=tailwind-css&logoColor=white) | `3.4` |
| **Chart Library** | ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=flat-square&logo=chart.js&logoColor=white) | `4.4` |
| **Icons** | ![Material Design](https://img.shields.io/badge/Material%20Design-757575?style=flat-square&logo=materialdesign&logoColor=white) | - |
| **Languages** | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat-square&logo=javascript&logoColor=%23F7DF1E) | - |
| **Storage** | ![LocalStorage](https://img.shields.io/badge/-LocalStorage-lightgrey?style=flat-square) | - |


### Development Tools
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) Version control
- ![VSCode](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) Code editor
- ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) Data exploration & model training

</details>

---
## 🚀 Key Features

### For End Users
* ✅ **Text Classification:** Instant topic prediction for Vietnamese text
* ✅ **Visual Results:** Donut chart and progress bars with confidence scores
* ✅ **History Management:** 
  - Auto-save classification results
  - Filter by topic
  - Delete single or multiple records
  - Click to reload previous results
* ✅ **Dark Mode:** Toggle between light/dark themes (persists across pages)
* ✅ **Responsive Design:** Seamless experience on all devices

### For Developers
* ✅ **RESTful API:** Easy integration with external applications
* ✅ **Pre-trained Model:** Ready-to-use classifier
* ✅ **Expandable Dataset:** Simple data addition process
* ✅ **Modular Code:** Clean separation of backend/frontend

---

## ⚙️ Installation & Setup

### System Requirements
```bash
Python   >= 3.11
pip      >= 23.0
Git      >= 2.40
```

### Quick Start

```bash
# 1. Clone repository
git clone https://github.com/TranDucLong040904/topic-classification.git
cd topic-classification

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows: 
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
cd backend
pip install -r requirements.txt

# 5. Run backend API
python app.py
# ✅ Backend runs at:  http://localhost:5000
```

### Launch Frontend

**Option 1: Direct file access**
```bash
cd ../frontend
start pages/home.html      # Windows
open pages/home.html       # macOS
xdg-open pages/home.html   # Linux
```

**Option 2: Local server**
```bash
cd frontend
python -m http.server 8000
# ✅ Visit: http://localhost:8000/pages/home.html
```

---

## 📖 Usage

<details>
<summary><b>1. Text Classification - Click to expand</b></summary>

<br>

```
Step 1: Navigate to "Classify" page
Step 2: Enter Vietnamese text (minimum 10 characters)
Step 3: Click "Classify" button
Step 4: View results: 
        • Main topic with confidence score
        • Top 5 topics (donut chart)
        • Detailed breakdown (progress bars)
```

</details>

<details>
<summary><b>2. History Management - Click to expand</b></summary>

<br>

```
View History:     Go to "History" page
Filter:           Select topic from dropdown
Select Multiple:  Check boxes → Click "Delete"
Reload Result:    Click on any history item
```

</details>

<details>
<summary><b>3. Theme Toggle - Click to expand</b></summary>

<br>

```
Toggle:         Click ☀️/🌙 icon in navbar
Auto-save:      Theme persists across pages and sessions
```

</details>

---

## 📂 Project Structure

<details>
<summary><b>Click to view folder structure</b></summary>

<br>

```
Topic Classification
├── 📁 backend
│   ├── 📁 data
│   │   └── 📄 improved_dataset.csv
│   ├── 📁 models
│   │   ├── 📄 topic_classifier.pkl
│   │   └── 📄 vectorizer.pkl
│   ├── 🐍 app.py
│   ├── 🐍 create_improved_dataset.py
│   ├── 📄 requirements.txt
│   ├── 🐍 test_api.py
│   └── 🐍 train_model.py
├── 📁 frontend
│   ├── 📁 css
│   │   ├── 🎨 classify.css
│   │   ├── 🎨 history.css
│   │   ├── 🎨 home.css
│   │   └── 🎨 shared.css
│   ├── 📁 js
│   │   ├── 📄 classify.js
│   │   ├── 📄 history.js
│   │   ├── 📄 navbar.js
│   │   └── 📄 theme.js
│   ├── 📁 libs
│   ├── 📁 pages
│   │   ├── 🌐 classify.html
│   │   ├── 🌐 history.html
│   │   └── 🌐 home.html
│   └── 📄 config.js
├── ⚙️ .gitignore
└── 📝 README.md
```

</details>

---

## 📊 Model Performance Evaluation

<div align="left">

| 🎯 Accuracy | 🎯 Precision | 🎯 Recall | 🎯 F1-Score |
| :---: | :---: | :---: | :---: |
| ![Accuracy](https://img.shields.io/badge/89.5%25-success?style=for-the-badge&logo=target&logoColor=white) | ![Precision](https://img.shields.io/badge/88.2%25-blue?style=for-the-badge&logo=unrealengine&logoColor=white) | ![Recall](https://img.shields.io/badge/87.9%25-blueviolet?style=for-the-badge&logo=threedotjs&logoColor=white) | ![F1](https://img.shields.io/badge/88.0%25-ff69b4?style=for-the-badge&logo=scikitlearn&logoColor=white) |

</div>

<br>

<details>
<summary><b>⚙️ View Configuration & Detailed Breakdown</b></summary>


### 🧠 Algorithm & Training Configuration
> **Core Algorithm:** `Multinomial Naive Bayes` with `TF-IDF Vectorization`

| Parameter | Value | Description |
| :--- | :--- | :--- |
| 📚 **Dataset Size** | `2,000` samples | Balanced (200/topic) |
| ✂️ **Split Ratio** | `80/20` | Train/Test split |
| 🔠 **TF-IDF Features** | `5,000` | Max vocabulary size |
| 🔗 **N-gram Range** | `(1, 2)` | Unigrams + Bigrams |
| 🧩 **Smoothing** | `alpha=1.0` | Laplace smoothing |
| 🎲 **Random State** | `42` | Reproducibility |

<br>

### 📈 Per-Topic Performance Analysis
*Visual representation of F1-Scores across all topics (Sorted by Performance).*

| Topic | Precision | Recall | F1-Score | Performance Rating |
| :--- | :---: | :---: | :---: | :--- |
| **Sports** (Thể thao) | 95% | 92% | **93%** | ![93%](https://img.shields.io/badge/Score-93%25-2ea44f?style=flat-square) |
| **Technology** (Công nghệ) | 91% | 89% | **90%** | ![90%](https://img.shields.io/badge/Score-90%25-2ea44f?style=flat-square) |
| **News** (Thời sự) | 90% | 88% | **89%** | ![89%](https://img.shields.io/badge/Score-89%25-0366d6?style=flat-square) |
| **Economy** (Kinh tế) | 90% | 88% | **89%** | ![89%](https://img.shields.io/badge/Score-89%25-0366d6?style=flat-square) |
| **Science** (Khoa học) | 89% | 87% | **88%** | ![88%](https://img.shields.io/badge/Score-88%25-0366d6?style=flat-square) |
| **Health** (Sức khỏe) | 88% | 86% | **87%** | ![87%](https://img.shields.io/badge/Score-87%25-0366d6?style=flat-square) |
| **Entertainment** (Giải trí) | 87% | 85% | **86%** | ![86%](https://img.shields.io/badge/Score-86%25-0366d6?style=flat-square) |
| **Culture** (Văn hóa) | 87% | 85% | **86%** | ![86%](https://img.shields.io/badge/Score-86%25-0366d6?style=flat-square) |
| **Law** (Pháp luật) | 86% | 84% | **85%** | ![85%](https://img.shields.io/badge/Score-85%25-f9a825?style=flat-square) |
| **Education** (Giáo dục) | 85% | 83% | **84%** | ![84%](https://img.shields.io/badge/Score-84%25-f9a825?style=flat-square) |

</details>

---

## 🖼️ Demo Screenshots

<details>
<summary><b>🏠 Home Page - Click to expand</b></summary>

<br>

**Landing Page (Light Mode):**

![Home Light](docs\assets\home-light.png)

**Landing Page (Dark Mode):**

![Home Dark](docs\assets\home-dark.png)

**Features Section:**

![Features](docs\assets\features-dark.png)

</details>

<details>
<summary><b>🔍 Classification Page - Click to expand</b></summary>

<br>

**Input Interface:**

![Classify Input](docs/assets/input.png)
![Classify Input](docs/assets/input-text.png)

**Results Display:**

![Classify Results](docs\assets\results.png)

**Mobile View:**

![Classify Mobile](docs\assets\mobile-view.png)

</details>

<details>
<summary><b>📜 History Page - Click to expand</b></summary>

<br>

**History List:**

![History List](docs\assets\history-list.png)

**Filter & Actions:**

![History Actions](docs\assets\filter-topic.png)

**Empty State:**

![History Empty](docs\assets\delete-all.png)
![alt text](docs/assets/empty-history.png)
</details>

---

## 📡 API Documentation

<details>
<summary><b>API Endpoints - Click to expand</b></summary>



### Base URL
```
http://localhost:5000
```

### 1. Health Check

**Endpoint:**
```http
GET /
```

**Response:**
```html
<h1>📰 Topic Classification API</h1>
<p>✅ API is running</p>
```

---

### 2. Classify Text

**Endpoint:**
```http
POST /predict
```

**Request Headers:**
```http
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "Đội tuyển Việt Nam giành chiến thắng 3-0 trong trận chung kết AFF Cup"
}
```

**Response (Success - 200):**
```json
{
  "status": "success",
  "top_topic": "Thể thao",
  "predictions": [
    {"topic": "Thể thao", "probability": 95.2},
    {"topic": "Văn hóa", "probability":  2.1},
    {"topic": "Thời sự", "probability": 1.5},
    {"topic": "Giải trí", "probability": 0.8},
    {"topic": "Kinh tế", "probability": 0.4}
  ]
}
```

**Response (Error - 400):**
```json
{
  "status": "error",
  "message": "Text is required"
}
```

---

### Usage Examples

**cURL:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Vietnamese stock market rises sharply today"}'
```

**Python:**
```python
import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={'text': 'Vietnamese stock market rises sharply today'}
)

data = response.json()
print(f"Topic: {data['top_topic']}")
print(f"Confidence: {data['predictions'][0]['probability']}%")
```

**JavaScript (Fetch API):**
```javascript
fetch('http://localhost:5000/predict', {
  method:  'POST',
  headers:  {'Content-Type': 'application/json'},
  body: JSON.stringify({
    text: 'Vietnamese stock market rises sharply today'
  })
})
.then(res => res.json())
.then(data => {
  console.log('Topic:', data.top_topic);
  console.log('Confidence:', data.predictions[0].probability + '%');
});
```

</details>

---

## 🗺️ Roadmap

<details>
<summary><b>Development Phases - Click to expand</b></summary>

### Phase 1-6: ✅ Completed
- [x] Environment setup
- [x] Backend API development
- [x] Frontend development
- [x] Model training with dataset
- [x] UI/UX improvements
- [x] Testing & debugging

### Phase 7: 🔄 In Progress
- [x] Documentation (README)
- [ ] Production deployment
- [ ] Technical report

### Phase 8: 📅 Planned
- [ ] Deploy Backend to Render
- [ ] Deploy Frontend to Vercel
- [ ] Custom domain configuration
- [ ] Performance optimization
- [ ] Expand training dataset
- [ ] Improve model accuracy (target 92%+)
- [ ] Add export functionality (CSV/PDF)
- [ ] API rate limiting
- [ ] User authentication (optional)
- [ ] Multi-language support

</details>

---

## 📜 License

```
Copyright © 2025 Tran Duc Long

This project is shared for EDUCATIONAL and REFERENCE purposes only. 

✅ Allowed: 
   • View and study the source code
   • Clone for personal learning and research
   • Contribute via pull requests

❌ Not Allowed: 
   • Commercial use without permission
   • Resale or redistribution
   • Claim as your own work

All intellectual property rights belong to the author.
```

---

## 🔗 References





### Official Documentation
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [Material Symbols Guide](https://fonts.google.com/icons)

### Datasets & Models
- [Hugging Face Vietnamese Dataset](https://huggingface.co/)
- [Vietnamese NLP Resources](https://github.com/undertheseanlp)


---

## ☎️ Contact
- **GitHub:** [Tran Duc Long](https://github.com/TranDucLong040904)
- **Email:** 22010139@st.phenikaa-uni.edu.vn
- **Project Repository:** [Topic Classification](https://github.com/TranDucLong040904/topic-classification.git)
<div align="center">

---
**⭐ If you find this project helpful, please give it a star! ⭐**

---
<br>

Made with ❤️ by **Tran Duc Long**

Copyright © 2025 • [MIT License](#-license)

**[⬆ Back to top](#-topic-classification---vietnamese-text-classifier)**

</div>