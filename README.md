# MCQ Generator

## Overview
The **MCQ Generator** is a Flask-based web application that generates multiple-choice questions (MCQs) from uploaded PDF or TXT files. The application uses **spaCy** for natural language processing to extract key nouns from text and formulate questions. The generated MCQs can then be displayed in an interactive format.

## Features
- Upload PDF or TXT files to generate MCQs
- Supports multiple file uploads
- Option to select the number of questions to generate
- Interactive UI using **TailwindCSS**
- Flask backend for processing text and generating MCQs using **spaCy**

## Technologies Used
- **Flask** (Python Web Framework)
- **spaCy** (Natural Language Processing)
- **PyPDF2** (PDF Text Extraction)
- **TailwindCSS** (Frontend Styling)

## Installation & Setup

### Prerequisites
Ensure you have Python installed (Python 3.7 or later is recommended). Install virtualenv for dependency management.

### Steps
1. **Clone the repository**
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download spaCy model**
   ```sh
   python -m spacy download en_core_web_sm
   ```

5. **Run the Flask application**
   ```sh
   python app.py
   ```

6. **Open in browser**
   - Go to `http://127.0.0.1:5000/`

## Usage
1. Upload one or more PDF/TXT files.
2. Select the number of MCQs to generate.
3. Click **Generate MCQs** to see the questions.
4. Click **Show Results** to reveal the correct answers.

## Project Structure
```
/MCQ-Generator
│-- static/             # Static files (CSS, images, icons)
│-- templates/          # HTML templates
│   │-- index.html      # Upload page
│   │-- mcqs.html       # MCQs display page
│-- app.py              # Flask backend
│-- requirements.txt    # Dependencies
│-- README.md           # Documentation
```

## Dependencies
- Flask
- Flask-Bootstrap
- spaCy
- PyPDF2
- Random (Python Standard Library)

## Future Enhancements
- Improve distractor selection for more challenging MCQs
- Add support for more file formats (DOCX, Markdown, etc.)
- Implement user authentication for saving progress
- Enhance UI with more interactive features



