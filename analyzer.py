import re
from collections import Counter
from textblob import TextBlob
import nltk

# NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load resume
with open('resume.txt', 'r', encoding='utf-8') as f:
    resume_text = f.read().lower()

# Load important skills
with open('important_skills.txt', 'r', encoding='utf-8') as f:
    skills_list = [line.strip().lower() for line in f.readlines()]

# Preprocess text: remove punctuation
resume_text_clean = re.sub(r'[^\w\s]', '', resume_text)

# Tokenize words
words = nltk.word_tokenize(resume_text_clean)

# Count skill mentions (multi-word aware)
skill_counter = Counter()
for skill in skills_list:
    skill_words = skill.split()
    # Match skill phrase in resume text
    count = sum(1 for i in range(len(words) - len(skill_words) + 1)
                if words[i:i+len(skill_words)] == skill_words)
    skill_counter[skill] = count

# Calculate resume strength
total_skills = len(skills_list)
matched_skills = sum(1 for count in skill_counter.values() if count > 0)
resume_strength = round((matched_skills / total_skills) * 100, 2)

# Top skills
top_skills = skill_counter.most_common(5)

# Missing important skills
missing_skills = [skill for skill, count in skill_counter.items() if count == 0]

# Sentiment analysis
blob = TextBlob(resume_text)
sentiment = blob.sentiment.polarity  # -1 (negative) to +1 (positive)

# Output
print("==== Resume Analysis ====")
print("Top Skills:", top_skills)
print("Missing Important Skills:", missing_skills)
print("Overall Resume Strength:", f"{resume_strength}%")
print("Sentiment Score:", round(sentiment, 2))