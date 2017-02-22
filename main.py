#!/usr/bin/env python3

import pyglet
import pyglet.media.procedural
from pyglet.media.procedural import Sine
from pyglet.window import key
from src.config import CTRL_CMD

class Sound (pyglet.media.procedural.Sine):
    def replay(self):
        self.seek(0)
        return self.play()

BLACK=(0, 0, 0, 255)
WHITE=(255, 255, 255, 255)
BCKND=(0, .5, .8, 1)

window = pyglet.window.Window(640, 480)

pyglet.gl.glClearColor(*BCKND)

checker_pattern = pyglet.image.CheckerImagePattern(color1=BLACK, color2=WHITE)
image = pyglet.image.create(64,64, checker_pattern)
image.anchor_x = 32
image.anchor_y = 32
sprite = pyglet.sprite.Sprite(img=image, x=320, y=240)

sound = Sine(0.1, 830)
sound.__class__ = Sound
player = pyglet.media.Player()


@window.event
def on_key_press(symbol, mods):
    #Manage exit
    if mods & CTRL_CMD and (symbol == key.Q or symbol == key.W):
        pyglet.app.exit()
    elif symbol == key.ESCAPE:
        return pyglet.event.EVENT_HANDLED
        
    elif symbol == key.A:
        sprite.x -= 5
        sound.replay()
    elif symbol == key.W:
        sprite.y += 5
        sound.replay()
    elif symbol == key.D:
        sprite.x += 5
        sound.replay()
    elif symbol == key.S:
        sprite.y -= 5
        sound.replay()

@window.event
def on_draw():
    window.clear()
    sprite.draw()

def update(dt):
    sprite.rotation += dt * 45
    
pyglet.clock.schedule_interval(update, 1 / 60.0)

pyglet.app.run()
