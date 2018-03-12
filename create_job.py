from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

###########################################################################
# Function definition
###########################################################################

def create_job(model_name,
				part_name,
				umat_filename,
				job_name,
				write_input,
				input_filename,
				write_cae,
				cae_filename,
				submit_job
				):

	print 'create_job'

	mdb.Job(name=job_name, model=model_name, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, 
    userSubroutine=umat_filename, 
    scratch='', multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)

	if write_input:
		mdb.jobs['Job-1'].writeInput(consistencyChecking=OFF)

	if write_cae:
		if cae_filename =='':
			cae_filename = job_name + '.cae'
		mdb.saveAs(pathName=cae_filename)

	if submit_job:
		mdb.jobs[job_name].submit(consistencyChecking=OFF)