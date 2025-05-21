import os
import re
import json
from bs4 import BeautifulSoup

def extract_questions_from_file(file_path):
    """Extract questions and answer choices from an HTML file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all question blocks - they have IDs like "question-27115-1"
    question_blocks = soup.find_all('div', id=re.compile(r'question-\d+-\d+'))
    
    questions = []
    for question_block in question_blocks:
        try:
            # Extract question number
            question_number = question_block.find('span', class_='qno').text.strip()
            
            # Extract question text
            question_text = question_block.find('div', class_='qtext').text.strip()
            
            # Extract answer choices
            answers = []
            answer_blocks = question_block.find_all('div', {'data-region': 'answer-label'})
            
            for answer_block in answer_blocks:
                option_label = answer_block.find('span', class_='answernumber').text.strip()
                option_text = answer_block.find('div', class_='flex-fill ml-1').text.strip()
                answers.append({
                    'label': option_label,
                    'text': option_text
                })
            
            questions.append({
                'number': question_number,
                'question': question_text,
                'options': answers
            })
            
        except Exception as e:
            print(f"Error processing a question in {file_path}: {e}")
    
    return questions

def main():
    # Find all HTML files
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and 'Kiểm tra giữa kỳ' in f]
    
    all_questions = []
    
    for html_file in html_files:
        print(f"Processing {html_file}...")
        extracted_questions = extract_questions_from_file(html_file)
        print(f"  Found {len(extracted_questions)} questions")
        all_questions.extend(extracted_questions)
    
    # Sort questions by number
    all_questions.sort(key=lambda q: int(q['number']))
    
    # Save to JSON file
    with open('questions.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_questions, json_file, ensure_ascii=False, indent=2)
    
    print(f"Extracted {len(all_questions)} questions and saved to questions.json")

if __name__ == "__main__":
    main() 