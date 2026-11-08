[Skip to main content](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#sphx-glr-download-users-explain-artists-patheffects-guide-py)
 to download the full example code.

Path effects guide[#](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#path-effects-guide "Link to this heading")

============================================================================================================================================

Defining paths that objects follow on a canvas.

Matplotlib's [`patheffects`](https://matplotlib.org/stable/api/patheffects_api.html#module-matplotlib.patheffects "matplotlib.patheffects")
 module provides functionality to apply a multiple draw stage to any Artist which can be rendered via a [`path.Path`](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path "matplotlib.path.Path")
.

Artists which can have a path effect applied to them include [`patches.Patch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch "matplotlib.patches.Patch")
, [`lines.Line2D`](https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D "matplotlib.lines.Line2D")
, [`collections.Collection`](https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.Collection "matplotlib.collections.Collection")
 and even [`text.Text`](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
. Each artist's path effects can be controlled via the [`Artist.set_path_effects`](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
 method, which takes an iterable of [`AbstractPathEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.AbstractPathEffect "matplotlib.patheffects.AbstractPathEffect")
 instances.

The simplest path effect is the [`Normal`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")
 effect, which simply draws the artist without any effect:

import matplotlib.pyplot as plt

import matplotlib.patheffects as path\_effects

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(5, 1.5))
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, 0.5, 'Hello path effects world!\\nThis is the normal '
                          'path effect.\\nPretty dull, huh?',
                ha\='center', va\='center', size\=20)
[text.set\_path\_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
(\[[path\_effects.Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")\
()\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![patheffects guide](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_001_2_00x.png)

Whilst the plot doesn't look any different to what you would expect without any path effects, the drawing of the text has now been changed to use the path effects framework, opening up the possibilities for more interesting examples.

Adding a shadow[#](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#adding-a-shadow "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

A far more interesting path effect than [`Normal`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")
 is the drop-shadow, which we can apply to any of our path based artists. The classes [`SimplePatchShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "matplotlib.patheffects.SimplePatchShadow")
 and [`SimpleLineShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimpleLineShadow "matplotlib.patheffects.SimpleLineShadow")
 do precisely this by drawing either a filled patch or a line patch below the original artist:

import matplotlib.patheffects as path\_effects

[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [plt.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html#matplotlib.pyplot.text "matplotlib.pyplot.text")
(0.5, 0.5, 'Hello path effects world!',
                path\_effects\=\[[path\_effects.withSimplePatchShadow](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.withSimplePatchShadow "matplotlib.patheffects.withSimplePatchShadow")\
()\])

[plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(\[0, 3, 2, 5\], linewidth\=5, color\='blue',
         path\_effects\=\[[path\_effects.SimpleLineShadow](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimpleLineShadow "matplotlib.patheffects.SimpleLineShadow")\
(),\
                       [path\_effects.Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")\
()\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![patheffects guide](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_002_2_00x.png)

Notice the two approaches to setting the path effects in this example. The first uses the `with*` classes to include the desired functionality automatically followed with the "normal" effect, whereas the latter explicitly defines the two path effects to draw.

Making an Artist stand out[#](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#making-an-artist-stand-out "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

One nice way of making artists visually stand out is to draw an outline in a bold color below the actual artist. The [`Stroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")
 path effect makes this a relatively simple task:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 1))
[text](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.5, 0.5, 'This text stands out because of\\n'
                          'its black border.', color\='white',
                          ha\='center', va\='center', size\=30)
[text.set\_path\_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
(\[[path\_effects.Stroke](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")\
(linewidth\=3, foreground\='black'),\
                       [path\_effects.Normal](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Normal "matplotlib.patheffects.Normal")\
()\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![patheffects guide](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_003_2_00x.png)

It is important to note that this effect only works because we have drawn the text path twice; once with a thick black line, and then once with the original text path on top.

You may have noticed that the keywords to [`Stroke`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.Stroke "matplotlib.patheffects.Stroke")
 and [`SimplePatchShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimplePatchShadow "matplotlib.patheffects.SimplePatchShadow")
 and [`SimpleLineShadow`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.SimpleLineShadow "matplotlib.patheffects.SimpleLineShadow")
 are not the usual Artist keywords (_facecolor_ _edgecolor_, etc.). This is because with these path effects we are operating at lower level of Matplotlib. In fact, the keywords which are accepted are those for a [`matplotlib.backend_bases.GraphicsContextBase`](https://matplotlib.org/stable/api/backend_bases_api.html#matplotlib.backend_bases.GraphicsContextBase "matplotlib.backend_bases.GraphicsContextBase")
 instance, which have been designed for making it easy to create new backends - and not for its user interface.

Greater control of the path effect Artist[#](https://matplotlib.org/stable/users/explain/artists/patheffects_guide.html#greater-control-of-the-path-effect-artist "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

As already mentioned, some of the path effects operate at a lower level than most users will be used to, meaning that setting keywords such as _facecolor_ and _edgecolor_ raise an AttributeError. Luckily there is a generic [`PathPatchEffect`](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathPatchEffect "matplotlib.patheffects.PathPatchEffect")
 path effect which creates a [`patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
 class with the original path. The keywords to this effect are identical to those of [`patches.PathPatch`](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.PathPatch.html#matplotlib.patches.PathPatch "matplotlib.patches.PathPatch")
:

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8.5, 1))
[t](https://matplotlib.org/stable/api/text_api.html#matplotlib.text.Text "matplotlib.text.Text")
 \= [fig.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.text.html#matplotlib.figure.Figure.text "matplotlib.figure.Figure.text")
(0.02, 0.5, 'Hatch shadow', fontsize\=75, weight\=1000, va\='center')
[t.set\_path\_effects](https://matplotlib.org/stable/api/_as_gen/matplotlib.artist.Artist.set_path_effects.html#matplotlib.artist.Artist.set_path_effects "matplotlib.artist.Artist.set_path_effects")
(\[\
    [path\_effects.PathPatchEffect](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathPatchEffect "matplotlib.patheffects.PathPatchEffect")\
(\
        offset\=(4, \-4), hatch\='xxxx', facecolor\='gray'),\
    [path\_effects.PathPatchEffect](https://matplotlib.org/stable/api/patheffects_api.html#matplotlib.patheffects.PathPatchEffect "matplotlib.patheffects.PathPatchEffect")\
(\
        edgecolor\='white', linewidth\=1.1, facecolor\='black')\])
[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![patheffects guide](https://matplotlib.org/stable/_images/sphx_glr_patheffects_guide_004_2_00x.png)

[`Download Jupyter notebook: patheffects_guide.ipynb`](https://matplotlib.org/stable/_downloads/b65d6b33e40d6e4514bfbd585d16bf06/patheffects_guide.ipynb)

[`Download Python source code: patheffects_guide.py`](https://matplotlib.org/stable/_downloads/d83c9d326d1def2bc076a8958cb7d12c/patheffects_guide.py)

[`Download zipped: patheffects_guide.zip`](https://matplotlib.org/stable/_downloads/a756c01cee4d49484c737f5961a1694f/patheffects_guide.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)

On this page