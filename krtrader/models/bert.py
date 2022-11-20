import transformers
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import torch


def encode(sentence):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')
    input_ids = torch.tensor(tokenizer.encode(sentence)).unsqueeze(0)  # Batch size 1
    outputs = model(input_ids)
    last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
    return last_hidden_states


def main():
    sentence1 = "Hello, my dog is cute"
    sentence2 = "Hello, my cat is cute"
    sentence3 = "Hello, my dog is not cute"
    print(f"sentence1: {sentence1}")
    print(f"sentence2: {sentence2}")
    print(f"sentence3: {sentence3}")
    print(f"Similarity of sentence1 and sentence2: {encode(sentence1).dot(encode(sentence2).T)}")
    print(f"Similarity of sentence1 and sentence3: {encode(sentence1).dot(encode(sentence3).T)}")


if __name__ == "__main__":
    main()