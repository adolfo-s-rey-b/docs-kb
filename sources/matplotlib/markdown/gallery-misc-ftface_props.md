[Skip to main content](https://matplotlib.org/stable/gallery/misc/ftface_props.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/ftface_props.html#sphx-glr-download-gallery-misc-ftface-props-py)
 to download the full example code.

Font properties[#](https://matplotlib.org/stable/gallery/misc/ftface_props.html#font-properties "Link to this heading")

========================================================================================================================

This example lists the attributes of an [`FT2Font`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
 object, which describe global font properties. For individual character metrics, use the [`Glyph`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.Glyph "matplotlib.ft2font.Glyph")
 object, as returned by [`load_char`](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.load_char "matplotlib.ft2font.FT2Font.load_char")
.

Num instances:   0
Num faces:       1
Num glyphs:      5343
Family name:     DejaVu Sans
Style name:      Oblique
PS name:         DejaVuSans-Oblique
Num fixed:       0
Bbox:                (-2080, -717, 3398, 2187)
EM:                  2048
Ascender:            1901
Descender:           -483
Height:              2384
Max adv width:       3461
Max adv height:      2384
Underline pos:       -175
Underline thickness: 90
Italic:           True
Bold:             False
Scalable:         True
Fixed Sizes:      False
Fixed Width:      False
Sfnt:             True
Horizontal:       True
Vertical:         False
Kerning:          True
Fast Glyphs:      False
Multiple Masters: False
Glyph Names:      True
External Stream:  True
Hinter:           True
Cid Keyed:        False
Tricky:           False
Color:            False
Variation:        False
Svg:              False
Sbix:             False
Sbix Overlay:     False

  

import os

import matplotlib
import matplotlib.ft2font as ft

[font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
 \= [ft.FT2Font](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font "matplotlib.ft2font.FT2Font")
(
    \# Use a font shipped with Matplotlib.
    [os.path.join](https://docs.python.org/3/library/os.path.html#os.path.join "os.path.join")
([matplotlib.get\_data\_path](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.get_data_path "matplotlib.get_data_path")
(),
                 'fonts/ttf/DejaVuSans-Oblique.ttf'))

print('Num instances:  ', [font.num\_named\_instances](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_named_instances "matplotlib.ft2font.FT2Font.num_named_instances")
)  \# number of named instances in file
print('Num faces:      ', [font.num\_faces](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_faces "matplotlib.ft2font.FT2Font.num_faces")
)            \# number of faces in file
print('Num glyphs:     ', [font.num\_glyphs](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_glyphs "matplotlib.ft2font.FT2Font.num_glyphs")
)           \# number of glyphs in the face
print('Family name:    ', [font.family\_name](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.family_name "matplotlib.ft2font.FT2Font.family_name")
)          \# face family name
print('Style name:     ', [font.style\_name](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.style_name "matplotlib.ft2font.FT2Font.style_name")
)           \# face style name
print('PS name:        ', [font.postscript\_name](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.postscript_name "matplotlib.ft2font.FT2Font.postscript_name")
)      \# the postscript name
print('Num fixed:      ', [font.num\_fixed\_sizes](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.num_fixed_sizes "matplotlib.ft2font.FT2Font.num_fixed_sizes")
)      \# number of embedded bitmaps

\# the following are only available if face.scalable
if [font.scalable](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.scalable "matplotlib.ft2font.FT2Font.scalable")
:
    \# the face global bounding box (xmin, ymin, xmax, ymax)
    print('Bbox:               ', [font.bbox](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.bbox "matplotlib.ft2font.FT2Font.bbox")
)
    \# number of font units covered by the EM
    print('EM:                 ', [font.units\_per\_EM](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.units_per_EM "matplotlib.ft2font.FT2Font.units_per_EM")
)
    \# the ascender in 26.6 units
    print('Ascender:           ', [font.ascender](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.ascender "matplotlib.ft2font.FT2Font.ascender")
)
    \# the descender in 26.6 units
    print('Descender:          ', [font.descender](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.descender "matplotlib.ft2font.FT2Font.descender")
)
    \# the height in 26.6 units
    print('Height:             ', [font.height](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.height "matplotlib.ft2font.FT2Font.height")
)
    \# maximum horizontal cursor advance
    print('Max adv width:      ', [font.max\_advance\_width](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.max_advance_width "matplotlib.ft2font.FT2Font.max_advance_width")
)
    \# same for vertical layout
    print('Max adv height:     ', [font.max\_advance\_height](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.max_advance_height "matplotlib.ft2font.FT2Font.max_advance_height")
)
    \# vertical position of the underline bar
    print('Underline pos:      ', [font.underline\_position](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.underline_position "matplotlib.ft2font.FT2Font.underline_position")
)
    \# vertical thickness of the underline
    print('Underline thickness:', [font.underline\_thickness](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.underline_thickness "matplotlib.ft2font.FT2Font.underline_thickness")
)

for [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
 in [ft.StyleFlags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.StyleFlags "matplotlib.ft2font.StyleFlags")
:
    [name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
.[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.replace('\_', ' ').title() + ':'
    print(f"{[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
:17}", [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
 in [font.style\_flags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.style_flags "matplotlib.ft2font.FT2Font.style_flags")
)

for [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
 in [ft.FaceFlags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
:
    [name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
 \= [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
.[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
.replace('\_', ' ').title() + ':'
    print(f"{[name](https://docs.python.org/3/library/stdtypes.html#str "builtins.str")
:17}", [flag](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FaceFlags "matplotlib.ft2font.FaceFlags")
 in [font.face\_flags](https://matplotlib.org/stable/api/ft2font.html#matplotlib.ft2font.FT2Font.face_flags "matplotlib.ft2font.FT2Font.face_flags")
)

[`Download Jupyter notebook: ftface_props.ipynb`](https://matplotlib.org/stable/_downloads/cb2f7f95910dcdfd5146478e03247867/ftface_props.ipynb)

[`Download Python source code: ftface_props.py`](https://matplotlib.org/stable/_downloads/743ad63e9e395c77c01d02248326773a/ftface_props.py)

[`Download zipped: ftface_props.zip`](https://matplotlib.org/stable/_downloads/8bc618f37f32df963fed43a24978a229/ftface_props.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)