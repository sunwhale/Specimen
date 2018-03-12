from abaqus import *
from abaqusConstants import *
import numpy as np

###########################################################################
# Function definition
###########################################################################

def create_part(model_name,
				part_name,
				gauge_length = 35.0,
				specimen_length = 180.0,
				grip_length = 60.0,
				inner_radius = 5.0,
				outer_radius_in_gauge_length = 6.0,
				outer_radius = 8.0,
				R1 = 1.0,
				R2 = 0.2,
				theta = 18.0
				):

	print 'create_part'

	# create specimen
	
	p = mdb.models[model_name].Part(name=part_name, dimensionality=THREE_D, 
	    type=DEFORMABLE_BODY)
	s = mdb.models[model_name].sketches['Sketch-1']
	p.BaseSolidRevolve(sketch=s, angle=360.0, flipRevolveDirection=OFF)

	# create the hole on one side by Sketch-3

	p = mdb.models[model_name].parts[part_name]
	p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=0.0)

	d1 = p.datums
	t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=d1[1], 
	    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
	s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200, gridSpacing=10, transform=t)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=SUPERIMPOSE)

	p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
	s1.retrieveSketch(sketch=mdb.models[model_name].sketches['Sketch-3'])

	d2 = p.datums
	p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=d2[1], sketchPlaneSide=SIDE1, 
	    sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=OFF)
	s1.unsetPrimaryObject()
	del mdb.models[model_name].sketches['__profile__']

	# create the hole on the other side by Sketch-3

	p = mdb.models[model_name].parts[part_name]

	d1 = p.datums
	t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=d1[1], 
	    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
	s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200, gridSpacing=10, transform=t)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=SUPERIMPOSE)

	p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
	s1.retrieveSketch(sketch=mdb.models[model_name].sketches['Sketch-3'])

	d2 = p.datums
	p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=d2[1], sketchPlaneSide=SIDE1, 
	    sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=ON)
	s1.unsetPrimaryObject()
	del mdb.models[model_name].sketches['__profile__']

	# 

	p = mdb.models[model_name].parts[part_name]
	d = p.datums
	p.DatumPlaneByRotation(plane=d[2], axis=d[1], angle=theta)

	# create the crack on one side by Sketch-4

	p = mdb.models[model_name].parts[part_name]
	d1 = p.datums
	t = p.MakeSketchTransform(sketchPlane=d1[5], sketchUpEdge=d1[1], 
	    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
	s = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200, gridSpacing=10, transform=t)
	g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
	s.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models[model_name].parts[part_name]
	p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
	s.retrieveSketch(sketch=mdb.models[model_name].sketches['Sketch-4'])
	p = mdb.models[model_name].parts[part_name]
	d2 = p.datums
	p.CutExtrude(sketchPlane=d2[5], sketchUpEdge=d2[1], sketchPlaneSide=SIDE1, 
	    sketchOrientation=RIGHT, sketch=s, flipExtrudeDirection=OFF)
	s.unsetPrimaryObject()
	del mdb.models[model_name].sketches['__profile__']

	# create the hole on the other side by Sketch-4

	p = mdb.models[model_name].parts[part_name]
	d1 = p.datums
	t = p.MakeSketchTransform(sketchPlane=d1[5], sketchUpEdge=d1[1], 
	    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
	s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200, gridSpacing=10, transform=t)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=SUPERIMPOSE)
	p = mdb.models[model_name].parts[part_name]
	p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
	s1.retrieveSketch(sketch=mdb.models[model_name].sketches['Sketch-4'])
	s1.mirror(mirrorLine=g[2], objectList=(g[5], g[6], g[7], g[8], v[0], v[1], 
	    v[2], v[3], v[4]))
	p = mdb.models[model_name].parts[part_name]
	d2 = p.datums
	p.CutExtrude(sketchPlane=d2[5], sketchUpEdge=d2[1], sketchPlaneSide=SIDE1, 
	    sketchOrientation=RIGHT, sketch=s1, flipExtrudeDirection=ON)
	s1.unsetPrimaryObject()
	del mdb.models[model_name].sketches['__profile__']

    # create datums

	p = mdb.models[model_name].parts[part_name]
	d = p.datums
	p.DatumPlaneByRotation(plane=d[2], axis=d[1], angle=45.0)
	p.DatumPlaneByRotation(plane=d[2], axis=d[1], angle=90.0)
	p.DatumPlaneByRotation(plane=d[2], axis=d[1], angle=90.0+theta)
	p.DatumPlaneByRotation(plane=d[2], axis=d[1], angle=135.0)
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(specimen_length/2.0 - grip_length))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(gauge_length/2.0))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(outer_radius))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(R1*2.0))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(0.0))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(-R1*2.0))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(-outer_radius))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(-gauge_length/2.0))
	p.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=float(-(specimen_length/2.0 - grip_length)))

	# create partitions

	p = mdb.models[model_name].parts[part_name]
	d1 = p.datums
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[2], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[5], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[8], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[9], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[10], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[11], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[12], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[13], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[14], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[15], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[16], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[17], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[18], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[19], cells=c)
	c = p.cells
	p.PartitionCellByDatumPlane(datumPlane=d1[20], cells=c)
	c = p.cells