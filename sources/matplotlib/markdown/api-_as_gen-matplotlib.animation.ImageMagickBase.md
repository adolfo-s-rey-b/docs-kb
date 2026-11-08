[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#main-content)

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
    

matplotlib.animation.ImageMagickBase[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib-animation-imagemagickbase "Link to this heading")

=========================================================================================================================================================================================

class matplotlib.animation.ImageMagickBase[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L654-L700)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase "Link to this definition")

Mixin class for ImageMagick output.

This is a base class for the concrete [`ImageMagickWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickWriter.html#matplotlib.animation.ImageMagickWriter "matplotlib.animation.ImageMagickWriter")
 and [`ImageMagickFileWriter`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickFileWriter.html#matplotlib.animation.ImageMagickFileWriter "matplotlib.animation.ImageMagickFileWriter")
 classes, which define an `input_names` attribute (or property) specifying the input names passed to ImageMagick.

\_\_init\_\_(_\*args_, _\*\*kwargs_)[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.__init__ "Link to this definition")

Methods

|     |     |
| --- | --- |
| [`__init__`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.__init__ "matplotlib.animation.ImageMagickBase.__init__")<br>(\*args, \*\*kwargs) |     |
| [`bin_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.bin_path "matplotlib.animation.ImageMagickBase.bin_path")<br>() |     |
| [`isAvailable`](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.isAvailable "matplotlib.animation.ImageMagickBase.isAvailable")<br>() |     |

classmethod bin\_path()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L686-L691)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.bin_path "Link to this definition")

classmethod isAvailable()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/animation.py#L693-L700)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ImageMagickBase.html#matplotlib.animation.ImageMagickBase.isAvailable "Link to this definition")

On this page