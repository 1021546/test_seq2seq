import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2,3"

USE_CUDA = torch.cuda.is_available()

MAX_LENGTH = 15
teacher_forcing_ratio = 1.0
save_dir = './save'
