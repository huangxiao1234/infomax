import os
import cv2
import numpy as np

def data_load(data_path):
	file_names = sorted(os.listdir(data_path))
	file_l=["\'"+i.split(".")[0]+"\'" for i in file_names]
	train_x = []
	for file_name in file_names:
		image = cv2.imread(data_path+file_name)
		train_x.append(image)
	d = np.array(train_x)
	print(d.shape)
	return d,file_l

if __name__ =="__main__":
	data = data_load("data/Image/")
