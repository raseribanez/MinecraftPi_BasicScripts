''' Always start your Minecraft programs like this '''

# These lines import minecraft into python
from mcpi.minecraft import Minecraft
from mcpi import block

# These lines create a connection with the current world
# and print a test message to confirm connection to the game
mc = Minecraft.create()
mc.postToChat("Python API Connection Established")
