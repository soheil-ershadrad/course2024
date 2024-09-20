#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({'font.size': 16})
import numpy as np
import os

def pdos_plotter():

	with open('POSCAR') as f:
		for i, lines in enumerate(f.readlines()):
			if i==5:
				num_element = len(lines.split())

	data=np.zeros((2001,2*num_element + 1))
	labels = []

	directory_path = os.getcwd()

	file_list = os.listdir(directory_path)
	file_list.sort(reverse=True)

	j=0
	for file_name in file_list:
		if "PDOS_" in file_name and "IPDOS_" not in file_name:
			j=j+1
			labels.append(file_name[5:-4])
			with open(file_name) as f:
				for i, lines in enumerate(f.readlines()):
					if i>0:
						z = lines.split()
						if len(z)>0 and z[0]!="#":
							y = [float(x) for x in z]
							data[i-1,0] = y[0]
							data[i-1,j] = y[-1]

	data=np.array(data)
	print(data[1000,:])
	print(labels)

	fig, axes = plt.subplots(1)

	for k, tag in enumerate(labels):
	 	axes.plot(data[:,0], data[:,k+1], label = tag)

	axes.set_xlabel('Energy (eV)')
	axes.set_ylabel('DOS (states/eV)')
#	axes.set_xticks(np.arange(-10, 11, 1))
#	axes.set_yticks(np.arange(-16, 16.1, 4))
#	axes.set_xlim([inp.dos_xlim[0], inp.dos_xlim[1]])
	axes.legend(loc='upper right', fontsize = 14, ncol = 2 , framealpha=1 )
	axes.axvline(x = 0.0  , linestyle = '--',  color = 'k')
	axes.axhline(y = 0.0, linestyle = '--', color = 'k')
	fig.tight_layout()
	fig.savefig("pdos.png", dpi=500)

	return


if __name__ == "__main__":
	pdos_plotter()
