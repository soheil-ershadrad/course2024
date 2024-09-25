#!/usr/bin/python
# -*- coding: UTF-8 -*- 
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams.update({'font.size': 16})
import numpy as np

def dos_plotter():
	data=[]

	with open('TDOS.dat') as f:
		for i, lines in enumerate(f.readlines()):
			if i>0:
				z = lines.split()
				if len(z)>0 and z[0]!="#":
					y = [float(x) for x in z]
					data.append(y)

	data=np.array(data)

	fig, axes = plt.subplots(1)

	axes.plot(data[:,0], data[:,1], color='blue', label = "Spin Up")
	axes.fill_between(data[:,0], data[:,1], color='blue', alpha=0.1)
	axes.plot(data[:,0], data[:,2], color='red', label = "Spin Down")
	axes.fill_between(data[:,0], data[:,2], color='red', alpha=0.1)


	axes.set_xlabel('Energy (eV)')
	axes.set_ylabel('DOS (states/eV)')
	#axes.set_xticks(np.arange(-10, 11, 1))
	#axes.set_yticks(np.arange(-16, 16.1, 4))
	#axes.set_xlim([inp.dos_xlim[0], inp.dos_xlim[1]])
	axes.legend(loc='upper right', fontsize = 16, framealpha=1 )
	axes.axvline(x = 0.0  , linestyle = '--',  color = 'k')
	axes.axhline(y = 0.0, linestyle = '--', color = 'k')
	fig.tight_layout()
	fig.savefig("dos.png", dpi=500)

	return



if __name__ == "__main__":
	dos_plotter()
