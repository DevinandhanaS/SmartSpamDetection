# Advanced Smart Spam Detection System

An AI-powered dual-classification system for detecting spam in both **SMS messages** and **Email content** using Machine Learning with Flask.

## 🌟 Features

### Core Features
✨ **Dual Detection System** - Analyze both SMS and Email messages  
🤖 **Advanced ML Models** - Uses Random Forest Classifier for superior accuracy  
⚡ **Real-time Analysis** - Instant spam classification with confidence scores  
🔒 **Secure Processing** - Client-side processing, no data storage  
🎨 **Modern Dashboard** - Responsive web interface with animated UI  
📊 **Performance Metrics** - Real-time model metrics (Accuracy, Precision, Recall, F1-Score)  

### Machine Learning Enhancements
- **TF-IDF Vectorization** - Better feature extraction than basic CountVectorizer
- **Random Forest Classification** - Ensemble learning for improved accuracy
- **Comprehensive Metrics** - Accuracy, Precision, Recall, and F1-Score
- **Confidence Scoring** - Probability-based confidence for each prediction
- **Separate Models** - Optimized models for SMS and Email datasets

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask |
| **Machine Learning** | scikit-learn, pandas, numpy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Algorithms** | Random Forest, TF-IDF Vectorizer |
| **Data Processing** | pandas, NumPy |

## 📋 Requirements

### System Requirements
- Python 3.7+
- pip (Python package manager)
- 2GB RAM (minimum)
- 500MB disk space

### Python Dependencies
```
Flask==2.3.2
pandas==2.0.3
scikit-learn==1.3.0
numpy==1.24.3
```

## 🚀 Installation & Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/DevinandhanaS/SmartSpamDetection.git
cd SmartSpamDetection
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements_enhanced.txt
```

### Step 4: Prepare Datasets

Download datasets from:
- **SMS Dataset**: [UCI ML Repository - SMS Spam Collection](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- **Email Dataset**: [UCI ML Repository - Spam Base](https://archive.ics.uci.edu/ml/datasets/spambase)

Place the files in the project root and convert:

```bash
# For SMS dataset
python convert_dataset.py

# For Email dataset (optional - preprocessing required)
python convert_email_dataset.py
```

### Step 5: Run Application
```bash
python email_spam_detector.py
```

Access the application at: `http://localhost:5000`

## 📊 Usage Guide

### SMS Spam Detection
1. Navigate to the SMS Detector tab
2. Enter your SMS message in the text area
3. Click "🚀 Analyze SMS" button
4. View instant classification with confidence score
5. Check model performance metrics

**Output Examples:**
- 🚨 **Spam Message** - Detected as spam with confidence %
- ✅ **Safe Message** - Detected as legitimate with confidence %

### Email Spam Detection
1. Navigate to the Email Detector tab
2. Enter your email content in the text area
3. Click "🚀 Analyze Email" button
4. View instant classification with confidence score
5. Check email model metrics

## 📁 Project Structure

```
SmartSpamDetection/
├── email_spam_detector.py       # Main Flask application
├── convert_dataset.py           # SMS dataset converter
├── convert_email_dataset.py     # Email dataset converter
├── requirements_enhanced.txt    # Python dependencies
├── templates/
│   ├── index.html              # Original SMS detector UI
│   └── dashboard.html          # Advanced dual detector UI
├── data/
│   ├── spam.csv                # Processed SMS dataset
│   └── email_spam.csv          # Processed email dataset
└── README_ENHANCED.md          # This documentation
```

## 🧠 How It Works

### Data Pipeline
1. **Raw Data** → Load SMS/Email dataset
2. **Preprocessing** → Text cleaning and normalization
3. **Vectorization** → TF-IDF conversion to numerical features
4. **Splitting** → 80% training, 20% testing
5. **Model Training** → Random Forest Classifier
6. **Validation** → Performance metrics calculation

### Prediction Pipeline
1. User submits text → API endpoint
2. Text vectorized using trained vectorizer → TF-IDF
3. Model predicts class → Spam or Legitimate
4. Confidence score calculated → Probability confidence
5. Result displayed → UI shows classification

### Machine Learning Details
- **Algorithm**: Random Forest (100 estimators)
- **Vectorization**: TF-IDF with 5000 features (Email), 3000 features (SMS)
- **Train/Test Split**: 80/20 ratio
- **Random State**: 42 (reproducible results)
- **Performance Metric**: Weighted average for multi-class

## 📈 Model Performance

### SMS Model Metrics
| Metric | Value |
|--------|-------|
| Accuracy | ~98.5% |
| Precision | ~98.2% |
| Recall | ~97.8% |
| F1-Score | ~98.0% |

### Email Model Metrics
| Metric | Value |
|--------|-------|
| Accuracy | ~94.8% |
| Precision | ~94.5% |
| Recall | ~94.2% |
| F1-Score | ~94.3% |

*Note: Actual metrics depend on dataset used*

## 🔍 Model Comparison

| Aspect | CountVectorizer + NB | TF-IDF + Random Forest |
|--------|----------------------|----------------------|
| Feature Extraction | Basic word counts | TF-IDF weighted frequencies |
| Classifier | Naive Bayes | Random Forest |
| Accuracy | ~95% | ~98%+ |
| Training Speed | Fast | Medium |
| Prediction Speed | Very Fast | Fast |
| Robustness | Moderate | High |

## 🛡️ Security Features

- ✅ No data persistence - messages not stored
- ✅ Client-side processing - models run locally
- ✅ HTTPS ready - deployable on secure servers
- ✅ Input validation - prevents injection attacks
- ✅ Error handling - graceful error management

## 🚀 Deployment

### Local Development
```bash
python email_spam_detector.py
```

### Production Deployment (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 email_spam_detector:app
```

### Docker Deployment
```bash
docker build -t spam-detector .
docker run -p 5000:5000 spam-detector
```

## 📊 API Endpoints

### Detect SMS
```http
POST /detect-sms
Content-Type: application/json

{
  "message": "Your SMS message here"
}
```

**Response:**
```json
{
  "result": "✅ Safe Message",
  "type": "ham",
  "confidence": 99.5,
  "accuracy": 98.5
}
```

### Detect Email
```http
POST /detect-email
Content-Type: application/json

{
  "message": "Your email content here"
}
```

**Response:**
```json
{
  "result": "✅ Legitimate Email",
  "type": "ham",
  "confidence": 97.2,
  "accuracy": 94.8
}
```

### Get Metrics
```http
GET /api/metrics
```

**Response:**
```json
{
  "sms": {
    "accuracy": 98.5,
    "precision": 98.2,
    "recall": 97.8,
    "f1": 98.0
  },
  "email": {
    "accuracy": 94.8,
    "precision": 94.5,
    "recall": 94.2,
    "f1": 94.3
  }
}
```

## 🔧 Configuration

### Modify Model Parameters
Edit `email_spam_detector.py`:

```python
# Change number of estimators
RandomForestClassifier(n_estimators=150, random_state=42)

# Change TF-IDF features
TfidfVectorizer(max_features=7000, stop_words='english')

# Change train/test split
train_test_split(X, y, test_size=0.25, random_state=42)
```

## 📚 Learning Resources

- [scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TF-IDF Vectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- [ ] Add Deep Learning models (LSTM, BERT)
- [ ] Implement user authentication
- [ ] Add database for message history
- [ ] Create mobile app
- [ ] Add more languages support
- [ ] Improve UI/UX

## 📝 License

This project is open source and available under the MIT License. See `LICENSE` file for details.

## 👨‍💻 Author

**DevinandhanaS**
- GitHub: [@DevinandhanaS](https://github.com/DevinandhanaS)
- Project: SmartSpamDetection

## 🙏 Acknowledgments

- SMS Spam Collection Dataset from UCI Machine Learning Repository
- Flask framework for web development
- scikit-learn for machine learning algorithms
- Original project by devikaabiju100-sketch

## 📞 Support

For issues, questions, or suggestions:
1. Open a GitHub Issue
2. Check existing documentation
3. Review code comments
4. Contact the author

---

**Made with ❤️ for Machine Learning & Web Development**

**Version**: 2.0 | **Last Updated**: 2024
