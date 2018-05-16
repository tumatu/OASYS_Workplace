import sys, numpy
import orangecanvas.resources as resources
import matplotlib.pyplot as plt
from oasys.widgets import gui as oasysgui
from oasys.widgets import congruence
from orangewidget import gui, widget
from orangewidget.settings import Setting
from oasys.util.oasys_util import EmittingStream
from pprint import pprint
import os.path

from orangecontrib.shadow.util.shadow_util import ShadowCongruence, ShadowPlot
from orangecontrib.shadow.util.shadow_objects import ShadowBeam, ShadowTriggerIn

from PyQt5.QtGui import QImage, QPixmap,  QPalette, QFont, QColor, QTextCursor
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QMessageBox

from orangecontrib.shadow.widgets.gui.ow_automatic_element import AutomaticElement
import hybrid_control1

print((hybrid_control1.__file__))
from orangecontrib.shadow.widgets.special_elements import ow_hybrid_screen
from silx.gui.plot.ImageView import ImageView


#beam = in_object_2
#print(ShadowCongruence.checkGoodBeam(self.input_beam))
#pprint(vars(in_object_2))
self=ow_hybrid_screen.HybridScreen()
self.input_beam= in_object_2
self.workspace_units_to_cm=0
if ShadowCongruence.checkEmptyBeam(self.input_beam):
    if ShadowCongruence.checkGoodBeam(self.input_beam):
        
        #sys.stdout = EmittingStream(textWritten=self.write_stdout)
        #print('1')
        self.check_fields()
        self.ghy_calcType=1
        self.ghy_distance=20
        self.ghy_focallength=20
        print('self.ghy_nbins_x',self.ghy_nbins_x)
        print('self.ghy_nbins_z',self.ghy_nbins_z)
        print('self.ghy_npeak',self.ghy_npeak)
        print('self.ghy_fftnpts',self.ghy_fftnpts)
        input_parameters = hybrid_control1.HybridInputParameters()
        #input_parameters.ghy_lengthunit = self.workspace_units
        input_parameters.widget = self
        input_parameters.shadow_beam = self.input_beam
        input_parameters.ghy_diff_plane = self.ghy_diff_plane + 1
        input_parameters.ghy_calcType = self.ghy_calcType + 1
        print('input_parameters.ghy_calcType',input_parameters.ghy_calcType)
        
        if self.distance_to_image_calc == 0:
            input_parameters.ghy_distance = -1
        else:
            input_parameters.ghy_distance = self.ghy_distance

        if self.focal_length_calc == 0:
            input_parameters.ghy_focallength = -1
        else:
            input_parameters.ghy_focallength = self.ghy_focallength

        if self.ghy_calcType != 0:
            input_parameters.ghy_nf = self.ghy_nf
        else:
            input_parameters.ghy_nf = 0
        
        input_parameters.ghy_nbins_x = int(self.ghy_nbins_x)
        
        input_parameters.ghy_nbins_z = int(self.ghy_nbins_z)
        input_parameters.ghy_npeak = int(self.ghy_npeak)
        input_parameters.ghy_fftnpts = int(self.ghy_fftnpts)
        input_parameters.file_to_write_out = self.file_to_write_out
        
        input_parameters.ghy_automatic = self.ghy_automatic
        print('1111')
        calculation_parameters = hybrid_control1.hy_run(input_parameters)
        #hybrid_control1.aaaa()
        print('3333')
        self.ghy_focallength = input_parameters.ghy_focallength
        self.ghy_distance = input_parameters.ghy_distance
        self.ghy_nbins_x = int(input_parameters.ghy_nbins_x)
        self.ghy_nbins_z = int(input_parameters.ghy_nbins_z)
        self.ghy_npeak   = int(input_parameters.ghy_npeak)
        self.ghy_fftnpts = int(input_parameters.ghy_fftnpts)
        
        if self.ghy_automatic == 1:
            do_plot_x = not calculation_parameters.beam_not_cut_in_x
            do_plot_z = not calculation_parameters.beam_not_cut_in_z
            
        else:
            do_plot_x = True
            do_plot_z = True
        do_nf = input_parameters.ghy_nf == 1 and input_parameters.ghy_calcType > 1
        #print('1')
        if do_plot_x or do_plot_z:
            self.setStatusMessage("Plotting Results")
        if self.ghy_diff_plane == 1:
            if do_plot_z:
                if not do_nf:
                    #plt.plot(calculation_parameters.dif_zp.scale*1e7,(calculation_parameters.dif_zp.np_array))
                    ticket=calculation_parameters.ff_beam._beam.histo1(3, nbins=500, nolost=1, ref=23)
                    plt.plot(ticket['bin_path'],ticket['histogram_path'])
                    plt.show()
                    #plot_histo_hybrid11(self,88, calculation_parameters.dif_zp, 0, title=u"\u2206" + "Zp", xtitle=r'$\Delta$Zp [$\mu$rad]', ytitle=r'Arbitrary Units', var=6)
                    