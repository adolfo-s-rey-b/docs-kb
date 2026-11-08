[Skip to main content](https://matplotlib.org/stable/api/patheffects_api.html#main-content)

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
    

`matplotlib.patheffects`[#](https://matplotlib.org/stable/api/patheffects_api.html#module-matplotlib.patheffects "Link to this heading")

=========================================================================================================================================

Defines classes for path effects. The path effects are supported in [`Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
, [`Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
 and [`Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
.

See also

[Path effects guide](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#patheffects-guide)

class matplotlib.patheffects.AbstractPathEffect(_offset\=(0.0, 0.0)_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L17-L68)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

A base class for path effects.

Subclasses should override the `draw_path` method to add effect functionality.

Parameters:

**offset**(float, float), default: (0, 0)

The (x, y) offset to apply to the path, measured in points.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L59-L68)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect.draw_path "Link to this definition")

Derived should override this method. The arguments are the same as [`matplotlib.backend_bases.RendererBase.draw_path()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
 except the first argument is a renderer.

class matplotlib.patheffects.Normal(_offset\=(0.0, 0.0)_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L154-L160)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

The "identity" PathEffect.

The Normal PathEffect's sole purpose is to draw the original artist with no special path effect.

Parameters:

**offset**(float, float), default: (0, 0)

The (x, y) offset to apply to the path, measured in points.

class matplotlib.patheffects.PathEffectRenderer(_path\_effects_, _renderer_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L71-L151)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer "Link to this definition")

Bases: [`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")

Implements a Renderer which contains another renderer.

This proxy then intercepts draw calls, calling the appropriate [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")
 draw method.

Note

Not all methods have been overridden on this RendererBase subclass. It may be necessary to add further methods to extend the PathEffects capabilities further.

Parameters:

**path\_effects**iterable of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

The path effects which this renderer represents.

**renderer**[`RendererBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase "matplotlib.backend_bases.RendererBase")
 subclass

close\_group(_s_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L150-L151)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.close_group "Link to this definition")

Close a grouping element with label _s_.

Only used by the SVG renderer.

copy\_with\_path\_effect(_path\_effects_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L96-L97)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.copy_with_path_effect "Link to this definition")

draw\_markers(_gc_, _marker\_path_, _marker\_trans_, _path_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L111-L127)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_markers "Link to this definition")

Draw a marker at each of _path_'s vertices (excluding control points).

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_path "matplotlib.patheffects.PathEffectRenderer.draw_path")
. Backends may want to override this method in order to draw the marker only once and reuse it multiple times.

Parameters:

**gc**[`GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")

The graphics context.

**marker\_path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

The path for the marker.

**marker\_trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

An affine transform applied to the marker.

**path**[`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")

The locations to draw the markers.

**trans**[`Transform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Transform "matplotlib.transforms.Transform")

An affine transform applied to the path.

**rgbFace**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, optional

draw\_path(_gc_, _tpath_, _affine_, _rgbFace\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L106-L109)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_path "Link to this definition")

Draw a [`Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
 instance using the given affine transform.

draw\_path\_collection(_gc_, _master\_transform_, _paths_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L129-L145)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_path_collection "Link to this definition")

Draw a collection of _paths_.

Each path is first transformed by the corresponding entry in _all\_transforms_ (a list of (3, 3) matrices) and then by _master\_transform_. They are then translated by the corresponding entry in _offsets_, which has been first transformed by _offset\_trans_.

_facecolors_, _edgecolors_, _linewidths_, _linestyles_, _antialiased_ and _hatchcolors_ are lists that set the corresponding properties.

Added in version 3.11: Allow _hatchcolors_ to be specified.

_offset\_position_ is unused now, but the argument is kept for backwards compatibility.

The base (fallback) implementation makes multiple calls to [`draw_path`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_path "matplotlib.patheffects.PathEffectRenderer.draw_path")
. Backends may want to override this in order to render each set of path data only once, and then reference that path multiple times with the different offsets, colors, styles etc. The generator methods `_iter_collection_raw_paths` and `_iter_collection` are provided to help with (and standardize) the implementation across backends. It is highly recommended to use those generators, so that changes to the behavior of [`draw_path_collection`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.draw_path_collection "matplotlib.patheffects.PathEffectRenderer.draw_path_collection")
 can be made globally.

open\_group(_s_, _gid\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L147-L148)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathEffectRenderer.open_group "Link to this definition")

Open a grouping element with label _s_ and _gid_ (if set) as id.

Only used by the SVG renderer.

class matplotlib.patheffects.PathPatchEffect(_offset\=(0, 0)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L343-L371)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathPatchEffect "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

Draws a [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 instance whose Path comes from the original PathEffect artist.

Parameters:

**offset**(float, float), default: (0, 0)

The (x, y) offset to apply to the path, in points.

**\*\*kwargs**

All keyword arguments are passed through to the [`PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 constructor. The properties which cannot be overridden are "path", "clip\_box" "transform" and "clip\_path".

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L364-L371)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathPatchEffect.draw_path "Link to this definition")

Derived should override this method. The arguments are the same as [`matplotlib.backend_bases.RendererBase.draw_path()`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.RendererBase.draw_path "matplotlib.backend_bases.RendererBase.draw_path")
 except the first argument is a renderer.

class matplotlib.patheffects.SimpleLineShadow(_offset\=(2, \-2)_, _shadow\_color\='k'_, _alpha\=0.3_, _rho\=0.3_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L286-L340)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimpleLineShadow "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

A simple shadow via a line.

Parameters:

**offset**(float, float), default: (2, -2)

The (x, y) offset to apply to the path, in points.

**shadow\_color**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)
, default: 'black'

The shadow color. A value of `None` takes the original artist's color with a scale factor of _rho_.

**alpha**float, default: 0.3

The alpha transparency of the created shadow patch.

**rho**float, default: 0.3

A scale factor to apply to the rgbFace color if _shadow\_color_ is `None`.

**\*\*kwargs**

Extra keywords are stored and passed through to `AbstractPathEffect._update_gc()`.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L319-L340)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimpleLineShadow.draw_path "Link to this definition")

Overrides the standard draw\_path to add the shadow offset and necessary color changes for the shadow.

class matplotlib.patheffects.SimplePatchShadow(_offset\=(2, \-2)_, _shadow\_rgbFace\=None_, _alpha\=None_, _rho\=0.3_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L218-L280)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

A simple shadow via a filled patch.

Parameters:

**offset**(float, float), default: (2, -2)

The (x, y) offset of the shadow in points.

**shadow\_rgbFace**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The shadow color.

**alpha**float, default: 0.3

The alpha transparency of the created shadow patch.

**rho**float, default: 0.3

A scale factor to apply to the rgbFace color if _shadow\_rgbFace_ is not specified.

**\*\*kwargs**

Extra keywords are stored and passed through to `AbstractPathEffect._update_gc()`.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L257-L280)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow.draw_path "Link to this definition")

Overrides the standard draw\_path to add the shadow offset and necessary color changes for the shadow.

class matplotlib.patheffects.Stroke(_offset\=(0, 0)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L193-L212)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

A line based PathEffect which re-draws a stroke.

The path will be stroked with its gc updated with the given keyword arguments, i.e., the keyword arguments should be valid gc parameter values.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L205-L212)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke.draw_path "Link to this definition")

Draw the path with updated gc.

class matplotlib.patheffects.TickedStroke(_offset\=(0, 0)_, _spacing\=10.0_, _angle\=45.0_, _length\=np.float64(1.4142135623730951)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L374-L508)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "Link to this definition")

Bases: [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")

A line-based PathEffect which draws a path with a ticked style.

This line style is frequently used to represent constraints in optimization. The ticks may be used to indicate that one side of the line is invalid or to represent a closed boundary of a domain (i.e. a wall or the edge of a pipe).

The spacing, length, and angle of ticks can be controlled.

This line style is sometimes referred to as a hatched line.

See also the [TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)
 example.

Parameters:

**offset**(float, float), default: (0, 0)

The (x, y) offset to apply to the path, in points.

**spacing**float, default: 10.0

The spacing between ticks in points.

**angle**float, default: 45.0

The angle between the path and the tick in degrees. The angle is measured as if you were an ant walking along the curve, with zero degrees pointing directly ahead, 90 to your left, -90 to your right, and 180 behind you. To change side of the ticks, change sign of the angle.

**length**float, default: 1.414

The length of the tick relative to spacing. Recommended length = 1.414 (sqrt(2)) when angle=45, length=1.0 when angle=90 and length=2.0 when angle=60.

**\*\*kwargs**

Extra keywords are stored and passed through to `AbstractPathEffect._update_gc()`.

Examples

See [TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)
.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L425-L508)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke.draw_path "Link to this definition")

Draw the path with updated gc.

class matplotlib.patheffects.withSimplePatchShadow(_offset\=(2, \-2)_, _shadow\_rgbFace\=None_, _alpha\=None_, _rho\=0.3_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L168-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withSimplePatchShadow "Link to this definition")

Bases: [`SimplePatchShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "matplotlib.patheffects.SimplePatchShadow")

A shortcut PathEffect for applying [`SimplePatchShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "matplotlib.patheffects.SimplePatchShadow")
 and then drawing the original Artist.

With this class you can use

artist.set\_path\_effects(\[patheffects.withSimplePatchShadow()\])

as a shortcut for

artist.set\_path\_effects(\[patheffects.SimplePatchShadow(),\
                         patheffects.Normal()\])

Parameters:

**offset**(float, float), default: (2, -2)

The (x, y) offset of the shadow in points.

**shadow\_rgbFace**[color](https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def)

The shadow color.

**alpha**float, default: 0.3

The alpha transparency of the created shadow patch.

**rho**float, default: 0.3

A scale factor to apply to the rgbFace color if _shadow\_rgbFace_ is not specified.

**\*\*kwargs**

Extra keywords are stored and passed through to `AbstractPathEffect._update_gc()`.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L169-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withSimplePatchShadow.draw_path "Link to this definition")

Overrides the standard draw\_path to add the shadow offset and necessary color changes for the shadow.

class matplotlib.patheffects.withStroke(_offset\=(0, 0)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L168-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke "Link to this definition")

Bases: [`Stroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")

A shortcut PathEffect for applying [`Stroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")
 and then drawing the original Artist.

With this class you can use

artist.set\_path\_effects(\[patheffects.withStroke()\])

as a shortcut for

artist.set\_path\_effects(\[patheffects.Stroke(),\
                         patheffects.Normal()\])

The path will be stroked with its gc updated with the given keyword arguments, i.e., the keyword arguments should be valid gc parameter values.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L169-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withStroke.draw_path "Link to this definition")

Draw the path with updated gc.

class matplotlib.patheffects.withTickedStroke(_offset\=(0, 0)_, _spacing\=10.0_, _angle\=45.0_, _length\=np.float64(1.4142135623730951)_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L168-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke "Link to this definition")

Bases: [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")

A shortcut PathEffect for applying [`TickedStroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.TickedStroke "matplotlib.patheffects.TickedStroke")
 and then drawing the original Artist.

With this class you can use

artist.set\_path\_effects(\[patheffects.withTickedStroke()\])

as a shortcut for

artist.set\_path\_effects(\[patheffects.TickedStroke(),\
                         patheffects.Normal()\])

Parameters:

**offset**(float, float), default: (0, 0)

The (x, y) offset to apply to the path, in points.

**spacing**float, default: 10.0

The spacing between ticks in points.

**angle**float, default: 45.0

The angle between the path and the tick in degrees. The angle is measured as if you were an ant walking along the curve, with zero degrees pointing directly ahead, 90 to your left, -90 to your right, and 180 behind you. To change side of the ticks, change sign of the angle.

**length**float, default: 1.414

The length of the tick relative to spacing. Recommended length = 1.414 (sqrt(2)) when angle=45, length=1.0 when angle=90 and length=2.0 when angle=60.

**\*\*kwargs**

Extra keywords are stored and passed through to `AbstractPathEffect._update_gc()`.

Examples

See [TickedStroke patheffect](https://matplotlib.org/stable/gallery/misc/tickedstroke_demo.html)
.

draw\_path(_renderer_, _gc_, _tpath_, _affine_, _rgbFace_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/patheffects.py#L169-L171)
[#](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withTickedStroke.draw_path "Link to this definition")

Draw the path with updated gc.

On this page