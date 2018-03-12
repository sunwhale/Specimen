from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _rsgTmp001_DB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Create Specimen',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        TabBook_2 = FXTabBook(p=self, tgt=None, sel=0,
            opts=TABBOOK_NORMAL,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_2, text='Part', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_2 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_2, text='Note: Create the part of the tubular specimen.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_2, text='Create parts', tgt=form.run_part_moduleKw, sel=0)
        HFrame_2 = FXHorizontalFrame(p=TabItem_2, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_5 = FXGroupBox(p=HFrame_2, text='Parameters', opts=FRAME_GROOVE)
        VAligner_3 = AFXVerticalAligner(p=GroupBox_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Gauge Length:', tgt=form.gauge_lengthKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Specimen Length:', tgt=form.specimen_lengthKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Grip Length:', tgt=form.grip_lengthKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Inner Radius:', tgt=form.inner_radiusKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Outer Radius:', tgt=form.outer_radiusKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Outer Radius in Gauge Length:', tgt=form.outer_radius_in_gauge_lengthKw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='R1:', tgt=form.R1Kw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='R2:', tgt=form.R2Kw, sel=0)
        AFXTextField(p=VAligner_3, ncols=12, labelText='Theta:', tgt=form.thetaKw, sel=0)
        GroupBox_4 = FXGroupBox(p=HFrame_2, text='Schematic', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, '1.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_4, text='', ic=icon)
        tabItem = FXTabItem(p=TabBook_2, text='Mesh', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_3, text='Note: Create mesh of the tubular specimen.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_3, text='Create mesh', tgt=form.run_mesh_moduleKw, sel=0)
        HFrame_4 = FXHorizontalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_7 = FXGroupBox(p=HFrame_4, text='Seeds of the mesh', opts=FRAME_GROOVE)
        VAligner_4 = AFXVerticalAligner(p=GroupBox_7, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=128, pt=0, pb=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 1:', tgt=form.seed_1Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 2:', tgt=form.seed_2Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 3:', tgt=form.seed_3Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 4:', tgt=form.seed_4Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 5:', tgt=form.seed_5Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 6:', tgt=form.seed_6Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 7:', tgt=form.seed_7Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 8:', tgt=form.seed_8Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 9:', tgt=form.seed_9Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 10:', tgt=form.seed_10Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 11:', tgt=form.seed_11Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 12:', tgt=form.seed_12Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 13:', tgt=form.seed_13Kw, sel=0)
        AFXTextField(p=VAligner_4, ncols=12, labelText='Seed 14:', tgt=form.seed_14Kw, sel=0)
        GroupBox_6 = FXGroupBox(p=HFrame_4, text='Schematic', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, '2.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_6, text='', ic=icon)
        tabItem = FXTabItem(p=TabBook_2, text='Material', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_4, text='Note: Create materials and sections.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_4, text='Define materials', tgt=form.run_material_moduleKw, sel=0)
        HFrame_7 = FXHorizontalFrame(p=TabItem_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_10 = FXGroupBox(p=HFrame_7, text='Parameters', opts=FRAME_GROOVE)
        VAligner_6 = AFXVerticalAligner(p=GroupBox_10, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXCheckButton(p=GroupBox_10, text='GH4169', tgt=form.material_GH4169Kw, sel=0)
        FXCheckButton(p=GroupBox_10, text='User defined material', tgt=form.material_userKw, sel=0)
        fileHandler = _rsgTmp001_DBFileHandler(form, 'umat_filename', 'All files (*)')
        fileTextHf = FXHorizontalFrame(p=GroupBox_10, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=50, labelText='File name:', tgt=form.umat_filenameKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        tabItem = FXTabItem(p=TabBook_2, text='Assembly', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_8 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_8, text='Note: Create assembly.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_8, text='Create assembly', tgt=form.run_assembly_moduleKw, sel=0)
        tabItem = FXTabItem(p=TabBook_2, text='Step', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_5 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_5, text='Note: Create steps.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_5, text='Create steps', tgt=form.run_step_moduleKw, sel=0)
        HFrame_6 = FXHorizontalFrame(p=TabItem_5, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_9 = FXGroupBox(p=HFrame_6, text='Parameters', opts=FRAME_GROOVE)
        VAligner_5 = AFXVerticalAligner(p=GroupBox_9, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_5, ncols=12, labelText='Time period:', tgt=form.timePeriodKw, sel=0)
        AFXTextField(p=VAligner_5, ncols=12, labelText='Maximum number of increments:', tgt=form.maxNumIncKw, sel=0)
        AFXTextField(p=VAligner_5, ncols=12, labelText='Initial increment size:', tgt=form.initialIncKw, sel=0)
        AFXTextField(p=VAligner_5, ncols=12, labelText='Minimum increment size:', tgt=form.minIncKw, sel=0)
        AFXTextField(p=VAligner_5, ncols=12, labelText='Maximum increment size:', tgt=form.maxIncKw, sel=0)
        tabItem = FXTabItem(p=TabBook_2, text='Load', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_6 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_6, text='Note: Create loads.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_6, text='Define loads', tgt=form.run_load_moduleKw, sel=0)
        HFrame_5 = FXHorizontalFrame(p=TabItem_6, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_8 = FXGroupBox(p=HFrame_5, text='Parameters', opts=FRAME_GROOVE)
        VAligner_12 = AFXVerticalAligner(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Loading cycles:', tgt=form.loading_cyclesKw, sel=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Displacement:', tgt=form.displacement_valueKw, sel=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Rotation(rad):', tgt=form.rotation_valueKw, sel=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Force:', tgt=form.force_valueKw, sel=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Torque:', tgt=form.torque_valueKw, sel=0)
        AFXTextField(p=VAligner_12, ncols=12, labelText='Temperature:', tgt=form.temperature_valueKw, sel=0)
        HFrame_12 = FXHorizontalFrame(p=GroupBox_8, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXCheckButton(p=HFrame_12, text='Displacement', tgt=form.add_displacementKw, sel=0)
        FXCheckButton(p=HFrame_12, text='Rotation', tgt=form.add_rotationKw, sel=0)
        FXCheckButton(p=HFrame_12, text='Force', tgt=form.add_forceKw, sel=0)
        FXCheckButton(p=HFrame_12, text='Torque', tgt=form.add_torqueKw, sel=0)
        FXCheckButton(p=HFrame_12, text='Temperature', tgt=form.add_temperatureKw, sel=0)
        if isinstance(GroupBox_8, FXHorizontalFrame):
            FXVerticalSeparator(p=GroupBox_8, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        else:
            FXHorizontalSeparator(p=GroupBox_8, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=2, pb=2)
        l = FXLabel(p=GroupBox_8, text='Amplitudes:', opts=JUSTIFY_LEFT)
        vf = FXVerticalFrame(GroupBox_8, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X,
            0,0,0,0, 0,0,0,0)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        vf.setSelector(99)
        table = AFXTable(vf, 6, 7, 6, 7, form.loading_conditionsKw, 0, AFXTABLE_EDITABLE|LAYOUT_FILL_X)
        table.setPopupOptions(AFXTable.POPUP_CUT|AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS|AFXTable.POPUP_READ_FROM_FILE|AFXTable.POPUP_WRITE_TO_FILE)
        table.setLeadingRows(1)
        table.setLeadingColumns(1)
        table.setColumnWidth(1, 100)
        table.setColumnType(1, AFXTable.FLOAT)
        table.setColumnWidth(2, 100)
        table.setColumnType(2, AFXTable.FLOAT)
        table.setColumnWidth(3, 100)
        table.setColumnType(3, AFXTable.FLOAT)
        table.setColumnWidth(4, 100)
        table.setColumnType(4, AFXTable.FLOAT)
        table.setColumnWidth(5, 100)
        table.setColumnType(5, AFXTable.FLOAT)
        table.setColumnWidth(6, 100)
        table.setColumnType(6, AFXTable.FLOAT)
        table.setLeadingRowLabels('Time\tDisplacement\tRoatation\tForce\tTorque\tTemperature')
        table.setStretchableColumn( table.getNumColumns()-1 )
        table.showHorizontalGrid(True)
        table.showVerticalGrid(True)
        tabItem = FXTabItem(p=TabBook_2, text='Job', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_7 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        l = FXLabel(p=TabItem_7, text='Note: Create jobs.', opts=JUSTIFY_LEFT)
        l.setFont( getAFXFont(FONT_BOLD) )
        FXCheckButton(p=TabItem_7, text='Create jobs', tgt=form.run_job_moduleKw, sel=0)
        HFrame_8 = FXHorizontalFrame(p=TabItem_7, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_11 = FXGroupBox(p=HFrame_8, text='Parameters', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='Job name:', tgt=form.job_nameKw, sel=0)
        FXCheckButton(p=GroupBox_11, text='Write the input file', tgt=form.write_inputKw, sel=0)
        FXCheckButton(p=GroupBox_11, text='Save the cae file as:', tgt=form.write_caeKw, sel=0)
        fileHandler = _rsgTmp001_DBFileHandler(form, 'cae_filename', '*.cae')
        fileTextHf = FXHorizontalFrame(p=GroupBox_11, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        fileTextHf.setSelector(99)
        AFXTextField(p=fileTextHf, ncols=50, labelText='File name:', tgt=form.cae_filenameKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        FXCheckButton(p=GroupBox_11, text='Submit', tgt=form.submit_jobKw, sel=0)


###########################################################################
# Class definition
###########################################################################

class _rsgTmp001_DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, _rsgTmp001_DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
