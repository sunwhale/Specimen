from abaqus import *
from abaqusConstants import *
from caeModules import *
import numpy as np

#==============================================================================
# class Load
#==============================================================================
class Load:
    """
    Define loadings.
    """
    def __init__(self, runing_time=[], temperature=[], axial_strain=[], 
                 shear_strain=[], axial_stress=[], force=[], torque=[], first_cycle_shift=0):
        self.runing_time = runing_time
        self.temperature = temperature
        self.axial_strain = axial_strain
        self.axial_stress = axial_stress
        self.shear_strain = shear_strain
        self.force = force
        self.torque = torque
        self.total_runing_time = self.runing_time[-1]
        self.length = len(self.runing_time)
        self.first_cycle_shift = first_cycle_shift
        self.segment = 1
        
    def setLoadUniaxial(self, cycles, runing_time, temperature, axial_strain):
        for n in range(cycles):
            self.runing_time += [ n*(runing_time[-1]-runing_time[0]) + time for time in runing_time[:-1]]
        self.temperature = temperature[:-1] * cycles
        self.axial_strain = axial_strain[:-1] * cycles
        
        self.runing_time.append(cycles*(runing_time[-1]-runing_time[0]))
        self.temperature.append(temperature[-1])
        self.axial_strain.append(axial_strain[-1])
        self.length = len(self.runing_time)
        self.axial_stress = np.zeros(self.length)
        self.torque = np.zeros(self.length)
        self.total_runing_time = self.runing_time[-1]
        self.segment = 1
        
    def listToArray(self):
        self.runing_time = np.array(self.runing_time)
        self.temperature = np.array(self.temperature)
        self.axial_strain = np.array(self.axial_strain)
        self.axial_stress = np.array(self.axial_stress)
        self.shear_strain = np.array(self.shear_strain)
        self.torque = np.array(self.torque)
        
    def setLoadBiaxial(self, cycles, runing_time, temperature, axial_strain, shear_strain, force, torque):
        for n in range(cycles):
            self.runing_time += [ n*(runing_time[-1]-runing_time[0]) + time for time in runing_time[:-1]]
        self.temperature += temperature[:-1] * cycles
        self.axial_strain += axial_strain[:-1] * cycles
        self.shear_strain += shear_strain[:-1] * cycles
        self.force += force[:-1] * cycles
        self.torque += torque[:-1] * cycles

        self.runing_time.append(cycles*(runing_time[-1]-runing_time[0]))
        self.temperature.append(temperature[-1])
        self.axial_strain.append(axial_strain[-1])
        self.shear_strain.append(shear_strain[-1])
        self.force.append(force[-1])
        self.torque.append(torque[-1])
        self.total_runing_time = self.runing_time[-1]

        if axial_strain[0]==0 and shear_strain[0]==0 and force[0]==0 and torque[0]==0:
            self.runing_time.pop(1)
            self.temperature.pop(1)
            self.axial_strain.pop(1)
            self.shear_strain.pop(1)
            self.force.pop(1)
            self.torque.pop(1)

        if axial_strain[0]<>0:
            self.runing_time[1] = self.first_cycle_shift
        if shear_strain[0]<>0:
            self.runing_time[1] = self.first_cycle_shift
        if force[0]<>0:
            self.runing_time[1] = self.first_cycle_shift
        if torque[0]<>0:
            self.runing_time[1] = self.first_cycle_shift

        self.length = len(self.runing_time)
        self.axial_stress = np.zeros(self.length)
        self.segment = 1
        
###########################################################################
# Function definition
###########################################################################

def create_load(model_name,
				part_name,
				instance_name,
				step_name,
				loading_cycles,
				loading_conditions,
				displacement_value,
				rotation_value,
				force_value,
				torque_value,
				temperature_value,
				add_displacement,
				add_rotation,
				add_force,
				add_torque,
				add_temperature
				):

	print 'create_load'

	runing_time = []
	temperature = []
	axial_strain = []
	shear_strain = []
	force = []
	torque = []
	
	for l in loading_conditions:
	    runing_time += [l[0]]
	    axial_strain += [l[1]]
	    shear_strain += [l[2]]
	    force += [l[3]]
	    torque += [l[4]]
	    temperature += [l[5]]

	load = Load(runing_time=[0], temperature=[0], axial_strain=[0], shear_strain=[0], force=[0], torque=[0], first_cycle_shift=runing_time[1]/2.0)

	load.setLoadBiaxial(int(loading_cycles),
	                   runing_time,
	                   temperature,
	                   axial_strain,
	                   shear_strain,
	                   force,
	                   torque
	                   )

	amp_displacement = []
	amp_rotation = []
	amp_force = []
	amp_torque = []
	amp_temperature = []

	for i in range(load.length):
		amp_displacement += [[load.runing_time[i],load.axial_strain[i]]]
		amp_rotation += [[load.runing_time[i],load.shear_strain[i]]]
		amp_temperature += [[load.runing_time[i],load.temperature[i]]]
		amp_force += [[load.runing_time[i],load.force[i]]]
		amp_torque += [[load.runing_time[i],load.torque[i]]]

	mdb.models[model_name].TabularAmplitude(name='Amp-displacement', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_displacement)
	mdb.models[model_name].TabularAmplitude(name='Amp-rotation', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_rotation)
	mdb.models[model_name].TabularAmplitude(name='Amp-temperature', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_temperature)
	mdb.models[model_name].TabularAmplitude(name='Amp-force', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_force)
	mdb.models[model_name].TabularAmplitude(name='Amp-torque', timeSpan=STEP, smooth=SOLVER_DEFAULT, data=amp_torque)

	a = mdb.models[model_name].rootAssembly
	f1 = a.instances[instance_name].faces
	faces1 = f1.getSequenceFromMask(mask=(
	    '[#0:12 #20010011 #1200 #40080084 #200020 ]', ), )
	a.Set(faces=faces1, name='Fixed')
	region = a.sets['Fixed']
	mdb.models[model_name].DisplacementBC(name='BC-Fixed', createStepName=step_name, 
	    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
	    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', 
	    localCsys=None)

	a = mdb.models[model_name].rootAssembly
	f1 = a.instances[instance_name].faces
	faces1 = f1.getSequenceFromMask(mask=(
	    '[#0:11 #80000000 #500400 #808000 #2102002 #1000040 ]', ), )
	a.Set(faces=faces1, name='Actuator')

	# Coupling
	a = mdb.models[model_name].rootAssembly

	a.ReferencePoint(point=(0.0, 0.0, 0.0))
	r1 = a.referencePoints
	refPoints1=(r1[r1.keys()[-1]], )
	region1=regionToolset.Region(referencePoints=refPoints1)
	
	s1 = a.instances[instance_name].faces
	side1Faces1 = s1.getSequenceFromMask(mask=(
	    '[#0:11 #80000000 #500400 #808000 #2102002 #1000040 ]', ), )
	a.Surface(side1Faces=side1Faces1, name='Actuator')
	region2=a.surfaces['Actuator']

	mdb.models[model_name].Coupling(name='Constraint-Actuator', controlPoint=region1, 
	    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
	    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=OFF, ur2=ON, ur3=OFF)
	
	region = regionToolset.Region(referencePoints=refPoints1)

	if add_displacement:
		mdb.models[model_name].DisplacementBC(name='BC-Displacement', createStepName=step_name, 
		    region=region, u1=UNSET, u2=displacement_value, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET, 
		    amplitude='Amp-displacement', fixed=OFF, distributionType=UNIFORM, 
		    fieldName='', localCsys=None)

	if add_rotation:
		mdb.models[model_name].DisplacementBC(name='BC-Rotation', createStepName=step_name, 
		    region=region, u1=UNSET, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=rotation_value, ur3=UNSET, 
		    amplitude='Amp-rotation', fixed=OFF, distributionType=UNIFORM, 
		    fieldName='', localCsys=None)

	if add_force:
		mdb.models[model_name].ConcentratedForce(name='Load-Force', createStepName=step_name, 
		    region=region, cf2=force_value, amplitude='Amp-force', distributionType=UNIFORM, field='', localCsys=None)

	if add_torque:
		mdb.models[model_name].Moment(name='Load-Moment', createStepName=step_name, 
	    	region=region, cm2=torque_value, amplitude='Amp-torque', distributionType=UNIFORM, field='', localCsys=None)