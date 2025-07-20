from transformers import AutoTokenizer

clinical_note = """
The patient presented with acute onset of severe abdominal pain, localized to the right lower quadrant, accompanied by nausea and vomiting.
Physical examination revealed rebound tenderness and guarding. Labs showed elevated white blood cell count. Suspected appendicitis, pending surgical consult.
"""

# Initialize tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the clinical note
inputs = tokenizer(clinical_note, return_tensors="pt", padding='max_length', truncation=True, max_length=512)

print(inputs)
