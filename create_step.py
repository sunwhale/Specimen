from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

###########################################################################
# Function definition
###########################################################################

def create_step(model_name,
				part_name,
				step_name,
				timePeriod,
				maxNumInc,
				initialInc,
				minInc,
				maxInc
				):

	print 'create_step'

	mdb.models[model_name].StaticStep(name=step_name, previous='Initial', 
    timePeriod=timePeriod, maxNumInc=maxNumInc, initialInc=initialInc, minInc=minInc, 
    maxInc=maxInc)

	return step_name