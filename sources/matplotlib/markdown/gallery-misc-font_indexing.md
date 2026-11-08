[Skip to main content](https://matplotlib.org/stable/gallery/misc/font_indexing.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/font_indexing.html#sphx-glr-download-gallery-misc-font-indexing-py)
 to download the full example code.

Font indexing[#](https://matplotlib.org/stable/gallery/misc/font_indexing.html#font-indexing "Link to this heading")

=====================================================================================================================

This example shows how the font tables relate to one another.

(16, 0, 1384, 1493)
36 57 65 86
AV 0
AV 0
AV -131
AT -159

  

import os

import matplotlib
from matplotlib.ft2font import [FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
, Kerning

[font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
 \= [FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
(
    [os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join")
([matplotlib.get\_data\_path](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
(), 'fonts/ttf/DejaVuSans.ttf'))
[font.set\_charmap](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.set_charmap "matplotlib.ft2font.FT2Font.set_charmap")
(0)

codes \= [font.get\_charmap](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_charmap "matplotlib.ft2font.FT2Font.get_charmap")
().items()

\# make a charname to charcode and glyphind dictionary
[coded](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {}
[glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= {}
for [ccode](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [glyphind](https://docs.python.org/3/library/functions.html#int "builtins.int")
 in codes:
    [name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [font.get\_glyph\_name](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_glyph_name "matplotlib.ft2font.FT2Font.get_glyph_name")
([glyphind](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
    [coded](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\] \= [ccode](https://docs.python.org/3/library/functions.html#int "builtins.int")
    [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\[[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")\
\] \= [glyphind](https://docs.python.org/3/library/functions.html#int "builtins.int")
    \# print(glyphind, ccode, hex(int(ccode)), name)

[code](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= [coded](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\]
[glyph](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")
 \= [font.load\_char](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")
([code](https://docs.python.org/3/library/functions.html#int "builtins.int")
)
print([glyph.bbox](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph.bbox "matplotlib.ft2font.Glyph.bbox")
)
print([glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['V'\], [coded](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [coded](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['V'\])
print('AV', [font.get\_kerning](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")
([glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['V'\], [Kerning.DEFAULT](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
))
print('AV', [font.get\_kerning](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")
([glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['V'\], [Kerning.UNFITTED](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
))
print('AV', [font.get\_kerning](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")
([glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['V'\], [Kerning.UNSCALED](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
))
print('AT', [font.get\_kerning](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.get_kerning "matplotlib.ft2font.FT2Font.get_kerning")
([glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['A'\], [glyphd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['T'\], [Kerning.UNSCALED](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Kerning "matplotlib.ft2font.Kerning")
))

[`Download Jupyter notebook: font_indexing.ipynb`](https://matplotlib.org/stable/_downloads/921c6fb5aee4de7c73df68b18fa386a9/font_indexing.ipynb)

[`Download Python source code: font_indexing.py`](https://matplotlib.org/stable/_downloads/eb89ff1d508f38419ceffd561af32d0b/font_indexing.py)

[`Download zipped: font_indexing.zip`](https://matplotlib.org/stable/_downloads/0e2424da31bfd2f51c010c8029efee59/font_indexing.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)