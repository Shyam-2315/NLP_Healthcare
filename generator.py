import json
import random
from faker import Faker
from tqdm import tqdm

fake = Faker()

# Sample ICD-10 and CPT code pools
icd10_codes_pool = ['J45.909', 'M54.5', 'I10', 'J02.9', 'F41.1', 'K21.9', 'E11.9', 'R07.89']
cpt_codes_pool = ['99203', '99204', '99212', '99213', '99214']

# Symptom templates
complaints = [
    "persistent dry cough", "low back pain", "high blood pressure", "sore throat",
    "anxiety for several months", "heartburn", "chest pain on exertion",
    "persistent headaches", "abdominal cramps", "shortness of breath",
    "joint stiffness in the morning", "skin rash", "vision disturbances",
    "dizziness and lightheadedness", "sleep disturbances"
]

assessments = [
    "Mild intermittent asthma exacerbation", "Acute Low Back Pain", "Essential Hypertension",
    "Acute Pharyngitis", "Generalized Anxiety Disorder", "Gastroesophageal Reflux Disease",
    "Atypical chest pain", "Migraine Headache", "Irritable Bowel Syndrome",
    "Chronic Obstructive Pulmonary Disease", "Osteoarthritis", "Eczema",
    "Diabetic Retinopathy", "Vertigo", "Insomnia"
]

plans = [
    "Initiated short-acting beta-agonist inhaler", "Advised rest and NSAIDs",
    "Continue current medication and monitor BP", "Recommended symptomatic relief with lozenges",
    "Discussed CBT and SSRI options", "Advised dietary modifications and PPIs",
    "Scheduled stress test", "Prescribed triptans for migraines",
    "Recommended probiotics and fiber diet", "Prescribed inhaled bronchodilators",
    "Referred for physiotherapy", "Advised moisturizing creams",
    "Scheduled ophthalmology follow-up", "Advised vestibular exercises",
    "Recommended sleep hygiene practices"
]

def generate_clinical_note(note_id):
    age = random.randint(18, 80)
    gender = random.choice(['male', 'female'])
    patient_status = random.choice(['new patient', 'established patient'])
    
    idx = random.randint(0, len(complaints)-1)

    note_text = (
        f"Patient is a {age}-year-old {gender}, {patient_status}, presenting with {complaints[idx]}. "
        f"Objective findings and vitals are within normal limits unless specified otherwise. "
        f"Assessment: {assessments[idx]}. "
        f"Plan: {plans[idx]}. Follow-up in {random.choice(['1 week', '4 weeks', '3 months', '6 months'])}."
    )

    return {
        "note_id": f"note_{note_id}",
        "clinical_note_text": note_text,
        "icd10_codes": [random.choice(icd10_codes_pool)],
        "cpt_codes": [random.choice(cpt_codes_pool)]
    }

# Number of records to generate
NUM_RECORDS = 10000
clinical_notes = []

print("Generating clinical notes data...")
for i in tqdm(range(1, NUM_RECORDS + 1)):
    clinical_notes.append(generate_clinical_note(i))

# Save to JSON
with open("clinical_notes.json", "w") as f:
    json.dump(clinical_notes, f, indent=2)

print(f"Successfully generated {NUM_RECORDS} clinical notes to 'clinical_notes.json'")
