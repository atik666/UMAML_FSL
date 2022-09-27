import pandas as pd
import numpy as np
import os
import shutil

data_type = 'train'

path = "/home/atik/Documents/MAML/Summer_1/datasets/miniImageNet/mini-imagenet/images"

files =pd.read_csv('/home/atik/Documents/MAML/Summer_1/datasets/miniImageNet/mini-imagenet/%s.csv' %data_type)

dirc = '/home/atik/Documents/UMAML_FSL/data/unlebelled/'

for i,_ in enumerate(files.iloc):
    loc_src = os.path.join(path, files.iloc[i][0]) 
    shutil.copy(loc_src, dirc)