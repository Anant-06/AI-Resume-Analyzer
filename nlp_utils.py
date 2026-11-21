
import spacy
import re

nlp = spacy.load("en_core_web_sm")

TECHNICAL_SKILLS = [
    "python", "java", "javascript", "jdbc",
    "c++", "sql", "html", "css",
    "react", "tensorflow", "pytorch",
    "machine learning", "deep learning",
    "nlp", "streamlit", "git", "docker",
    "scikit-learn", "opencv"
]


def extract_entities(text):
    doc = nlp(text)

    entities = []
    seen = set()

    # Recognize technical skills
    for skill in TECHNICAL_SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            key = (skill.lower(), "SKILL")

            if key not in seen:
                entities.append((skill, "SKILL"))
                seen.add(key)

    # Recognize general named entities
    for ent in doc.ents:
        name = ent.text.strip()
        label = ent.label_

        if name.lower() in TECHNICAL_SKILLS:
            continue

        key = (name.lower(), label)

        if key not in seen:
            entities.append((name, label))
            seen.add(key)

    return entities
