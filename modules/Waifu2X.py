import src.return_data as return_data
import os
from src.settings import *
import src.runAI.transition_detection
from src.return_data import *
from src.messages import *
from src.discord_rpc import *
import os
from modules.commands import *
from cv2 import VideoCapture, CAP_PROP_FRAME_WIDTH, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FPS, CAP_PROP_FRAME_COUNT
import modules.upscale as upscale
import src.thisdir
from src.log import *
#this file changes the GUI aspects of the AI
thisdir = src.thisdir.thisdir()
homedir = os.path.expanduser(r"~")
def modelOptions(self):
    log('Model: Waifu2x')
    self.times=1
    self.render='esrgan'
    self.ui.Rife_Model.clear()
    self.ui.FPSPreview.setText('RES:')
    modified_list = list(map(lambda x: x.replace('models-',''), self.get_models_from_dir('waifu2x')))
    self.ui.Rife_Model.addItems(modified_list)
    if  'cunet' in modified_list:self.ui.Rife_Model.setCurrentText(f'cunet')
            

    
    
    self.ui.RifeStart.clicked.disconnect()
    try:
        self.ui.Rife_Model.currentIndexChanged.disconnect()
    except:
        pass
    self.ui.Rife_Model.currentIndexChanged.connect((self.greyOutRealSRTimes))
    
    self.greyOutRealSRTimes()
    
    self.ui.RifeStart.clicked.connect(lambda: upscale.start_upscale(self,'waifu2x-ncnn-vulkan'))
    self.ui.Rife_Times.clear()
    
    self.ui.denoiseLevelLabel.show()
    self.ui.denoiseLevelSpinBox.show()
    self.ui.Rife_Times.addItem('1X')
    self.ui.Rife_Times.addItem('2X')
    self.ui.Rife_Times.setCurrentIndex(0)

