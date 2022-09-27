import pandas as pd
import numpy as np
import os
import shutil

data_type = 'val'

path = "/home/atik/Documents/MAML/Summer_1/datasets/miniImageNet/mini-imagenet/images"

files =pd.read_csv('/home/atik/Documents/MAML/Summer_1/datasets/miniImageNet/mini-imagenet/%s.csv' %data_type)

classes = np.unique(files['label'])

dirc = '/home/atik/Documents/UMAML_FSL/data/'+data_type+'/'

for i in range(len(classes)):
    if not os.path.exists(dirc+classes[i]):
        os.mkdir(dirc+classes[i])
    
for i,j in enumerate(files.iloc):

    loc_src = os.path.join(path, files.iloc[i][0])
    loc_des = os.path.join(dirc, j[1])
    
    shutil.copy(loc_src, loc_des)
    
    
