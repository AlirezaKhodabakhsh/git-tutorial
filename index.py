import torch
print("Version pytorch is : {}".format(torch.__version__))
dtype = torch.float
device  = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
A=torch.tensor([1,2,3], dtype = dtype, device=device)