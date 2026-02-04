"""
Email Fraud Detection Module
Analyzes emails for phishing and fraud indicators
"""

import re
from email.parser import Parser
from urllib.parse import urlparse
import urllib.parse


class EmailAnalyzer:
    def __init__(self):
        self.phishing_keywords = [
            'urgent', 'immediately', 'verify', 'confirm', 'suspend',
            'account', 'unauthorized', 'action required', 'click here',
            'limited time', 'congratulations', 'you won', 'prize',
            'free gift', 'claim now', 'expires soon', 'verify identity'
        ]
        
        self.suspicious_sender_patterns = [
            r'noreply', r'no-reply', r'do-not-reply', r'donotreply',
            r'notification', r'alert', r'system', r'admin', r'service'
        ]
        
    def extract_urls(self, text):
        """Extract all URLs from text"""
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls = re.findall(url_pattern, text)
        return urls
    
    def analyze_sender(self, sender_email):
        """Analyze sender email address"""
        if not sender_email:
            return {'score': 30, 'reasons': ['No sender information']}
        
        score = 0
        reasons = []
        
        # Check for suspicious patterns
        for pattern in self.suspicious_sender_patterns:
            if re.search(pattern, sender_email.lower()):
                score += 10
                reasons.append(f'Suspicious sender pattern: {pattern}')
        
        # Check for mismatched domain
        if '@' in sender_email:
            domain = sender_email.split('@')[1].lower()
            if domain in ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']:
                # Common legitimate domains, reduce score slightly
                if 'bank' in sender_email.lower() or 'official' in sender_email.lower():
                    score += 15
                    reasons.append('Personal email used for official communication')
        
        return {'score': min(score, 50), 'reasons': reasons}
    
    def analyze_subject(self, subject):
        """Analyze email subject line"""
        if not subject:
            return {'score': 0, 'reasons': []}
        
        score = 0
        reasons = []
        subject_lower = subject.lower()
        
        # Check for urgency indicators
        urgency_words = ['urgent', 'immediate', 'asap', 'hurry', 'expires', 'limited']
        if any(word in subject_lower for word in urgency_words):
            score += 15
            reasons.append('Subject contains urgency indicators')
        
        # Check for phishing keywords
        phishing_count = sum(1 for keyword in self.phishing_keywords if keyword in subject_lower)
        if phishing_count > 2:
            score += 20
            reasons.append(f'Subject contains {phishing_count} phishing keywords')
        
        # Check for all caps
        if subject.isupper() and len(subject) > 10:
            score += 10
            reasons.append('Subject is in all caps (urgency tactic)')
        
        return {'score': min(score, 50), 'reasons': reasons}
    
    def analyze_content(self, content):
        """Analyze email body content"""
        if not content:
            return {'score': 0, 'reasons': []}
        
        score = 0
        reasons = []
        content_lower = content.lower()
        
        # Check for phishing keywords
        phishing_count = sum(1 for keyword in self.phishing_keywords if keyword in content_lower)
        if phishing_count > 5:
            score += 25
            reasons.append(f'Content contains {phishing_count} phishing keywords')
        
        # Extract and check URLs
        urls = self.extract_urls(content)
        if urls:
            suspicious_urls = 0
            for url in urls:
                parsed = urlparse(url)
                if not parsed.scheme or parsed.scheme != 'https':
                    suspicious_urls += 1
            
            if suspicious_urls > 0:
                score += 15
                reasons.append(f'{suspicious_urls} URLs without HTTPS')
            
            if len(urls) > 3:
                score += 10
                reasons.append('Multiple URLs in email body')
        
        # Check for grammar/spelling mistakes (simple check)
        if re.search(r'\b(click|here|verify|confirm)\s+(here|now|link)\b', content_lower):
            score += 10
            reasons.append('Contains common phishing phrases')
        
        # Check for requests for sensitive information
        sensitive_patterns = [
            r'password', r'pin', r'ssn', r'social security', r'credit card',
            r'account number', r'login', r'credentials'
        ]
        sensitive_count = sum(1 for pattern in sensitive_patterns if re.search(pattern, content_lower))
        if sensitive_count > 2:
            score += 20
            reasons.append('Asks for sensitive information')
        
        return {'score': min(score, 50), 'reasons': reasons}
    
    def analyze_headers(self, headers):
        """Analyze email headers"""
        score = 0
        reasons = []
        
        if not headers:
            return {'score': 0, 'reasons': []}
        
        # Check for SPF/DKIM (would require proper email parsing)
        # For now, check common header issues
        
        if 'From' in headers and 'Reply-To' in headers:
            if headers['From'] != headers.get('Reply-To'):
                # Check if domains match
                from_domain = headers['From'].split('@')[-1] if '@' in headers['From'] else ''
                reply_domain = headers['Reply-To'].split('@')[-1] if '@' in headers['Reply-To'] else ''
                
                if from_domain != reply_domain:
                    score += 15
                    reasons.append('From and Reply-To domains do not match')
        
        return {'score': min(score, 30), 'reasons': reasons}
    
    def analyze(self, email_content, sender=None, subject=None, headers=None):
        """Main analysis function"""
        risk_score = 0
        all_reasons = []
        
        # Analyze sender
        if sender:
            sender_analysis = self.analyze_sender(sender)
            risk_score += sender_analysis['score']
            all_reasons.extend(sender_analysis['reasons'])
        
        # Analyze subject
        if subject:
            subject_analysis = self.analyze_subject(subject)
            risk_score += subject_analysis['score']
            all_reasons.extend(subject_analysis['reasons'])
        
        # Analyze content
        content_analysis = self.analyze_content(email_content)
        risk_score += content_analysis['score']
        all_reasons.extend(content_analysis['reasons'])
        
        # Analyze headers
        if headers:
            headers_analysis = self.analyze_headers(headers)
            risk_score += headers_analysis['score']
            all_reasons.extend(headers_analysis['reasons'])
        
        # Normalize risk score to 0-100
        risk_score = min(risk_score, 100)
        is_fraud = risk_score >= 50
        
        return {
            'is_fraud': is_fraud,
            'risk_score': risk_score,
            'reasons': all_reasons if all_reasons else ['No suspicious indicators found'],
            'sender_analysis': sender_analysis if sender else None,
            'subject_analysis': subject_analysis if subject else None,
            'content_analysis': content_analysis
        }

