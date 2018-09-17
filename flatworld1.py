# A basic flat world - blocks will be same colour and water still exists

from mcpi.minecraft import Minecraft
from mcpi import block
import sys


mc = Minecraft.create()
mc.postToChat("Python API Connection Established")
mc.setBlocks(-128,0,-128,128,64,128,0)
if(len(sys.argv) > 1):
    bid = int(sys,argv[1])
