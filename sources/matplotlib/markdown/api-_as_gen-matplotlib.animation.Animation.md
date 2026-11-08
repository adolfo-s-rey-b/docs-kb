[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#main-content)

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
    

matplotlib.animation.Animation[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib-animation-animation "Link to this heading")

=======================================================================================================================================================================

class matplotlib.animation.Animation(_fig_, _event\_source_, _blit\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L859-L1421)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "Link to this definition")

Abstract base class for Animations.

Note

You must store the created Animation in a variable that lives as long as the animation should run. Otherwise, the Animation object will be garbage-collected and the animation stops.

Parameters:

**fig**[`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")

The figure object used to get needed events, such as draw or resize.

**event\_source**object

A class that can run a callback when desired events are generated, as well as be stopped and started.

Examples include timers (see [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")
) and file system notifications.

**blit**bool, default: False

Whether blitting is used to optimize drawing. If the backend does not support blitting, then this parameter has no effect.

See also

[`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
, [`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")

\_\_init\_\_(_fig_, _event\_source_, _blit\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L890-L916)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.__init__ "matplotlib.animation.Animation.__init__")<br>(fig, event\_source\[, blit\]) |     |
| [`new_frame_seq`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.new_frame_seq "matplotlib.animation.Animation.new_frame_seq")<br>() | Return a new sequence of frame information. |
| [`new_saved_frame_seq`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.new_saved_frame_seq "matplotlib.animation.Animation.new_saved_frame_seq")<br>() | Return a new sequence of saved/cached frame information. |
| [`pause`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.pause "matplotlib.animation.Animation.pause")<br>() | Pause the animation. |
| [`resume`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.resume "matplotlib.animation.Animation.resume")<br>() | Resume the animation. |
| [`save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")<br>(filename\[, writer, fps, dpi, codec, ...\]) | Save the animation as a movie file by drawing every frame. |
| [`to_html5_video`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_html5_video "matplotlib.animation.Animation.to_html5_video")<br>(\[embed\_limit\]) | Convert the animation to an HTML5 `<video>` tag. |
| [`to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")<br>(\[fps, embed\_frames, default\_mode\]) | Generate HTML representation of the animation. |

new\_frame\_seq()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1163-L1166)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.new_frame_seq "Link to this definition")

Return a new sequence of frame information.

new\_saved\_frame\_seq()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1168-L1171)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.new_saved_frame_seq "Link to this definition")

Return a new sequence of saved/cached frame information.

pause()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1409-L1414)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.pause "Link to this definition")

Pause the animation.

resume()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1416-L1421)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.resume "Link to this definition")

Resume the animation.

save(_filename_, _writer\=None_, _fps\=None_, _dpi\=None_, _codec\=None_, _bitrate\=None_, _extra\_args\=None_, _metadata\=None_, _extra\_anim\=None_, _savefig\_kwargs\=None_, _\*_, _progress\_callback\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L951-L1146)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "Link to this definition")

Save the animation as a movie file by drawing every frame.

Parameters:

**filename**str

The output filename, e.g., `mymovie.mp4`.

**writer**[`AbstractMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter "matplotlib.animation.AbstractMovieWriter")
 subclass or str, default: `[rcParams["animation.writer"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.writer#rcparam-animation-writer) ` (default: `'ffmpeg'`)

The writer used to grab the frames and create the movie file. This can be an instance of an [`AbstractMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter "matplotlib.animation.AbstractMovieWriter")
 subclass or a string. The builtin writers are

| str | class |
| --- | --- |
| 'ffmpeg' | [`FFMpegWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter "matplotlib.animation.FFMpegWriter") |
| 'ffmpeg\_file' | [`FFMpegFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "matplotlib.animation.FFMpegFileWriter") |
| 'imagemagick' | [`ImageMagickWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickWriter.html#matplotlib.animation.ImageMagickWriter "matplotlib.animation.ImageMagickWriter") |
| 'imagemagick\_file' | [`ImageMagickFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickFileWriter.html#matplotlib.animation.ImageMagickFileWriter "matplotlib.animation.ImageMagickFileWriter") |
| 'pillow' | [`PillowWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter "matplotlib.animation.PillowWriter") |
| 'html' | [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter") |

**fps**int, optional

Movie frame rate (per second). If not set, the frame rate from the animation's frame interval.

**dpi**float, default: `[rcParams["savefig.dpi"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=savefig.dpi#rcparam-savefig-dpi) ` (default: `'figure'`)

Controls the dots per inch for the movie frames. Together with the figure's size in inches, this controls the size of the movie.

**codec**str, default: `[rcParams["animation.codec"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.codec#rcparam-animation-codec) ` (default: `'h264'`).

The video codec to use. Not all codecs are supported by a given [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
.

**bitrate**int, default: `[rcParams["animation.bitrate"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.bitrate#rcparam-animation-bitrate) ` (default: `-1`)

The bitrate of the movie, in kilobits per second. Higher values means higher quality movies, but increase the file size. A value of -1 lets the underlying movie encoder select the bitrate.

**extra\_args**list of str or None, optional

Extra command-line arguments passed to the underlying movie encoder. These arguments are passed last to the encoder, just before the output filename. The default, None, means to use `[rcParams["animation.[name-of-encoder]_args"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.[name-of-encoder]_args#rcparam-animation-ffmpeg-args) ` for the builtin writers.

**metadata**dict\[str, str\], default: {}

Dictionary of keys and values for metadata to include in the output file. Some keys that may be of use include: title, artist, genre, subject, copyright, srcform, comment.

**extra\_anim**list, default: \[\]

Additional [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 objects that should be included in the saved movie file. These need to be from the same [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 instance. Also, animation frames will just be simply combined, so there should be a 1:1 correspondence between the frames from the different animations.

**savefig\_kwargs**dict, default: {}

Keyword arguments passed to each [`savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.savefig.html#matplotlib.figure.Figure.savefig "matplotlib.figure.Figure.savefig")
 call used to save the individual frames.

**progress\_callback**function, optional

A callback function that will be called for every frame to notify the saving progress. It must have the signature

def func(current\_frame: int, total\_frames: int) \-> Any

where _current\_frame_ is the current frame number and _total\_frames_ is the total number of frames to be saved. _total\_frames_ is set to None, if the total number of frames cannot be determined. Return values may exist but are ignored.

Example code to write the progress to stdout:

progress\_callback \= lambda i, n: print(f'Saving frame {i}/{n}')

Notes

_fps_, _codec_, _bitrate_, _extra\_args_ and _metadata_ are used to construct a [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
 instance and can only be passed if _writer_ is a string. If they are passed as non-_None_ and _writer_ is a [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")
 will be raised.

to\_html5\_video(_embed\_limit\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1279-L1355)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_html5_video "Link to this definition")

Convert the animation to an HTML5 `<video>` tag.

This saves the animation as an h264 video, encoded in base64 directly into the HTML5 video tag. This respects `[rcParams["animation.writer"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.writer#rcparam-animation-writer) ` (default: `'ffmpeg'`) and `[rcParams["animation.bitrate"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.bitrate#rcparam-animation-bitrate) ` (default: `-1`). This also makes use of the _interval_ to control the speed, and uses the _repeat_ parameter to decide whether to loop.

Parameters:

**embed\_limit**float, optional

Limit, in MB, of the returned animation. No animation is created if the limit is exceeded. Defaults to `[rcParams["animation.embed_limit"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=animation.embed_limit#rcparam-animation-embed-limit) ` (default: `20.0`) = 20.0.

Returns:

str

An HTML5 video tag with the animation embedded as base64 encoded h264 video. If the _embed\_limit_ is exceeded, this returns the string "Video too large to embed."

to\_jshtml(_fps\=None_, _embed\_frames\=True_, _default\_mode\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L1357-L1399)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "Link to this definition")

Generate HTML representation of the animation.

Parameters:

**fps**int, optional

Movie frame rate (per second). If not set, the frame rate from the animation's frame interval.

**embed\_frames**bool, optional

**default\_mode**str, optional

What to do when the animation ends. Must be one of `{'loop', 'once', 'reflect'}`. Defaults to `'loop'` if the _repeat_ parameter is True, otherwise `'once'`.

Returns:

str

An HTML representation of the animation embedded as a js object as produced with the [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter")
.

On this page