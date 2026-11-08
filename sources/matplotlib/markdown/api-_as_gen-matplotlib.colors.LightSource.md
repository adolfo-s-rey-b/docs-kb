[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#main-content)

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
    

matplotlib.colors.LightSource[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib-colors-lightsource "Link to this heading")

====================================================================================================================================================================

class matplotlib.colors.LightSource(_azdeg\=315_, _altdeg\=45_, _hsv\_min\_val\=0_, _hsv\_max\_val\=1_, _hsv\_min\_sat\=1_, _hsv\_max\_sat\=0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3803-L4230)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Create a light source coming from the specified azimuth and elevation. Angles are in degrees, with the azimuth measured clockwise from north and elevation up from the zero plane of the surface.

[`shade`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "matplotlib.colors.LightSource.shade")
 is used to produce "shaded" RGB values for a data array. [`shade_rgb`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade_rgb "matplotlib.colors.LightSource.shade_rgb")
 can be used to combine an RGB image with an elevation map. [`hillshade`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.hillshade "matplotlib.colors.LightSource.hillshade")
 produces an illumination map of a surface.

Specify the azimuth (measured clockwise from south) and altitude (measured up from the plane of the surface) of the light source in degrees.

Parameters:

**azdeg**float, default: 315 degrees (from the northwest)

The azimuth (0-360, degrees clockwise from North) of the light source.

**altdeg**float, default: 45 degrees

The altitude (0-90, degrees up from horizontal) of the light source.

**hsv\_min\_val**number, default: 0

The minimum value ("v" in "hsv") that the _intensity_ map can shift the output image to.

**hsv\_max\_val**number, default: 1

The maximum value ("v" in "hsv") that the _intensity_ map can shift the output image to.

**hsv\_min\_sat**number, default: 1

The minimum saturation value that the _intensity_ map can shift the output image to.

**hsv\_max\_sat**number, default: 0

The maximum saturation value that the _intensity_ map can shift the output image to.

Notes

For backwards compatibility, the parameters _hsv\_min\_val_, _hsv\_max\_val_, _hsv\_min\_sat_, and _hsv\_max\_sat_ may be supplied at initialization as well. However, these parameters will only be used if "blend\_mode='hsv'" is passed into [`shade`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "matplotlib.colors.LightSource.shade")
 or [`shade_rgb`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade_rgb "matplotlib.colors.LightSource.shade_rgb")
. See the documentation for [`blend_hsv`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.blend_hsv "matplotlib.colors.LightSource.blend_hsv")
 for more details.

blend\_hsv(_rgb_, _intensity_, _hsv\_max\_sat\=None_, _hsv\_max\_val\=None_, _hsv\_min\_val\=None_, _hsv\_min\_sat\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L4119-L4191)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.blend_hsv "Link to this definition")

Take the input data array, convert to HSV values in the given colormap, then adjust those color values to give the impression of a shaded relief map with a specified light source. RGBA values are returned, which can then be used to plot the shaded image with imshow.

The color of the resulting image will be darkened by moving the (s, v) values (in HSV colorspace) toward (hsv\_min\_sat, hsv\_min\_val) in the shaded regions, or lightened by sliding (s, v) toward (hsv\_max\_sat, hsv\_max\_val) in regions that are illuminated. The default extremes are chose so that completely shaded points are nearly black (s = 1, v = 0) and completely illuminated points are nearly white (s = 0, v = 1).

Parameters:

**rgb**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).

**intensity**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).

**hsv\_max\_sat**number, optional

The maximum saturation value that the _intensity_ map can shift the output image to. If not provided, use the value provided upon initialization.

**hsv\_min\_sat**number, optional

The minimum saturation value that the _intensity_ map can shift the output image to. If not provided, use the value provided upon initialization.

**hsv\_max\_val**number, optional

The maximum value ("v" in "hsv") that the _intensity_ map can shift the output image to. If not provided, use the value provided upon initialization.

**hsv\_min\_val**number, optional

The minimum value ("v" in "hsv") that the _intensity_ map can shift the output image to. If not provided, use the value provided upon initialization.

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 3) RGB array representing the combined images.

blend\_overlay(_rgb_, _intensity_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L4212-L4230)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.blend_overlay "Link to this definition")

Combine an RGB image with an intensity map using "overlay" blending.

Parameters:

**rgb**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).

**intensity**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).

Returns:

ndarray

An (M, N, 3) RGB array representing the combined images.

blend\_soft\_light(_rgb_, _intensity_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L4193-L4210)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.blend_soft_light "Link to this definition")

Combine an RGB image with an intensity map using "soft light" blending, using the "pegtop" formula.

Parameters:

**rgb**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 3) RGB array of floats ranging from 0 to 1 (color image).

**intensity**[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 1) array of floats ranging from 0 to 1 (grayscale image).

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 3) RGB array representing the combined images.

property direction[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.direction "Link to this definition")

The unit vector direction towards the light source.

hillshade(_elevation_, _vert\_exag\=1_, _dx\=1_, _dy\=1_, _fraction\=1.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3870-L3921)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.hillshade "Link to this definition")

Calculate the illumination intensity for a surface using the defined azimuth and elevation for the light source.

This computes the normal vectors for the surface, and then passes them on to [`shade_normals`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade_normals "matplotlib.colors.LightSource.shade_normals")

Parameters:

**elevation**2D array-like

The height values used to generate an illumination map

**vert\_exag**number, optional

The amount to exaggerate the elevation values by when calculating illumination. This can be used either to correct for differences in units between the x-y coordinate system and the elevation coordinate system (e.g. decimal degrees vs. meters) or to exaggerate or de-emphasize topographic effects.

**dx**number, optional

The x-spacing (columns) of the input _elevation_ grid.

**dy**number, optional

The y-spacing (rows) of the input _elevation_ grid.

**fraction**number, optional

Increases or decreases the contrast of the hillshade. Values greater than one will cause intermediate values to move closer to full illumination or shadow (and clipping any values that move beyond 0 or 1). Note that this is not visually or mathematically the same as vertical exaggeration.

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

A 2D array of illumination values between 0-1, where 0 is completely in shadow and 1 is completely illuminated.

shade(_data_, _cmap_, _norm\=None_, _blend\_mode\='overlay'_, _vmin\=None_, _vmax\=None_, _vert\_exag\=1_, _dx\=1_, _dy\=1_, _fraction\=1_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3969-L4043)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade "Link to this definition")

Combine colormapped data values with an illumination intensity map (a.k.a. "hillshade") of the values.

Parameters:

**data**2D array-like

The height values used to generate a shaded map.

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")

The colormap used to color the _data_ array. Note that this must be a [`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
 instance. For example, rather than passing in `cmap='gist_earth'`, use `cmap=plt.get_cmap('gist_earth')` instead.

**norm**[`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 instance, optional

The normalization used to scale values before colormapping. If None, the input will be linearly scaled between its min and max.

**blend\_mode**{'hsv', 'overlay', 'soft'} or callable, optional

The type of blending used to combine the colormapped data values with the illumination intensity. Default is "overlay". Note that for most topographic surfaces, "overlay" or "soft" appear more visually realistic. If a user-defined function is supplied, it is expected to combine an (M, N, 3) RGB array of floats (ranging 0 to 1) with an (M, N, 1) hillshade array (also 0 to 1). (Call signature `func(rgb, illum, **kwargs)`) Additional kwargs supplied to this function will be passed on to the _blend\_mode_ function.

**vmin**float or None, optional

The minimum value used in colormapping _data_. If _None_ the minimum value in _data_ is used. If _norm_ is specified, then this argument will be ignored.

**vmax**float or None, optional

The maximum value used in colormapping _data_. If _None_ the maximum value in _data_ is used. If _norm_ is specified, then this argument will be ignored.

**vert\_exag**number, optional

The amount to exaggerate the elevation values by when calculating illumination. This can be used either to correct for differences in units between the x-y coordinate system and the elevation coordinate system (e.g. decimal degrees vs. meters) or to exaggerate or de-emphasize topography.

**dx**number, optional

The x-spacing (columns) of the input _elevation_ grid.

**dy**number, optional

The y-spacing (rows) of the input _elevation_ grid.

**fraction**number, optional

Increases or decreases the contrast of the hillshade. Values greater than one will cause intermediate values to move closer to full illumination or shadow (and clipping any values that move beyond 0 or 1). Note that this is not visually or mathematically the same as vertical exaggeration.

**\*\*kwargs**

Additional kwargs are passed on to the _blend\_mode_ function.

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (M, N, 4) array of floats ranging between 0-1.

shade\_normals(_normals_, _fraction\=1.0_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L3923-L3967)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade_normals "Link to this definition")

Calculate the illumination intensity for the normal vectors of a surface using the defined azimuth and elevation for the light source.

Imagine an artificial sun placed at infinity in some azimuth and elevation position illuminating our surface. The parts of the surface that slope toward the sun should brighten while those sides facing away should become darker.

Parameters:

**fraction**number, optional

Increases or decreases the contrast of the hillshade. Values greater than one will cause intermediate values to move closer to full illumination or shadow (and clipping any values that move beyond 0 or 1). Note that this is not visually or mathematically the same as vertical exaggeration.

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

A 2D array of illumination values between 0-1, where 0 is completely in shadow and 1 is completely illuminated.

shade\_rgb(_rgb_, _elevation_, _fraction\=1.0_, _blend\_mode\='hsv'_, _vert\_exag\=1_, _dx\=1_, _dy\=1_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L4045-L4117)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#matplotlib.colors.LightSource.shade_rgb "Link to this definition")

Use this light source to adjust the colors of the _rgb_ input array to give the impression of a shaded relief map with the given _elevation_.

Parameters:

**rgb**array-like

An (M, N, 3) RGB array, assumed to be in the range of 0 to 1.

**elevation**array-like

An (M, N) array of the height values used to generate a shaded map.

**fraction**number

Increases or decreases the contrast of the hillshade. Values greater than one will cause intermediate values to move closer to full illumination or shadow (and clipping any values that move beyond 0 or 1). Note that this is not visually or mathematically the same as vertical exaggeration.

**blend\_mode**{'hsv', 'overlay', 'soft'} or callable, optional

The type of blending used to combine the colormapped data values with the illumination intensity. For backwards compatibility, this defaults to "hsv". Note that for most topographic surfaces, "overlay" or "soft" appear more visually realistic. If a user-defined function is supplied, it is expected to combine an (M, N, 3) RGB array of floats (ranging 0 to 1) with an (M, N, 1) hillshade array (also 0 to 1). (Call signature `func(rgb, illum, **kwargs)`) Additional kwargs supplied to this function will be passed on to the _blend\_mode_ function.

**vert\_exag**number, optional

The amount to exaggerate the elevation values by when calculating illumination. This can be used either to correct for differences in units between the x-y coordinate system and the elevation coordinate system (e.g. decimal degrees vs. meters) or to exaggerate or de-emphasize topography.

**dx**number, optional

The x-spacing (columns) of the input _elevation_ grid.

**dy**number, optional

The y-spacing (rows) of the input _elevation_ grid.

**\*\*kwargs**

Additional kwargs are passed on to the _blend\_mode_ function.

Returns:

[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")

An (m, n, 3) array of floats ranging between 0-1.

Examples using `matplotlib.colors.LightSource`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.LightSource.html#examples-using-matplotlib-colors-lightsource "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_shading_example_thumb.png)

[Shading example](https://matplotlib.org/stable/gallery/images_contours_and_fields/shading_example.html)

Shading example

![](https://matplotlib.org/stable/_images/sphx_glr_custom_shaded_3d_surface_thumb.png)

[Custom hillshading in a 3D surface plot](https://matplotlib.org/stable/gallery/mplot3d/custom_shaded_3d_surface.html)

Custom hillshading in a 3D surface plot

![](https://matplotlib.org/stable/_images/sphx_glr_demo_agg_filter_thumb.png)

[AGG filter](https://matplotlib.org/stable/gallery/misc/demo_agg_filter.html)

AGG filter

![](https://matplotlib.org/stable/_images/sphx_glr_mandelbrot_thumb.png)

[Shaded & power normalized rendering](https://matplotlib.org/stable/gallery/showcase/mandelbrot.html)

Shaded & power normalized rendering

![](https://matplotlib.org/stable/_images/sphx_glr_advanced_hillshading_thumb.png)

[Hillshading](https://matplotlib.org/stable/gallery/specialty_plots/advanced_hillshading.html)

Hillshading

![](https://matplotlib.org/stable/_images/sphx_glr_topographic_hillshading_thumb.png)

[Topographic hillshading](https://matplotlib.org/stable/gallery/specialty_plots/topographic_hillshading.html)

Topographic hillshading

On this page