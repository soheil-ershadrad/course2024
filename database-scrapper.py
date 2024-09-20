from mp_api.client import MPRester
import os
import numpy as np
api_key = "xxxxxxxxxxxxxxxxx"  # Replace with your actual API key

# Initialize the MPRester with your API key
with MPRester(api_key) as mpr:
    for i in range(1,10):
        id = f"mp-{i}"
        print(id)
        docs = mpr.materials.summary.search(material_ids=[f"{id}"], fields=['structure', 'nsites', 'elements', 'nelements', 'symmetry', 'is_magnetic', 'ordering', 'total_magnetization', 'total_magnetization_normalized_vol', 'total_magnetization_normalized_formula_units', 'num_magnetic_sites', 'num_unique_magnetic_sites'])
        if docs != []:
            structure = docs[0].structure
            nsites = docs[0].nsites
            elements = docs[0].elements
            nelements = docs[0].nelements
            symmetry = docs[0].symmetry
            is_magnetic  = docs[0].is_magnetic
            ordering = docs[0].ordering
            total_magnetization= docs[0].total_magnetization
            num_magnetic_sites = docs[0].num_magnetic_sites
            num_unique_magnetic_sites = docs[0].num_unique_magnetic_sites

            elements = ', '.join(str(item) for item in elements)
            elements = np.array(elements)
            structure = mpr.get_structure_by_material_id(f"{id}")
            poscar = structure.to(fmt="poscar")
            lines = poscar.splitlines()
            name = lines[0]
            remaining_lines = lines[1:]
            poscar = "\n".join(remaining_lines)
            with open(f"POSCAR-{id}", "w") as f:
                f.write(f'''{name} {nsites} {elements} {nelements} {ordering} {total_magnetization} {num_magnetic_sites} {num_unique_magnetic_sites} \n {poscar}''')
