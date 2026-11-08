[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#main-content)

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
    

matplotlib.animation.PillowWriter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib-animation-pillowwriter "Link to this heading")

================================================================================================================================================================================

class matplotlib.animation.PillowWriter(_fps\=5_, _metadata\=None_, _codec\=None_, _bitrate\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L485-L516)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter "Link to this definition")

\_\_init\_\_(_fps\=5_, _metadata\=None_, _codec\=None_, _bitrate\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L148-L152)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.__init__ "matplotlib.animation.PillowWriter.__init__")<br>(\[fps, metadata, codec, bitrate\]) |     |
| [`finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.finish "matplotlib.animation.PillowWriter.finish")<br>() | Finish any processing for writing the movie. |
| [`grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.grab_frame "matplotlib.animation.PillowWriter.grab_frame")<br>(\*\*savefig\_kwargs) | Grab the image information from the figure and save as a movie frame. |
| [`isAvailable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.isAvailable "matplotlib.animation.PillowWriter.isAvailable")<br>() |     |
| `saving`(fig, outfile, dpi, \*args, \*\*kwargs) | Context manager to facilitate writing the movie file. |
| [`setup`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.setup "matplotlib.animation.PillowWriter.setup")<br>(fig, outfile\[, dpi\]) | Setup for writing the movie file. |

Attributes

|     |     |
| --- | --- |
| `frame_size` | A tuple `(width, height)` in pixels of a movie frame. |

finish()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L513-L516)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.finish "Link to this definition")

Finish any processing for writing the movie.

grab\_frame(_\*\*savefig\_kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L498-L511)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.grab_frame "Link to this definition")

Grab the image information from the figure and save as a movie frame.

All keyword arguments in _savefig\_kwargs_ are passed on to the [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 call that saves the figure. However, several keyword arguments that are supported by [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 may not be passed as they are controlled by the MovieWriter:

*   _dpi_, _bbox\_inches_: These may not be passed because each frame of the
    
    animation much be exactly the same size in pixels.
    
*   _format_: This is controlled by the MovieWriter.
    

classmethod isAvailable()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L490-L492)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.isAvailable "Link to this definition")

setup(_fig_, _outfile_, _dpi\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L494-L496)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter.setup "Link to this definition")

Setup for writing the movie file.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure object that contains the information for frames.

**outfile**str

The filename of the resulting movie file.

**dpi**float, default: `fig.dpi`

The DPI (or resolution) for the file. This controls the size in pixels of the resulting movie file.

On this page