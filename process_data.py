import h5py
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

ground_truth_path = filedialog.askopenfilename(title="Select a ground truth data")
dir_path = filedialog.askdirectory(title="Select a folder with images", mustexist=1)
dir_to_save = filedialog.askdirectory(title="Select a folder to save", mustexist=1)
f = h5py.File(ground_truth_path)
img_list = os.listdir(dir_path)
img_list.sort()

# getting size of images
img_height = f['ground_truth_data/imgsize'][0, 0]/6
img_width = f['ground_truth_data/imgsize'][1, 0]/6

for x in range(f['ground_truth_data/list'].shape[1]):
    bbox = f[f['ground_truth_data/list'][0, x]]['bbox'][:].transpose()/6
    imgname = ''.join([chr(c) for c in f[f['ground_truth_data/list'][0, x]]['imgname'][:]])

    str = ''
    for item in bbox:
        if np.isscalar(item) or len(item) != 4: continue
        dw = 1/img_width
        dh = 1/img_height
        x = (item[0] + item[2] + item[0]) / 2.0
        y = (item[1] + item[3] + item[1]) / 2.0
        w = item[2]
        h = item[3]
        x = x * dw
        w = w * dw
        y = y * dh
        h = h * dh
        tmp = '0 ' + x.__str__() + ' ' + y.__str__() + ' ' + w.__str__() + ' ' + h.__str__() + '\n'
        str += tmp

    # write the path of each image to a file
    os.system("echo '{0}' > {2}/{1}txt".format(str, imgname[:-3], dir_to_save))
    # copy images that fit to dataset to the selected folder
    [os.system("cp image-set/{0} {1}/{0}".format(img, dir_to_save)) for img in img_list if img == imgname]