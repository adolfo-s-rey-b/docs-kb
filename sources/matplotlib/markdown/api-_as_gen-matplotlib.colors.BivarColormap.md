[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#main-content)

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
    

matplotlib.colors.BivarColormap[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib-colors-bivarcolormap "Link to this heading")

==========================================================================================================================================================================

class matplotlib.colors.BivarColormap(_N\=256_, _M\=256_, _shape\='square'_, _origin\=(0, 0)_, _name\='bivariate colormap'_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1687-L2187)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Base class for all bivariate to RGBA mappings.

Designed as a drop-in replacement for Colormap when using a 2D lookup table. To be used with [`ScalarMappable`](https://matplotlib.org/stable/api/cm_api.html#matplotlib.cm.ScalarMappable "matplotlib.cm.ScalarMappable")
.

Parameters:

**N**int, default: 256

The number of RGB quantization levels along the first axis.

**M**int, default: 256

The number of RGB quantization levels along the second axis.

**shape**{'square', 'circle', 'ignore', 'circleignore'}

*   'square' each variate is clipped to \[0,1\] independently
    
*   'circle' the variates are clipped radially to the center of the colormap, and a circular mask is applied when the colormap is displayed
    
*   'ignore' the variates are not clipped, but instead assigned the 'outside' color
    
*   'circleignore' a circular mask is applied, but the data is not clipped and instead assigned the 'outside' color
    

**origin**(float, float), default: (0,0)

The relative origin of the colormap. Typically (0, 0), for colormaps that are linear on both axis, and (.5, .5) for circular colormaps. Used when getting 1D colormaps from 2D colormaps.

**name**str, optional

The name of the colormap.

\_\_call\_\_(_X_, _alpha\=None_, _bytes\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1739-L1834)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.__call__ "Link to this definition")

Parameters:

**X**tuple (X0, X1), X0 and X1: float or int or array-like

The data value(s) to convert to RGBA.

*   For floats, _X_ should be in the interval `[0.0, 1.0]` to return the RGBA values `X*100` percent along the Colormap.
    
*   For integers, _X_ should be in the interval `[0, Colormap.N)` to return RGBA values _indexed_ from the Colormap with index `X`.\
    \
\
**alpha**float or array-like or None, default: None\
\
Alpha must be a scalar between 0 and 1, a sequence of such floats with shape matching X0, or None.\
\
**bytes**bool, default: False\
\
If False (default), the returned RGBA values will be floats in the interval `[0, 1]` otherwise they will be [`numpy.uint8`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint8 "(in NumPy v2.5)")\
s in the interval `[0, 255]`.\
\
Returns:\
\
Tuple of RGBA values if X is scalar, otherwise an array of\
\
RGBA values with a shape of `X.shape + (4, )`.\
\
copy()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2185-L2187)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.copy "Link to this definition")\
\
Return a copy of the colormap.\
\
get\_bad()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1890-L1892)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.get_bad "Link to this definition")\
\
Get the color for masked values.\
\
get\_outside()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1894-L1896)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.get_outside "Link to this definition")\
\
Get the color for out-of-range values.\
\
property lut[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.lut "Link to this definition")\
\
For external access to the lut, i.e. for displaying the cmap. For circular colormaps this returns a lut with a circular mask.\
\
Internal functions (such as to\_rgb()) should use \_lut which stores the lut without a circular mask A lut without the circular mask is needed in to\_rgb() because the conversion from floats to ints results in some some pixel-requests just outside of the circular mask\
\
property origin[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.origin "Link to this definition")\
\
resampled(_lutshape_, _transposed\=False_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1898-L1966)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.resampled "Link to this definition")\
\
Return a new colormap with _lutshape_ entries.\
\
Note that this function does not move the origin.\
\
Parameters:\
\
**lutshape**tuple of ints or None\
\
The tuple must be of length 2, and each entry is either an int or None.\
\
*   If an int, the corresponding axis is resampled.\
    \
*   If negative the corresponding axis is resampled in reverse\
    \
*   If -1, the axis is inverted\
    \
*   If 1 or None, the corresponding axis is not resampled.\
    \
\
**transposed**bool, default: False\
\
if True, the axes are swapped after resampling\
\
Returns:\
\
BivarColormap\
\
reversed(_axis\_0\=True_, _axis\_1\=True_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1968-L1974)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.reversed "Link to this definition")\
\
Reverses both or one of the axis.\
\
property shape[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.shape "Link to this definition")\
\
transposed()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1976-L1980)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.transposed "Link to this definition")\
\
Transposes the colormap by swapping the order of the axis\
\
with\_extremes(_\*_, _bad\=None_, _outside\=None_, _shape\=None_, _origin\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L1982-L2031)\
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.with_extremes "Link to this definition")\
\
Return a copy of the [`BivarColormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap "matplotlib.colors.BivarColormap")\
 with modified attributes.\
\
Note that the _outside_ color is only relevant if [`shape`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BivarColormap.html#matplotlib.colors.BivarColormap.shape "matplotlib.colors.BivarColormap.shape")\
 = 'ignore' or 'circleignore'.\
\
Parameters:\
\
**bad**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
, optional\
\
If given, the _bad_ value is set accordingly in the copy.\
\
**outside**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)\
, optional\
\
If given and shape is 'ignore' or 'circleignore', values _outside_ the colormap are colored accordingly in the copy.\
\
**shape**{'square', 'circle', 'ignore', 'circleignore'}\
\
*   If 'square' each variate is clipped to \[0,1\] independently\
    \
*   If 'circle' the variates are clipped radially to the center of the colormap, and a circular mask is applied when the colormap is displayed\
    \
*   If 'ignore' the variates are not clipped, but instead assigned the _outside_ color\
    \
*   If 'circleignore' a circular mask is applied, but the data is not clipped and instead assigned the _outside_ color\
    \
\
**origin**(float, float)\
\
The relative origin of the colormap. Typically (0, 0), for colormaps that are linear on both axis, and (.5, .5) for circular colormaps. Used when getting 1D colormaps from 2D colormaps.\
\
Returns:\
\
BivarColormap\
\
copy of self with attributes set\
\
On this page