
from flask import Flask, request, jsonify
import pickle
import re

app = Flask(__name__)

def preprocess_text(text):
    text = text.lower()
    text = text.strip()
    text = re.sub(r'[?!]{2,}', '', text)
    text = re.sub(r',+', ',', text)
    text = text.replace(' u ', ' you ')
    text = text.replace(' plz ', ' please ')
    text = text.replace(' w/ ', ' with ')
    text = text.replace('schdule', 'schedule')
    text = text.replace('intrsted', 'interested')
    text = text.replace('alredy', 'already')
    text = text.replace('oppurtunity', 'opportunity')
    text = text.replace('intrest', 'interest')
    text = text.replace('commited', 'committed')
    text = text.replace('lets', 'let us')
    return text

with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({'error': 'Missing text field'}), 400

        text = data['text']

        if not text or text.strip() == '':
            return jsonify({'error': 'Text field is empty'}), 400

        processed_text = preprocess_text(text)
        text_tfidf = vectorizer.transform([processed_text])

        prediction = model.predict(text_tfidf)[0]
        probabilities = model.predict_proba(text_tfidf)[0]
        confidence = max(probabilities)

        return jsonify({
            'label': prediction,
            'confidence': round(confidence, 3)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/', methods=['GET'])
def home():
    return 'Reply Classification API is running. Use /predict endpoint to POST data.', 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
