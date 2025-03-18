# URL Content Q&A Tool

A web-based tool that allows users to enter URLs, then ask questions based on the content of those pages.

## Features

- Input multiple URLs to analyze
- Scrape and preprocess web content
- Ask questions about the content
- Get answers based solely on the scraped content
- Clean, user-friendly interface

## Installation

### Local Setup

1. Clone this repository
```
git clone https://github.com/yourusername/url-content-qa-tool.git
cd url-content-qa-tool
```

2. Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the requirements
```
pip install -r requirements.txt
```

4. Run the application
```
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

### Deployment Option

The application can be easily deployed to Heroku:

1. Create a Heroku account and install the Heroku CLI
2. Login to Heroku CLI and create a new app
```
heroku login
heroku create your-app-name
```

3. Push to Heroku
```
git push heroku main
```

4. Open the app
```
heroku open
```

## How to Use

1. **Add URLs**: Enter one or more URLs in the input field and click "Add URL" for each.
2. **Ask a Question**: Type your question about the content from those URLs.
3. **Get Answer**: Click "Ask Question" to receive an answer based solely on the content from the provided URLs.

## Technical Details

### How It Works

1. **Content Scraping**: When a URL is added, the application uses BeautifulSoup to extract and clean the text content.
2. **Text Processing**: NLTK is used to tokenize the content into sentences.
3. **Relevance Analysis**: When a question is asked, the tool uses TF-IDF vectorization and cosine similarity to find the most relevant sentences from the scraped content.
4. **Answer Generation**: The most relevant sentences are combined to form the answer.

### Technology Stack

- **Flask**: Web framework
- **BeautifulSoup**: HTML parsing and content extraction
- **NLTK**: Natural language processing
- **scikit-learn**: TF-IDF vectorization and similarity measurement
- **Bootstrap**: Frontend styling
- **JavaScript**: Client-side interaction

## Project Structure

```
url-content-qa-tool/
│
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
├── Procfile           # For Heroku deployment
├── templates/         
│   └── index.html     # Frontend template
└── README.md          # This file
```

## Limitations

- The tool relies on TF-IDF and cosine similarity for finding relevant content, which works well for factual questions but may struggle with complex queries.
- It doesn't understand context beyond sentence level or perform reasoning.
- Some websites may block scraping or have dynamically loaded content that can't be accessed.

## Future Improvements

- Implement more advanced NLP techniques
- Add caching to improve performance
- Support PDF and other document formats
- Implement rate limiting for URL scraping
- Add user accounts to save URL collections
