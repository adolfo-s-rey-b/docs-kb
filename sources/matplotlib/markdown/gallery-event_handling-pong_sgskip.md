[Skip to main content](https://matplotlib.org/stable/gallery/event_handling/pong_sgskip.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

Note

[Go to the end](https://matplotlib.org/stable/gallery/event_handling/pong_sgskip.html#sphx-glr-download-gallery-event-handling-pong-sgskip-py)
 to download the full example code.

Pong[#](https://matplotlib.org/stable/gallery/event_handling/pong_sgskip.html#pong "Link to this heading")

===========================================================================================================

A Matplotlib based game of Pong illustrating one way to write interactive animations that are easily ported to multiple backends.

Note

This example exercises the interactive capabilities of Matplotlib, and this will not appear in the static documentation. Please run this code on your machine to see the interactivity.

You can copy and paste individual parts, or download the entire example using the link at the bottom of the page.

import time

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import [randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")
, [randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")

from matplotlib.font\_manager import [FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")

instructions \= """
Player A:       Player B:
  'e'      up     'i'
  'd'     down    'k'

press 't' -- close these instructions
            (animation will be much faster)
press 'a' -- add a puck
press 'A' -- remove a puck
press '1' -- slow down all pucks
press '2' -- speed up all pucks
press '3' -- slow down distractors
press '4' -- speed up distractors
press ' ' -- reset the first puck
press 'n' -- toggle distractors on/off
press 'g' -- toggle the game on/off

  """

class Pad:
    def \_\_init\_\_(self, disp, x, y, type\='l'):
        self.disp \= disp
        self.x \= x
        self.y \= y
        self.w \= .3
        self.score \= 0
        self.xoffset \= 0.3
        self.yoffset \= 0.1
        if type \== 'r':
            self.xoffset \*= \-1.0

        if type \== 'l' or type \== 'r':
            self.signx \= \-1.0
            self.signy \= 1.0
        else:
            self.signx \= 1.0
            self.signy \= \-1.0

    def contains(self, loc):
        return self.disp.get\_bbox().contains(loc.x, loc.y)

class Puck:
    def \_\_init\_\_(self, disp, pad, field):
        self.vmax \= .2
        self.disp \= disp
        self.field \= field
        self.\_reset(pad)

    def \_reset(self, pad):
        self.x \= pad.x + pad.xoffset
        if pad.y < 0:
            self.y \= pad.y + pad.yoffset
        else:
            self.y \= pad.y \- pad.yoffset
        self.vx \= pad.x \- self.x
        self.vy \= pad.y + pad.w/2 \- self.y
        self.\_speedlimit()
        self.\_slower()
        self.\_slower()

    def update(self, pads):
        self.x += self.vx
        self.y += self.vy
        for pad in pads:
            if pad.contains(self):
                self.vx \*= 1.2 \* pad.signx
                self.vy \*= 1.2 \* pad.signy
        fudge \= .001
        \# probably cleaner with something like...
        if self.x < fudge:
            pads\[1\].score += 1
            self.\_reset(pads\[0\])
            return True
        if self.x \> 7 \- fudge:
            pads\[0\].score += 1
            self.\_reset(pads\[1\])
            return True
        if self.y < \-1 + fudge or self.y \> 1 \- fudge:
            self.vy \*= \-1.0
            \# add some randomness, just to make it interesting
            self.vy \-= ([randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
()/300.0 + 1/300.0) \* [np.sign](https://numpy.org/doc/stable/reference/generated/numpy.sign.html#numpy.sign "numpy.sign")
(self.vy)
        self.\_speedlimit()
        return False

    def \_slower(self):
        self.vx /= 5.0
        self.vy /= 5.0

    def \_faster(self):
        self.vx \*= 5.0
        self.vy \*= 5.0

    def \_speedlimit(self):
        if self.vx \> self.vmax:
            self.vx \= self.vmax
        if self.vx < \-self.vmax:
            self.vx \= \-self.vmax

        if self.vy \> self.vmax:
            self.vy \= self.vmax
        if self.vy < \-self.vmax:
            self.vy \= \-self.vmax

class Game:
    def \_\_init\_\_(self, ax):
        \# create the initial line
        self.ax \= ax
        ax.xaxis.set\_visible(False)
        ax.set\_xlim(0, 7)
        ax.yaxis.set\_visible(False)
        ax.set\_ylim(\-1, 1)
        pad\_a\_x \= 0
        pad\_b\_x \= .50
        pad\_a\_y \= pad\_b\_y \= .30
        pad\_b\_x += 6.3

        \# pads
        pA, \= self.ax.barh(pad\_a\_y, .2,
                           height\=.3, color\='k', alpha\=.5, edgecolor\='b',
                           lw\=2, label\="Player B",
                           animated\=True)
        pB, \= self.ax.barh(pad\_b\_y, .2,
                           height\=.3, left\=pad\_b\_x, color\='k', alpha\=.5,
                           edgecolor\='r', lw\=2, label\="Player A",
                           animated\=True)

        \# distractors
        self.x \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2.22\*[np.pi](https://numpy.org/doc/stable/reference/constants.html#numpy.pi "numpy.pi")
, 0.01)
        self.line, \= self.ax.plot(self.x, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(self.x), "r",
                                  animated\=True, lw\=4)
        self.line2, \= self.ax.plot(self.x, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.x), "g",
                                   animated\=True, lw\=4)
        self.line3, \= self.ax.plot(self.x, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.x), "g",
                                   animated\=True, lw\=4)
        self.line4, \= self.ax.plot(self.x, [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.x), "r",
                                   animated\=True, lw\=4)

        \# center line
        self.centerline, \= self.ax.plot(\[3.5, 3.5\], \[1, \-1\], 'k',
                                        alpha\=.5, animated\=True, lw\=8)

        \# puck (s)
        self.puckdisp \= self.ax.scatter(\[1\], \[1\], label\='\_nolegend\_',
                                        s\=200, c\='g',
                                        alpha\=.9, animated\=True)

        self.canvas \= self.ax.figure.canvas
        self.background \= None
        self.cnt \= 0
        self.distract \= True
        self.res \= 100.0
        self.on \= False
        self.inst \= True    \# show instructions from the beginning
        self.pads \= \[Pad(pA, pad\_a\_x, pad\_a\_y),\
                     Pad(pB, pad\_b\_x, pad\_b\_y, 'r')\]
        self.pucks \= \[\]
        self.i \= self.ax.annotate(instructions, (.5, 0.5),
                                  name\='monospace',
                                  verticalalignment\='center',
                                  horizontalalignment\='center',
                                  multialignment\='left',
                                  xycoords\='axes fraction',
                                  animated\=False)
        self.canvas.mpl\_connect('key\_press\_event', self.on\_key\_press)

    def draw(self):
        draw\_artist \= self.ax.draw\_artist
        if self.background is None:
            self.background \= self.canvas.copy\_from\_bbox(self.ax.bbox)

        \# restore the clean slate background
        self.canvas.restore\_region(self.background)

        \# show the distractors
        if self.distract:
            self.line.set\_ydata([np.sin](https://numpy.org/doc/stable/reference/generated/numpy.sin.html#numpy.sin "numpy.sin")
(self.x + self.cnt/self.res))
            self.line2.set\_ydata([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.cos.html#numpy.cos "numpy.cos")
(self.x \- self.cnt/self.res))
            self.line3.set\_ydata([np.tan](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")
(self.x + self.cnt/self.res))
            self.line4.set\_ydata([np.tan](https://numpy.org/doc/stable/reference/generated/numpy.tan.html#numpy.tan "numpy.tan")
(self.x \- self.cnt/self.res))
            draw\_artist(self.line)
            draw\_artist(self.line2)
            draw\_artist(self.line3)
            draw\_artist(self.line4)

        \# pucks and pads
        if self.on:
            self.ax.draw\_artist(self.centerline)
            for pad in self.pads:
                pad.disp.set\_y(pad.y)
                pad.disp.set\_x(pad.x)
                self.ax.draw\_artist(pad.disp)

            for puck in self.pucks:
                if puck.update(self.pads):
                    \# we only get here if someone scored
                    self.pads\[0\].disp.set\_label(f"   {self.pads\[0\].score}")
                    self.pads\[1\].disp.set\_label(f"   {self.pads\[1\].score}")
                    self.ax.legend(loc\='center', framealpha\=.2,
                                   facecolor\='0.5',
                                   prop\=[FontProperties](https://matplotlib.org/stable/api/font_manager_api.html#matplotlib.font_manager.FontProperties "matplotlib.font_manager.FontProperties")
(size\='xx-large',
                                                       weight\='bold'))

                    self.background \= None
                    self.ax.figure.canvas.draw\_idle()
                    return
                puck.disp.set\_offsets(\[\[puck.x, puck.y\]\])
                self.ax.draw\_artist(puck.disp)

        \# just redraw the Axes rectangle
        self.canvas.blit(self.ax.bbox)
        self.canvas.flush\_events()
        if self.cnt \== 50000:
            \# just so we don't get carried away
            print("...and you've been playing for too long!!!")
            [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
()

        self.cnt += 1

    def on\_key\_press(self, event):
        if event.key \== '3':
            self.res \*= 5.0
        if event.key \== '4':
            self.res /= 5.0

        if event.key \== 'e':
            self.pads\[0\].y += .1
            if self.pads\[0\].y \> 1 \- .3:
                self.pads\[0\].y \= 1 \- .3
        if event.key \== 'd':
            self.pads\[0\].y \-= .1
            if self.pads\[0\].y < \-1:
                self.pads\[0\].y \= \-1

        if event.key \== 'i':
            self.pads\[1\].y += .1
            if self.pads\[1\].y \> 1 \- .3:
                self.pads\[1\].y \= 1 \- .3
        if event.key \== 'k':
            self.pads\[1\].y \-= .1
            if self.pads\[1\].y < \-1:
                self.pads\[1\].y \= \-1

        if event.key \== 'a':
            self.pucks.append(Puck(self.puckdisp,
                                   self.pads\[[randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
(2)\],
                                   self.ax.bbox))
        if event.key \== 'A' and len(self.pucks):
            self.pucks.pop()
        if event.key \== ' ' and len(self.pucks):
            self.pucks\[0\].\_reset(self.pads\[[randint](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html#numpy.random.randint "numpy.random.randint")\
(2)\])
        if event.key \== '1':
            for p in self.pucks:
                p.\_slower()
        if event.key \== '2':
            for p in self.pucks:
                p.\_faster()

        if event.key \== 'n':
            self.distract \= not self.distract

        if event.key \== 'g':
            self.on \= not self.on
        if event.key \== 't':
            self.inst \= not self.inst
            self.i.set\_visible(not self.i.get\_visible())
            self.background \= None
            self.canvas.draw\_idle()
        if event.key \== 'q':
            [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
()

fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
canvas \= ax.figure.canvas
animation \= Game(ax)

\# disable the default key bindings
if fig.canvas.manager.key\_press\_handler\_id is not None:
    canvas.mpl\_disconnect(fig.canvas.manager.key\_press\_handler\_id)

\# reset the blitting background on redraw
def on\_redraw(event):
    animation.background \= None

\# bootstrap after the first draw
def start\_anim(event):
    canvas.mpl\_disconnect(start\_anim.cid)

    start\_anim.timer.add\_callback(animation.draw)
    start\_anim.timer.start()
    canvas.mpl\_connect('draw\_event', on\_redraw)

start\_anim.cid \= canvas.mpl\_connect('draw\_event', start\_anim)
start\_anim.timer \= animation.canvas.new\_timer(interval\=1)

tstart \= [time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
()

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()
print('FPS: %f' % (animation.cnt/([time.time](https://docs.python.org/3/library/time.html#time.time "time.time")
() \- tstart)))

#

Tags: [interactivity: event-handling](https://matplotlib.org/stable/_tags/interactivity-event-handling.html)
 [purpose: fun](https://matplotlib.org/stable/_tags/purpose-fun.html)

[`Download Jupyter notebook: pong_sgskip.ipynb`](https://matplotlib.org/stable/_downloads/4953df1126b554664d22e3efba5d0f57/pong_sgskip.ipynb)

[`Download Python source code: pong_sgskip.py`](https://matplotlib.org/stable/_downloads/b047032cf62d3ac8a0705adf298a6fb8/pong_sgskip.py)

[`Download zipped: pong_sgskip.zip`](https://matplotlib.org/stable/_downloads/7590e857b369e7e2193dc6b57f3625e3/pong_sgskip.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)