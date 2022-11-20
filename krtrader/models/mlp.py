import torch
import torch.nn as nn


class MLP(torch.nn.Module):
    """An example of how to define a MLP model"""
    def __init__(self, input_dim, output_dim):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, output_dim)
        self.relu = nn.ReLU()


    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


if __name__ == "__main__":
    input_dim = 10
    output_dim = 1
    model = MLP(input_dim, output_dim)
    x = torch.randn(1, input_dim)
    print(model(x))