[Skip to main content](https://matplotlib.org/stable/api/animation_api.html#main-content)

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
    

`matplotlib.animation`[#](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "Link to this heading")

===================================================================================================================================

[Animation](https://matplotlib.org/stable/api/animation_api.html#id3)
[#](https://matplotlib.org/stable/api/animation_api.html#animation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The easiest way to make a live animation in Matplotlib is to use one of the [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 classes.

See also

*   [Animations using Matplotlib](https://matplotlib.org/stable/users/explain/animations/animations.html#animations)
    

Inheritance diagram of matplotlib.animation.FuncAnimation, matplotlib.animation.ArtistAnimation

|     |     |
| --- | --- |
| [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation") | Abstract base class for Animations. |
| [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation") | [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")<br> subclass that makes an animation by repeatedly calling a function _func_. |
| [`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation") | [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation")<br> subclass that creates an animation by using a fixed set of [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")<br> objects. |

In both cases it is critical to keep a reference to the instance object. The animation is advanced by a timer (typically from the host GUI framework) which the [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 object holds the only reference to. If you do not hold a reference to the [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")
 object, it (and hence the timers) will be garbage collected which will stop the animation.

To save an animation use [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
, [`Animation.to_html5_video`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_html5_video "matplotlib.animation.Animation.to_html5_video")
, or [`Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
.

See [Helper Classes](https://matplotlib.org/stable/api/animation_api.html#ani-writer-classes)
 below for details about what movie formats are supported.

### `FuncAnimation`[#](https://matplotlib.org/stable/api/animation_api.html#funcanimation "Link to this heading")

The inner workings of [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 is more-or-less:

for d in frames:
    artists \= func(d, \*fargs)
    fig.canvas.draw\_idle()
    fig.canvas.start\_event\_loop(interval)

with details to handle 'blitting' (to dramatically improve the live performance), to be non-blocking, not repeatedly start/stop the GUI event loop, handle repeats, multiple animated axes, and easily save the animation to a movie file.

'Blitting' is a [standard technique](https://en.wikipedia.org/wiki/Bit_blit)
 in computer graphics. The general gist is to take an existing bit map (in our case a mostly rasterized figure) and then 'blit' one more artist on top. Thus, by managing a saved 'clean' bitmap, we can only re-draw the few artists that are changing at each frame and possibly save significant amounts of time. When we use blitting (by passing `blit=True`), the core loop of [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 gets a bit more complicated:

ax \= fig.gca()

def update\_blit(artists):
    fig.canvas.restore\_region(bg\_cache)
    for a in artists:
        a.axes.draw\_artist(a)

    ax.figure.canvas.blit(ax.bbox)

artists \= init\_func()

for a in artists:
   a.set\_animated(True)

fig.canvas.draw()
bg\_cache \= fig.canvas.copy\_from\_bbox(ax.bbox)

for f in frames:
    artists \= func(f, \*fargs)
    update\_blit(artists)
    fig.canvas.start\_event\_loop(interval)

This is of course leaving out many details (such as updating the background when the figure is resized or fully re-drawn). However, this hopefully minimalist example gives a sense of how `init_func` and `func` are used inside of [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 and the theory of how 'blitting' works.

Note

The zorder of artists is not taken into account when 'blitting' because the 'blitted' artists are always drawn on top.

The expected signature on `func` and `init_func` is very simple to keep [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 out of your book keeping and plotting logic, but this means that the callable objects you pass in must know what artists they should be working on. There are several approaches to handling this, of varying complexity and encapsulation. The simplest approach, which works quite well in the case of a script, is to define the artist at a global scope and let Python sort things out. For example:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax \= plt.subplots()
xdata, ydata \= \[\], \[\]
ln, \= ax.plot(\[\], \[\], 'ro')

def init():
    ax.set\_xlim(0, 2\*np.pi)
    ax.set\_ylim(\-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set\_data(xdata, ydata)
    return ln,

ani \= FuncAnimation(fig, update, frames\=np.linspace(0, 2\*np.pi, 128),
                    init\_func\=init, blit\=True)
plt.show()

The second method is to use [`functools.partial`](https://docs.python.org/3/library/functools.html#functools.partial "(in Python v3.14)")
 to pass arguments to the function:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

fig, ax \= plt.subplots()
line1, \= ax.plot(\[\], \[\], 'ro')

def init():
    ax.set\_xlim(0, 2\*np.pi)
    ax.set\_ylim(\-1, 1)
    return line1,

def update(frame, ln, x, y):
    x.append(frame)
    y.append(np.sin(frame))
    ln.set\_data(x, y)
    return ln,

ani \= FuncAnimation(
    fig, partial(update, ln\=line1, x\=\[\], y\=\[\]),
    frames\=np.linspace(0, 2\*np.pi, 128),
    init\_func\=init, blit\=True)

plt.show()

A third method is to use closures to build up the required artists and functions. A fourth method is to create a class.

#### Examples[#](https://matplotlib.org/stable/api/animation_api.html#examples "Link to this heading")

*   [Decay](https://matplotlib.org/stable/gallery/animation/animate_decay.html)
    
*   [The Bayes update](https://matplotlib.org/stable/gallery/animation/bayes_update.html)
    
*   [The double pendulum problem](https://matplotlib.org/stable/gallery/animation/double_pendulum.html)
    
*   [Animated histogram](https://matplotlib.org/stable/gallery/animation/animated_histogram.html)
    
*   [Rain simulation](https://matplotlib.org/stable/gallery/animation/rain.html)
    
*   [Animated 3D random walk](https://matplotlib.org/stable/gallery/animation/random_walk.html)
    
*   [Basic animated line plot](https://matplotlib.org/stable/gallery/animation/simple_anim.html)
    
*   [Oscilloscope](https://matplotlib.org/stable/gallery/animation/strip_chart.html)
    
*   [Matplotlib unchained](https://matplotlib.org/stable/gallery/animation/unchained.html)
    

### `ArtistAnimation`[#](https://matplotlib.org/stable/api/animation_api.html#artistanimation "Link to this heading")

#### Examples[#](https://matplotlib.org/stable/api/animation_api.html#id1 "Link to this heading")

*   [Animated image using a precomputed list of images](https://matplotlib.org/stable/gallery/animation/dynamic_image.html)
    

[Writer Classes](https://matplotlib.org/stable/api/animation_api.html#id4)
[#](https://matplotlib.org/stable/api/animation_api.html#writer-classes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Inheritance diagram of matplotlib.animation.FFMpegFileWriter, matplotlib.animation.FFMpegWriter, matplotlib.animation.ImageMagickFileWriter, matplotlib.animation.ImageMagickWriter, matplotlib.animation.PillowWriter, matplotlib.animation.HTMLWriter

The provided writers fall into a few broad categories.

The Pillow writer relies on the Pillow library to write the animation, keeping all data in memory.

|     |     |
| --- | --- |
| [`PillowWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter "matplotlib.animation.PillowWriter") |     |

The HTML writer generates JavaScript-based animations.

|     |     |
| --- | --- |
| [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter") | Writer for JavaScript-based HTML movies. |

The pipe-based writers stream the captured frames over a pipe to an external process. The pipe-based variants tend to be more performant, but may not work on all systems.

|     |     |
| --- | --- |
| [`FFMpegWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter "matplotlib.animation.FFMpegWriter") | Pipe-based ffmpeg writer. |
| [`ImageMagickWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickWriter.html#matplotlib.animation.ImageMagickWriter "matplotlib.animation.ImageMagickWriter") | Pipe-based animated gif writer. |

The file-based writers save temporary files for each frame which are stitched into a single file at the end. Although slower, these writers can be easier to debug.

|     |     |
| --- | --- |
| [`FFMpegFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "matplotlib.animation.FFMpegFileWriter") | File-based ffmpeg writer. |
| [`ImageMagickFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickFileWriter.html#matplotlib.animation.ImageMagickFileWriter "matplotlib.animation.ImageMagickFileWriter") | File-based animated gif writer. |

The writer classes provide a way to grab sequential frames from the same underlying [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. They all provide three methods that must be called in sequence:

*   [`setup`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.setup "matplotlib.animation.AbstractMovieWriter.setup")
     prepares the writer (e.g. opening a pipe). Pipe-based and file-based writers take different arguments to `setup()`.
    
*   [`grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.grab_frame "matplotlib.animation.AbstractMovieWriter.grab_frame")
     can then be called as often as needed to capture a single frame at a time
    
*   [`finish`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.finish "matplotlib.animation.AbstractMovieWriter.finish")
     finalizes the movie and writes the output file to disk.
    

Example:

moviewriter \= MovieWriter(...)
moviewriter.setup(fig, 'my\_movie.ext', dpi\=100)
for j in range(n):
    update\_figure(j)
    moviewriter.grab\_frame()
moviewriter.finish()

If using the writer classes directly (not through [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
), it is strongly encouraged to use the [`saving`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.saving "matplotlib.animation.AbstractMovieWriter.saving")
 context manager:

with moviewriter.saving(fig, 'myfile.mp4', dpi\=100):
    for j in range(n):
        update\_figure(j)
        moviewriter.grab\_frame()

to ensure that setup and cleanup are performed as necessary.

### Examples[#](https://matplotlib.org/stable/api/animation_api.html#id2 "Link to this heading")

*   [Frame grabbing](https://matplotlib.org/stable/gallery/animation/frame_grabbing_sgskip.html)
    

[Helper Classes](https://matplotlib.org/stable/api/animation_api.html#id5)
[#](https://matplotlib.org/stable/api/animation_api.html#helper-classes "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Animation Base Classes[#](https://matplotlib.org/stable/api/animation_api.html#animation-base-classes "Link to this heading")

|     |     |
| --- | --- |
| [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation") | Abstract base class for Animations. |
| [`TimedAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.TimedAnimation.html#matplotlib.animation.TimedAnimation "matplotlib.animation.TimedAnimation") | Abstract [`Animation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation "matplotlib.animation.Animation")<br> subclass for time-based animation. |

### Writer Registry[#](https://matplotlib.org/stable/api/animation_api.html#writer-registry "Link to this heading")

A module-level registry is provided to map between the name of the writer and the class to allow a string to be passed to [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
 instead of a writer instance.

|     |     |
| --- | --- |
| [`MovieWriterRegistry`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriterRegistry.html#matplotlib.animation.MovieWriterRegistry "matplotlib.animation.MovieWriterRegistry") | Registry of available writer classes by human readable name. |

### Writer Base Classes[#](https://matplotlib.org/stable/api/animation_api.html#writer-base-classes "Link to this heading")

To reduce code duplication base classes

|     |     |
| --- | --- |
| [`AbstractMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter "matplotlib.animation.AbstractMovieWriter") | Abstract base class for writing movies, providing a way to grab frames by calling [`grab_frame`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.AbstractMovieWriter.html#matplotlib.animation.AbstractMovieWriter.grab_frame "matplotlib.animation.AbstractMovieWriter.grab_frame")<br>. |
| [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter") | Base class for writing movies. |
| [`FileMovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FileMovieWriter.html#matplotlib.animation.FileMovieWriter "matplotlib.animation.FileMovieWriter") | [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")<br> for writing to individual files and stitching at the end. |

and mixins

|     |     |
| --- | --- |
| [`FFMpegBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegBase.html#matplotlib.animation.FFMpegBase "matplotlib.animation.FFMpegBase") | Mixin class for FFMpeg output. |
| [`ImageMagickBase`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase "matplotlib.animation.ImageMagickBase") | Mixin class for ImageMagick output. |

are provided.

See the source code for how to easily implement new [`MovieWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.MovieWriter.html#matplotlib.animation.MovieWriter "matplotlib.animation.MovieWriter")
 classes.

On this page