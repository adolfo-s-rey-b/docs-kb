[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#main-content)

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
    

matplotlib.animation.FuncAnimation[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib-animation-funcanimation "Link to this heading")

===================================================================================================================================================================================

class matplotlib.animation.FuncAnimation(_fig_, _func_, _frames\=None_, _init\_func\=None_, _fargs\=None_, _save\_count\=None_, _\*_, _cache\_frame\_data\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1570-L1828)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "Link to this definition")

[`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")
 subclass that makes an animation by repeatedly calling a function _func_.

Note

You must store the created Animation in a variable that lives as long as the animation should run. Otherwise, the Animation object will be garbage-collected and the animation stops.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure object used to get needed events, such as draw or resize.

**func**callable

The function to call at each frame. The first argument will be the next value in _frames_. Any additional positional arguments can be supplied using [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
 or via the _fargs_ parameter.

The required signature is:

def func(frame, \*fargs) \-> iterable\_of\_artists

It is often more convenient to provide the arguments using [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
. In this way it is also possible to pass keyword arguments. To pass a function with both positional and keyword arguments, set all arguments as keyword arguments, just leaving the _frame_ argument unset:

def func(frame, art, \*, y\=None):
    ...

ani \= FuncAnimation(fig, partial(func, art\=ln, y\='foo'))

If `blit == True`, _func_ must return an iterable of all artists that were modified or created. This information is used by the blitting algorithm to determine which parts of the figure have to be updated. The return value is unused if `blit == False` and may be omitted in that case.

**frames**iterable, int, generator function, or None, optional

Source of data to pass _func_ and each frame of the animation

*   If an iterable, then simply use the values provided. If the iterable has a length, it will override the _save\_count_ kwarg.
    
*   If an integer, then equivalent to passing `range(frames)`
    
*   If a generator function, then must have the signature:
    
    def gen\_function() \-> obj
    
*   If _None_, then equivalent to passing `itertools.count`.
    

In all of these cases, the values in _frames_ is simply passed through to the user-supplied _func_ and thus can be of any type.

**init\_func**callable, optional

A function used to draw a clear frame. If not given, the results of drawing from the first item in the frames sequence will be used. This function will be called once before the first frame.

The required signature is:

def init\_func() \-> iterable\_of\_artists

If `blit == True`, _init\_func_ must return an iterable of artists to be re-drawn. This information is used by the blitting algorithm to determine which parts of the figure have to be updated. The return value is unused if `blit == False` and may be omitted in that case.

**fargs**tuple or None, optional

Additional arguments to pass to each call to _func_. Note: the use of [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
 is preferred over _fargs_. See _func_ for details.

**save\_count**int, optional

Fallback for the number of values from _frames_ to cache. This is only used if the number of frames cannot be inferred from _frames_, i.e. when it's an iterator without length or a generator.

**interval**int, default: 200

Delay between frames in milliseconds.

**repeat\_delay**int, default: 0

The delay in milliseconds between consecutive animation runs, if _repeat_ is True.

**repeat**bool, default: True

Whether the animation repeats when the sequence of frames is completed.

**blit**bool, default: False

Whether blitting is used to optimize drawing. Note: when using blitting, any animated artists will be drawn according to their zorder; however, they will be drawn on top of any previous artists, regardless of their zorder.

**cache\_frame\_data**bool, default: True

Whether frame data is cached. Disabling cache might be helpful when frames contain large objects.

\_\_init\_\_(_fig_, _func_, _frames\=None_, _init\_func\=None_, _fargs\=None_, _save\_count\=None_, _\*_, _cache\_frame\_data\=True_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1673-L1740)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.__init__ "matplotlib.animation.FuncAnimation.__init__")<br>(fig, func\[, frames, init\_func, ...\]) |     |
| [`new_frame_seq`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.new_frame_seq "matplotlib.animation.FuncAnimation.new_frame_seq")<br>() | Return a new sequence of frame information. |
| [`new_saved_frame_seq`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.new_saved_frame_seq "matplotlib.animation.FuncAnimation.new_saved_frame_seq")<br>() | Return a new sequence of saved/cached frame information. |
| `pause`() | Pause the animation. |
| `resume`() | Resume the animation. |
| `save`(filename\[, writer, fps, dpi, codec, ...\]) | Save the animation as a movie file by drawing every frame. |
| `to_html5_video`(\[embed\_limit\]) | Convert the animation to an HTML5 `<video>` tag. |
| `to_jshtml`(\[fps, embed\_frames, default\_mode\]) | Generate HTML representation of the animation. |

new\_frame\_seq()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1742-L1744)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.new_frame_seq "Link to this definition")

Return a new sequence of frame information.

new\_saved\_frame\_seq()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1746-L1766)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation.new_saved_frame_seq "Link to this definition")

Return a new sequence of saved/cached frame information.

On this page