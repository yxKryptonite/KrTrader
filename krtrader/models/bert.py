import transformers
from transformers import BertTokenizer, BertModel, BertForMaskedLM
import torch
import torch.nn as nn


class BertModel(nn.Module):
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertModel.from_pretrained('bert-base-uncased')


    def forward(self, sentence):
        input_ids = torch.tensor(self.tokenizer.encode(sentence)).unsqueeze(0)  # Batch size 1
        outputs = self.model(input_ids)
        last_hidden_states = outputs[0]  # The last hidden-state is the first element of the output tuple
        return last_hidden_states


    def encode(self, sentence):
        return self.forward(sentence) 


def main():
    model = BertModel()
    sentence1 = "Hello, my dog is cute"
    sentence2 = "Hello, my cat is cute"
    sentence3 = "Hello, my dog is not cute"
    print(f"sentence1: {sentence1}")
    print(f"sentence2: {sentence2}")
    print(f"sentence3: {sentence3}")
    print(f"Similarity of sentence1 and sentence2: {model.encode(sentence1).dot(model.encode(sentence2).T)}")
    print(f"Similarity of sentence1 and sentence3: {model.encode(sentence1).dot(model.encode(sentence3).T)}")


if __name__ == "__main__":
    main()