# ============================================
# TRAIN MODEL PHÂN LOẠI TOPIC
# Train Topic Classification Model
# ============================================

import pandas as pd
import pickle
import os
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from underthesea import word_tokenize
import re

# ============================================
# CẤU HÌNH - CONFIGURATION
# ============================================

# File input - SỬA ĐỔI QUAN TRỌNG
# Input file - IMPORTANT CHANGE
INPUT_FILE = 'data/huggingface_dataset.csv'

# Thư mục lưu model
# Model output directory
OUTPUT_DIR = 'models'

# ============================================
# HÀM TIỀN XỬ LÝ - PREPROCESSING FUNCTIONS
# ============================================

def clean_text(text):
    """
    Làm sạch văn bản
    Clean text data
    """
    # Chuyển về chữ thường
    # Convert to lowercase
    text = text.lower()
    
    # Loại bỏ ký tự đặc biệt, giữ lại chữ cái tiếng Việt
    # Remove special characters, keep Vietnamese letters
    text = re.sub(r'[^\w\sáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', ' ', text)
    
    # Loại bỏ khoảng trắng thừa
    # Remove extra spaces
    text = ' '.join(text.split())
    
    return text


def tokenize_text(text):
    """
    Tách từ tiếng Việt
    Vietnamese word tokenization
    """
    try:
        tokens = word_tokenize(text, format="text")
        return tokens
    except: 
        return text


def load_dataset(file_path):
    """
    Đọc dataset từ file CSV
    Load dataset from CSV file
    """
    print(f"📂 Đang đọc dataset từ: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ Không tìm thấy file: {file_path}")
        print("💡 Chạy download_huggingface.py trước!")
        return None
    
    df = pd.read_csv(file_path)
    print(f"✅ Đã đọc {len(df)} mẫu")
    print(f"\n📊 Phân bố topics:")
    print(df['topic'].value_counts())
    
    return df


def preprocess_data(df):
    """
    Tiền xử lý dữ liệu
    Preprocess data
    """
    print("\n🧹 Đang tiền xử lý dữ liệu...")
    
    # Làm sạch văn bản
    # Clean text
    print("   - Làm sạch văn bản...")
    df['text_clean'] = df['text'].apply(clean_text)
    
    # Tách từ tiếng Việt
    # Vietnamese word tokenization
    print("   - Tách từ tiếng Việt (có thể mất 1-2 phút)...")
    df['text_tokenized'] = df['text_clean'].apply(tokenize_text)
    
    print("✅ Hoàn thành tiền xử lý")
    
    return df


# ============================================
# HÀM TRAIN MODEL - TRAINING FUNCTIONS
# ============================================

def train_model(df):
    """
    Train model phân loại topic
    Train topic classification model
    """
    print("\n🤖 BẮT ĐẦU TRAIN MODEL...\n")
    
    # Chia train/test (80/20)
    # Split train/test (80/20)
    X = df['text_tokenized']
    y = df['topic']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"📊 Dữ liệu train: {len(X_train)} mẫu")
    print(f"📊 Dữ liệu test: {len(X_test)} mẫu")
    
    # TF-IDF Vectorizer
    # Convert text to TF-IDF features
    print("\n🔤 Đang tạo TF-IDF features...")
    vectorizer = TfidfVectorizer(
        max_features=5000,      # Giữ 5000 từ quan trọng nhất
        ngram_range=(1, 2),     # Unigram + Bigram
        min_df=1,               # Từ xuất hiện ít nhất 1 lần
        max_df=0.9              # Bỏ từ xuất hiện >90% documents
    )
    
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    print(f"✅ TF-IDF shape: {X_train_tfidf.shape}")
    
    # Train Naive Bayes Model
    # Train Multinomial Naive Bayes classifier
    print("\n🎓 Đang train Multinomial Naive Bayes...")
    model = MultinomialNB(alpha=0.1)
    model.fit(X_train_tfidf, y_train)
    
    print("✅ Train model hoàn thành!")
    
    # Đánh giá model
    # Evaluate model
    print("\n📈 ĐÁNH GIÁ MODEL:\n")
    
    # Accuracy trên test set
    # Accuracy on test set
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"🎯 Accuracy: {accuracy*100:.2f}%")
    
    # Classification report chi tiết
    # Detailed classification report
    print("\n📊 Chi tiết theo từng topic:")
    print(classification_report(y_test, y_pred, zero_division=0))
    
    # Confusion Matrix
    print("\n🔢 Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    return model, vectorizer, accuracy


def save_model(model, vectorizer, output_dir=OUTPUT_DIR):
    """
    Lưu model và vectorizer
    Save model and vectorizer
    """
    print(f"\n💾 Đang lưu model...")
    
    # Tạo thư mục nếu chưa có
    # Create directory if not exists
    Path(output_dir).mkdir(exist_ok=True)
    
    # Lưu model
    # Save model
    model_path = Path(output_dir) / 'topic_classifier.pkl'
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"✅ Model đã lưu tại: {model_path}")
    
    # Lưu vectorizer
    # Save vectorizer
    vectorizer_path = Path(output_dir) / 'vectorizer.pkl'
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)
    print(f"✅ Vectorizer đã lưu tại:  {vectorizer_path}")


def test_prediction(model, vectorizer):
    """
    Test thử dự đoán với câu mẫu
    Test prediction with sample sentences
    """
    print("\n🧪 TEST THỬ DỰ ĐOÁN:\n")
    
    # Các câu test mẫu
    # Sample test sentences
    test_texts = [
        "Đội tuyển Việt Nam giành chiến thắng 2-0 trong trận đấu vòng loại World Cup hôm qua",
        "Giá vàng hôm nay tăng mạnh do ảnh hưởng của thị trường thế giới",
        "Apple vừa ra mắt iPhone mới với nhiều tính năng công nghệ đột phá",
        "Bộ Giáo dục công bố phương án thi tốt nghiệp THPT năm nay",
        "Bác sĩ khuyên nên ăn nhiều rau xanh để tăng cường sức khỏe"
    ]
    
    for text in test_texts:
        # Tiền xử lý
        # Preprocess
        text_clean = clean_text(text)
        text_tokenized = tokenize_text(text_clean)
        
        # Vectorize
        text_tfidf = vectorizer.transform([text_tokenized])
        
        # Dự đoán
        # Predict
        prediction = model.predict(text_tfidf)[0]
        proba = model.predict_proba(text_tfidf)[0]
        
        # Lấy top 3 topics
        # Get top 3 topics
        top_indices = proba.argsort()[-3:][::-1]
        top_topics = [(model.classes_[i], proba[i]*100) for i in top_indices]
        
        print(f"📝 Text: {text[: 70]}...")
        print(f"🎯 Dự đoán: {prediction}")
        print(f"📊 Top 3 topics:")
        for topic, prob in top_topics:
            print(f"   - {topic}: {prob:.2f}%")
        print()


# ============================================
# MAIN - CHẠY CHÍNH
# ============================================

def main():
    print()
    print("=" * 70)
    print("TRAIN MODEL PHÂN LOẠI TOPIC VĂN BẢN TIẾNG VIỆT")
    print("Train Vietnamese Text Topic Classification Model")
    print("=" * 70)
    print()
    
    # Load dataset
    df = load_dataset(INPUT_FILE)
    
    if df is None:
        return
    
    # Preprocess
    df = preprocess_data(df)
    
    # Train
    model, vectorizer, accuracy = train_model(df)
    
    # Save
    save_model(model, vectorizer)
    
    # Test
    test_prediction(model, vectorizer)
    
    # Kết quả cuối cùng
    # Final results
    print("\n" + "=" * 70)
    print("✅ HOÀN THÀNH BƯỚC 5.2 - TRAIN MODEL!")
    print("=" * 70)
    print(f"\n📊 Kết quả:")
    print(f"   - Accuracy: {accuracy*100:.2f}%")
    print(f"   - Model: {OUTPUT_DIR}/topic_classifier.pkl")
    print(f"   - Vectorizer: {OUTPUT_DIR}/vectorizer.pkl")
    print(f"\n➡️ Tiếp theo: Test API backend (chạy app.py)")


if __name__ == "__main__":
    main()