import os
import re
import json
import argparse
from collections import defaultdict
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from difflib import SequenceMatcher

class LegalDocAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.load_text()
        self.sentences = sent_tokenize(self.text)
        self.analysis = {}
    
    def load_text(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def extract_clauses(self):
        pattern = r'\b(shall|must|may|will|should)\b.*?\.'  # Simple legal obligation detection
        clauses = re.findall(pattern, self.text, re.IGNORECASE)
        self.analysis['clauses'] = clauses
    
    def summarize(self, num_sentences=5):
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(self.sentences)
        scores = tfidf_matrix.sum(axis=1).flatten().tolist()
        ranked_sentences = [sentence for _, sentence in sorted(zip(scores, self.sentences), reverse=True)]
        self.analysis['summary'] = ranked_sentences[:num_sentences]
    
    def compare_documents(self, other_text):
        matcher = SequenceMatcher(None, self.text, other_text)
        similarity = matcher.ratio()
        self.analysis['similarity_score'] = similarity
    
    def save_analysis(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.analysis, f, indent=4)
    
    def run_analysis(self):
        self.extract_clauses()
        self.summarize()
        return self.analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze legal documents for key clauses and summarization.")
    parser.add_argument("file", help="Path to the legal document file")
    parser.add_argument("--compare", help="Path to another document for comparison", default=None)
    parser.add_argument("--output", help="File to save analysis", default="analysis.json")
    
    args = parser.parse_args()
    analyzer = LegalDocAnalyzer(args.file)
    results = analyzer.run_analysis()
    
    if args.compare:
        with open(args.compare, 'r', encoding='utf-8') as f:
            other_text = f.read()
        analyzer.compare_documents(other_text)
    
    analyzer.save_analysis(args.output)
    print(f"Analysis saved to {args.output}")
