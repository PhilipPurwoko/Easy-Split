import os
import shutil

# You can change to your own data directory
data_dir = 'data'

# Getting class information
all_class = {'train':{},'valid':{}}
for cl in os.listdir(data_dir):
	items = os.listdir(f'{data_dir}/{cl}')
	test_count = int(0.2*(len(items)))
	all_class['train'][cl] = items[test_count:]
	all_class['valid'][cl] = items[:test_count]

# Moving files for each class
for category,cl in all_class.items():
	for sub_class,item in cl.items():
		for i in item:
			print(f'{category}/{sub_class}/{i}')
			des_path = f'dataset/{category}/{sub_class}/'
			os.makedirs(des_path, exist_ok=True)
			shutil.move(f'{data_dir}/{sub_class}/{i}',des_path)