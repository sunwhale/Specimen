from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class _rsgTmp001_Form(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='create_specimen',
            objectName='kernel', registerQuery=False)
        pickedDefault = ''
        self.run_part_moduleKw = AFXBoolKeyword(self.cmd, 'run_part_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.gauge_lengthKw = AFXFloatKeyword(self.cmd, 'gauge_length', True, 35.0)
        self.specimen_lengthKw = AFXFloatKeyword(self.cmd, 'specimen_length', True, 180.0)
        self.grip_lengthKw = AFXFloatKeyword(self.cmd, 'grip_length', True, 60.0)
        self.inner_radiusKw = AFXFloatKeyword(self.cmd, 'inner_radius', True, 5.0)
        self.outer_radiusKw = AFXFloatKeyword(self.cmd, 'outer_radius', True, 8.0)
        self.outer_radius_in_gauge_lengthKw = AFXFloatKeyword(self.cmd, 'outer_radius_in_gauge_length', True, 6.0)
        self.R1Kw = AFXFloatKeyword(self.cmd, 'R1', True, 1.0)
        self.R2Kw = AFXFloatKeyword(self.cmd, 'R2', True, 0.2)
        self.thetaKw = AFXFloatKeyword(self.cmd, 'theta', True, 18.0)
        self.run_mesh_moduleKw = AFXBoolKeyword(self.cmd, 'run_mesh_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.seed_1Kw = AFXIntKeyword(self.cmd, 'seed_1', True, 30)
        self.seed_2Kw = AFXIntKeyword(self.cmd, 'seed_2', True, 15)
        self.seed_3Kw = AFXIntKeyword(self.cmd, 'seed_3', True, 15)
        self.seed_4Kw = AFXIntKeyword(self.cmd, 'seed_4', True, 15)
        self.seed_5Kw = AFXIntKeyword(self.cmd, 'seed_5', True, 4)
        self.seed_6Kw = AFXIntKeyword(self.cmd, 'seed_6', True, 15)
        self.seed_7Kw = AFXIntKeyword(self.cmd, 'seed_7', True, 15)
        self.seed_8Kw = AFXIntKeyword(self.cmd, 'seed_8', True, 15)
        self.seed_9Kw = AFXIntKeyword(self.cmd, 'seed_9', True, 15)
        self.seed_10Kw = AFXIntKeyword(self.cmd, 'seed_10', True, 15)
        self.seed_11Kw = AFXIntKeyword(self.cmd, 'seed_11', True, 15)
        self.seed_12Kw = AFXIntKeyword(self.cmd, 'seed_12', True, 15)
        self.seed_13Kw = AFXIntKeyword(self.cmd, 'seed_13', True, 15)
        self.seed_14Kw = AFXIntKeyword(self.cmd, 'seed_14', True, 15)
        self.run_material_moduleKw = AFXBoolKeyword(self.cmd, 'run_material_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.material_GH4169Kw = AFXBoolKeyword(self.cmd, 'material_GH4169', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.material_userKw = AFXBoolKeyword(self.cmd, 'material_user', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.umat_filenameKw = AFXStringKeyword(self.cmd, 'umat_filename', True, '')
        self.run_assembly_moduleKw = AFXBoolKeyword(self.cmd, 'run_assembly_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.run_step_moduleKw = AFXBoolKeyword(self.cmd, 'run_step_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.timePeriodKw = AFXFloatKeyword(self.cmd, 'timePeriod', True, 1)
        self.maxNumIncKw = AFXIntKeyword(self.cmd, 'maxNumInc', True, 10000)
        self.initialIncKw = AFXFloatKeyword(self.cmd, 'initialInc', True, 0.1)
        self.minIncKw = AFXFloatKeyword(self.cmd, 'minInc', True, 0.00001)
        self.maxIncKw = AFXFloatKeyword(self.cmd, 'maxInc', True, 1)
        self.run_load_moduleKw = AFXBoolKeyword(self.cmd, 'run_load_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.loading_cyclesKw = AFXIntKeyword(self.cmd, 'loading_cycles', True, 20)
        self.displacement_valueKw = AFXFloatKeyword(self.cmd, 'displacement_value', True, 1)
        self.rotation_valueKw = AFXFloatKeyword(self.cmd, 'rotation_value', True, 0.1)
        self.force_valueKw = AFXFloatKeyword(self.cmd, 'force_value', True, 1)
        self.torque_valueKw = AFXFloatKeyword(self.cmd, 'torque_value', True, 1)
        self.temperature_valueKw = AFXFloatKeyword(self.cmd, 'temperature_value', True, 1)
        self.add_displacementKw = AFXBoolKeyword(self.cmd, 'add_displacement', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.add_rotationKw = AFXBoolKeyword(self.cmd, 'add_rotation', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.add_forceKw = AFXBoolKeyword(self.cmd, 'add_force', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.add_torqueKw = AFXBoolKeyword(self.cmd, 'add_torque', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.add_temperatureKw = AFXBoolKeyword(self.cmd, 'add_temperature', AFXBoolKeyword.TRUE_FALSE, True, False)
        self.loading_conditionsKw = AFXTableKeyword(self.cmd, 'loading_conditions', True)
        self.loading_conditionsKw.setColumnType(0, AFXTABLE_TYPE_FLOAT)
        self.loading_conditionsKw.setColumnType(1, AFXTABLE_TYPE_FLOAT)
        self.loading_conditionsKw.setColumnType(2, AFXTABLE_TYPE_FLOAT)
        self.loading_conditionsKw.setColumnType(3, AFXTABLE_TYPE_FLOAT)
        self.loading_conditionsKw.setColumnType(4, AFXTABLE_TYPE_FLOAT)
        self.loading_conditionsKw.setColumnType(5, AFXTABLE_TYPE_FLOAT)
        self.run_job_moduleKw = AFXBoolKeyword(self.cmd, 'run_job_module', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.job_nameKw = AFXStringKeyword(self.cmd, 'job_name', True, 'Job-1')
        self.write_inputKw = AFXBoolKeyword(self.cmd, 'write_input', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.write_caeKw = AFXBoolKeyword(self.cmd, 'write_cae', AFXBoolKeyword.TRUE_FALSE, True, True)
        self.cae_filenameKw = AFXStringKeyword(self.cmd, 'cae_filename', True, '')
        self.submit_jobKw = AFXBoolKeyword(self.cmd, 'submit_job', AFXBoolKeyword.TRUE_FALSE, True, False)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _rsgTmp001_DB
        return _rsgTmp001_DB._rsgTmp001_DB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def deactivate(self):
    
        try:
            osutils.remove(os.path.join('c:\\Users\\Z620\\abaqus_plugins\\Specimen', '_rsgTmp001_DB.py'), force=True )
            osutils.remove(os.path.join('c:\\Users\\Z620\\abaqus_plugins\\Specimen', '_rsgTmp001_DB.pyc'), force=True )
        except:
            pass
        try:
            osutils.remove(os.path.join('c:\\Users\\Z620\\abaqus_plugins\\Specimen', '_rsgTmp001_Form.py'), force=True )
            osutils.remove(os.path.join('c:\\Users\\Z620\\abaqus_plugins\\Specimen', '_rsgTmp001_Form.pyc'), force=True )
        except:
            pass
        AFXForm.deactivate(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getCommandString(self):

        cmds = 'import kernel\n'
        cmds += AFXForm.getCommandString(self)
        return cmds

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
