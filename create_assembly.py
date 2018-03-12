from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np


###########################################################################
# Function definition
###########################################################################

def create_assembly(model_name,
					part_name,
					instance_name
					):

	print 'create_assembly'

	a = mdb.models[model_name].rootAssembly
	a.DatumCsysByDefault(CARTESIAN)
	p = mdb.models[model_name].parts[part_name]
	a.Instance(name=instance_name, part=p, dependent=ON)

	return instance_name