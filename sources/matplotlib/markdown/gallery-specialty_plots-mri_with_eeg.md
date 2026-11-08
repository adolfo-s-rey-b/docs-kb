[Skip to main content](https://matplotlib.org/stable/gallery/specialty_plots/mri_with_eeg.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/specialty_plots/mri_with_eeg.html#sphx-glr-download-gallery-specialty-plots-mri-with-eeg-py)
 to download the full example code.

MRI with EEG[#](https://matplotlib.org/stable/gallery/specialty_plots/mri_with_eeg.html#mri-with-eeg "Link to this heading")

=============================================================================================================================

Displays a set of subplots with an MRI image, its intensity histogram and some EEG traces.

![mri with eeg](https://matplotlib.org/stable/_images/sphx_glr_mri_with_eeg_001_2_00x.png)

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [plt.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot_mosaic.html#matplotlib.pyplot.subplot_mosaic "matplotlib.pyplot.subplot_mosaic")
(
    \[\["image", "density"\],\
     \["EEG", "EEG"\]\],
    layout\="constrained",
    \# "image" will contain a square image. We fine-tune the width so that
    \# there is no excess horizontal or vertical margin around the image.
    width\_ratios\=\[1.05, 2\],
)

\# Load the MRI data (256x256 16-bit integers)
with [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('s1045.ima.gz') as [dfile](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile")
:
    [im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.frombuffer](https://numpy.org/doc/stable/reference/generated/numpy.frombuffer.html#numpy.frombuffer "numpy.frombuffer")
([dfile.read](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")
(), [np.uint16](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.uint16 "numpy.uint16")
).reshape((256, 256))

\# Plot the MRI image
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["image"\].imshow([im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, cmap\="gray")
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["image"\].axis('off')

\# Plot the histogram of MRI intensity
[im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
.nonzero()\]  \# Ignore the background
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["density"\].hist([im](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, bins\=[np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 2\*\*16+1, 512))
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["density"\].set(xlabel\='Intensity (a.u.)', xlim\=(0, 2\*\*16),
                   ylabel\='MRI density', yticks\=\[\])
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["density"\].minorticks\_on()

\# Load the EEG data
[n\_samples](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 800, 4
with [cbook.get\_sample\_data](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.get_sample_data "matplotlib.cbook.get_sample_data")
('eeg.dat') as eegfile:
    [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.fromfile](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
(eegfile, dtype\=float).reshape(([n\_samples](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
))
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 10 \* [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
([n\_samples](https://docs.python.org/3/library/functions.html#int "builtins.int")
) / [n\_samples](https://docs.python.org/3/library/functions.html#int "builtins.int")

\# Plot the EEG
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["EEG"\].set\_xlabel('Time (s)')
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["EEG"\].set\_xlim(0, 10)
[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
 \= ([data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.min() \- [data](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
.max()) \* 0.7  \# Crowd them a bit.
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["EEG"\].set\_ylim(\-[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, [n\_rows](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \* [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
)
[axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["EEG"\].set\_yticks(\[0, [dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
, 2\*[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
, 3\*[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")\
\], labels\=\['PG3', 'PG5', 'PG7', 'PG9'\])

for [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [data\_col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 in enumerate([data.T](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
):
    [axd](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["EEG"\].plot([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [data\_col](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [i](https://docs.python.org/3/library/functions.html#int "builtins.int")
\*[dy](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.float64 "numpy.float64")
, color\="C0")

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

**Total running time of the script:** (0 minutes 1.499 seconds)

[`Download Jupyter notebook: mri_with_eeg.ipynb`](https://matplotlib.org/stable/_downloads/a101e8e1a467e65908f23d68b1302ac9/mri_with_eeg.ipynb)

[`Download Python source code: mri_with_eeg.py`](https://matplotlib.org/stable/_downloads/f256ad1c5f1c41eadcdd71b58639c9c6/mri_with_eeg.py)

[`Download zipped: mri_with_eeg.zip`](https://matplotlib.org/stable/_downloads/376cfdaa47c8e623b5f97c4cc52d9f5a/mri_with_eeg.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)