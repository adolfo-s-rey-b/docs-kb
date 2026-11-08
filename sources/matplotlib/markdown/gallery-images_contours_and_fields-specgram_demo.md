[Skip to main content](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html#sphx-glr-download-gallery-images-contours-and-fields-specgram-demo-py)
 to download the full example code.

Spectrogram[#](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html#spectrogram "Link to this heading")

=======================================================================================================================================

Plotting a spectrogram using [`specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html#matplotlib.axes.Axes.specgram "matplotlib.axes.Axes.specgram")
.

import matplotlib.pyplot as plt
import numpy as np

\# Fixing random state for reproducibility
[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(19680801)

[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.0005
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0.0, 20.5, [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
[s1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 100 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 2 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(2 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* 400 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)

\# create a transient "chirp"
[s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
 <= 10\] \= [s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[12 <= [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
\] \= 0

\# add some noise into the mix
[nse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.01 \* [np.random.random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.random.html#numpy.random.random "numpy.random.random")
(size\=len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))

[x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [s1](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [s2](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 + [nse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
  \# the signal
[NFFT](https://docs.python.org/3/library/functions.html#int "builtins.int")
 \= 1024  \# the length of the windowing segments
[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1/[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
  \# the sampling frequency

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
, ([ax1](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
, [ax2](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html#matplotlib.axes.Axes "matplotlib.axes.Axes")
) \= [plt.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots "matplotlib.pyplot.subplots")
(nrows\=2, sharex\=True)
[ax1.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot "matplotlib.axes.Axes.plot")
([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
)
[ax1.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Signal')

[Pxx](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [freqs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [bins](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [im](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")
 \= [ax2.specgram](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html#matplotlib.axes.Axes.specgram "matplotlib.axes.Axes.specgram")
([x](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [NFFT](https://docs.python.org/3/library/functions.html#int "builtins.int")
\=[NFFT](https://docs.python.org/3/library/functions.html#int "builtins.int")
, [Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
)
\# The \`specgram\` method returns 4 objects. They are:
\# - Pxx: the periodogram
\# - freqs: the frequency vector
\# - bins: the centers of the time bins
\# - im: the .image.AxesImage instance representing the data in the plot
[ax2.set\_xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html#matplotlib.axes.Axes.set_xlabel "matplotlib.axes.Axes.set_xlabel")
('Time (s)')
[ax2.set\_ylabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html#matplotlib.axes.Axes.set_ylabel "matplotlib.axes.Axes.set_ylabel")
('Frequency (Hz)')
[ax2.set\_xlim](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlim.html#matplotlib.axes.Axes.set_xlim "matplotlib.axes.Axes.set_xlim")
(0, 20)

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![specgram demo](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_001_2_00x.png)

References

The use of the following functions, methods, classes and modules is shown in this example:

*   [`matplotlib.axes.Axes.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html#matplotlib.axes.Axes.specgram "matplotlib.axes.Axes.specgram")
     / [`matplotlib.pyplot.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "matplotlib.pyplot.specgram")
    

**Total running time of the script:** (0 minutes 1.225 seconds)

[`Download Jupyter notebook: specgram_demo.ipynb`](https://matplotlib.org/stable/_downloads/477677ca771a108eb0204c44fd33428d/specgram_demo.ipynb)

[`Download Python source code: specgram_demo.py`](https://matplotlib.org/stable/_downloads/e46a8d77906904db48e0e64959be9b24/specgram_demo.py)

[`Download zipped: specgram_demo.zip`](https://matplotlib.org/stable/_downloads/5a2fd9b9cc32f68cdef2c2f0ad2d503b/specgram_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)