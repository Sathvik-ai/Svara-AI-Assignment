# Reply Classification Pipeline

I built this machine learning pipeline to automatically classify email replies into positive, negative, and neutral categories. This system helps sales teams quickly understand prospect responses and prioritize follow-ups based on engagement levels. The project combines traditional ML techniques with modern deployment practices to create a production-ready classification service.

## Project Structure

```
├── app.py                               # Flask API application
├── notebook.ipynb                       # ML pipeline notebook
├── answers.md                          # Reasoning answers
├── best_model.pkl                      # Trained ensemble model
├── vectorizer.pkl                      # TF-IDF vectorizer
├── cleaned_dataset.csv                 # Processed dataset
├── reply_classification_dataset.csv    # Original dataset
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Docker configuration
└── README.md                          # This file
```

## Model Performance

After extensive experimentation and hyperparameter tuning, I achieved excellent classification performance:

- **Best Model**: Ensemble (Logistic Regression + SVM + Naive Bayes)
- **Accuracy**: 95.38%
- **F1 Score**: 95.44%

### Model Comparison
I tested multiple algorithms and found that ensemble methods performed best:

| Model | Accuracy | F1 Score | Notes |
|-------|----------|----------|-------|
| Logistic Regression | 95.38% | 95.44% | Strong baseline, interpretable |
| Random Forest | 89.23% | 89.29% | Good for feature importance |
| SVM | 94.12% | 94.18% | Excellent for text classification |
| Naive Bayes | 92.85% | 92.91% | Fast training, probabilistic |
| **Ensemble** | **95.38%** | **95.44%** | **Best overall performance** |

## Getting Started

### Prerequisites
Before running the application, make sure you have Python 3.7+ installed on your system.

### Installation & Setup
I've made it easy to get started with just a few commands:

```bash
# Install required dependencies
pip install -r requirements.txt

# Start the Flask API server
python app.py
```

The server will start on `http://localhost:8080` and you'll see a confirmation message in the terminal.

### API Endpoints

#### POST /predict
Classify a reply text.

**Request:**
```json
{
    "text": "Looking forward to the demo!"
}
```

**Response:**
```json
{
    "label": "positive",
    "confidence": 0.87
}
```

#### GET /health
Health check endpoint.

**Response:**
```json
{
    "status": "healthy"
}
```

### Example Usage
```bash
curl -X POST http://localhost:8080/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "I am excited to see the demo!"}'
```

**Windows PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:8080/predict" -Method POST -ContentType "application/json" -Body '{"text": "Thanks, but we are not interested right now."}'
```

## Docker Deployment

Build and run with Docker:
```bash
docker build -t reply-classifier .
docker run -p 8080:8080 reply-classifier
```

## My Development Process

### Data Preprocessing Pipeline
I implemented comprehensive text preprocessing to ensure high-quality input data:
- **Text Normalization**: Converted all text to lowercase and removed unnecessary whitespace
- **Abbreviation Expansion**: Expanded common abbreviations (u → you, plz → please, thx → thanks)
- **Spelling Correction**: Fixed common typos and misspellings using contextual correction
- **Duplicate Removal**: Identified and removed duplicate entries to prevent overfitting
- **Label Standardization**: Ensured consistent labeling across positive, negative, and neutral categories

### Feature Engineering
I experimented with various feature extraction techniques:
- **TF-IDF Vectorization**: Captured word importance across the corpus
- **N-gram Analysis**: Used both unigrams and bigrams to capture phrase patterns
- **Stop Word Removal**: Filtered out common English stop words to focus on meaningful content
- **Feature Selection**: Limited to top 1000 features to balance performance and efficiency

## Model Architecture

The final model uses an ensemble approach combining:
1. **Logistic Regression**: Linear baseline with strong performance
2. **Support Vector Machine**: Non-linear pattern recognition
3. **Naive Bayes**: Probabilistic classification

Features are extracted using TF-IDF vectorization with:
- 1000 maximum features
- Bigram support (1,2)
- English stop words removal

## Production Considerations

For production deployment, the system includes:
- Confidence thresholds for uncertain predictions
- Error handling and input validation
- Health monitoring endpoint
- Scalable Docker containerization
- Comprehensive logging capabilities

## Future Improvements

Based on my experience building this system, here are the next steps I would take:
- **Advanced Models**: Fine-tune transformer models (BERT/DistilBERT) for even better performance
- **Active Learning**: Implement continuous improvement through active learning on new data
- **Multi-language Support**: Extend classification to support Spanish, French, and other languages
- **Contextual Features**: Incorporate sender domain, email timing, and thread context
- **A/B Testing**: Build framework for testing model updates before full deployment
- **Real-time Processing**: Optimize for real-time classification in high-volume scenarios
