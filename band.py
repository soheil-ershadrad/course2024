#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({'font.size': 16})
import numpy as np

num_cut = 10

def band_plotter():

	data=[]
	kpts=[]
	with open('KLABELS') as f:
		for i, lines in enumerate(f.readlines()):
			if i>0 and len(lines.split())==2:
				kpts.append(float(lines.split()[1]))
			

	with open('BAND.dat') as f:
		for i, lines in enumerate(f.readlines()):
			z = lines.split()
			if len(z)>0 and z[0]!="#" and z[0]!="#K-Path(1/A)":
				y = [float(x) for x in z]
				data.append(y)

	data=np.array(data)

	fig, axes = plt.subplots(1)

	for i in range(data.shape[0]):
			axes.plot(data[i*num_cut:i*num_cut+num_cut,0], data[i*num_cut:i*num_cut+num_cut,1], color='b', )


	axes.set_ylabel('Energy (eV)')
	#axes.legend(loc='upper right', fontsize = 16, framealpha=1 )
	#axes.set_ylim([inp.band_ylim[0], inp.band_ylim[1]])
	axes.set_xlim([0, kpts[-1]])
	#axes.set_yticks(np.arange(-5, 5.001, 1))
	axes.axhline(y = 0.0, linestyle = '--', color = 'k')
	axes.set_xticks([0, kpts[1], kpts[-1]])		# needs to be modified
	axes.set_xticklabels(['\u0393', 'M' , '\u0393'])	# needs to be modified

	fig.tight_layout()
 
	fig.savefig("band.png", dpi=500)

	return

if __name__ == "__main__":
	band_plotter()
