<div align="right">
  <a href="README.md"><img src="https://img.shields.io/badge/English-blue?style=flat-square&logo=github&logoColor=white&labelColor=000080" alt="English"></a>
  <a href="README.vi.md"><img src="https://img.shields.io/badge/Tiếng_Việt-red?style=flat-square&color=C90000" alt="Tiếng Việt"></a>
</div>

# 📰 Topic Classification - Phân Loại Văn Bản Tiếng Việt

![Banner](docs/assets/banner.png)

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

## 📖 Giới Thiệu

**Topic Classification** là một ứng dụng web tích hợp trí tuệ nhân tạo (AI), có khả năng tự động phân loại văn bản tiếng Việt thành **10 chủ đề định sẵn** với độ chính xác cao (85-92%). Được xây dựng dựa trên thuật toán **Naive Bayes** và kỹ thuật vector hóa **TF-IDF**, hệ thống giúp sắp xếp hiệu quả các bài báo tin tức, bài đăng mạng xã hội và các nội dung văn bản khác.

**Điểm Nổi Bật:**
- 🎯 **10 Chủ Đề:** Thể thao, Kinh tế, Giải trí, Công nghệ, Giáo dục, Sức khỏe, Pháp luật, Thời sự, Khoa học, Văn hóa.
- ⚡ **Thời Gian Thực:** Trả kết quả phân loại chỉ trong vài giây.
- 💾 **Lịch Sử:** Lưu và xem lại các kết quả phân loại trước đây.
- 🌓 **Chế Độ Tối:** Giao diện hiện đại với tùy chọn chủ đề Sáng/Tối (Dark Mode).
- 📱 **Tương Thích:** Tối ưu hóa hiển thị cho máy tính, máy tính bảng và điện thoại di động.

---

## 📑 Mục Lục

- [Giới Thiệu](#-giới-thiệu)
- [Tác Giả](#-tác-giả)
- [Công Nghệ Sử Dụng](#-công-nghệ-sử-dụng)
- [Tính Năng Chính](#-tính-năng-chính)
- [Cài Đặt & Thiết Lập](#-cài-đặt--thiết-lập)
- [Hướng Dẫn Sử Dụng](#-hướng-dẫn-sử-dụng)
- [Cấu Trúc Dự Án](#-cấu-trúc-dự-án)
- [Chi Tiết Mô Hình](#-chi-tiết-mô-hình)
- [Ảnh Demo](#-ảnh-demo)
- [Tài Liệu API](#-tài-liệu-api)
- [Lộ Trình Phát Triển](#-lộ-trình-phát-triển)
- [Giấy Phép](#-giấy-phép)
- [Tham Khảo](#-tham-khảo)

---
## 👨‍💻 Tác Giả

Dự án được phát triển và duy trì bởi:

| Avatar | Thông tin | Liên hệ |
| :---: | :--- | :--- |
| <img src="docs/assets/github-avatar.png" width="80" height="80" style="border-radius:50%; object-fit:cover;"/> | **Trần Đức Long** | [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)]([https://github.com/TranDucLong040904](https://github.com/TranDucLong040904))<br>[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:22010139@st.phenikaa-uni.edu.vn) |

## 🛠️ Công Nghệ Sử Dụng

<details>
<summary><b>Nhấn để xem chi tiết công nghệ</b></summary>

### Backend (Xử lý)
| Thành phần | Công nghệ | Phiên bản |
|-----------|------------|---------|
| **Framework** | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) | `3.0.0` |
| **Thư viện AI** | ![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat-square&logo=scikit-learn&logoColor=white) | `1.3.2` |
| **Ngôn ngữ** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) | `3.11` |
| **Thuật toán** | **Multinomial Naive Bayes + TF-IDF** | - |
| **Bổ trợ** | ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat-square&logo=numpy&logoColor=white) | - |

### Frontend (Giao diện)
| Thành phần | Công nghệ | Phiên bản |
|-----------|------------|---------|
| **CSS Framework** | ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-%2338B2AC.svg?style=flat-square&logo=tailwind-css&logoColor=white) | `3.4` |
| **Biểu đồ** | ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=flat-square&logo=chart.js&logoColor=white) | `4.4` |
| **Icons** | ![Material Design](https://img.shields.io/badge/Material%20Design-757575?style=flat-square&logo=materialdesign&logoColor=white) | - |
| **Ngôn ngữ** | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat-square&logo=javascript&logoColor=%23F7DF1E) | - |
| **Lưu trữ** | ![LocalStorage](https://img.shields.io/badge/-LocalStorage-lightgrey?style=flat-square) | - |


### Công Cụ Phát Triển
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) Quản lý phiên bản (Version control)
- ![VSCode](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) Trình soạn thảo code
- ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) Khám phá dữ liệu & huấn luyện mô hình

</details>

---
## 🚀 Tính Năng Chính

### Dành Cho Người Dùng
* ✅ **Phân Loại Văn Bản:** Dự đoán chủ đề tức thì cho văn bản tiếng Việt.
* ✅ **Kết Quả Trực Quan:** Hiển thị biểu đồ Donut và thanh tiến trình kèm độ tin cậy (%).
* ✅ **Quản Lý Lịch Sử:** - Tự động lưu kết quả phân loại.
  - Lọc lịch sử theo chủ đề.
  - Xóa một hoặc nhiều bản ghi cùng lúc.
  - Nhấn vào lịch sử để xem lại kết quả cũ.
* ✅ **Chế Độ Tối (Dark Mode):** Chuyển đổi linh hoạt Sáng/Tối (tự động lưu trạng thái).
* ✅ **Giao Diện Responsive:** Trải nghiệm mượt mà trên mọi thiết bị.

### Dành Cho Lập Trình Viên
* ✅ **RESTful API:** Dễ dàng tích hợp với các ứng dụng bên ngoài.
* ✅ **Mô Hình Pre-trained:** Trình phân loại đã được huấn luyện sẵn, dùng được ngay.
* ✅ **Mở Rộng Dữ Liệu:** Quy trình thêm dữ liệu huấn luyện đơn giản.
* ✅ **Code Module Hóa:** Phân tách rõ ràng giữa Backend và Frontend.

---

## ⚙️ Cài Đặt & Thiết Lập

### Yêu Cầu Hệ Thống
```bash
Python   >= 3.11
pip      >= 23.0
Git      >= 2.40
```

### Bắt Đầu Nhanh

```bash
# 1. Clone kho lưu trữ (tải code về máy)
git clone https://github.com/TranDucLong040904/topic-classification.git
cd topic-classification

# 2. Tạo môi trường ảo (Virtual Environment)
python -m venv venv

# 3. Kích hoạt môi trường ảo
# Trên Windows: 
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate

# 4. Cài đặt các thư viện cần thiết
cd backend
pip install -r requirements.txt

# 5. Chạy Backend API
python app.py
# ✅ Backend sẽ chạy tại:  http://localhost:5000
```

### Chạy Giao Diện (Frontend)

**Cách 1: Mở file trực tiếp**
```bash
cd ../frontend
start pages/home.html      # Windows
open pages/home.html       # macOS
xdg-open pages/home.html   # Linux
```

**Cách 2: Dùng Local Server (Khuyên dùng)**
```bash
cd frontend
python -m http.server 8000
# ✅ Truy cập: http://localhost:8000/pages/home.html
```

---

## 📖 Hướng Dẫn Sử Dụng

<details>
<summary><b>1. Phân Loại Văn Bản - Nhấn để mở rộng</b></summary>

<br>

```
Bước 1: Truy cập trang "Phân Loại" (Classify)
Bước 2: Nhập văn bản tiếng Việt cần kiểm tra (tối thiểu 10 ký tự)
Bước 3: Nhấn nút "Phân Loại Ngay"
Bước 4: Xem kết quả: 
        • Chủ đề chính kèm độ tin cậy (%)
        • Top 5 chủ đề liên quan (biểu đồ tròn)
        • Chi tiết điểm số từng chủ đề
```

</details>

<details>
<summary><b>2. Quản Lý Lịch Sử - Nhấn để mở rộng</b></summary>

<br>

```
Xem Lịch Sử:     Truy cập trang "Lịch Sử"
Lọc Dữ Liệu:     Chọn chủ đề từ menu thả xuống (Dropdown)
Xóa Nhiều Mục:   Tích vào ô vuông bên cạnh → Nhấn "Xóa"
Xem Lại:         Nhấn vào bất kỳ mục nào trong danh sách để xem lại kết quả
```

</details>

<details>
<summary><b>3. Đổi Giao Diện - Nhấn để mở rộng</b></summary>

<br>

```
Chuyển đổi:     Nhấn vào biểu tượng ☀️/🌙 trên thanh menu
Tự động lưu:    Chế độ đã chọn sẽ được giữ nguyên khi bạn tải lại trang
```

</details>

---

## 📂 Cấu Trúc Dự Án

<details>
<summary><b>Nhấn để xem cây thư mục</b></summary>

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

## 📊 Đánh Giá Hiệu Suất Mô Hình

<div align="left">

| 🎯 Accuracy | 🎯 Precision | 🎯 Recall | 🎯 F1-Score |
| :---: | :---: | :---: | :---: |
| ![Accuracy](https://img.shields.io/badge/89.5%25-success?style=for-the-badge&logo=target&logoColor=white) | ![Precision](https://img.shields.io/badge/88.2%25-blue?style=for-the-badge&logo=unrealengine&logoColor=white) | ![Recall](https://img.shields.io/badge/87.9%25-blueviolet?style=for-the-badge&logo=threedotjs&logoColor=white) | ![F1](https://img.shields.io/badge/88.0%25-ff69b4?style=for-the-badge&logo=scikitlearn&logoColor=white) |

</div>

<br>

<details>
<summary><b>⚙️ Xem Cấu Hình & Chi Tiết Phân Tích</b></summary>


### 🧠 Cấu Hình Thuật Toán & Huấn Luyện
> **Thuật toán cốt lõi:** `Multinomial Naive Bayes` với `TF-IDF Vectorization`

| Tham số | Giá trị | Mô tả |
| :--- | :--- | :--- |
| 📚 **Kích thước Dữ liệu** | `2,000` mẫu | Cân bằng (200 mẫu/chủ đề) |
| ✂️ **Tỷ lệ Chia tập** | `80/20` | Train/Test split |
| 🔠 **TF-IDF Features** | `5,000` | Số lượng từ vựng tối đa |
| 🔗 **N-gram Range** | `(1, 2)` | Unigrams + Bigrams |
| 🧩 **Smoothing** | `alpha=1.0` | Làm mịn Laplace |
| 🎲 **Random State** | `42` | Đảm bảo kết quả tái lập được |

<br>

### 📈 Phân Tích Hiệu Suất Theo Chủ Đề
*Biểu đồ trực quan điểm số F1-Score trên tất cả các chủ đề (Sắp xếp theo hiệu suất).*

| Chủ đề | Precision | Recall | F1-Score | Đánh Giá Hiệu Suất |
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

## 🖼️ Ảnh Demo

<details>
<summary><b>🏠 Trang Chủ - Nhấn để mở rộng</b></summary>

<br>

**Trang chính (Chế độ Sáng):**

![Home Light](docs/assets/home-light.png)

**Trang chính (Chế độ Tối):**

![Home Dark](docs/assets/home-dark.png)

**Phần Tính năng:**

![Features](docs/assets/features-dark.png)

</details>

<details>
<summary><b>🔍 Trang Phân Loại - Nhấn để mở rộng</b></summary>

<br>

**Giao diện Nhập liệu:**

![Classify Input](docs/assets/input.png)
![Classify Input](docs/assets/input-text.png)

**Hiển thị Kết quả:**

![Classify Results](docs/assets/results.png)

**Giao diện Mobile:**

![Classify Mobile](docs/assets/mobile-view.png)

</details>

<details>
<summary><b>📜 Trang Lịch Sử - Nhấn để mở rộng</b></summary>

<br>

**Danh sách Lịch sử:**

![History List](docs/assets/history-list.png)

**Bộ lọc & Thao tác:**

![History Actions](docs/assets/filter-topic.png)

**Trạng thái Trống:**

![History Empty](docs/assets/delete-all.png)
![alt text](docs/assets/empty-history.png)
</details>

---

## 📡 Tài Liệu API

<details>
<summary><b>Các Endpoint API - Nhấn để mở rộng</b></summary>



### Đường dẫn gốc (Base URL)
```
http://localhost:5000
```

### 1. Kiểm tra Trạng thái (Health Check)

**Endpoint:**
```http
GET /
```

**Phản hồi:**
```html
<h1>📰 Topic Classification API</h1>
<p>✅ API is running</p>
```

---

### 2. Phân Loại Văn Bản

**Endpoint:**
```http
POST /predict
```

**Request Headers:**
```http
Content-Type: application/json
```

**Request Body (Thân yêu cầu):**
```json
{
  "text": "Đội tuyển Việt Nam giành chiến thắng 3-0 trong trận chung kết AFF Cup"
}
```

**Response (Thành công - 200):**
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

**Response (Lỗi - 400):**
```json
{
  "status": "error",
  "message": "Text is required"
}
```

---

### Ví dụ Sử dụng

**cURL:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text":"Thị trường chứng khoán Việt Nam tăng mạnh hôm nay"}'
```

**Python:**
```python
import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={'text': 'Thị trường chứng khoán Việt Nam tăng mạnh hôm nay'}
)

data = response.json()
print(f"Chủ đề: {data['top_topic']}")
print(f"Độ tin cậy: {data['predictions'][0]['probability']}%")
```

**JavaScript (Fetch API):**
```javascript
fetch('http://localhost:5000/predict', {
  method:  'POST',
  headers:  {'Content-Type': 'application/json'},
  body: JSON.stringify({
    text: 'Thị trường chứng khoán Việt Nam tăng mạnh hôm nay'
  })
})
.then(res => res.json())
.then(data => {
  console.log('Chủ đề:', data.top_topic);
  console.log('Độ tin cậy:', data.predictions[0].probability + '%');
});
```

</details>

---

## 🗺️ Lộ Trình Phát Triển

<details>
<summary><b>Các Giai Đoạn Phát Triển - Nhấn để mở rộng</b></summary>

### Giai đoạn 1-6: ✅ Đã Hoàn Thành
- [x] Thiết lập môi trường
- [x] Phát triển Backend API
- [x] Phát triển Giao diện Frontend
- [x] Huấn luyện mô hình với bộ dữ liệu
- [x] Cải thiện UI/UX
- [x] Kiểm thử & sửa lỗi

### Giai đoạn 7: 🔄 Đang Thực Hiện
- [x] Viết tài liệu (README)
- [ ] Triển khai môi trường Production
- [ ] Báo cáo kỹ thuật

### Giai đoạn 8: 📅 Dự Kiến
- [ ] Triển khai Backend lên Render
- [ ] Triển khai Frontend lên Vercel
- [ ] Cấu hình tên miền riêng
- [ ] Tối ưu hóa hiệu suất
- [ ] Mở rộng bộ dữ liệu huấn luyện
- [ ] Cải thiện độ chính xác mô hình (mục tiêu > 92%)
- [ ] Thêm tính năng xuất dữ liệu (CSV/PDF)
- [ ] Giới hạn tốc độ gọi API (Rate limiting)
- [ ] Xác thực người dùng (Đăng nhập/Đăng ký)
- [ ] Hỗ trợ đa ngôn ngữ

</details>

---

## 📜 Giấy Phép

```
Bản quyền © 2025 Trần Đức Long

Dự án này được chia sẻ chỉ với mục đích GIÁO DỤC và THAM KHẢO.

✅ Được phép: 
   • Xem và nghiên cứu mã nguồn
   • Clone về để học tập và nghiên cứu cá nhân
   • Đóng góp thông qua Pull Requests

❌ Không được phép: 
   • Sử dụng cho mục đích thương mại khi chưa có sự cho phép
   • Bán lại hoặc phân phối lại
   • Tự nhận là sản phẩm của riêng mình

Mọi quyền sở hữu trí tuệ thuộc về tác giả.
```

---

## 🔗 Tham Khảo

### Tài Liệu Chính Thức
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Chart.js Documentation](https://www.chartjs.org/docs/)
- [Material Symbols Guide](https://fonts.google.com/icons)

### Dữ Liệu & Mô Hình
- [Hugging Face Vietnamese Dataset](https://huggingface.co/)
- [Vietnamese NLP Resources](https://github.com/undertheseanlp)


---

## ☎️ Liên Hệ
- **GitHub:** [Trần Đức Long](https://github.com/TranDucLong040904)
- **Email:** 22010139@st.phenikaa-uni.edu.vn
- **Kho lưu trữ dự án:** [Topic Classification](https://github.com/TranDucLong040904/topic-classification.git)
<div align="center">

---
**⭐ Nếu bạn thấy dự án này hữu ích, hãy tặng 1 sao nhé! ⭐**

---
<br>

Được thực hiện với ❤️ bởi **Trần Đức Long**

Bản quyền © 2025 • [Giấy Phép MIT](#-giấy-phép)

**[⬆ Về đầu trang](#-topic-classification---phân-loại-văn-bản-tiếng-việt)**

</div>