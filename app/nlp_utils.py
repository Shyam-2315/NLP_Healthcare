from transformers import AutoTokenizer, AutoModel
import torch

model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext"

# Load Tokenizer: AutoTokenizer automatically selects the correct tokenizer class
# based on the model_name and downloads its vocabulary files.
tokenizer = AutoTokenizer.from_pretrained(model_name)
print(f"Tokenizer loaded: {type(tokenizer)}")

# Load Model: AutoModel automatically selects the correct model class (e.g., BertModel)
# and downloads its pre-trained weights. AutoModel is used for general embeddings,
# as it provides the raw hidden states without a task-specific head.
model = AutoModel.from_pretrained(model_name)
model.eval() # Set the model to evaluation mode; crucial for inference to disable dropout etc.
print(f"Model loaded: {type(model)}")