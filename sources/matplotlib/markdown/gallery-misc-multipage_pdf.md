[Skip to main content](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html#sphx-glr-download-gallery-misc-multipage-pdf-py)
 to download the full example code.

Multipage PDF[#](https://matplotlib.org/stable/gallery/misc/multipage_pdf.html#multipage-pdf "Link to this heading")

=====================================================================================================================

This is a demo of creating a pdf file with several pages, as well as adding metadata and annotations to pdf files.

import datetime

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend\_pdf import [PdfPages](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")

\# Create the PdfPages object to which we will save the pages:
\# The with statement makes sure that the PdfPages object is closed properly at
\# the end of the block, even if an Exception occurs.
with [PdfPages](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
('multipage\_pdf.pdf') as [pdf](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages "matplotlib.backends.backend_pdf.PdfPages")
:
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(3, 3))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
(range(7), \[3, 1, 4, 1, 5, 9, 2\], 'r-o')
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Page One')
    [pdf.savefig](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.savefig "matplotlib.backends.backend_pdf.PdfPages.savefig")
()  \# saves the current figure into a pdf page
    [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
()

    \# if LaTeX is not installed or error caught, change to \`False\`
    [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['text.usetex'\] \= True
    [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(8, 6))
    [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 5, 0.1)
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
), 'b-')
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Page Two')
    [pdf.attach\_note](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.attach_note "matplotlib.backends.backend_pdf.PdfPages.attach_note")
("plot of sin(x)")  \# attach metadata (as pdf note) to page
    [pdf.savefig](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.savefig "matplotlib.backends.backend_pdf.PdfPages.savefig")
()
    [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
()

    [plt.rcParams](https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.RcParams "matplotlib.RcParams")
\['text.usetex'\] \= False
    [fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(4, 5))
    [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot "matplotlib.pyplot.plot")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \*\* 2, 'ko')
    [plt.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html#matplotlib.pyplot.title "matplotlib.pyplot.title")
('Page Three')
    [pdf.savefig](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.savefig "matplotlib.backends.backend_pdf.PdfPages.savefig")
([fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
)  \# or you can pass a Figure object to pdf.savefig
    [plt.close](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html#matplotlib.pyplot.close "matplotlib.pyplot.close")
()

    \# We can also set the file's metadata via the PdfPages object:
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [pdf.infodict](https://matplotlib.org/stable/api/backend_pdf_api.html#matplotlib.backends.backend_pdf.PdfPages.infodict "matplotlib.backends.backend_pdf.PdfPages.infodict")
()
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['Title'\] \= 'Multipage PDF Example'
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['Author'\] \= 'Jouni K. Sepp\\xe4nen'
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['Subject'\] \= 'How to create a multipage pdf file and set its metadata'
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['Keywords'\] \= 'PdfPages multipage keywords author title subject'
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['CreationDate'\] \= [datetime.datetime](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
(2009, 11, 13)
    [d](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\['ModDate'\] \= [datetime.datetime.today](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "datetime.datetime.today")
()

[`Download Jupyter notebook: multipage_pdf.ipynb`](https://matplotlib.org/stable/_downloads/ead9c446872f9c5f61a2173ec954ab1e/multipage_pdf.ipynb)

[`Download Python source code: multipage_pdf.py`](https://matplotlib.org/stable/_downloads/d23c7f0745416d8f00af47b8cc0f6394/multipage_pdf.py)

[`Download zipped: multipage_pdf.zip`](https://matplotlib.org/stable/_downloads/a80294ecbd554c9e90c864a139963128/multipage_pdf.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)