
from pyglet.window import key
from sys import platform

if platform == 'darwin':
  CTRL_CMD = key.MOD_COMMAND
else:
  CTRL_CMD = key.MOD_CTRL
