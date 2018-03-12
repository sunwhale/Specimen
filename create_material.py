from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

###########################################################################
# Function definition
###########################################################################

def create_material(model_name,
					part_name,
					material_user,
					material_GH4169
					):
	
	material_name = 'GH4169'
	section_name = 'Section-GH4169'
	mdb.models[model_name].Material(name=material_name)
	mdb.models[model_name].materials[material_name].Density(temperatureDependency=ON, table=((8.24E-9, 20), ))
	mdb.models[model_name].materials[material_name].Conductivity(temperatureDependency=ON, table=((13.4, 11), (14.7, 100), (15.9, 200), (17.8, 300), (18.3, 400), (19.6, 500), (21.2, 600), (22.8, 700), (23.6, 800), (27.6, 900), (30.4, 1000), ))
	mdb.models[model_name].materials[material_name].SpecificHeat(temperatureDependency=ON, table=((481.4E6, 300), (493.9E6, 400), (514.8E6, 500), (539E6, 600), (573.4E6, 700), (615.3E6, 800), (657.2E6, 900), (707.4E6, 1000), ))
	mdb.models[model_name].materials[material_name].Expansion(temperatureDependency=ON, table=((9.1E-6, -253), (11E-6, -183), (11.8E-6, 20), (11.8E-6, 100), (13E-6, 200), (13.5E-6, 300), (14.1E-6, 400), (14.4E-6, 500), (14.8E-6, 600), (15.4E-6, 700), (17E-6, 800), (18.4E-6, 900), (18.7E-6, 1000), ))
	mdb.models[model_name].materials[material_name].Elastic(temperatureDependency=ON, table=((204E3, 0.3, 20), (181E3, 0.3, 300), (176E3, 0.31, 400), (160E3, 0.32, 500), (160E3, 0.32, 550), (150E3, 0.32, 600), (146E3, 0.325, 650), (141E3, 0.33, 700), ))
	mdb.models[model_name].HomogeneousSolidSection(name=section_name, material=material_name, thickness=None)
	
	material_name = 'User'
	section_name = 'Section-User'
	mdb.models[model_name].Material(name=material_name)
	mdb.models[model_name].materials[material_name].Depvar(n=200)
	mdb.models[model_name].materials[material_name].UserMaterial(mechanicalConstants=(0.0, ))
	mdb.models[model_name].HomogeneousSolidSection(name=section_name, material=material_name, thickness=None)

	p = mdb.models[model_name].parts[part_name]
	c = p.cells
	region = regionToolset.Region(cells=c)

	if material_GH4169:
		section_name = 'Section-GH4169'
	if material_user:
		section_name = 'Section-User'

	p.SectionAssignment(region=region, sectionName=section_name, offset=0.0, 
	    offsetType=MIDDLE_SURFACE, offsetField='', 
	    thicknessAssignment=FROM_SECTION)