# Running the URL Content Q&A Tool Locally

This guide provides step-by-step instructions to get the URL Content Q&A Tool running on your local machine.

## Prerequisites

Before starting, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Setup Instructions

### 1. Create a Project Directory

```bash
mkdir url-content-qa-tool
cd url-content-qa-tool
```

### 2. Create the Project Structure

Create the following directory structure:

```
url-content-qa-tool/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
└── README.md
```

You can use these commands to create the directories and files:

```bash
mkdir templates
touch app.py requirements.txt Procfile README.md templates/index.html
```

### 3. Add Code to Files

Copy the code from the artifacts into each file:

- Copy the Flask application code to `app.py`
- Copy the HTML template code to `templates/index.html`
- Copy the dependencies list to `requirements.txt`
- Add `web: gunicorn app:app` to the `Procfile`

### 4. Set Up a Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages including Flask, BeautifulSoup, NLTK, and scikit-learn.

### 6. Run the Application

```bash
python app.py
```

The application should now be running at `http://localhost:5000`.

### 7. Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

## Using the Application

1. **Add URLs**: Enter a URL in the input field and click "Add URL". The application will scrape the content and add it to the list.

2. **Ask Questions**: Type your question in the text area and click "Ask Question". The application will process your question and provide an answer based on the content from the URLs you've added.

3. **Remove URLs**: Click the "×" button next to a URL to remove it from the list.

## Troubleshooting

If you encounter any issues:

- **Dependencies not installing**: Make sure you're using the correct Python version and that pip is up to date.
- **Application not starting**: Check for error messages in the terminal.
- **URLs not scraping**: Some websites may block scraping. Try with different URLs.
- **NLTK data missing**: If you see an error about missing NLTK data, run `python -c "import nltk; nltk.download('punkt')"`.

## Shutting Down

To stop the application, press `Ctrl+C` in the terminal.

To deactivate the virtual environment, run:

```bash
deactivate
```
