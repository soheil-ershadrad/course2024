#https://wiki.fysik.dtu.dk/ase/ase/build/build.html

import ase.build
from ase.io import write

#Nano Ribbon 

ribbon = ase.build.graphene_nanoribbon(
        n = 2, # The width of the nanoribbon.
        m = 8, # The length of the nanoribbon.
        type = 'armchair', # The orientation, either ‘zigzag’ or ‘armchair’.
        sheet = False, # If true, make an infinite sheet instead of a ribbon. 
        saturated = False, # If true, hydrogen atoms are placed along the edge.
        vacuum = 10, # Amount of vacuum added to non-periodic directions, if present.
)

write('POSCARribbon', ribbon, format='vasp')
###############

# Carbon Nano Tube

cnt = ase.build.nanotube(3, 3, length=6, symbol='C')

# Set lattice vectors
cnt.set_cell([[10, 0, 0], [0, 10, 0], [0, 0, 10]], scale_atoms=False)
cnt.center()

write('POSCARtube', cnt , format='vasp')
###############

#C60

molecule = ase.build.molecule('C60', cell = [10,10,10])

molecule.center()

write('POSCARc60', molecule, format='vasp')
###############
