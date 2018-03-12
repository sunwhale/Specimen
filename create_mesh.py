from abaqus import *
from abaqusConstants import *
import mesh

###########################################################################
# Function definition
###########################################################################

def create_mesh(model_name,
				part_name,
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
				seed_20 = 5):
	
	print 'create_mesh'

	p = mdb.models[model_name].parts[part_name]
	e = p.edges

	# seed_1 = 5
	# seed_2 = 5
	# seed_3 = 5
	# seed_4 = 5
	# seed_5 = 1
	# seed_6 = 5
	# seed_7 = 5
	# seed_8 = 5
	# seed_9 = 5
	# seed_10 = 5
	# seed_11 = 5
	# seed_12 = 5
	# seed_13 = 5
	# seed_14 = 5

	p.seedPart(size=0.5, deviationFactor=0.1, minSizeFactor=0.1)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #8 #40000000 #0 #200 #800000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_1, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #800 #0:3 #1000 #0:7 #41000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_2, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #400 #0:3 #2000 #0:7 #4800 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_3, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #20000 #0 #1044000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_4, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:19 #440000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_5, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #10 #20000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_6, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #1 #4 #8 #80 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_7, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:6 #10000000:2 #0:3 #8800 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_8, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #4 #0:2 #400 #400000 #0 #1000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_9, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:7 #2000008 #0:3 #4000000 #10 ]', ), 
	    )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_10, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #200 #0 #820000 #0:4 #40 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_11, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:5 #80000000 #0 #8000 #0:2 #410000 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_12, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #8000 #0 #208400 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_13, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=('[#0:8 #10000 #200 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=seed_14, constraint=FINER)


	pickedEdges = e.getSequenceFromMask(mask=(
	    '[#0 #5aad56d0 #4d56ab5 #d5000000 #17bdef6 #30000000 #81860301', 
	    ' #703 #82 #0:5 #1458aa00 #52505 #5dddda00 #a0000000', 
	    ' #366cd9b4 #243085b7 #251a0108 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=2, constraint=FINER)

	pickedEdges = e.getSequenceFromMask(mask=(
	    '[#0:5 #46800000 #2a28542a #54 #8304100 #2 #0:2', 
	    ' #2a154680 #15155 #c3000000 #90 ]', ), )
	p.seedEdgeByNumber(edges=pickedEdges, number=4, constraint=FINER)

	elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
	elemType2 = mesh.ElemType(elemCode=C3D15, elemLibrary=STANDARD)
	elemType3 = mesh.ElemType(elemCode=C3D10, elemLibrary=STANDARD)
	c = p.cells
	pickedRegions =(c, )
	p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
	    elemType3))
	p.generateMesh()