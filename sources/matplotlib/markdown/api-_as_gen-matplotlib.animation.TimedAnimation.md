[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#main-content)

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
    

matplotlib.animation.TimedAnimation[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib-animation-timedanimation "Link to this heading")

======================================================================================================================================================================================

class matplotlib.animation.TimedAnimation(_fig_, _interval\=200_, _repeat\_delay\=0_, _repeat\=True_, _event\_source\=None_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1424-L1490)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "Link to this definition")

Abstract [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 subclass for time-based animation.

A new frame is drawn every _interval_ milliseconds.

Note

You must store the created Animation in a variable that lives as long as the animation should run. Otherwise, the Animation object will be garbage-collected and the animation stops.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure object used to get needed events, such as draw or resize.

**interval**int, default: 200

Delay between frames in milliseconds.

**repeat\_delay**int, default: 0

The delay in milliseconds between consecutive animation runs, if _repeat_ is True.

**repeat**bool, default: True

Whether the animation repeats when the sequence of frames is completed.

**blit**bool, default: False

Whether blitting is used to optimize drawing.

\_\_init\_\_(_fig_, _interval\=200_, _repeat\_delay\=0_, _repeat\=True_, _event\_source\=None_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1450-L1460)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation.__init__ "matplotlib.animation.TimedAnimation.__init__")<br>(fig\[, interval, repeat\_delay, ...\]) |     |
| `new_frame_seq`() | Return a new sequence of frame information. |
| `new_saved_frame_seq`() | Return a new sequence of saved/cached frame information. |
| `pause`() | Pause the animation. |
| `resume`() | Resume the animation. |
| `save`(filename\[, writer, fps, dpi, codec, ...\]) | Save the animation as a movie file by drawing every frame. |
| `to_html5_video`(\[embed\_limit\]) | Convert the animation to an HTML5 `<video>` tag. |
| `to_jshtml`(\[fps, embed\_frames, default\_mode\]) | Generate HTML representation of the animation. |

On this page