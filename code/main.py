import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class Grid():
    def __init__(self, size):
        self.size = size
        