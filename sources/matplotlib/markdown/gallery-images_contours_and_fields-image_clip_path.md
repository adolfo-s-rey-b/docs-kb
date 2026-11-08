[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html#sphx-glr-download-gallery-images-contours-and-fields-image-clip-path-py)
 to download the full example code.

Clipping images with patches[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_clip_path.html#clipping-images-with-patches "Link to this heading")

===========================================================================================================================================================================

Demo of image that's been clipped by a circular patch.

from PIL import Image

import matplotlib.pyplot as plt

import matplotlib.cbook as cbook
import matplotlib.patches as patches

[image](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
 \= [Image.open](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open "PIL.Image.open")
([cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
("grace\_hopper.jpg"))

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([image](https://pillow.readthedocs.io/en/stable/reference/plugins.html#PIL.JpegImagePlugin.JpegImageFile "PIL.JpegImagePlugin.JpegImageFile")
)
[patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
 \= [patches.Circle](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
((260, 200), radius\=200, transform\=[ax.transData](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.CompositeGenericTransform "matplotlib.transforms.CompositeGenericTransform")
)
[im.set\_clip\_path](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
([patch](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Circle.html#matplotlib.patches.Circle "matplotlib.patches.Circle")
)

[ax.axis](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axis.html#matplotlib.axes.Axes.axis "matplotlib.axes.Axes.axis")
('off')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image clip path](https://matplotlib.org/stable/_images/sphx_glr_image_clip_path_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
     / [`matplotlib.pyplot.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow "matplotlib.pyplot.imshow")
    
*   [`matplotlib.artist.Artist.set_clip_path`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_clip_path.html#matplotlib.artist.Artist.set_clip_path "matplotlib.artist.Artist.set_clip_path")
    

[`Download Jupyter notebook: image_clip_path.ipynb`](https://matplotlib.org/stable/_downloads/051b3eaa40b0559c106645ff213ae918/image_clip_path.ipynb)

[`Download Python source code: image_clip_path.py`](https://matplotlib.org/stable/_downloads/ce934135c1eb77d0aa284a948f1a584e/image_clip_path.py)

[`Download zipped: image_clip_path.zip`](https://matplotlib.org/stable/_downloads/0eaf8cc7522980ed00d6ce8ece9ff741/image_clip_path.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)