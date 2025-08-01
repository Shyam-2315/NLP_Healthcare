import torch
from transformers import AutoTokenizer, AutoModel

def get_clinical_note_embedding(note: str, model, tokenizer) -> torch.Tensor:
    """
    Tokenizes a raw clinical note, passes it through the pre-trained transformer model,
    and obtains a sentence embedding using mean pooling of the last hidden state.

    Args:
        note (str): The raw clinical note text to be embedded.
        model: The loaded Hugging Face AutoModel instance.
        tokenizer: The loaded Hugging Face AutoTokenizer instance.

    Returns:
        torch.Tensor: A tensor representing the sentence embedding of the note.
                      The shape will be (1, hidden_size), where hidden_size is
                      the dimensionality of the model's embeddings (e.g., 768 for base models).
    """
    # 1. Tokenize the note:
    #    - return_tensors="pt" ensures PyTorch tensors are returned.
    #    - padding='max_length' pads the sequence to the specified max_length.
    #    - truncation=True truncates the sequence if it exceeds the max_length.
    #    - max_length=512 explicitly sets the maximum sequence length, which is common for BERT models.
    inputs = tokenizer(note, return_tensors="pt", padding='max_length', truncation=True, max_length=512)

    # 2. Pass the tokens through the model:
    #    - model.eval() ensures the model is in evaluation mode (disables dropout, etc.).
    #    - with torch.no_grad() disables gradient calculations, saving memory and speeding up inference.
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)

    # 3. Obtain sentence embedding:
    #    - outputs.last_hidden_state: Tensor of shape (batch_size, sequence_length, hidden_size)
    #      containing contextualized embeddings for each token.
    #    -.mean(dim=1): Performs mean pooling across the sequence_length dimension to
    #      derive a single vector for the entire sequence.
    sentence_embedding = outputs.last_hidden_state.mean(dim=1)

    return sentence_embedding

if __name__ == "__main__":
    model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"

    print(f"Attempting to load model and tokenizer for: '{model_name}'...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        print("Model and tokenizer loaded successfully.")
    except Exception as e:
        print(f"Error loading model or tokenizer: {e}")
        print("Please ensure you have an active internet connection or the model is cached locally. "
              "You might also need to install the 'transformers' library: pip install transformers torch")
        exit()

    sample_clinical_note = "The patient presented with acute onset of severe abdominal pain, localized to the right lower quadrant, accompanied by nausea and vomiting. Physical examination revealed rebound tenderness and guarding. Labs showed elevated white blood cell count. Suspected appendicitis, pending surgical consult."

    print(f"\nProcessing the following clinical note:\n---")
    print(sample_clinical_note)
    print(f"---\n")

    embedding = get_clinical_note_embedding(sample_clinical_note, model, tokenizer)

    print(f"Successfully obtained sentence embedding.")
    print(f"Embedding Tensor Shape: {embedding.shape}")