[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#main-content)

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
    

matplotlib.animation.FileMovieWriter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib-animation-filemoviewriter "Link to this heading")

=========================================================================================================================================================================================

class matplotlib.animation.FileMovieWriter(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L382-L482)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "Link to this definition")

[`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
 for writing to individual files and stitching at the end.

This must be sub-classed to be useful.

Parameters:

**fps**int, default: 5

Movie frame rate (per second).

**codec**str or None, default: `[rcParams["animation.codec"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.codec#rcparam-animation-codec) ` (default: `'h264'`)

The codec to use.

**bitrate**int, default: `[rcParams["animation.bitrate"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.bitrate#rcparam-animation-bitrate) ` (default: `-1`)

The bitrate of the movie, in kilobits per second. Higher values means higher quality movies, but increase the file size. A value of -1 lets the underlying movie encoder select the bitrate.

**extra\_args**list of str or None, optional

Extra command-line arguments passed to the underlying movie encoder. These arguments are passed last to the encoder, just before the filename. The default, None, means to use `[rcParams["animation.[name-of-encoder]_args"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.[name-of-encoder]_args#rcparam-animation-ffmpeg-args) ` for the builtin writers.

**metadata**dict\[str, str\], default: {}

A dictionary of keys and values for metadata to include in the output file. Some keys that may be of use include: title, artist, genre, subject, copyright, srcform, comment.

\_\_init\_\_(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L388-L390)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.__init__ "Link to this definition")

Parameters:

**fps**int, default: 5

Movie frame rate (per second).

**codec**str or None, default: `[rcParams["animation.codec"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.codec#rcparam-animation-codec) ` (default: `'h264'`)

The codec to use.

**bitrate**int, default: `[rcParams["animation.bitrate"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.bitrate#rcparam-animation-bitrate) ` (default: `-1`)

The bitrate of the movie, in kilobits per second. Higher values means higher quality movies, but increase the file size. A value of -1 lets the underlying movie encoder select the bitrate.

**extra\_args**list of str or None, optional

Extra command-line arguments passed to the underlying movie encoder. These arguments are passed last to the encoder, just before the filename. The default, None, means to use `[rcParams["animation.[name-of-encoder]_args"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.[name-of-encoder]_args#rcparam-animation-ffmpeg-args) ` for the builtin writers.

**metadata**dict\[str, str\], default: {}

A dictionary of keys and values for metadata to include in the output file. Some keys that may be of use include: title, artist, genre, subject, copyright, srcform, comment.

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.__init__ "matplotlib.animation.FileMovieWriter.__init__")<br>(\*args, \*\*kwargs) |     |
| `bin_path`() | Return the binary path to the commandline tool used by a specific subclass. |
| [`finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.finish "matplotlib.animation.FileMovieWriter.finish")<br>() | Finish any processing for writing the movie. |
| [`grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.grab_frame "matplotlib.animation.FileMovieWriter.grab_frame")<br>(\*\*savefig\_kwargs) | Grab the image information from the figure and save as a movie frame. |
| `isAvailable`() | Return whether a MovieWriter subclass is actually available. |
| `saving`(fig, outfile, dpi, \*args, \*\*kwargs) | Context manager to facilitate writing the movie file. |
| [`setup`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.setup "matplotlib.animation.FileMovieWriter.setup")<br>(fig, outfile\[, dpi, frame\_prefix\]) | Setup for writing the movie file. |

Attributes

|     |     |
| --- | --- |
| [`frame_format`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.frame_format "matplotlib.animation.FileMovieWriter.frame_format") | Format (png, jpeg, etc.) to use for saving the frames, which can be decided by the individual subclasses. |
| `frame_size` | A tuple `(width, height)` in pixels of a movie frame. |
| `supported_formats` |     |

finish()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L471-L482)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.finish "Link to this definition")

Finish any processing for writing the movie.

property frame\_format[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.frame_format "Link to this definition")

Format (png, jpeg, etc.) to use for saving the frames, which can be decided by the individual subclasses.

grab\_frame(_\*\*savefig\_kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L458-L469)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.grab_frame "Link to this definition")

Grab the image information from the figure and save as a movie frame.

All keyword arguments in _savefig\_kwargs_ are passed on to the [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 call that saves the figure. However, several keyword arguments that are supported by [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 may not be passed as they are controlled by the MovieWriter:

*   _dpi_, _bbox\_inches_: These may not be passed because each frame of the
    
    animation much be exactly the same size in pixels.
    
*   _format_: This is controlled by the MovieWriter.
    

setup(_fig_, _outfile_, _dpi\=None_, _frame\_prefix\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L392-L428)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.setup "Link to this definition")

Setup for writing the movie file.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure to grab the rendered frames from.

**outfile**str

The filename of the resulting movie file.

**dpi**float, default: `fig.dpi`

The dpi of the output file. This, with the figure size, controls the size in pixels of the resulting movie file.

**frame\_prefix**str, optional

The filename prefix to use for temporary files. If _None_ (the default), files are written to a temporary directory which is deleted by [`finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter.finish "matplotlib.animation.FileMovieWriter.finish")
; if not _None_, no temporary files are deleted.

On this page