import json
import os

def load_and_inspect_clinical_data(filepath="C:\\Projects\\NLP HealthCare\\data\\clinical_notes.json"):
    """
    Loads the clinical notes dataset from a JSON file and prints a summary.
    """
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found. Please ensure it's in the correct directory.")
        print("You need to save the JSON data provided in the report (Section 5) into a file named 'super_dataset.json'.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"Successfully loaded {len(data)} clinical notes from '{filepath}'\n")
        print("--- Data Inspection Summary ---")
        for i, note in enumerate(data):
            note_id = note.get('note_id', 'N/A')
            clinical_note_text_snippet = note.get('clinical_note_text', 'N/A')
            icd10_codes = ', '.join(note.get('icd10_codes',))
            cpt_codes = ', '.join(note.get('cpt_codes',))

            print(f"\nNote ID: {note_id}")
            print(f"  Clinical Note (snippet): {clinical_note_text_snippet[:100]}...")
            print(f"  ICD-10 Codes: {icd10_codes}")
            print(f"  CPT Codes: {cpt_codes}")

            if i >= 4 and len(data) > 5: # Limit output for brevity in demo if more than 5 notes
                print(f"\n... and {len(data) - (i+1)} more notes (full data available in JSON file).")
                break
        print("\n--- End of Summary ---")

    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'. Please check file format for validity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    load_and_inspect_clinical_data()