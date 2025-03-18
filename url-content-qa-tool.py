# app.py
from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import os

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)

# Store scraped content
url_contents = {}

def scrape_url(url):
    """Scrape content from a URL and return cleaned text."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
        
        # Get text
        text = soup.get_text()
        
        # Clean text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def extract_relevant_sentences(query, content, top_n=5):
    """Extract most relevant sentences from content based on query."""
    sentences = sent_tokenize(content)
    
    # Filter out very short sentences
    sentences = [s for s in sentences if len(s.split()) > 3]
    
    if not sentences:
        return "No relevant content found."
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # If only one sentence, return it
    if len(sentences) == 1:
        return sentences[0]
    
    try:
        # Create TF-IDF matrix
        tfidf_matrix = vectorizer.fit_transform(sentences + [query])
        
        # Calculate similarity between query and each sentence
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
        
        # Get indices of top N most similar sentences
        top_indices = similarity_scores.argsort()[-top_n:][::-1]
        
        # Return top sentences in their original order
        sorted_indices = sorted(top_indices)
        relevant_sentences = [sentences[i] for i in sorted_indices]
        
        return " ".join(relevant_sentences)
    except Exception as e:
        # Fallback if vectorization fails
        return " ".join(sentences[:3])

def answer_question(query, content):
    """Generate an answer to a question based on content."""
    relevant_text = extract_relevant_sentences(query, content)
    return relevant_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    
    # Basic URL validation
    if not re.match(r'^https?://', url):
        url = 'http://' + url
    
    # Scrape content
    content = scrape_url(url)
    
    # Store content
    url_contents[url] = content
    
    return jsonify({"success": True, "message": f"Successfully scraped {url}"})

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query')
    urls = data.get('urls', [])
    
    if not query:
        return jsonify({"error": "No question provided"}), 400
    
    if not urls:
        return jsonify({"error": "No URLs provided"}), 400
    
    # Get content for each URL
    contents = []
    for url in urls:
        if url in url_contents:
            contents.append(url_contents[url])
        else:
            # If URL not scraped yet, scrape it now
            content = scrape_url(url)
            url_contents[url] = content
            contents.append(content)
    
    # Combine all content
    all_content = " ".join(contents)
    
    # Answer the question
    answer = answer_question(query, all_content)
    
    return jsonify({"answer": answer})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
