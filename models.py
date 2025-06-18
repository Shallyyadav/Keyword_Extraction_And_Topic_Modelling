import json
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TextAnalysis(db.Model):
    """Model for storing text analysis results."""
    id = db.Column(db.Integer, primary_key=True)
    text_content = db.Column(db.Text, nullable=False)
    word_count = db.Column(db.Integer)
    unique_word_count = db.Column(db.Integer)
    sentence_count = db.Column(db.Integer)
    avg_words_per_sentence = db.Column(db.Float)
    avg_word_length = db.Column(db.Float)
    keywords = db.Column(db.Text)  
    topics = db.Column(db.Text)    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, text_content, stats, keywords, topics):
        self.text_content = text_content
        
        self.word_count = stats.get('word_count', 0)
        self.unique_word_count = stats.get('unique_word_count', 0)
        self.sentence_count = stats.get('sentence_count', 0)
        self.avg_words_per_sentence = stats.get('avg_words_per_sentence', 0)
        self.avg_word_length = stats.get('avg_word_length', 0)
        
        self.keywords = json.dumps(keywords)
        self.topics = json.dumps(topics)
    
    def to_dict(self):
        return {
            'id': self.id,
            'text_content': self.text_content[:100] + '...' if len(self.text_content) > 100 else self.text_content,
            'stats': {
                'word_count': self.word_count,
                'unique_word_count': self.unique_word_count,
                'sentence_count': self.sentence_count,
                'avg_words_per_sentence': self.avg_words_per_sentence,
                'avg_word_length': self.avg_word_length
            },
            'keywords': json.loads(self.keywords),
            'topics': json.loads(self.topics),
            'created_at': self.created_at.isoformat()
        }