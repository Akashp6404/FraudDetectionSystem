"""
Test script for Phishing & Fraud Detection System
"""

from url_analyzer import URLAnalyzer
from email_analyzer import EmailAnalyzer
from ml_model import PhishingDetectorModel

def test_url_analyzer():
    """Test URL analyzer"""
    print("=" * 60)
    print("Testing URL Analyzer")
    print("=" * 60)
    
    analyzer = URLAnalyzer()
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "http://bit.ly/suspicious-link",
        "https://192.168.1.1/login",
        "https://secure-bank-verify-account.com",
    ]
    
    for url in test_urls:
        print(f"\nTesting URL: {url}")
        result = analyzer.analyze(url)
        print(f"Risk Score: {result['risk_score']}")
        print(f"Is Phishing: {result['is_phishing']}")
        print(f"Reasons: {', '.join(result['reasons'])}")


def test_email_analyzer():
    """Test email analyzer"""
    print("\n" + "=" * 60)
    print("Testing Email Analyzer")
    print("=" * 60)
    
    analyzer = EmailAnalyzer()
    
    # Test emails
    test_emails = [
        {
            "sender": "noreply@bank.com",
            "subject": "URGENT: Verify your account immediately",
            "content": "Click here to verify your account. This is urgent!"
        },
        {
            "sender": "friend@example.com",
            "subject": "Hello",
            "content": "Just checking in. How are you doing?"
        }
    ]
    
    for email in test_emails:
        print(f"\nTesting Email from: {email['sender']}")
        result = analyzer.analyze(
            email['content'],
            sender=email['sender'],
            subject=email['subject']
        )
        print(f"Risk Score: {result['risk_score']}")
        print(f"Is Fraud: {result['is_fraud']}")
        print(f"Reasons: {', '.join(result['reasons'])}")


def test_ml_model():
    """Test ML model"""
    print("\n" + "=" * 60)
    print("Testing ML Model")
    print("=" * 60)
    
    model = PhishingDetectorModel()
    
    # Test features
    test_features = {
        'url_length': 50,
        'domain_length': 10,
        'path_length': 20,
        'query_length': 0,
        'has_subdomain': 0,
        'has_port': 0,
        'has_ip': 0,
        'suspicious_keywords_count': 5,
        'special_char_count': 3,
        'hyphen_count': 2,
        'dot_count': 3,
        'is_shortened': 1,
        'has_https': 1,
        'path_depth': 2,
        'query_params_count': 0,
        'is_ip_in_domain': 0
    }
    
    print("\nTesting with suspicious URL features:")
    result = model.predict(test_features)
    print(f"Prediction: {'Phishing' if result['is_phishing'] else 'Safe'}")
    print(f"Confidence: {result['confidence'] * 100:.2f}%")


if __name__ == "__main__":
    print("Phishing & Fraud Detection System - Test Script\n")
    
    try:
        test_url_analyzer()
        test_email_analyzer()
        test_ml_model()
        print("\n" + "=" * 60)
        print("All tests completed!")
        print("=" * 60)
    except Exception as e:
        print(f"\nError during testing: {e}")
        import traceback
        traceback.print_exc()

