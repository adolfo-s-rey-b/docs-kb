[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#sphx-glr-download-gallery-images-contours-and-fields-image-antialiasing-py)
 to download the full example code.

Image resampling[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#image-resampling "Link to this heading")

======================================================================================================================================================

Images are represented by discrete pixels assigned color values, either on the screen or in an image file. When a user calls [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 with a data array, it is rare that the size of the data array exactly matches the number of pixels allotted to the image in the figure, so Matplotlib resamples or [scales](https://en.wikipedia.org/wiki/Image_scaling)
 the data or image to fit. If the data array is larger than the number of pixels allotted in the rendered figure, then the image will be "down-sampled" and image information will be lost. Conversely, if the data array is smaller than the number of output pixels then each data point will get multiple pixels, and the image is "up-sampled".

In the following figure, the first data array has size (450, 450), but is represented by far fewer pixels in the figure, and hence is down-sampled. The second data array has size (4, 4), and is represented by far more pixels, and hence is up-sampled.

import matplotlib.pyplot as plt
import numpy as np

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(4, 2))

\# First we generate a 450x450 pixel image with varying frequency content:
[N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 450
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 0.5
[y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \- 0.5
[aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.ones](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones "numpy.ones")
(([N](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [N](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
[aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::2, :\] \= \-1

[X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.meshgrid](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([X](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 + [Y](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2)
[f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 5
[k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 100
[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 2 \* ([f0](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [k](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\*\*2 / 2))
\# make the left hand side of this
[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 2), :\]\[[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[:int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 2), :\] < 0.4\] \= \-1
[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 2), :\]\[[R](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\[:int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 2), :\] < 0.3\] \= 1
[aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 3):\] \= [a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:, int([N](https://docs.python.org/3/library/functions.html#int "builtins.int")\
 / 3):\]
[alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='RdBu\_r')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title('(450, 450) Down-sampled', fontsize\='medium')

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801+9)
[asmall](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(4, 4)
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([asmall](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='viridis')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title('(4, 4) Up-sampled', fontsize\='medium')

![(450, 450) Down-sampled, (4, 4) Up-sampled](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_001_2_00x.png)

Matplotlib's [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 method has two keyword arguments to allow the user to control how resampling is done. The _interpolation_ keyword argument allows a choice of the kernel that is used for resampling, allowing either [anti-alias](https://en.wikipedia.org/wiki/Anti-aliasing_filter)
 filtering if down-sampling, or smoothing of pixels if up-sampling. The _interpolation\_stage_ keyword argument, determines if this smoothing kernel is applied to the underlying data, or if the kernel is applied to the RGBA pixels.

`interpolation_stage='rgba'`: Data -> Normalize -> RGBA -> Interpolate/Resample

`interpolation_stage='data'`: Data -> Interpolate/Resample -> Normalize -> RGBA

For both keyword arguments, Matplotlib has a default "auto", that is recommended for most situations, and is described below. Note that this default behaves differently if the image is being down- or up-sampled, as described below.

Down-sampling and modest up-sampling[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#down-sampling-and-modest-up-sampling "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When down-sampling data, we usually want to remove aliasing by smoothing the image first and then sub-sampling it. In Matplotlib, we can do that smoothing before mapping the data to colors, or we can do the smoothing on the RGB(A) image pixels. The differences between these are shown below, and controlled with the _interpolation\_stage_ keyword argument.

The following images are down-sampled from 450 data pixels to approximately 125 pixels or 250 pixels (depending on your display). The underlying image has alternating +1, -1 stripes on the left side, and a varying wavelength ([chirp](https://en.wikipedia.org/wiki/Chirp)
) pattern in the rest of the image. If we zoom, we can see this detail without any down-sampling:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(4, 4), layout\='compressed')
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='nearest', [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='RdBu\_r')
[ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(100, 200)
[ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(275, 175)
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
('Zoom')

![Zoom](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_002_2_00x.png)

If we down-sample, the simplest algorithm is to decimate the data using [nearest-neighbor interpolation](https://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
. We can do this in either data space or RGBA space:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(5, 2.7), layout\='compressed')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, \['nearest', 'nearest'\],
                                       \['data', 'rgba'\]):
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, interpolation\_stage\=[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
              [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='RdBu\_r')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f"interpolation='{[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'\\nstage='{[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'")

![interpolation='nearest' stage='data', interpolation='nearest' stage='rgba'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_003_2_00x.png)

Nearest interpolation is identical in data and RGBA space, and both exhibit [Moiré](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern)
 patterns because the high-frequency data is being down-sampled and shows up as lower frequency patterns. We can reduce the Moiré patterns by applying an anti-aliasing filter to the image before rendering:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(5, 2.7), layout\='compressed')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
, \['hanning', 'hanning'\],
                                       \['data', 'rgba'\]):
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, interpolation\_stage\=[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
              [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='RdBu\_r')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f"interpolation='{[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'\\nstage='{[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![interpolation='hanning' stage='data', interpolation='hanning' stage='rgba'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_004_2_00x.png)

The [Hanning](https://en.wikipedia.org/wiki/Hann_function)
 filter smooths the underlying data so that each new pixel is a weighted average of the original underlying pixels. This greatly reduces the Moiré patterns. However, when the _interpolation\_stage_ is set to 'data', it also introduces white regions to the image that are not in the original data, both in the alternating bands on the left hand side of the image, and in the boundary between the red and blue of the large circles in the middle of the image. The interpolation at the 'rgba' stage has a different artifact, with the alternating bands coming out a shade of purple; even though purple is not in the original colormap, it is what we perceive when a blue and red stripe are close to each other.

The default for the _interpolation_ keyword argument is 'auto' which will choose a Hanning filter if the image is being down-sampled or up-sampled by less than a factor of three. The default _interpolation\_stage_ keyword argument is also 'auto', and for images that are down-sampled or up-sampled by less than a factor of three it defaults to 'rgba' interpolation.

Anti-aliasing filtering is needed, even when up-sampling. The following image up-samples 450 data pixels to 530 rendered pixels. You may note a grid of line-like artifacts which stem from the extra pixels that had to be made up. Since interpolation is 'nearest' they are the same as a neighboring line of pixels and thus stretch the image locally so that it looks distorted.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6.8, 6.8))
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='nearest', [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='grey')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("up-sampled by factor a 1.17, interpolation='nearest'")

![up-sampled by factor a 1.17, interpolation='nearest'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_005_2_00x.png)

Better anti-aliasing algorithms can reduce this effect:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6.8, 6.8))
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\='auto', [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='grey')
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("up-sampled by factor a 1.17, interpolation='auto'")

![up-sampled by factor a 1.17, interpolation='auto'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_006_2_00x.png)

Apart from the default 'hanning' anti-aliasing, [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 supports a number of different interpolation algorithms, which may work better or worse depending on the underlying data.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(7, 4), layout\='constrained')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, \['hanning', 'lanczos'\]):
    [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='gray')
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
(f"interpolation='{[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'")

![interpolation='hanning', interpolation='lanczos'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_007_2_00x.png)

A final example shows the desirability of performing the anti-aliasing at the RGBA stage when using non-trivial interpolation kernels. In the following, the data in the outer circle is exactly 0.0, and data in the inner circle is exactly 2.0. If we perform the _interpolation\_stage_ in 'data' space and use an anti-aliasing filter (first panel), then floating point imprecision makes some of the data values just a bit less than zero or a bit more than 2.0, and they get assigned the under- or over- colors. This can be avoided if you do not use an anti-aliasing filter (_interpolation_ set to 'nearest'), however, that makes the part of the data susceptible to Moiré patterns much worse (second panel). Therefore, we recommend the default _interpolation_ of 'hanning'/'auto', and _interpolation\_stage_ of 'rgba'/'auto' for most down-sampling situations (last panel).

[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [alarge](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + 1
[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
 \= [plt.get\_cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.get_cmap.html#matplotlib.pyplot.get_cmap "matplotlib.pyplot.get_cmap")
('RdBu\_r')
[cmap.set\_under](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_under "matplotlib.colors.Colormap.set_under")
('yellow')
[cmap.set\_over](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap.set_over "matplotlib.colors.Colormap.set_over")
('limegreen')

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 3, figsize\=(7, 3), layout\='constrained')
for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
,
                             \['hanning', 'nearest', 'hanning', \],
                             \['data', 'data', 'rgba'\]):
    [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, interpolation\=[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, interpolation\_stage\=[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
,
                   [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\=[cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
, vmin\=0, vmax\=2)
    [title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= f"interpolation='{[interp](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'\\nstage='{[space](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
}'"
    if [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \== [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[2\]:
        [title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 += '\\nDefault'
    [ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
([title](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, fontsize\='medium')
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, extend\='both', shrink\=0.8)

![interpolation='hanning' stage='data', interpolation='nearest' stage='data', interpolation='hanning' stage='rgba' Default](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_008_2_00x.png)

Up-sampling[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#up-sampling "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

If we up-sample, then we can represent a data pixel by many image or screen pixels. In the following example, we greatly over-sample the small data matrix.

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801+9)
[a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.rand](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html#numpy.random.rand "numpy.random.rand")
(4, 4)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(6.5, 4), layout\='compressed')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([asmall](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='viridis')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("interpolation='auto'\\nstage='auto'")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([asmall](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='viridis', interpolation\="nearest",
              interpolation\_stage\="data")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("interpolation='nearest'\\nstage='data'")
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![interpolation='auto' stage='auto', interpolation='nearest' stage='data'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_009_2_00x.png)

The _interpolation_ keyword argument can be used to smooth the pixels if desired. However, that almost always is better done in data space, rather than in RGBA space where the filters can cause colors that are not in the colormap to be the result of the interpolation. In the following example, note that when the interpolation is 'rgba' there are red colors as interpolation artifacts. Therefore, the default 'auto' choice for _interpolation\_stage_ is set to be the same as 'data' when up-sampling is greater than a factor of three:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(1, 2, figsize\=(6.5, 4), layout\='compressed')
[im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].imshow([a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='viridis', interpolation\='sinc', interpolation\_stage\='data')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title("interpolation='sinc'\\nstage='data'\\n(default for upsampling)")
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].imshow([a](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='viridis', interpolation\='sinc', interpolation\_stage\='rgba')
[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[1\].set\_title("interpolation='sinc'\\nstage='rgba'")
[fig.colorbar](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.colorbar.html#matplotlib.figure.Figure.colorbar "matplotlib.figure.Figure.colorbar")
([im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, shrink\=0.7, extend\='both')

![interpolation='sinc' stage='data' (default for upsampling), interpolation='sinc' stage='rgba'](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_010_2_00x.png)

Avoiding resampling[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_antialiasing.html#avoiding-resampling "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to avoid resampling data when making an image. One method is to simply save to a vector backend (pdf, eps, svg) and use `interpolation='none'`. Vector backends allow embedded images, however be aware that some vector image viewers may smooth image pixels.

The second method is to exactly match the size of your axes to the size of your data. The following figure is exactly 2 inches by 2 inches, and if the dpi is 200, then the 400x400 data is not resampled at all. If you download this image and zoom in an image viewer you should see the individual stripes on the left hand side (note that if you have a non hiDPI or "retina" screen, the html may serve a 100x100 version of the image, which will be downsampled.)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(2, 2))
[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [fig.add\_axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.add_axes.html#matplotlib.figure.Figure.add_axes "matplotlib.figure.Figure.add_axes")
((0, 0, 1, 1))
[ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([aa](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:400, :400\], [cmap](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LinearSegmentedColormap.html#matplotlib.colors.LinearSegmentedColormap "matplotlib.colors.LinearSegmentedColormap")
\='RdBu\_r', interpolation\='nearest')
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![image antialiasing](https://matplotlib.org/stable/_images/sphx_glr_image_antialiasing_011_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
    

**Total running time of the script:** (0 minutes 10.533 seconds)

[`Download Jupyter notebook: image_antialiasing.ipynb`](https://matplotlib.org/stable/_downloads/2fbe4413b0e026535c43cbc125dcdd6c/image_antialiasing.ipynb)

[`Download Python source code: image_antialiasing.py`](https://matplotlib.org/stable/_downloads/b6b8bdee6cb17ac313bed674ef0b372b/image_antialiasing.py)

[`Download zipped: image_antialiasing.zip`](https://matplotlib.org/stable/_downloads/9df878d7230ef27700e412b745f96d30/image_antialiasing.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page