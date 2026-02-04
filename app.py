"""
Phishing & Fraud Detection System - Main Application
Flask web application with API endpoints
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from url_analyzer import URLAnalyzer
from email_analyzer import EmailAnalyzer
from ml_model import PhishingDetectorModel
import os

app = Flask(__name__)
CORS(app)

# Initialize analyzers
url_analyzer = URLAnalyzer()
email_analyzer = EmailAnalyzer()
ml_model = PhishingDetectorModel()

# Try to load existing model, otherwise use heuristics
ml_model.load_model()


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/check-url', methods=['GET', 'POST'])
def check_url_page():
    """URL check page"""
    if request.method == 'POST':
        url = request.form.get('url', '')
        result = url_analyzer.analyze(url)
        
        # Get ML prediction if features available
        if 'features' in result:
            ml_prediction = ml_model.predict(result['features'])
            result['ml_prediction'] = ml_prediction
            # Combine heuristic and ML scores
            result['final_risk_score'] = (result['risk_score'] + (ml_prediction['confidence'] * 100)) / 2
        
        return render_template('result.html', result=result, type='URL', input_value=url)
    
    return render_template('check_url.html')


@app.route('/check-email', methods=['GET', 'POST'])
def check_email_page():
    """Email check page"""
    if request.method == 'POST':
        email_content = request.form.get('email_content', '')
        sender = request.form.get('sender', '')
        subject = request.form.get('subject', '')
        
        result = email_analyzer.analyze(email_content, sender=sender, subject=subject)
        
        return render_template('result.html', result=result, type='Email', 
                             input_value=email_content, sender=sender, subject=subject)
    
    return render_template('check_email.html')


@app.route('/api/check-url', methods=['POST'])
def api_check_url():
    """API endpoint for URL checking"""
    try:
        data = request.get_json()
        url = data.get('url', '')
        
        if not url:
            return jsonify({
                'success': False,
                'error': 'URL is required'
            }), 400
        
        result = url_analyzer.analyze(url)
        
        # Get ML prediction
        if 'features' in result:
            ml_prediction = ml_model.predict(result['features'])
            result['ml_prediction'] = ml_prediction
            result['final_risk_score'] = (result['risk_score'] + (ml_prediction['confidence'] * 100)) / 2
        
        return jsonify({
            'success': True,
            'result': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/check-email', methods=['POST'])
def api_check_email():
    """API endpoint for email checking"""
    try:
        data = request.get_json()
        email_content = data.get('email', '') or data.get('email_content', '')
        sender = data.get('sender', '')
        subject = data.get('subject', '')
        headers = data.get('headers', {})
        
        if not email_content:
            return jsonify({
                'success': False,
                'error': 'Email content is required'
            }), 400
        
        result = email_analyzer.analyze(email_content, sender=sender, subject=subject, headers=headers)
        
        return jsonify({
            'success': True,
            'result': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/analytics')
def analytics():
    """Analytics dashboard page"""
    return render_template('analytics.html')


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Phishing & Fraud Detection System'
    })


if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    print("Starting Phishing & Fraud Detection System...")
    print("Access the web interface at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

