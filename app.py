

from flask import Flask, render_template, request,make_response
from flask_bootstrap import Bootstrap
import spacy
from collections import Counter
import random
import PyPDF2
from PyPDF2 import PdfReader,PdfWriter  


app = Flask(__name__)
Bootstrap(app)


nlp = spacy.load("en_core_web_sm")

def generate_mcqs(text, num_questions=5):
   
    if text is None:
        return []


    doc = nlp(text)

    
    sentences = [sent.text for sent in doc.sents]

    
    num_questions = min(num_questions, len(sentences))

    
    selected_sentences = random.sample(sentences, num_questions)

    
    mcqs = []

    
    for sentence in selected_sentences:
        sent_doc = nlp(sentence)

        nouns = [token.text for token in sent_doc if token.pos_ == "NOUN"]

        if len(nouns) < 2:
            continue

        noun_counts = Counter(nouns)

        if noun_counts:
            subject = noun_counts.most_common(1)[0][0]

            question_stem = sentence.replace(subject, "______")

            fallback_nouns = ["All","None","Can't answer"]

            answer_choices = [subject]  
            selected_distractors = set([subject])  

            for _ in range(3):  
                remaining_nouns = list(set(nouns) - selected_distractors)  
                
                if remaining_nouns:  
                    distractor = random.choice(remaining_nouns)
                else:  
                    distractor = random.choice(list(set(fallback_nouns) - selected_distractors))
                
                answer_choices.append(distractor)
                selected_distractors.add(distractor)

            while len(answer_choices) < 4:
                extra_distractor = random.choice(list(set(fallback_nouns) - selected_distractors))
                answer_choices.append(extra_distractor)
                selected_distractors.add(extra_distractor)

            random.shuffle(answer_choices)

            correct_answer = chr(64 + answer_choices.index(subject) + 1) 
            mcqs.append((question_stem, answer_choices, correct_answer))

    return mcqs





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = ""

        # Check if files were uploaded
        if 'files[]' in request.files:
            files = request.files.getlist('files[]')
            for file in files:
                if file.filename.endswith('.pdf'):
                    # Process PDF file
                    text += process_pdf(file)
                elif file.filename.endswith('.txt'):
                    # Process text file
                    text += file.read().decode('utf-8')
        else:
            # Process manual input
            text = request.form['text']

        # Get the selected number of questions from the dropdown menu
        num_questions = int(request.form['num_questions'])

        mcqs = generate_mcqs(text, num_questions=num_questions)  # Pass the selected number of questions
        print(mcqs)
        # Ensure each MCQ is formatted correctly as (question_stem, answer_choices, correct_answer)
        mcqs_with_index = [(i + 1, mcq) for i, mcq in enumerate(mcqs)]
        return render_template('mcqs.html', mcqs=mcqs_with_index)

    return render_template('index.html')




def process_pdf(file):
    # Initialize an empty string to store the extracted text
    text = ""

    # Create a PyPDF2 PdfReader object
    pdf_reader = PdfReader(file)

    # Loop through each page of the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Extract text from the current page
        page_text = pdf_reader.pages[page_num].extract_text()
        # Append the extracted text to the overall text
        text += page_text

    return text


if __name__ == '__main__':
    app.run(debug=True)