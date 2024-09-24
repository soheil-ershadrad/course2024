#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({'font.size': 16})
import numpy as np

num_cut = 20 # Needs to be updated based on number of segments in the KPOINTS file
file_name = "PBAND_C.dat" # needs to be modified to the element of interest
orbitals =  ["s", "py", "pz", "px"]  # modify based on PBAND_X.dat file sequence 

def band_plotter():

	data=[]
	kpts=[]
	with open('KLABELS') as f:
		for i, lines in enumerate(f.readlines()):
			if i>0 and len(lines.split())==2:
				kpts.append(float(lines.split()[1]))
			

	with open(file_name) as f:
		for i, lines in enumerate(f.readlines()):
			z = lines.split()
			if len(z)>0 and z[0]!="#" and z[0]!="#K-Path(1/A)" and  z[0]!= "#K-Path" :
				y = [float(x) for x in z]
				data.append(y)

	data=np.array(data)
	print(data)

	fig, axes = plt.subplots(1)

	color_list=["r", "b","g", "orange", "magenta", "gold", "saddlebrown", "cyan", "k"]

	for k in range(len(orbitals)):
		for i in range(data.shape[0]):
			axes.scatter(data[i*num_cut:i*num_cut+num_cut,0], data[i*num_cut:i*num_cut+num_cut,1], s=20*data[i*num_cut:i*num_cut+num_cut,k+2], color= color_list[k] )
	

	legend_handles = [plt.Line2D([0], [0], color=color_list[i], label=orbitals[i]) for i in range(k+1)]

	axes.set_ylabel('Energy (eV)')
	axes.legend(handles=legend_handles, fontsize = 16, framealpha=1 )
	axes.set_ylim([-10, 10])
	axes.set_xlim([0, kpts[-1]])
	#axes.set_yticks(np.arange(-5, 5.001, 1))
	axes.axhline(y = 0.0, linestyle = '--', color = 'k')
	axes.set_xticks(list(kpts))
	axes.set_xticklabels(['\u0393', 'X' , 'K', '\u0393'])	# needs to be modified

	fig.tight_layout()
 
	fig.savefig("fatband.png", dpi=500)

	return

if __name__ == "__main__":
	band_plotter()
