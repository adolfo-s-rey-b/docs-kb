[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#main-content)

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
    

matplotlib.animation.FFMpegFileWriter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib-animation-ffmpegfilewriter "Link to this heading")

============================================================================================================================================================================================

class matplotlib.animation.FFMpegFileWriter(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L611-L650)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "Link to this definition")

File-based ffmpeg writer.

Frames are written to temporary files on disk and then stitched together at the end.

This effectively works as a slideshow input to ffmpeg with the fps passed as `-framerate`, so see also [their notes on frame rates](https://trac.ffmpeg.org/wiki/Slideshow#Framerates)
 for further details.

Parameters:

**\*args, \*\*kwargs**

All arguments are forwarded to [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
. See [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter")
 for a list of all possible parameters.

\_\_init\_\_(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L388-L390)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter.__init__ "matplotlib.animation.FFMpegFileWriter.__init__")<br>(\*args, \*\*kwargs) |     |
| `bin_path`() | Return the binary path to the commandline tool used by a specific subclass. |
| `finish`() | Finish any processing for writing the movie. |
| `grab_frame`(\*\*savefig\_kwargs) | Grab the image information from the figure and save as a movie frame. |
| `isAvailable`() | Return whether a MovieWriter subclass is actually available. |
| `saving`(fig, outfile, dpi, \*args, \*\*kwargs) | Context manager to facilitate writing the movie file. |
| `setup`(fig, outfile\[, dpi, frame\_prefix\]) | Setup for writing the movie file. |

Attributes

|     |     |
| --- | --- |
| `frame_format` | Format (png, jpeg, etc.) to use for saving the frames, which can be decided by the individual subclasses. |
| `frame_size` | A tuple `(width, height)` in pixels of a movie frame. |
| `output_args` |     |
| [`supported_formats`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter.supported_formats "matplotlib.animation.FFMpegFileWriter.supported_formats") |     |

supported\_formats \= \['png', 'jpeg', 'tiff', 'raw', 'rgba'\][#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter.supported_formats "Link to this definition")

On this page