[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#main-content)

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
    

matplotlib.colors.make\_norm\_from\_scale[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#matplotlib-colors-make-norm-from-scale "Link to this heading")

==================================================================================================================================================================================================

matplotlib.colors.make\_norm\_from\_scale(_scale\_cls_, _base\_norm\_cls\=None_, _\*_, _init\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/colors.py#L2841-L2887)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#matplotlib.colors.make_norm_from_scale "Link to this definition")

Decorator for building a [`Normalize`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Normalize.html#matplotlib.colors.Normalize "matplotlib.colors.Normalize")
 subclass from a [`ScaleBase`](https://matplotlib.org/stable/api/scale_api.html#matplotlib.scale.ScaleBase "matplotlib.scale.ScaleBase")
 subclass.

After

@make\_norm\_from\_scale(scale\_cls)
class norm\_cls(Normalize):
    ...

_norm\_cls_ is filled with methods so that normalization computations are forwarded to _scale\_cls_ (i.e., _scale\_cls_ is the scale that would be used for the colorbar of a mappable normalized with _norm\_cls_).

If _init_ is not passed, then the constructor signature of _norm\_cls_ will be `norm_cls(vmin=None, vmax=None, clip=False)`; these three parameters will be forwarded to the base class (`Normalize.__init__`), and a _scale\_cls_ object will be initialized with no arguments (other than a dummy axis).

If the _scale\_cls_ constructor takes additional parameters, then _init_ should be passed to [`make_norm_from_scale`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.make_norm_from_scale.html#matplotlib.colors.make_norm_from_scale "matplotlib.colors.make_norm_from_scale")
. It is a callable which is _only_ used for its signature. First, this signature will become the signature of _norm\_cls_. Second, the _norm\_cls_ constructor will bind the parameters passed to it using this signature, extract the bound _vmin_, _vmax_, and _clip_ values, pass those to `Normalize.__init__`, and forward the remaining bound values (including any defaults defined by the signature) to the _scale\_cls_ constructor.

On this page