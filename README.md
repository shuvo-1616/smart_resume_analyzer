# smart_resume_analyzer
# Smart Resume Analyzer (AI CV Checker)

Analyze resumes to extract top skills, missing skills, and overall resume strength.

## Features
- Multi-word skill detection
- Top skills ranking
- Missing important skills recommendation
- Overall resume strength calculation
- Sentiment analysis

## How to Run

1. Install required libraries:

pip install textblob pip install nltk

2. Run the analyzer:

python analyzer.py

3. Output:

==== Resume Analysis ==== Top Skills: [('python', 5), ('machine learning', 3), ('data analysis', 2)] Missing Important Skills: ['sql', 'tensorflow', 'pytorch'] Overall Resume Strength: 82% Sentiment Score: 0.15

## Files
- `resume.txt` → Example candidate resume
- `important_skills.txt` → List of key skills
- `analyzer.py` → Main Python script
- `requirements.txt` → Required Python libraries
- `README.md` → Project description & usage
