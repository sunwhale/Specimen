from abaqus import *
from abaqusConstants import *
import numpy as np

###########################################################################
# Function definition
###########################################################################

def create_sketch(model_name,
				  part_name,
				  gauge_length = 35.0,
				  specimen_length = 180.0,
				  grip_length = 60.0,
				  inner_radius = 5.0,
				  outer_radius_in_gauge_length = 6.0,
				  outer_radius = 8.0,
				  R1 = 1.0,
				  R2 = 0.2,
				  theta = 18.0):

	print 'create_sketch'

	l = outer_radius_in_gauge_length * np.deg2rad(theta)

	# Sketch-1

	gauge_and_transition_length = specimen_length - 2*grip_length
	point_A = np.array([outer_radius_in_gauge_length,gauge_length/2])
	point_B = np.array([outer_radius,gauge_and_transition_length/2])
	point_D = np.array([outer_radius,gauge_length/2])

	length_AB = np.linalg.norm(point_A-point_B)
	length_AD = np.linalg.norm(point_A-point_D)
	length_AC = length_AB*length_AB/length_AD/2
	transition_radius = length_AC

	s1 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200.0)
	g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
	s1.setPrimaryObject(option=STANDALONE)
	s1.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
	s1.FixedConstraint(entity=g[2])

	s1.Spot(point=(inner_radius, specimen_length/2))
	s1.Spot(point=(outer_radius, specimen_length/2))
	s1.Spot(point=(outer_radius, gauge_and_transition_length/2))
	s1.Spot(point=(outer_radius_in_gauge_length/2, gauge_length/2))
	s1.Spot(point=(outer_radius_in_gauge_length/2, 0.0))
	s1.Spot(point=(outer_radius_in_gauge_length/2, -gauge_length/2))
	s1.Spot(point=(outer_radius, -gauge_and_transition_length/2))
	s1.Spot(point=(outer_radius, -specimen_length/2))
	s1.Spot(point=(inner_radius, -specimen_length/2))

	s1.Line(point1=(outer_radius, gauge_and_transition_length/2), point2=(outer_radius, specimen_length/2))
	s1.VerticalConstraint(entity=g[3], addUndoState=False)

	s1.Line(point1=(outer_radius, specimen_length/2), point2=(inner_radius, specimen_length/2))
	s1.HorizontalConstraint(entity=g[4], addUndoState=False)
	s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)

	s1.Line(point1=(inner_radius, specimen_length/2), point2=(inner_radius, -specimen_length/2))
	s1.VerticalConstraint(entity=g[5], addUndoState=False)
	s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)

	s1.Line(point1=(inner_radius, -specimen_length/2), point2=(outer_radius, -specimen_length/2))
	s1.HorizontalConstraint(entity=g[6], addUndoState=False)
	s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)

	s1.Line(point1=(outer_radius, -specimen_length/2), point2=(outer_radius, -gauge_and_transition_length/2))
	s1.VerticalConstraint(entity=g[7], addUndoState=False)
	s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)

	s1.Line(point1=(outer_radius_in_gauge_length, gauge_length/2), point2=(outer_radius_in_gauge_length, -gauge_length/2))
	s1.VerticalConstraint(entity=g[8], addUndoState=False)

	s1.ArcByCenterEnds(center=(transition_radius+outer_radius, gauge_length/2), 
		point1=(outer_radius_in_gauge_length, gauge_length/2), 
		point2=(outer_radius, gauge_and_transition_length/2), direction=CLOCKWISE)

	s1.ArcByCenterEnds(center=(transition_radius+outer_radius, -gauge_length/2), 
		point1=(outer_radius_in_gauge_length, -gauge_length/2), 
		point2=(outer_radius, -gauge_and_transition_length/2), direction=COUNTERCLOCKWISE)

	s1.DistanceDimension(entity1=g[2], entity2=g[5], textPoint=(-20, 
	    -30), value=inner_radius)
	s1.DistanceDimension(entity1=g[2], entity2=g[8], textPoint=(-10, 
	    -10), value=outer_radius_in_gauge_length)
	s1.DistanceDimension(entity1=g[2], entity2=g[3], textPoint=(-10, 
	    20), value=outer_radius)
	s1.DistanceDimension(entity1=g[2], entity2=g[7], textPoint=(-10, 
	    -20), value=outer_radius)
	s1.ObliqueDimension(vertex1=v[13], vertex2=v[14], textPoint=(-10, 
	    -5), value=specimen_length)
	s1.ObliqueDimension(vertex1=v[9], vertex2=v[10], textPoint=(10, 
	    20), value=grip_length)
	s1.ObliqueDimension(vertex1=v[19], vertex2=v[20], textPoint=(20, 
	    5), value=gauge_length)
	s1.ObliqueDimension(vertex1=v[17], vertex2=v[18], textPoint=(10, 
	    -20), value=grip_length)

	s1.Spot(point=(0.0, 0.0))
	s1.CoincidentConstraint(entity1=v[21], entity2=v[2])
	s1.CoincidentConstraint(entity1=v[23], entity2=v[6])
	s1.FixedConstraint(entity=v[25])
	s1.EqualDistanceConstraint(entity1=v[19], entity2=v[20], midpoint=v[25])
	s1.EqualDistanceConstraint(entity1=v[0], entity2=v[8], midpoint=v[25])

	s1.TangentConstraint(entity1=g[8], entity2=g[9])
	s1.TangentConstraint(entity1=g[8], entity2=g[10])

	mdb.models[model_name].sketches.changeKey(fromName='__profile__', 
	    toName='Sketch-1')
	s1.unsetPrimaryObject()

	# Sketch-2

	s2 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200.0)
	g, v, d, c = s2.geometry, s2.vertices, s2.dimensions, s2.constraints
	s2.setPrimaryObject(option=STANDALONE)
	s2.Spot(point=(0.0, 0.0))
	s2.Spot(point=(-10.0, 5.0))
	s2.Spot(point=(-10.0, -5.0))
	s2.Spot(point=(-20.0, 5.0))
	s2.Spot(point=(-20.0, -5.0))
	s2.Spot(point=(-20.0, 0.0))
	s2.ArcByCenterEnds(center=(0.0, 0.0), point1=(-10.0, -5.0), point2=(-10.0, 5.0), 
	    direction=COUNTERCLOCKWISE)
	s2.Line(point1=(-10.0, 5.0), point2=(-20.0, 5.0))
	s2.HorizontalConstraint(entity=g[3], addUndoState=False)
	s2.Line(point1=(-10.0, -5.0), point2=(-20.0, -5.0))
	s2.HorizontalConstraint(entity=g[4], addUndoState=False)
	s2.ArcByCenterEnds(center=(-20.0, 0.0), point1=(-20.0, 5.0), point2=(-20.0, 
	    -5.0), direction=COUNTERCLOCKWISE)
	s2.FixedConstraint(entity=v[0])
	s2.EqualDistanceConstraint(entity1=v[1], entity2=v[2], midpoint=v[0])
	s2.EqualDistanceConstraint(entity1=v[3], entity2=v[4], midpoint=v[0])
	s2.RadialDimension(curve=g[2], textPoint=(10, 10), 
	    radius=11.1803398874989)
	s2.ObliqueDimension(vertex1=v[9], vertex2=v[10], textPoint=(-10, 
	    10), value=10.0)
	s2.RadialDimension(curve=g[5], textPoint=(-30, 10), 
	    radius=5.0)
	s2.TangentConstraint(entity1=g[3], entity2=g[5])
	s2.TangentConstraint(entity1=g[4], entity2=g[5])

	d[0].setValues(value=R1, )
	d[1].setValues(value=l, )
	d[2].setValues(value=R2, )

	mdb.models[model_name].sketches.changeKey(fromName='__profile__', 
	    toName='Sketch-2')
	s2.unsetPrimaryObject()

	# Sketch-3

	s3 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200.0)
	g, v, d, c = s3.geometry, s3.vertices, s3.dimensions, s3.constraints
	s3.setPrimaryObject(option=STANDALONE)
	s3.Spot(point=(0.0, 0.0))
	s3.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(10.0, 0.0))
	s3.FixedConstraint(entity=v[0])
	s3.RadialDimension(curve=g[2], textPoint=(10, 10), 
	    radius=10.0)
	d[0].setValues(value=R1, )
	mdb.models[model_name].sketches.changeKey(fromName='__profile__', 
	    toName='Sketch-3')
	s3.unsetPrimaryObject()

	# Sketch-4

	s4 = mdb.models[model_name].ConstrainedSketch(name='__profile__', 
	    sheetSize=200.0)
	g, v, d, c = s4.geometry, s4.vertices, s4.dimensions, s4.constraints
	s4.setPrimaryObject(option=STANDALONE)
	s4.Spot(point=(0.0, 0.0))
	s4.Spot(point=(0.0, 5.0))
	s4.Spot(point=(10.0, 5.0))
	s4.Spot(point=(10.0, -5.0))
	s4.Spot(point=(0.0, -5.0))
	s4.ArcByCenterEnds(center=(0.0, 0.0), point1=(0.0, -5.0), point2=(0.0, 5.0), 
	    direction=CLOCKWISE)
	s4.Line(point1=(0.0, 5.0), point2=(10.0, 5.0))
	s4.HorizontalConstraint(entity=g[3], addUndoState=False)
	s4.Line(point1=(10.0, 5.0), point2=(10.0, -5.0))
	s4.VerticalConstraint(entity=g[4], addUndoState=False)
	s4.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
	s4.Line(point1=(10.0, -5.0), point2=(0.0, -5.0))
	s4.HorizontalConstraint(entity=g[5], addUndoState=False)
	s4.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
	s4.FixedConstraint(entity=v[0])
	s4.RadialDimension(curve=g[2], textPoint=(-10, 10), 
	    radius=5.0)
	s4.ObliqueDimension(vertex1=v[8], vertex2=v[9], textPoint=(5, 
	    10), value=10.0)
	s4.TangentConstraint(entity1=g[2], entity2=g[3])
	s4.TangentConstraint(entity1=g[2], entity2=g[5])

	d[0].setValues(value=R2, )
	d[1].setValues(value=l, )

	mdb.models[model_name].sketches.changeKey(fromName='__profile__', 
	    toName='Sketch-4')
	s4.unsetPrimaryObject()