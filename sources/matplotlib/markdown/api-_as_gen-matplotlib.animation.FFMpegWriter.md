[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#main-content)

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
    

matplotlib.animation.FFMpegWriter[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib-animation-ffmpegwriter "Link to this heading")

================================================================================================================================================================================

class matplotlib.animation.FFMpegWriter(_fps\=5_, _codec\=None_, _bitrate\=None_, _extra\_args\=None_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L583-L607)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter "Link to this definition")

Pipe-based ffmpeg writer.

Frames are streamed directly to ffmpeg via a pipe and written in a single pass.

This effectively works as a slideshow input to ffmpeg with the fps passed as `-framerate`, so see also [their notes on frame rates](https://trac.ffmpeg.org/wiki/Slideshow#Framerates)
 for further details.

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

\_\_init\_\_(_fps\=5_, _codec\=None_, _bitrate\=None_, _extra\_args\=None_, _metadata\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L260-L295)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter.__init__ "Link to this definition")

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
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter.__init__ "matplotlib.animation.FFMpegWriter.__init__")<br>(\[fps, codec, bitrate, extra\_args, ...\]) |     |
| `bin_path`() | Return the binary path to the commandline tool used by a specific subclass. |
| `finish`() | Finish any processing for writing the movie. |
| `grab_frame`(\*\*savefig\_kwargs) | Grab the image information from the figure and save as a movie frame. |
| `isAvailable`() | Return whether a MovieWriter subclass is actually available. |
| `saving`(fig, outfile, dpi, \*args, \*\*kwargs) | Context manager to facilitate writing the movie file. |
| `setup`(fig, outfile\[, dpi\]) | Setup for writing the movie file. |

Attributes

|     |     |
| --- | --- |
| `frame_size` | A tuple `(width, height)` in pixels of a movie frame. |
| `output_args` |     |
| `supported_formats` |     |

On this page