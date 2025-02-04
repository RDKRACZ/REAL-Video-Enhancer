#This script creates a class that takes in params like "RealESRGAN or Rife", the model for the program,  the times of upscaling, and the path of the video, and the output path
# hz
import src.return_data as return_data
import os
from src.settings import *
from threading import Thread
import src.runAI.transition_detection
from src.return_data import *
from src.messages import *
from src.discord_rpc import *
import os
from modules.commands import *
import src.thisdir
import modules.interpolate as interpolate
import src.onProgramStart as onProgramStart
from src.log import *
thisdir = src.thisdir.thisdir()
homedir = os.path.expanduser(r"~")


def modelOptions(self):
    self.times=2
    log('Model: IFRNET')
    self.render='rife'
    self.ui.Rife_Model.clear()
    self.ui.Rife_Times.clear()
    self.ui.FPSPreview.setText('FPS:')
    
    self.ui.Rife_Times.addItem('2X')

    self.ui.Rife_Times.currentIndexChanged.connect(self.showChangeInFPS)
    try:
        self.ui.Rife_Model.currentIndexChanged.disconnect()
    except:
        pass
    self.ui.Rife_Times.setCurrentIndex(0)
    self.ui.denoiseLevelLabel.hide()
    self.ui.denoiseLevelSpinBox.hide()
    self.showChangeInFPS()
    try:
        self.ui.RifeStart.clicked.disconnect() 
    except:
        pass
    self.ui.Rife_Model.addItems(self.get_models_from_dir('ifrnet'))
    self.ui.RifeStart.clicked.connect(lambda: interpolate.start_interpolation(self,'ifrnet-ncnn-vulkan'))