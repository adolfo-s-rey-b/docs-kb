[Skip to main content](https://matplotlib.org/stable/users/explain/colors/colormaps.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/colors/colormaps.html#sphx-glr-download-users-explain-colors-colormaps-py)
 to download the full example code.

Choosing Colormaps in Matplotlib[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#choosing-colormaps-in-matplotlib "Link to this heading")

===============================================================================================================================================================

Matplotlib has a number of built-in colormaps accessible via [`matplotlib.colormaps`](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.colormaps "matplotlib.colormaps")
. There are also external libraries that have many extra colormaps, which can be viewed in the [Third-party colormaps](https://matplotlib.org/mpl-third-party/#colormaps-and-styles)
 section of the Matplotlib documentation. Here we briefly discuss how to choose between the many options. For help on creating your own colormaps, see [Creating Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormap-manipulation.html#colormap-manipulation)
.

To get a list of all registered colormaps, you can do:

from matplotlib import colormaps
list(colormaps)

Overview[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#overview "Link to this heading")

---------------------------------------------------------------------------------------------------------------

The idea behind choosing a good colormap is to find a good representation in 3D colorspace for your data set. The best colormap for any given data set depends on many things including:

*   Whether representing form or metric data ([\[Ware\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#ware)
    )
    
*   Your knowledge of the data set (_e.g._, is there a critical value from which the other values deviate?)
    
*   If there is an intuitive color scheme for the parameter you are plotting
    
*   If there is a standard in the field the audience may be expecting
    

For many applications, a perceptually uniform colormap is the best choice; i.e. a colormap in which equal steps in data are perceived as equal steps in the color space. Researchers have found that the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue. Therefore, colormaps which have monotonically increasing lightness through the colormap will be better interpreted by the viewer. Wonderful examples of perceptually uniform colormaps can be found in the [Third-party colormaps](https://matplotlib.org/mpl-third-party/#colormaps-and-styles)
 section as well.

Color can be represented in 3D space in various ways. One way to represent color is using CIELAB. In CIELAB, color space is represented by lightness, \\(L^\*\\); red-green, \\(a^\*\\); and yellow-blue, \\(b^\*\\). The lightness parameter \\(L^\*\\) can then be used to learn more about how the matplotlib colormaps will be perceived by viewers.

An excellent starting resource for learning about human perception of colormaps is from [\[IBM\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#ibm)
.

Classes of colormaps[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#classes-of-colormaps "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

Colormaps are often split into several categories based on their function (see, _e.g._, [\[Moreland\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#moreland)
):

1.  Sequential: change in lightness and often saturation of color incrementally, often using a single hue; should be used for representing information that has ordering.
    
2.  Diverging: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero.
    
3.  Cyclic: change in lightness of two different colors that meet in the middle and beginning/end at an unsaturated color; should be used for values that wrap around at the endpoints, such as phase angle, wind direction, or time of day.
    
4.  Qualitative: often are miscellaneous colors; should be used to represent information which does not have ordering or relationships.
    

from colorspacious import cspace\_converter

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

First, we'll show the range of each colormap. Note that some seem to change more "quickly" than others.

[cmaps](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {}

[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 256)
[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

def plot\_color\_gradients(category, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    \# Create figure and adjust figure height to number of colormaps
    nrows \= len([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
    figh \= 0.35 + 0.15 + (nrows + (nrows \- 1) \* 0.1) \* 0.22
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=nrows + 1, figsize\=(6.4, figh))
    [fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(top\=1 \- 0.35 / figh, bottom\=0.15 / figh,
                        left\=0.2, right\=0.99)
    [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0\].set\_title(f'{category} colormaps', fontsize\=14)

    for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, name in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
        [ax.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, aspect\='auto', [cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\[name\])
        [ax.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text "matplotlib.axes.Axes.text")
(\-0.01, 0.5, name, va\='center', ha\='right', fontsize\=10,
                transform\=[ax.transAxes](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.BboxTransformTo "matplotlib.transforms.BboxTransformTo")
)

    \# Turn off \*all\* ticks & spines, not just the ones with colormaps.
    for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
:
        [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()

    \# Save colormap list for later.
    [cmaps](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[category\] \= [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")

### Sequential[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#sequential "Link to this heading")

For the Sequential plots, the lightness value increases monotonically through the colormaps. This is good. Some of the \\(L^\*\\) values in the colormaps span from 0 to 100 (binary and the other grayscale), and others start around \\(L^\*=20\\). Those that have a smaller range of \\(L^\*\\) will accordingly have a smaller perceptual range. Note also that the \\(L^\*\\) function varies amongst the colormaps: some are approximately linear in \\(L^\*\\) and others are more curved.

plot\_color\_gradients('Perceptually Uniform Sequential',
                     \['viridis', 'plasma', 'inferno', 'magma', 'cividis'\])

![Perceptually Uniform Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_001_2_00x.png)

plot\_color\_gradients('Sequential',
                     \['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',\
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',\
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'\])

![Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_002_2_00x.png)

### Sequential2[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#sequential2 "Link to this heading")

Many of the \\(L^\*\\) values from the Sequential2 plots are monotonically increasing, but some (autumn, cool, spring, and winter) plateau or even go both up and down in \\(L^\*\\) space. Others (afmhot, copper, gist\_heat, and hot) have kinks in the \\(L^\*\\) functions. Data that is being represented in a region of the colormap that is at a plateau or kink will lead to a perception of banding of the data in those values in the colormap (see [\[mycarta-banding\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#mycarta-banding)
 for an excellent example of this).

plot\_color\_gradients('Sequential (2)',
                     \['gray', 'bone', 'pink', 'spring', 'summer', 'autumn',\
                      'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist\_heat',\
                      'copper'\])

![Sequential (2) colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_003_2_00x.png)

Discouraged

For backward compatibility we additionally support the following colormap names, which are identical to other builtin colormaps. Their use is discouraged. Use the suggested replacement instead.

| Colormap | Use identical replacement instead |
| --- | --- |
| gist\_gray | gray |
| gist\_yarg | gray\_r |
| binary | gray\_r |

### Diverging[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#diverging "Link to this heading")

For the Diverging maps, we want to have monotonically increasing \\(L^\*\\) values up to a maximum, which should be close to \\(L^\*=100\\), followed by monotonically decreasing \\(L^\*\\) values. We are looking for approximately equal minimum \\(L^\*\\) values at opposite ends of the colormap. By these measures, BrBG and RdBu are good options. coolwarm is a good option, but it doesn't span a wide range of \\(L^\*\\) values (see grayscale section below).

Berlin, Managua, and Vanimo are dark-mode diverging colormaps, with minimum lightness at the center, and maximum at the extremes. These are taken from F. Crameri's [\[scientific-colour-maps\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#scientific-colour-maps)
 version 8.0.1.

plot\_color\_gradients('Diverging',
                     \['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',\
                      'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',\
                      'berlin', 'managua', 'vanimo'\])

![Diverging colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_004_2_00x.png)

### Cyclic[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#cyclic "Link to this heading")

For Cyclic maps, we want to start and end on the same color, and meet a symmetric center point in the middle. \\(L^\*\\) should change monotonically from start to middle, and inversely from middle to end. It should be symmetric on the increasing and decreasing side, and only differ in hue. At the ends and middle, \\(L^\*\\) will reverse direction, which should be smoothed in \\(L^\*\\) space to reduce artifacts. See [\[kovesi-colormaps\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#kovesi-colormaps)
 for more information on the design of cyclic maps.

The often-used HSV colormap is included in this set of colormaps, although it is not symmetric to a center point. Additionally, the \\(L^\*\\) values vary widely throughout the colormap, making it a poor choice for representing data for viewers to see perceptually. See an extension on this idea at [\[mycarta-jet\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#mycarta-jet)
.

plot\_color\_gradients('Cyclic', \['twilight', 'twilight\_shifted', 'hsv'\])

![Cyclic colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_005_2_00x.png)

### Qualitative[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#qualitative "Link to this heading")

Qualitative colormaps are not aimed at being perceptual maps, but looking at the lightness parameter can verify that for us. The \\(L^\*\\) values move all over the place throughout the colormap, and are clearly not monotonically increasing. These would not be good options for use as perceptual colormaps.

plot\_color\_gradients('Qualitative',
                     \['Pastel1', 'Pastel2', 'Paired', 'Accent', 'okabe\_ito',\
                      'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20',\
                      'tab20b', 'tab20c'\])

![Qualitative colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_006_2_00x.png)

### Miscellaneous[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#miscellaneous "Link to this heading")

Some of the miscellaneous colormaps have particular uses for which they have been created. For example, gist\_earth, ocean, and terrain all seem to be created for plotting topography (green/brown) and water depths (blue) together. We would expect to see a divergence in these colormaps, then, but multiple kinks may not be ideal, such as in gist\_earth and terrain. CMRmap was created to convert well to grayscale, though it does appear to have some small kinks in \\(L^\*\\). cubehelix was created to vary smoothly in both lightness and hue, but appears to have a small hump in the green hue area. turbo was created to display depth and disparity data.

The often-used jet colormap is included in this set of colormaps. We can see that the \\(L^\*\\) values vary widely throughout the colormap, making it a poor choice for representing data for viewers to see perceptually. See an extension on this idea at [\[mycarta-jet\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#mycarta-jet)
 and [\[turbo\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#turbo)
.

plot\_color\_gradients('Miscellaneous',
                     \['flag', 'prism', 'ocean', 'gist\_earth', 'terrain',\
                      'gist\_stern', 'gnuplot', 'gnuplot2', 'CMRmap',\
                      'cubehelix', 'brg', 'gist\_rainbow', 'rainbow', 'jet',\
                      'turbo', 'nipy\_spectral', 'gist\_ncar'\])

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Miscellaneous colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_007_2_00x.png)

Lightness of Matplotlib colormaps[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#lightness-of-matplotlib-colormaps "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Here we examine the lightness values of the matplotlib colormaps. Note that some documentation on the colormaps is available ([\[list-colormaps\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#list-colormaps)
).

[mpl.rcParams.update](https://docs.python.org/3/library/stdtypes.html#dict.update "builtins.dict.update")
({'font.size': 12})

\# Number of colormap per subplot for particular cmap categories
[\_DSUBS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'Perceptually Uniform Sequential': 5, 'Sequential': 6,
          'Sequential (2)': 6, 'Diverging': 6, 'Cyclic': 3,
          'Qualitative': 4, 'Miscellaneous': 6}

\# Spacing between the colormaps of a subplot
[\_DC](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {'Perceptually Uniform Sequential': 1.4, 'Sequential': 0.7,
       'Sequential (2)': 1.4, 'Diverging': 1.4, 'Cyclic': 1.4,
       'Qualitative': 1.4, 'Miscellaneous': 1.4}

\# Indices to step through colormap
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, 100)

\# Do plot
for [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 in [cmaps](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():

    \# Do subplots so that colormaps have enough space.
    \# Default is 6 colormaps per subplot.
    [dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [\_DSUBS](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.get([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, 6)
    [nsubplots](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= int([np.ceil](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(len([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
) / [dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

    \# squeeze=False to handle similarly the case of a single subplot
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=[nsubplots](https://docs.python.org/3/library/functions.html#int "builtins.int")
, squeeze\=False,
                            figsize\=(7, 2.6\*[nsubplots](https://docs.python.org/3/library/functions.html#int "builtins.int")
))

    for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in enumerate([axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
):

        [locs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[\]  \# locations for text labels

        for [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in enumerate([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\*[dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")\
:([i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
+1)\*[dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\]):

            \# Get RGB values for colormap and convert the colormap in
            \# CAM02-UCS colorspace.  lab\[0, :, 0\] is the lightness.
            [rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\[[cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\]([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\[[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :, :3\]
            [lab](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= cspace\_converter("sRGB1", "CAM02-UCS")([rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

            \# Plot colormap L values.  Do separately for each category
            \# so each plot can be pretty.  To make scatter markers change
            \# color along plot:
            \# https://stackoverflow.com/q/8202605/

            if [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \== 'Sequential':
                \# These colormaps all start at high lightness, but we want them
                \# reversed to look nice in the plot, so reverse the order.
                [y\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [lab](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, ::\-1, 0\]
                [c\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[::\-1\]
            else:
                [y\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [lab](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :, 0\]
                [c\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")

            [dc](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= [\_DC](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.get([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, 1.4)  \# cmaps horizontal spacing
            [ax.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter "matplotlib.axes.Axes.scatter")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dc](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [y\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, c\=[c\_](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, s\=300, linewidths\=0.0)

            \# Store locations for colormap labels
            if [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('Perceptually Uniform Sequential',
                                 'Sequential'):
                [locs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[\-1\] + [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dc](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
            elif [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in ('Diverging', 'Qualitative', 'Cyclic',
                                   'Miscellaneous', 'Sequential (2)'):
                [locs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
.append([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[int([x.size](https://docs.python.org/3/library/functions.html#int "builtins.int")\
/2.)\] + [j](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dc](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

        \# Set up the axis limits:
        \#   \* the 1st subplot is used as a reference for the x-axis limits
        \#   \* lightness values goes from 0 to 100 (y-axis limits)
        [ax.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, 0\].get\_xlim())
        [ax.set\_ylim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html#matplotlib.axes.Axes.set_ylim "matplotlib.axes.Axes.set_ylim")
(0.0, 100.0)

        \# Set up labels for colormaps
        [ax.xaxis.set\_ticks\_position](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.XAxis.set_ticks_position.html#matplotlib.axis.XAxis.set_ticks_position "matplotlib.axis.XAxis.set_ticks_position")
('top')
        [ticker](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
 \= [mpl.ticker.FixedLocator](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
([locs](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)
        [ax.xaxis.set\_major\_locator](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_locator.html#matplotlib.axis.Axis.set_major_locator "matplotlib.axis.Axis.set_major_locator")
([ticker](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedLocator "matplotlib.ticker.FixedLocator")
)
        [formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
 \= [mpl.ticker.FixedFormatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[[i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\*[dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")\
:([i](https://docs.python.org/3/library/functions.html#int "builtins.int")\
+1)\*[dsub](https://docs.python.org/3/library/functions.html#int "builtins.int")\
\])
        [ax.xaxis.set\_major\_formatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_major_formatter.html#matplotlib.axis.Axis.set_major_formatter "matplotlib.axis.Axis.set_major_formatter")
([formatter](https://matplotlib.org/stable/api/ticker_api.html#matplotlib.ticker.FixedFormatter "matplotlib.ticker.FixedFormatter")
)
        [ax.xaxis.set\_tick\_params](https://matplotlib.org/stable/api/_as_gen/matplotlib.axis.Axis.set_tick_params.html#matplotlib.axis.Axis.set_tick_params "matplotlib.axis.Axis.set_tick_params")
(rotation\=50)
        [ax.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Lightness $L^\*$', fontsize\=12)

    [ax.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 + ' colormaps', fontsize\=14)

    [fig.tight\_layout](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.tight_layout.html#matplotlib.figure.Figure.tight_layout "matplotlib.figure.Figure.tight_layout")
(h\_pad\=0.0, pad\=1.5)
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_008_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_009_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_010_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_011_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_012_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_013_2_00x.png)
*   ![colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_014_2_00x.png)

Grayscale conversion[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#grayscale-conversion "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

It is important to pay attention to conversion to grayscale for color plots, since they may be printed on black and white printers. If not carefully considered, your readers may end up with indecipherable plots because the grayscale changes unpredictably through the colormap.

Conversion to grayscale is done in many different ways [\[bw\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#bw)
. Some of the better ones use a linear combination of the rgb values of a pixel, but weighted according to how we perceive color intensity. A nonlinear method of conversion to grayscale is to use the \\(L^\*\\) values of the pixels. In general, similar principles apply for this question as they do for presenting one's information perceptually; that is, if a colormap is chosen that is monotonically increasing in \\(L^\*\\) values, it will print in a reasonable manner to grayscale.

With this in mind, we see that the Sequential colormaps have reasonable representations in grayscale. Some of the Sequential2 colormaps have decent enough grayscale representations, though some (autumn, spring, summer, winter) have very little grayscale change. If a colormap like this was used in a plot and then the plot was printed to grayscale, a lot of the information may map to the same gray values. The Diverging colormaps mostly vary from darker gray on the outer edges to white in the middle. Some (PuOr and seismic) have noticeably darker gray on one side than the other and therefore are not very symmetric. coolwarm has little range of gray scale and would print to a more uniform plot, losing a lot of detail. Note that overlaid, labeled contours could help differentiate between one side of the colormap vs. the other since color cannot be used once a plot is printed to grayscale. Many of the Qualitative and Miscellaneous colormaps, such as Accent, hsv, jet and turbo, change from darker to lighter and back to darker grey throughout the colormap. This would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale.

[mpl.rcParams.update](https://docs.python.org/3/library/stdtypes.html#dict.update "builtins.dict.update")
({'font.size': 14})

\# Indices to step through colormap.
[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0.0, 1.0, 100)

[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.linspace](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")
(0, 1, 256)
[gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
(([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

def plot\_color\_gradients([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=len([cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
), ncols\=2)
    [fig.subplots\_adjust](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplots_adjust.html#matplotlib.figure.Figure.subplots_adjust "matplotlib.figure.Figure.subplots_adjust")
(top\=0.95, bottom\=0.01, left\=0.2, right\=0.99,
                        wspace\=0.05)
    [fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 + ' colormaps', fontsize\=14, y\=1.0, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\=0.6)

    for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, name in zip([axs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
):

        \# Get RGB values for colormap.
        [rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\[name\]([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)\[[np.newaxis](https://numpy.org/doc/stable/reference/constants.html#numpy.newaxis "numpy.newaxis")\
, :, :3\]

        \# Get colormap in CAM02-UCS colorspace. We want the lightness.
        [lab](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= cspace\_converter("sRGB1", "CAM02-UCS")([rgb](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
        L \= [lab](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[0, :, 0\]
        L \= [np.float32](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float32 "numpy.float32")
([np.vstack](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")
((L, L, L)))

        [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].imshow([gradient](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, aspect\='auto', [cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=[mpl.colormaps](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ColormapRegistry "matplotlib.cm.ColormapRegistry")
\[name\])
        [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[1\].imshow(L, aspect\='auto', [cmap](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\='binary\_r', vmin\=0., vmax\=100.)
        pos \= list([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\[0\].get\_position().bounds)
        x\_text \= pos\[0\] \- 0.01
        y\_text \= pos\[1\] + pos\[3\]/2.
        [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(x\_text, y\_text, name, va\='center', ha\='right', fontsize\=10)

    \# Turn off \*all\* ticks & spines, not just the ones with colormaps.
    for [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 in [axs.flat](https://numpy.org/doc/stable/reference/generated/numpy.flatiter.html#numpy.flatiter "numpy.flatiter")
:
        [ax.set\_axis\_off](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_axis_off.html#matplotlib.axes.Axes.set_axis_off "matplotlib.axes.Axes.set_axis_off")
()

    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

for [cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 in [cmaps](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.items():

    plot\_color\_gradients([cmap\_category](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, [cmap\_list](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
)

*   ![Perceptually Uniform Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_015_2_00x.png)
*   ![Sequential colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_016_2_00x.png)
*   ![Sequential (2) colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_017_2_00x.png)
*   ![Diverging colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_018_2_00x.png)
*   ![Cyclic colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_019_2_00x.png)
*   ![Qualitative colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_020_2_00x.png)
*   ![Miscellaneous colormaps](https://matplotlib.org/stable/_images/sphx_glr_colormaps_021_2_00x.png)

Color vision deficiencies[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#color-vision-deficiencies "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------

There is a lot of information available about color blindness (_e.g._, [\[colorblindness\]](https://matplotlib.org/stable/users/explain/colors/colormaps.html#colorblindness)
). Additionally, there are tools available to convert images to how they look for different types of color vision deficiencies.

The most common form of color vision deficiency involves differentiating between red and green. Thus, avoiding colormaps with both red and green will avoid many problems in general.

References[#](https://matplotlib.org/stable/users/explain/colors/colormaps.html#references "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

\[[Ware](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id1)\
\]

[https://dl.acm.org/doi/10.1109/38.7760](https://dl.acm.org/doi/10.1109/38.7760)

\[[Moreland](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id3)\
\]

[http://www.kennethmoreland.com/color-maps/ColorMapsExpanded.pdf](http://www.kennethmoreland.com/color-maps/ColorMapsExpanded.pdf)

\[[list-colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id10)\
\]

[https://gist.github.com/endolith/2719900#id7](https://gist.github.com/endolith/2719900#id7)

\[[mycarta-banding](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id4)\
\]

[https://mycarta.wordpress.com/2012/10/14/the-rainbow-is-deadlong-live-the-rainbow-part-4-cie-lab-heated-body/](https://mycarta.wordpress.com/2012/10/14/the-rainbow-is-deadlong-live-the-rainbow-part-4-cie-lab-heated-body/)

\[mycarta-jet\] ([1](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id7)
,[2](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id8)
)

[https://mycarta.wordpress.com/2012/10/06/the-rainbow-is-deadlong-live-the-rainbow-part-3/](https://mycarta.wordpress.com/2012/10/06/the-rainbow-is-deadlong-live-the-rainbow-part-3/)

\[[kovesi-colormaps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id6)\
\]

[https://arxiv.org/abs/1509.03700](https://arxiv.org/abs/1509.03700)

\[[bw](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id11)\
\]

[https://tannerhelland.com/3643/grayscale-image-algorithm-vb6/](https://tannerhelland.com/3643/grayscale-image-algorithm-vb6/)

\[[colorblindness](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id12)\
\]

[http://www.color-blindness.com/](http://www.color-blindness.com/)

\[[IBM](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id2)\
\]

[https://doi.org/10.1109/VISUAL.1995.480803](https://doi.org/10.1109/VISUAL.1995.480803)

\[[turbo](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id9)\
\]

[https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html)

\[[scientific-colour-maps](https://matplotlib.org/stable/users/explain/colors/colormaps.html#id5)\
\]

[https://doi.org/10.5281/zenodo.1243862](https://doi.org/10.5281/zenodo.1243862)

**Total running time of the script:** (0 minutes 18.862 seconds)

[`Download Jupyter notebook: colormaps.ipynb`](https://matplotlib.org/stable/_downloads/a58dec1c9a88487f9b1de45f0eb2443c/colormaps.ipynb)

[`Download Python source code: colormaps.py`](https://matplotlib.org/stable/_downloads/b9d28120854d00e968560ceab43ae8e9/colormaps.py)

[`Download zipped: colormaps.zip`](https://matplotlib.org/stable/_downloads/2f54b3d6ec1d413c1311f9167151ce8d/colormaps.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page