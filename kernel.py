# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 11:50:47 2017

@author: j.Sun
"""
from abaqus import *
from abaqusConstants import *
import numpy as np
import create_sketch
import create_part
import create_mesh
import create_material
import create_assembly
import create_step
import create_load
import create_job

def create_specimen(gauge_length = 35.0,
					specimen_length = 180.0,
					grip_length = 60.0,
					inner_radius = 5.0,
					outer_radius_in_gauge_length = 6.0,
					outer_radius = 8.0,
					R1 = 1.0,
					R2 = 0.2,
					theta = 18.0,
					seed_1 = 5,
					seed_2 = 5,
					seed_3 = 5,
					seed_4 = 5,
					seed_5 = 5,
					seed_6 = 5,
					seed_7 = 5,
					seed_8 = 5,
					seed_9 = 5,
					seed_10 = 5,
					seed_11 = 5,
					seed_12 = 5,
					seed_13 = 5,
					seed_14 = 5,
					seed_15 = 5,
					seed_16 = 5,
					seed_17 = 5,
					seed_18 = 5,
					seed_19 = 5,
					seed_20 = 5,
					timePeriod = 1,
					maxNumInc = 10000,
					initialInc = 1,
					minInc = 1,
					maxInc = 1,
					loading_cycles = 20,
					loading_conditions = [],
					displacement_value = 0,
					rotation_value = 0,
					force_value = 0,
					torque_value = 0,
					temperature_value = 0,
					add_displacement = 0,
					add_rotation = 0,
					add_force = 0,
					add_torque = 0,
					add_temperature = 0,
					material_user = False,
					material_GH4169 = False,
					umat_filename = '',
					job_name = '',
					write_input = False,
					input_filename = '',
					write_cae = False,
					cae_filename = '',
					submit_job = False,
					run_part_module = False,
					run_mesh_module = False,
					run_material_module = False,
					run_assembly_module = False,
					run_step_module = False,
					run_load_module = False,
					run_job_module = False
					):

	model_name = 'Model-1'
	part_name = 'Specimen'
	instance_name = 'Specimen-1'
	step_name = 'Step-1'

	reload(create_sketch)
	reload(create_part)
	reload(create_mesh)
	reload(create_material)
	reload(create_assembly)
	reload(create_step)
	reload(create_load)
	reload(create_job)

	if run_part_module:
		create_sketch.create_sketch(model_name,
					  part_name,
					  gauge_length = gauge_length,
					  specimen_length = specimen_length,
					  grip_length = grip_length,
					  inner_radius = inner_radius,
					  outer_radius_in_gauge_length = outer_radius_in_gauge_length,
					  outer_radius = outer_radius,
					  R1 = R1,
					  R2 = R2,
					  theta = theta)

		create_part.create_part(model_name,
					part_name,
					gauge_length = gauge_length,
					specimen_length = specimen_length,
					grip_length = grip_length,
					inner_radius = inner_radius,
					outer_radius_in_gauge_length = outer_radius_in_gauge_length,
					outer_radius = outer_radius,
					R1 = R1,
					R2 = R2,
					theta = theta)

	if run_mesh_module:
		create_mesh.create_mesh(model_name,
					part_name,
		    		seed_1 = seed_1,
					seed_2 = seed_2,
					seed_3 = seed_3,
					seed_4 = seed_4,
					seed_5 = seed_5,
					seed_6 = seed_6,
					seed_7 = seed_7,
					seed_8 = seed_8,
					seed_9 = seed_9,
					seed_10 = seed_10,
					seed_11 = seed_11,
					seed_12 = seed_12,
					seed_13 = seed_13,
					seed_14 = seed_14,
					seed_15 = 5,
					seed_16 = 5,
					seed_17 = 5,
					seed_18 = 5,
					seed_19 = 5,
					seed_20 = 5)

	if run_material_module:
		create_material.create_material(model_name,
						part_name,
						material_user,
						material_GH4169
						)

	if run_assembly_module:
		instance_name = create_assembly.create_assembly(model_name,
										part_name,
										instance_name
										)

	if run_step_module:
		step_name = create_step.create_step(model_name,
								part_name,
								step_name,
								timePeriod,
								maxNumInc,
								initialInc,
								minInc,
								maxInc
								)

	if run_load_module:
		create_load.create_load(model_name,
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
					)

	if run_job_module:
		create_job.create_job(model_name,
					part_name,
					umat_filename,
					job_name,
					write_input,
					input_filename,
					write_cae,
					cae_filename,
					submit_job,
					)
		
	# p = mdb.models[model_name].parts[part_name]
	# session.viewports['Viewport: 1'].setValues(displayedObject=p)
	# session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
	# session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
	#     meshTechnique=ON)
	# session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
	#     referenceRepresentation=OFF)
	# session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
	# session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
	# session.viewports['Viewport: 1'].view.setValues(nearPlane=418.093, 
	#     farPlane=454.107, width=32.1041, height=21.845, cameraPosition=(-0.933243, 
	#     -1.49707, 436.1), cameraTarget=(-0.933243, -1.49707, 3.05176e-005))