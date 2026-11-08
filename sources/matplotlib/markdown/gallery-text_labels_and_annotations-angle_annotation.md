[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#sphx-glr-download-gallery-text-labels-and-annotations-angle-annotation-py)
 to download the full example code.

Scale invariant angle label[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#scale-invariant-angle-label "Link to this heading")

===========================================================================================================================================================================

This example shows how to create a scale invariant angle annotation. It is often useful to mark angles between lines or inside shapes with a circular arc. While Matplotlib provides an [`Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
, an inherent problem when directly using it for such purposes is that an arc being circular in data space is not necessarily circular in display space. Also, the arc's radius is often best defined in a coordinate system which is independent of the actual data coordinates - at least if you want to be able to freely zoom into your plot without the annotation growing to infinity.

This calls for a solution where the arc's center is defined in data space, but its radius in a physical unit like points or pixels, or as a ratio of the Axes dimension. The following `AngleAnnotation` class provides such solution.

The example below serves two purposes:

*   It provides a ready-to-use solution for the problem of easily drawing angles in graphs.
    
*   It shows how to subclass a Matplotlib artist to enhance its functionality, as well as giving a hands-on example on how to use Matplotlib's [transform system](https://matplotlib.org/stable/users/explain/artists/transforms_tutorial.html#transforms-tutorial)
    .
    

If mainly interested in the former, you may copy the below class and jump to the [Usage](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#angle-annotation-usage)
 section.

AngleAnnotation class[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#angleannotation-class "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The essential idea here is to subclass [`Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
 and set its transform to the [`IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
, making the parameters of the arc defined in pixel space. We then override the `Arc`'s attributes `_center`, `theta1`, `theta2`, `width` and `height` and make them properties, coupling to internal methods that calculate the respective parameters each time the attribute is accessed and thereby ensuring that the arc in pixel space stays synchronized with the input points and size. For example, each time the arc's drawing method would query its `_center` attribute, instead of receiving the same number all over again, it will instead receive the result of the `get_center_in_pixels` method we defined in the subclass. This method transforms the center in data coordinates to pixels via the Axes transform `ax.transData`. The size and the angles are calculated in a similar fashion, such that the arc changes its shape automatically when e.g. zooming or panning interactively.

The functionality of this class allows to annotate the arc with a text. This text is a [`Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
 stored in an attribute `text`. Since the arc's position and radius are defined only at draw time, we need to update the text's position accordingly. This is done by reimplementing the `Arc`'s `draw()` method to let it call an updating method for the text.

The arc and the text will be added to the provided Axes at instantiation: it is hence not strictly necessary to keep a reference to it.

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import [Arc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
from matplotlib.transforms import Bbox, [IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
, [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")

class AngleAnnotation([Arc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
):
    """
    Draws an arc between two vectors which appears circular in display space.
    """
    def \_\_init\_\_(self, xy, [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
, size\=75, unit\="points", [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=None,
                 [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\="", textposition\="inside", text\_kw\=None, \*\*kwargs):
        """
        Parameters
        ----------
        xy, p1, p2 : tuple or array of two floats
            Center position and two points. Angle annotation is drawn between
            the two vectors connecting \*p1\* and \*p2\* with \*xy\*, respectively.
            Units are data coordinates.

        size : float
            Diameter of the angle annotation in units specified by \*unit\*.

        unit : str
            One of the following strings to specify the unit of \*size\*:

            \* "pixels": pixels
            \* "points": points, use points instead of pixels to not have a
              dependence on the DPI
            \* "axes width", "axes height": relative units of Axes width, height
            \* "axes min", "axes max": minimum or maximum of relative Axes
              width, height

        ax : \`matplotlib.axes.Axes\`, default: current Axes
            The Axes to add the angle annotation to.

        text : str
            The text to mark the angle with.

        textposition : {"inside", "outside", "edge"}
            Whether to show the text in- or outside the arc. "edge" can be used
            for custom positions anchored at the arc's edge.

        text\_kw : dict
            Dictionary of arguments passed to the Annotation.

        \*\*kwargs
            Further parameters are passed to \`matplotlib.patches.Arc\`. Use this
            to specify, color, linewidth etc. of the arc.

        """
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 or [plt.gca](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.gca.html#matplotlib.pyplot.gca "matplotlib.pyplot.gca")
()
        self.\_xydata \= xy  \# in data coordinates
        self.vec1 \= [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
        self.vec2 \= [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
        self.size \= size
        self.unit \= unit
        self.textposition \= textposition

        super().\_\_init\_\_(self.\_xydata, size, size, angle\=0.0,
                         theta1\=self.theta1, theta2\=self.theta2, \*\*kwargs)

        self.set\_transform([IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
())
        self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.add\_patch(self)

        self.[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(ha\="center", va\="center",
                       xycoords\=[IdentityTransform](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
(),
                       xytext\=(0, 0), textcoords\="offset points",
                       annotation\_clip\=True)
        self.[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
.update(text\_kw or {})
        self.[text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.annotate([text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, xy\=self.\_center, \*\*self.[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

    def get\_size(self):
        factor \= 1.
        if self.unit \== "points":
            factor \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.figure.dpi / 72.
        elif self.unit\[:4\] \== "axes":
            b \= [TransformedBbox](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
([Bbox.unit](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox.unit "matplotlib.transforms.Bbox.unit")
(), self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transAxes)
            dic \= {"max": max(b.width, b.height),
                   "min": min(b.width, b.height),
                   "width": b.width, "height": b.height}
            factor \= dic\[self.unit\[5:\]\]
        return self.size \* factor

    def set\_size(self, size):
        self.size \= size

    def get\_center\_in\_pixels(self):
        """return center in pixels"""
        return self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transData.transform(self.\_xydata)

    def set\_center(self, xy):
        """set center in data coordinates"""
        self.\_xydata \= xy

    def get\_theta(self, vec):
        vec\_in\_pixels \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.transData.transform(vec) \- self.\_center
        return [np.rad2deg](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.arctan2](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(vec\_in\_pixels\[1\], vec\_in\_pixels\[0\]))

    def get\_theta1(self):
        return self.get\_theta(self.vec1)

    def get\_theta2(self):
        return self.get\_theta(self.vec2)

    def set\_theta(self, angle):
        pass

    \# Redefine attributes of the Arc to always give values in pixel space
    \_center \= property(get\_center\_in\_pixels, set\_center)
    theta1 \= property(get\_theta1, set\_theta)
    theta2 \= property(get\_theta2, set\_theta)
    width \= property(get\_size, set\_size)
    height \= property(get\_size, set\_size)

    \# The following two methods are needed to update the text position.
    def draw(self, renderer):
        self.update\_text()
        super().draw(renderer)

    def update\_text(self):
        c \= self.\_center
        s \= self.get\_size()
        angle\_span \= (self.theta2 \- self.theta1) % 360
        angle \= [np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(self.theta1 + angle\_span / 2)
        r \= s / 2
        if self.textposition \== "inside":
            r \= s / [np.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html#numpy.interp "numpy.interp")
(angle\_span, \[60, 90, 135, 180\],
                                          \[3.3, 3.5, 3.8, 4\])
        self.[text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.xy \= c + r \* [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle)\])
        if self.textposition \== "outside":
            def R90(a, r, w, h):
                if a < [np.arctan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(h/2/(r+w/2)):
                    return [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((r+w/2)\*\*2 + ([np.tan](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(a)\*(r+w/2))\*\*2)
                else:
                    c \= [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
((w/2)\*\*2+(h/2)\*\*2)
                    T \= [np.arcsin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(c \* [np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2 \- a + [np.arcsin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(h/2/c))/r)
                    xy \= r \* [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(a + T), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(a + T)\])
                    xy += [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[w/2, h/2\])
                    return [np.sqrt](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([np.sum](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum "numpy.sum")
(xy\*\*2))

            def R(a, r, w, h):
                aa \= (a % ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/4))\*((a % ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2)) <= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/4) + \\
                     ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/4 \- (a % ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/4)))\*((a % ([np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/2)) \>= [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
/4)
                return R90(aa, r, \*\[w, h\]\[::int([np.sign](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(2\*a)))\])

            bbox \= self.[text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.get\_window\_extent()
            X \= R(angle, r, bbox.width, bbox.height)
            trans \= self.[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
.figure.dpi\_scale\_trans.inverted()
            offs \= trans.transform(((X\-s/2), 0))\[0\] \* 72
            self.[text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.set\_position(\[offs\*[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle), offs\*[np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle)\])

Usage[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#usage "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Required arguments to `AngleAnnotation` are the center of the arc, _xy_, and two points, such that the arc spans between the two vectors connecting _p1_ and _p2_ with _xy_, respectively. Those are given in data coordinates. Further arguments are the _size_ of the arc and its _unit_. Additionally, a _text_ can be specified, that will be drawn either in- or outside of the arc, according to the value of _textposition_. Usage of those arguments is shown below.

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
 \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
()
[fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()  \# Need to draw the figure to define renderer
[ax.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("AngleLabel example")

\# Plot two crossing lines and label each angle between them with the above
\# \`\`AngleAnnotation\`\` tool.
[center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
 \= (4.5, 650)
[p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(2.5, 710), (6.0, 605)\]
[p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(3.0, 275), (5.5, 900)\]
[line1](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*zip(\*[p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[line2](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*zip(\*[p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
[point](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, \= [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*[center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, marker\="o")

am1 \= [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
([center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size\=75, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$\\alpha$")
am2 \= [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
([center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size\=35, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$\\beta$")
am3 \= [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
([center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size\=75, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$\\gamma$")
am4 \= [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
([center](https://docs.python.org/3/library/stdtypes.html#tuple "builtins.tuple")
, [p2](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [p1](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size\=35, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$\\theta$")

\# Showcase some styling options for the angle arc, as well as the text.
[p](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
 \= \[(6.0, 400), (5.3, 410), (5.6, 300)\]
[ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*zip(\*[p](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
))
am5 \= [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
([p](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[1\], [p](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[0\], [p](https://docs.python.org/3/library/stdtypes.html#list "builtins.list")
\[2\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, size\=40, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$\\Phi$",
                      linestyle\="--", color\="gray", textposition\="outside",
                      text\_kw\=dict(fontsize\=16, color\="gray"))

![AngleLabel example](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_001_2_00x.png)

`AngleLabel` options[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/angle_annotation.html#anglelabel-options "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

The _textposition_ and _unit_ keyword arguments may be used to modify the location of the text label, as shown below:

\# Helper function to draw angle easily.
def plot\_angle([ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, pos, angle, length\=0.95, acol\="C0", \*\*kwargs):
    vec2 \= [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(\[[np.cos](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle)), [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
([np.deg2rad](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")\
(angle))\])
    xy \= [np.c\_](https://numpy.org/doc/stable/reference/generated/numpy.c_.html#numpy.c_ "numpy.c_")
\[\[length, 0\], \[0, 0\], vec2\*length\].T + [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
(pos)
    [ax.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
(\*xy.T, color\=acol)
    return [AngleAnnotation](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
(pos, xy\[0\], xy\[2\], [ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
\=[ax](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, \*\*kwargs)

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True)
[fig.suptitle](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.suptitle.html#matplotlib.figure.Figure.suptitle "matplotlib.figure.Figure.suptitle")
("AngleLabel keyword arguments")
[fig.canvas.draw](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.FigureCanvasBase.draw "matplotlib.backend_bases.FigureCanvasBase.draw")
()  \# Need to draw the figure to define renderer

\# Showcase different text positions.
[ax1.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(y\=0.4)
[ax1.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("textposition")
[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict(size\=75, unit\="points", [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$60°$")

am6 \= plot\_angle([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (2.0, 0), 60, textposition\="inside", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am7 \= plot\_angle([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (3.5, 0), 60, textposition\="outside", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am8 \= plot\_angle([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (5.0, 0), 60, textposition\="edge",
                 text\_kw\=dict(bbox\=dict(boxstyle\="round", fc\="w")), \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am9 \= plot\_angle([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (6.5, 0), 60, textposition\="edge",
                 text\_kw\=dict(xytext\=(30, 20), arrowprops\=dict(arrowstyle\="->",
                              connectionstyle\="arc3,rad=-0.2")), \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

for [x](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip(\[2.0, 3.5, 5.0, 6.5\], \['"inside"', '"outside"', '"edge"',\
                                          '"edge", custom arrow'\]):
    [ax1.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, xy\=([x](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0), xycoords\=[ax1.get\_xaxis\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform")
(),
                 bbox\=dict(boxstyle\="round", fc\="w"), ha\="left", fontsize\=8,
                 annotation\_clip\=True)

\# Showcase different size units. The effect of this can best be observed
\# by interactively changing the figure size
[ax2.margins](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html#matplotlib.axes.Axes.margins "matplotlib.axes.Axes.margins")
(y\=0.4)
[ax2.set\_title](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html#matplotlib.axes.Axes.set_title "matplotlib.axes.Axes.set_title")
("unit")
[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= dict([text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
\=r"$60°$", textposition\="outside")

am10 \= plot\_angle([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (2.0, 0), 60, size\=50, unit\="pixels", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am11 \= plot\_angle([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (3.5, 0), 60, size\=50, unit\="points", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am12 \= plot\_angle([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (5.0, 0), 60, size\=0.25, unit\="axes min", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)
am13 \= plot\_angle([ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, (6.5, 0), 60, size\=0.25, unit\="axes max", \*\*[kw](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
)

for [x](https://docs.python.org/3/library/functions.html#float "builtins.float")
, [text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 in zip(\[2.0, 3.5, 5.0, 6.5\], \['"pixels"', '"points"',\
                                          '"axes min"', '"axes max"'\]):
    [ax2.annotate](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
([text](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
, xy\=([x](https://docs.python.org/3/library/functions.html#float "builtins.float")
, 0), xycoords\=[ax2.get\_xaxis\_transform](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.get_xaxis_transform.html#matplotlib.axes.Axes.get_xaxis_transform "matplotlib.axes.Axes.get_xaxis_transform")
(),
                 bbox\=dict(boxstyle\="round", fc\="w"), ha\="left", fontsize\=8,
                 annotation\_clip\=True)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![AngleLabel keyword arguments, textposition, unit](https://matplotlib.org/stable/_images/sphx_glr_angle_annotation_002_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.patches.Arc`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html#matplotlib.patches.Arc "matplotlib.patches.Arc")
    
*   [`matplotlib.axes.Axes.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate "matplotlib.axes.Axes.annotate")
     / [`matplotlib.pyplot.annotate`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.annotate.html#matplotlib.pyplot.annotate "matplotlib.pyplot.annotate")
    
*   [`matplotlib.text.Annotation`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Annotation "matplotlib.text.Annotation")
    
*   [`matplotlib.transforms.IdentityTransform`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.IdentityTransform "matplotlib.transforms.IdentityTransform")
    
*   [`matplotlib.transforms.TransformedBbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.TransformedBbox "matplotlib.transforms.TransformedBbox")
    
*   [`matplotlib.transforms.Bbox`](https://matplotlib.org/stable/api/transformations.html#matplotlib.transforms.Bbox "matplotlib.transforms.Bbox")
    

**Total running time of the script:** (0 minutes 1.610 seconds)

[`Download Jupyter notebook: angle_annotation.ipynb`](https://matplotlib.org/stable/_downloads/d50a07beba6cff38addad517c5db2d2d/angle_annotation.ipynb)

[`Download Python source code: angle_annotation.py`](https://matplotlib.org/stable/_downloads/c293090f798b3d244c3be9d67f90f728/angle_annotation.py)

[`Download zipped: angle_annotation.zip`](https://matplotlib.org/stable/_downloads/8f5aada654666f4ef79abde7a1d69839/angle_annotation.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page