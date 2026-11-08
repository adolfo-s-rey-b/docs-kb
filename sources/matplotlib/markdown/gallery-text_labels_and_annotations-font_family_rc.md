[Skip to main content](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html#sphx-glr-download-gallery-text-labels-and-annotations-font-family-rc-py)
 to download the full example code.

Configure the font family[#](https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html#configure-the-font-family "Link to this heading")

=====================================================================================================================================================================

You can explicitly set which font family is picked up, either by specifying family names of fonts installed on user's system, or generic-families (e.g., 'serif', 'sans-serif', 'monospace', 'fantasy' or 'cursive'), or a combination of both. (see [Text properties and layout](https://matplotlib.org/stable/users/explain/text/text_props.html#text-props)
)

In the example below, we are overriding the default sans-serif generic family to include a specific (Tahoma) font. (Note that the best way to achieve this would simply be to prepend 'Tahoma' in 'font.family')

The default family is set with the font.family rcparam, e.g.

rcParams\['font.family'\] \= 'sans-serif'

and for the font.family you set a list of font styles to try to find in order:

rcParams\['font.sans-serif'\] \= \['Tahoma', 'DejaVu Sans',\
                               'Lucida Grande', 'Verdana'\]

The `font.family` defaults are OS dependent and can be viewed with:

import matplotlib.pyplot as plt

print([plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.sans-serif"\]\[0\])
print([plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.monospace"\]\[0\])

DejaVu Sans
DejaVu Sans Mono

Choose default sans-serif font

def print\_text(text):
    fig, ax \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(figsize\=(6, 1), facecolor\="#eefade")
    ax.text(0.5, 0.5, text, ha\='center', va\='center', size\=40)
    ax.axis("off")
    [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.family"\] \= "sans-serif"
print\_text("Hello World! 01")

![font family rc](https://matplotlib.org/stable/_images/sphx_glr_font_family_rc_001_2_00x.png)

Choose sans-serif font and specify to it to "Nimbus Sans"

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.family"\] \= "sans-serif"
[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.sans-serif"\] \= \["Nimbus Sans"\]
print\_text("Hello World! 02")

![font family rc](https://matplotlib.org/stable/_images/sphx_glr_font_family_rc_002_2_00x.png)

Choose default monospace font

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.family"\] \= "monospace"
print\_text("Hello World! 03")

![font family rc](https://matplotlib.org/stable/_images/sphx_glr_font_family_rc_003_2_00x.png)

Choose monospace font and specify to it to "FreeMono"

[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.family"\] \= "monospace"
[plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\["font.monospace"\] \= \["FreeMono"\]
print\_text("Hello World! 04")

![font family rc](https://matplotlib.org/stable/_images/sphx_glr_font_family_rc_004_2_00x.png)

[`Download Jupyter notebook: font_family_rc.ipynb`](https://matplotlib.org/stable/_downloads/66637889d80e1ce800c1e3de058c22be/font_family_rc.ipynb)

[`Download Python source code: font_family_rc.py`](https://matplotlib.org/stable/_downloads/855769f70f221ad26f2f3ef0c960bb67/font_family_rc.py)

[`Download zipped: font_family_rc.zip`](https://matplotlib.org/stable/_downloads/6ab3a89e502eb9bce49afdea59857292/font_family_rc.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)