"""
Machine Learning Model for Phishing Detection
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os


class PhishingDetectorModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.model_path = 'models/phishing_detector.pkl'
        self.scaler_path = 'models/scaler.pkl'
        
    def create_model(self):
        """Create and train a new model"""
        # This is a simplified model
        # In production, use a real dataset
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=20,
            random_state=42,
            n_jobs=-1
        )
        return self.model
    
    def train(self, X, y):
        """Train the model"""
        if self.model is None:
            self.create_model()
        
        # Normalize features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train the model
        self.model.fit(X_scaled, y)
        
        return self.model
    
    def predict(self, features):
        """Predict if URL/email is phishing"""
        if self.model is None:
            if os.path.exists(self.model_path):
                self.load_model()
            else:
                # Return default prediction based on heuristics
                return self._heuristic_predict(features)
        
        # Convert features to numpy array
        if isinstance(features, dict):
            feature_vector = self._dict_to_vector(features)
        else:
            feature_vector = features
        
        # Normalize
        feature_vector = feature_vector.reshape(1, -1)
        feature_vector_scaled = self.scaler.transform(feature_vector)
        
        # Predict
        prediction = self.model.predict(feature_vector_scaled)[0]
        probability = self.model.predict_proba(feature_vector_scaled)[0]
        
        return {
            'prediction': int(prediction),
            'is_phishing': bool(prediction),
            'confidence': float(max(probability))
        }
    
    def _heuristic_predict(self, features):
        """Fallback heuristic prediction if model not available"""
        if isinstance(features, dict):
            risk_score = 0
            
            if features.get('is_shortened', 0):
                risk_score += 20
            if features.get('has_ip', 0) or features.get('is_ip_in_domain', 0):
                risk_score += 30
            if not features.get('has_https', 0):
                risk_score += 25
            if features.get('suspicious_keywords_count', 0) > 3:
                risk_score += 15
            if features.get('special_char_count', 0) > 5:
                risk_score += 10
            
            is_phishing = risk_score >= 50
            confidence = min(risk_score / 100, 0.95)
            
            return {
                'prediction': 1 if is_phishing else 0,
                'is_phishing': is_phishing,
                'confidence': confidence
            }
        
        return {
            'prediction': 0,
            'is_phishing': False,
            'confidence': 0.5
        }
    
    def _dict_to_vector(self, features_dict):
        """Convert features dictionary to numpy vector"""
        feature_order = [
            'url_length', 'domain_length', 'path_length', 'query_length',
            'has_subdomain', 'has_port', 'has_ip', 'suspicious_keywords_count',
            'special_char_count', 'hyphen_count', 'dot_count', 'is_shortened',
            'has_https', 'path_depth', 'query_params_count', 'is_ip_in_domain'
        ]
        
        vector = []
        for feature in feature_order:
            vector.append(features_dict.get(feature, 0))
        
        return np.array(vector)
    
    def save_model(self):
        """Save the trained model"""
        os.makedirs('models', exist_ok=True)
        joblib.dump(self.model, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)
        print(f"Model saved to {self.model_path}")
    
    def load_model(self):
        """Load a saved model"""
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
            print(f"Model loaded from {self.model_path}")
            return True
        return False


def generate_sample_data():
    """Generate sample training data (for demonstration)"""
    # In production, use real phishing dataset
    np.random.seed(42)
    
    n_samples = 1000
    features = []
    labels = []
    
    for _ in range(n_samples):
        # Simulate features
        sample = {
            'url_length': np.random.randint(20, 200),
            'domain_length': np.random.randint(5, 50),
            'path_length': np.random.randint(0, 100),
            'query_length': np.random.randint(0, 100),
            'has_subdomain': np.random.randint(0, 2),
            'has_port': np.random.randint(0, 2),
            'has_ip': np.random.randint(0, 2),
            'suspicious_keywords_count': np.random.randint(0, 10),
            'special_char_count': np.random.randint(0, 20),
            'hyphen_count': np.random.randint(0, 5),
            'dot_count': np.random.randint(1, 10),
            'is_shortened': np.random.randint(0, 2),
            'has_https': np.random.randint(0, 2),
            'path_depth': np.random.randint(0, 10),
            'query_params_count': np.random.randint(0, 10),
            'is_ip_in_domain': np.random.randint(0, 2)
        }
        
        # Generate label based on features (simplified)
        is_phishing = (
            sample['has_ip'] or
            sample['is_ip_in_domain'] or
            (not sample['has_https']) or
            (sample['suspicious_keywords_count'] > 5) or
            sample['is_shortened']
        )
        
        features.append(sample)
        labels.append(1 if is_phishing else 0)
    
    return features, labels

