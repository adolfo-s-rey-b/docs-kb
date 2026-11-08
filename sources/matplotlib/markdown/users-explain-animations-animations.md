[Skip to main content](https://matplotlib.org/stable/users/explain/animations/animations.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/animations/animations.html#sphx-glr-download-users-explain-animations-animations-py)
 to download the full example code.

Animations using Matplotlib[#](https://matplotlib.org/stable/users/explain/animations/animations.html#animations-using-matplotlib "Link to this heading")

==========================================================================================================================================================

Based on its plotting functionality, Matplotlib also provides an interface to generate animations using the [`animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")
 module. An animation is a sequence of frames where each frame corresponds to a plot on a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
. This tutorial covers a general guideline on how to create such animations and the different options available. More information is available in the API description: [`animation`](https://matplotlib.org/stable/api/animation_api.html#module-matplotlib.animation "matplotlib.animation")

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation

Animation classes[#](https://matplotlib.org/stable/users/explain/animations/animations.html#animation-classes "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The animation process in Matplotlib can be thought of in 2 different ways:

*   [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
    : Generate data for first frame and then modify this data for each frame to create an animated plot.
    
*   [`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
    : Generate a list (iterable) of artists that will draw in each frame in the animation.
    

[`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 is more efficient in terms of speed and memory as it draws an artist once and then modifies it. On the other hand [`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 is flexible as it allows any iterable of artists to be animated in a sequence.

### `FuncAnimation`[#](https://matplotlib.org/stable/users/explain/animations/animations.html#funcanimation "Link to this heading")

The [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 class allows us to create an animation by passing a function that iteratively modifies the data of a plot. This is achieved by using the _setter_ methods on various [`Artist`](https://matplotlib.org/stable/api/artist_api.html#matplotlib.artist.Artist "matplotlib.artist.Artist")
 (examples: [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
, etc.). A usual [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 object takes a [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 that we want to animate and a function _func_ that modifies the data plotted on the figure. It uses the _frames_ parameter to determine the length of the animation. The _interval_ parameter is used to determine time in milliseconds between drawing of two frames. Animating using [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 typically requires these steps:

1.  Plot the initial figure as you would in a static plot. Save all the created artists, which are returned by the plot functions, in variables so that you can access and modify them later in the animation function.
    
2.  Create an animation function that updates the artists for a given frame. Typically, this calls `set_*` methods of the artists.
    
3.  Create a [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
    , passing the [`Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
     and the animation function.
    
4.  Save or show the animation using one of the following methods:
    
    *   [`pyplot.show`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
         to show the animation in a window
        
    *   [`Animation.to_html5_video`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_html5_video "matplotlib.animation.Animation.to_html5_video")
         to create an HTML `<video>` tag
        
    *   [`Animation.to_jshtml`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.to_jshtml "matplotlib.animation.Animation.to_jshtml")
         to create HTML code with interactive JavaScript animation controls
        
    *   [`Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
         to save the animation to a file
        

The following table shows a few plotting methods, the artists they return and some commonly used `set_*` methods that update the underlying data. While updating data is the most common operation in animations, you can also update other aspects such as color or text position.

| Plotting method | Artist | Data set methods |
| --- | --- | --- |
| [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot") | [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D") | [`set_data`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_data "matplotlib.lines.Line2D.set_data")<br>, [`set_xdata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")<br>, [`set_ydata`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata") |
| [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter") | [`collections.PathCollection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection") | [`set_offsets`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.set_offsets "matplotlib.collections.PathCollection.set_offsets") |
| [`Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow") | [`image.AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage") | `AxesImage.set_data` |
| [`Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate") | [`text.Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation") | [`update_positions`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation.update_positions "matplotlib.text.Annotation.update_positions") |
| [`Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh") | [`patches.Rectangle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle "matplotlib.patches.Rectangle") | [`set_angle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_angle "matplotlib.patches.Rectangle.set_angle")<br>, [`set_bounds`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_bounds "matplotlib.patches.Rectangle.set_bounds")<br>, [`set_height`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_height "matplotlib.patches.Rectangle.set_height")<br>, [`set_width`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_width "matplotlib.patches.Rectangle.set_width")<br>, [`set_x`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_x "matplotlib.patches.Rectangle.set_x")<br>, [`set_y`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_y "matplotlib.patches.Rectangle.set_y")<br>, [`set_xy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html#matplotlib.patches.Rectangle.set_xy "matplotlib.patches.Rectangle.set_xy") |
| [`Axes.fill`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html#matplotlib.axes.Axes.fill "matplotlib.axes.Axes.fill") | [`patches.Polygon`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon "matplotlib.patches.Polygon") | [`set_xy`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html#matplotlib.patches.Polygon.set_xy "matplotlib.patches.Polygon.set_xy") |
| [`Axes.add_patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.add_patch.html#matplotlib.axes.Axes.add_patch "matplotlib.axes.Axes.add_patch")<br>([`patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse")<br>) | [`patches.Ellipse`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse "matplotlib.patches.Ellipse") | [`set_angle`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.set_angle "matplotlib.patches.Ellipse.set_angle")<br>, [`set_center`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.set_center "matplotlib.patches.Ellipse.set_center")<br>, [`set_height`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.set_height "matplotlib.patches.Ellipse.set_height")<br>, [`set_width`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Ellipse.html#matplotlib.patches.Ellipse.set_width "matplotlib.patches.Ellipse.set_width") |
| [`Axes.set_title`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")<br>, [`Axes.text`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text") | [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text") | [`set_text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text.set_text "matplotlib.text.Text.set_text") |

Covering the set methods for all types of artists is beyond the scope of this tutorial but can be found in their respective documentations. An example of such update methods in use for [`Axes.scatter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
 and [`Axes.plot`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
 is as follows.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 3, 40)
[g](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= \-9.81
[v0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 12
[z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [g](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 / 2 + [v0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[v02](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [g](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 / 2 + [v02](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[scat](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
 \= [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], c\="b", s\=5, label\=f'v0 = {[v0](https://docs.python.org/3/library/functions.html#int "builtins.int")
} m/s')
[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], [z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\], label\=f'v0 = {[v02](https://docs.python.org/3/library/functions.html#int "builtins.int")
} m/s')\[0\]
[ax.set](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set.html#matplotlib.axes.Axes.set "matplotlib.axes.Axes.set")
(xlim\=(0, 3), ylim\=(\-4, 10), xlabel\='Time \[s\]', ylabel\='Z \[m\]')
[ax.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html#matplotlib.axes.Axes.legend "matplotlib.axes.Axes.legend")
()

def update(frame):
    \# for each frame, update the data stored on each artist.
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:frame\]
    y \= [z](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:frame\]
    \# update the scatter plot:
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.stack](https://numpy.org/doc/stable/reference/generated/numpy.stack.html#numpy.stack "numpy.stack")
(\[[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
, y\]).T
    [scat.set\_offsets](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection.set_offsets "matplotlib.collections.PathCollection.set_offsets")
([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
    \# update the line plot:
    [line2.set\_xdata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_xdata "matplotlib.lines.Line2D.set_xdata")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:frame\])
    [line2.set\_ydata](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_ydata "matplotlib.lines.Line2D.set_ydata")
([z2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:frame\])
    return ([scat](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.PathCollection "matplotlib.collections.PathCollection")
, [line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
)

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 \= [animation.FuncAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, func\=update, frames\=40, interval\=30)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

### `ArtistAnimation`[#](https://matplotlib.org/stable/users/explain/animations/animations.html#artistanimation "Link to this heading")

[`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 can be used to generate animations if there is data stored on various different artists. This list of artists is then converted frame by frame into an animation. For example, when we use [`Axes.barh`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
 to plot a bar-chart, it creates a number of artists for each of the bar and error bars. To update the plot, one would need to update each of the bars from the container individually and redraw them. Instead, [`animation.ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 can be used to plot each frame individually and then stitched together to form an animation. A barchart race is a simple example for this.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator "numpy.random.Generator")
 \= [np.random.default\_rng](https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng "numpy.random.default_rng")
(19680801)
[data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[20, 20, 20, 20\])
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[1, 2, 3, 4\])

[artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]
[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \['tab:blue', 'tab:red', 'tab:green', 'tab:purple'\]
for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in range(20):
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 += [rng.integers](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.integers.html#numpy.random.Generator.integers "numpy.random.Generator.integers")
(low\=0, high\=10, size\=[data.shape](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
)
    [container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
 \= [ax.barh](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.barh.html#matplotlib.axes.Axes.barh "matplotlib.axes.Axes.barh")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\=[colors](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    [artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([container](https://matplotlib.org/stable/api/container_api.html#matplotlib.container.BarContainer "matplotlib.container.BarContainer")
)

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 \= [animation.ArtistAnimation](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
\=[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\=[artists](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, interval\=400)
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

Animation writers[#](https://matplotlib.org/stable/users/explain/animations/animations.html#animation-writers "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Animation objects can be saved to disk using various multimedia writers (ex: Pillow, _ffpmeg_, _imagemagick_). Not all video formats are supported by all writers. There are 4 major types of writers:

*   [`PillowWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter "matplotlib.animation.PillowWriter")
     - Uses the Pillow library to create the animation.
    
*   [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter")
     - Used to create JavaScript-based animations.
    
*   Pipe-based writers - [`FFMpegWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter "matplotlib.animation.FFMpegWriter")
     and [`ImageMagickWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickWriter.html#matplotlib.animation.ImageMagickWriter "matplotlib.animation.ImageMagickWriter")
     are pipe based writers. These writers pipe each frame to the utility (_ffmpeg_ / _imagemagick_) which then stitches all of them together to create the animation.
    
*   File-based writers - [`FFMpegFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "matplotlib.animation.FFMpegFileWriter")
     and [`ImageMagickFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickFileWriter.html#matplotlib.animation.ImageMagickFileWriter "matplotlib.animation.ImageMagickFileWriter")
     are examples of file-based writers. These writers are slower than their pipe-based alternatives but are more useful for debugging as they save each frame in a file before stitching them together into an animation.
    

### Saving Animations[#](https://matplotlib.org/stable/users/explain/animations/animations.html#saving-animations "Link to this heading")

| Writer | Supported Formats |
| --- | --- |
| [`PillowWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.PillowWriter.html#matplotlib.animation.PillowWriter "matplotlib.animation.PillowWriter") | .gif, .apng, .webp |
| [`HTMLWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.HTMLWriter.html#matplotlib.animation.HTMLWriter "matplotlib.animation.HTMLWriter") | .htm, .html, .png |
| [`FFMpegWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegWriter.html#matplotlib.animation.FFMpegWriter "matplotlib.animation.FFMpegWriter")<br><br>[`FFMpegFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FFMpegFileWriter.html#matplotlib.animation.FFMpegFileWriter "matplotlib.animation.FFMpegFileWriter") | All formats supported by [_ffmpeg_](https://www.ffmpeg.org/general.html#Supported-File-Formats_002c-Codecs-or-Features)<br>: `ffmpeg -formats` |
| [`ImageMagickWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickWriter.html#matplotlib.animation.ImageMagickWriter "matplotlib.animation.ImageMagickWriter")<br><br>[`ImageMagickFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickFileWriter.html#matplotlib.animation.ImageMagickFileWriter "matplotlib.animation.ImageMagickFileWriter") | All formats supported by [_imagemagick_](https://imagemagick.org/script/formats.php#supported)<br>: `magick -list format` |

To save animations using any of the writers, we can use the [`animation.Animation.save`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.Animation.html#matplotlib.animation.Animation.save "matplotlib.animation.Animation.save")
 method. It takes the _filename_ that we want to save the animation as and the _writer_, which is either a string or a writer object. It also takes an _fps_ argument. This argument is different than the _interval_ argument that [`FuncAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation "matplotlib.animation.FuncAnimation")
 or [`ArtistAnimation`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
 uses. _fps_ determines the frame rate that the **saved** animation uses, whereas _interval_ determines the frame rate that the **displayed** animation uses.

Below are a few examples that show how to save an animation with different writers.

Pillow writers:

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/pillow\_example.gif", writer\="pillow")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/pillow\_example.apng", writer\="pillow")

HTML writers:

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/html\_example.html", writer\="html")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/html\_example.htm", writer\="html")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/html\_example.png", writer\="html")

FFMpegWriter:

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/ffmpeg\_example.mkv", writer\="ffmpeg")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/ffmpeg\_example.mp4", writer\="ffmpeg")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/ffmpeg\_example.mjpeg", writer\="ffmpeg")

Imagemagick writers:

[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/imagemagick\_example.gif", writer\="imagemagick")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="/tmp/imagemagick\_example.webp", writer\="imagemagick")
[ani](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html#matplotlib.animation.ArtistAnimation "matplotlib.animation.ArtistAnimation")
.save(filename\="apng:/tmp/imagemagick\_example.apng",
         writer\="imagemagick", extra\_args\=\["-quality", "100"\])

(the `extra_args` for _apng_ are needed to reduce filesize by ~10x)

Note that _ffmpeg_ and _imagemagick_ need to be separately installed. A cross-platform way to obtain _ffmpeg_ is to install the `imageio_ffmpeg` PyPI package, and then to set `rcParams["animation.ffmpeg_path"] = imageio_ffmpeg.get_ffmpeg_exe()`.

**Total running time of the script:** (0 minutes 16.925 seconds)

[`Download Jupyter notebook: animations.ipynb`](https://matplotlib.org/stable/_downloads/ce5593ca1443c961ec69e74b0af5c61c/animations.ipynb)

[`Download Python source code: animations.py`](https://matplotlib.org/stable/_downloads/b5546881188fb3e3d279d5a734f9240d/animations.py)

[`Download zipped: animations.zip`](https://matplotlib.org/stable/_downloads/506f596f4fea247b69376ea5f89e3e5d/animations.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page