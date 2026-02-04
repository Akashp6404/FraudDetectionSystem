"""
URL Phishing Detection Module
Analyzes URLs for phishing indicators
"""

import re
import urllib.parse
from urllib.parse import urlparse
import tldextract
import socket
import ssl
import requests
from datetime import datetime


class URLAnalyzer:
    def __init__(self):
        self.suspicious_keywords = [
            'secure', 'account', 'update', 'verify', 'confirm', 'suspend',
            'restrict', 'unauthorized', 'action', 'required', 'immediately',
            'urgent', 'click', 'here', 'limited', 'time', 'offer', 'win',
            'prize', 'congratulations', 'free', 'gift', 'reward'
        ]
        
        self.shortener_domains = [
            'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'buff.ly',
            'short.link', 'tiny.cc', 'is.gd', 'cli.gs', 'shorturl.at'
        ]
        
    def extract_features(self, url):
        """Extract features from URL for analysis"""
        features = {}
        
        try:
            parsed = urlparse(url)
            domain_info = tldextract.extract(url)
            
            # Basic URL features
            features['url_length'] = len(url)
            features['domain_length'] = len(domain_info.domain)
            features['path_length'] = len(parsed.path) if parsed.path else 0
            features['query_length'] = len(parsed.query) if parsed.query else 0
            
            # Domain features
            features['has_subdomain'] = 1 if domain_info.subdomain else 0
            features['has_port'] = 1 if parsed.port else 0
            features['has_ip'] = 1 if self._is_ip_address(parsed.netloc) else 0
            
            # Suspicious patterns
            features['suspicious_keywords_count'] = sum(
                1 for keyword in self.suspicious_keywords 
                if keyword.lower() in url.lower()
            )
            
            features['special_char_count'] = sum(
                1 for char in url if char in ['@', '?', '=', '%', '&']
            )
            
            features['hyphen_count'] = url.count('-')
            features['dot_count'] = url.count('.')
            
            # Shortened URL check
            features['is_shortened'] = 1 if any(
                shortener in url.lower() for shortener in self.shortener_domains
            ) else 0
            
            # HTTPS check
            features['has_https'] = 1 if parsed.scheme == 'https' else 0
            
            # Path depth
            features['path_depth'] = parsed.path.count('/') - 1 if parsed.path else 0
            
            # Query parameters count
            features['query_params_count'] = len(parsed.query.split('&')) if parsed.query else 0
            
            # Check for IP address in domain
            if parsed.hostname:
                features['is_ip_in_domain'] = 1 if self._is_ip_address(parsed.hostname) else 0
            
            return features
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return None
    
    def _is_ip_address(self, string):
        """Check if string is an IP address"""
        try:
            socket.inet_aton(string)
            return True
        except:
            return False
    
    def check_ssl_certificate(self, url):
        """Check SSL certificate validity"""
        try:
            parsed = urlparse(url)
            hostname = parsed.hostname
            
            if not hostname:
                return False
            
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert()
                    return True
        except Exception:
            return False
    
    def check_domain_age(self, domain):
        """Check if domain is newly registered (placeholder)"""
        # In production, use WHOIS API
        # For now, return default value
        return 0  # 0 means unable to determine
    
    def analyze(self, url):
        """Main analysis function"""
        if not url:
            return {
                'is_phishing': True,
                'risk_score': 100,
                'reasons': ['Invalid or empty URL']
            }
        
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        features = self.extract_features(url)
        
        if not features:
            return {
                'is_phishing': True,
                'risk_score': 80,
                'reasons': ['Unable to analyze URL']
            }
        
        reasons = []
        risk_score = 0
        
        # Calculate risk score based on features
        if features['is_shortened']:
            risk_score += 15
            reasons.append('Uses URL shortener')
        
        if features['has_ip'] or features['is_ip_in_domain']:
            risk_score += 20
            reasons.append('Uses IP address instead of domain')
        
        if not features['has_https']:
            risk_score += 25
            reasons.append('No HTTPS encryption')
        elif not self.check_ssl_certificate(url):
            risk_score += 15
            reasons.append('Invalid or expired SSL certificate')
        
        if features['suspicious_keywords_count'] > 3:
            risk_score += 10
            reasons.append(f'Contains {features["suspicious_keywords_count"]} suspicious keywords')
        
        if features['url_length'] > 75:
            risk_score += 5
            reasons.append('Unusually long URL')
        
        if features['special_char_count'] > 5:
            risk_score += 10
            reasons.append('Contains many special characters')
        
        if features['hyphen_count'] > 3:
            risk_score += 5
            reasons.append('Multiple hyphens in domain (typosquatting)')
        
        if features['path_depth'] > 5:
            risk_score += 5
            reasons.append('Deep path structure')
        
        risk_score = min(risk_score, 100)
        is_phishing = risk_score >= 50
        
        return {
            'is_phishing': is_phishing,
            'risk_score': risk_score,
            'reasons': reasons if reasons else ['No suspicious indicators found'],
            'features': features
        }

