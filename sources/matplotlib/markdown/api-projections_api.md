[Skip to main content](https://matplotlib.org/stable/api/projections_api.html#main-content)

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
    

`matplotlib.projections`[#](https://matplotlib.org/stable/api/projections_api.html#module-matplotlib.projections "Link to this heading")

=========================================================================================================================================

Non-separable transforms that map from data space to screen space.

Projections are defined as [`Axes`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 subclasses. They include the following elements:

*   A transformation from data coordinates into display coordinates.
    
*   An inverse of that transformation. This is used, for example, to convert mouse positions from screen space back into data space.
    
*   Transformations for the gridlines, ticks and ticklabels. Custom projections will often need to place these elements in special locations, and Matplotlib has a facility to help with doing so.
    
*   Setting up default values (overriding [`cla`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.cla.html#matplotlib.axes.Axes.cla "matplotlib.axes.Axes.cla")
    ), since the defaults for a rectilinear Axes may not be appropriate.
    
*   Defining the shape of the Axes, for example, an elliptical Axes, that will be used to draw the background of the plot and for clipping any data elements.
    
*   Defining custom locators and formatters for the projection. For example, in a geographic projection, it may be more convenient to display the grid in degrees, even if the data is in radians.
    
*   Set up interactive panning and zooming. This is left as an "advanced" feature left to the reader, but there is an example of this for polar plots in [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
    .
    
*   Any additional methods for additional convenience or features.
    

Once the projection Axes is defined, it can be used in one of two ways:

*   By defining the class attribute `name`, the projection Axes can be registered with [`matplotlib.projections.register_projection`](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "matplotlib.projections.register_projection")
     and subsequently simply invoked by name:
    
    fig.add\_subplot(projection\="my\_proj\_name")
    
*   For more complex, parameterisable projections, a generic "projection" object may be defined which includes the method `_as_mpl_axes`. `_as_mpl_axes` should take no arguments and return the projection's Axes subclass and a dictionary of additional arguments to pass to the subclass' `__init__` method. Subsequently a parameterised projection can be initialised with:
    
    fig.add\_subplot(projection\=MyProjection(param1\=param1\_value))
    
    where MyProjection is an object which implements a `_as_mpl_axes` method.
    

A full-fledged and heavily annotated example is in [Custom projection](https://matplotlib.org/stable/gallery/misc/custom_projection.html)
. The polar plot functionality in [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html#module-matplotlib.projections.polar "matplotlib.projections.polar")
 may also be of interest.

class matplotlib.projections.ProjectionRegistry[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L69-L88)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.ProjectionRegistry "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A mapping of registered projection names to projection classes.

get\_projection\_class(_name_, _\_error\_cls\=<class 'KeyError'>_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L81-L84)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.ProjectionRegistry.get_projection_class "Link to this definition")

Get a projection class from its _name_.

get\_projection\_names()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L86-L88)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.ProjectionRegistry.get_projection_names "Link to this definition")

Return the names of all projections currently registered.

register(_\*projections_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L75-L79)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.ProjectionRegistry.register "Link to this definition")

Register a new set of projections.

matplotlib.projections.get\_projection\_class(_projection\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L111-L120)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.get_projection_class "Link to this definition")

Get a projection class from its name.

If _projection_ is None, a standard rectilinear projection is returned.

matplotlib.projections.get\_projection\_names()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L86-L88)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.get_projection_names "Link to this definition")

Return the names of all projections currently registered.

matplotlib.projections.register\_projection(_cls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/projections/__init__.py#L107-L108)
[#](https://matplotlib.org/stable/api/projections_api.html#matplotlib.projections.register_projection "Link to this definition")

Built-in projections[#](https://matplotlib.org/stable/api/projections_api.html#built-in-projections "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Matplotlib has built-in support for polar and some geographic projections. See the following pages for more information:

*   [`matplotlib.projections.polar`](https://matplotlib.org/stable/api/projections/polar.html)
    
*   [`matplotlib.projections.geo`](https://matplotlib.org/stable/api/projections/geo.html)
    

On this page