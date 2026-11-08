[Skip to main content](https://matplotlib.org/stable/gallery/lines_bars_and_markers/spectrum_demo.html#main-content)

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

[Go to the end](https://matplotlib.org/stable/gallery/lines_bars_and_markers/spectrum_demo.html#sphx-glr-download-gallery-lines-bars-and-markers-spectrum-demo-py)
 to download the full example code.

Spectrum representations[#](https://matplotlib.org/stable/gallery/lines_bars_and_markers/spectrum_demo.html#spectrum-representations "Link to this heading")

=============================================================================================================================================================

The plots show different spectrum representations of a sine signal with additive noise. A (frequency) spectrum of a discrete-time signal is calculated by utilizing the fast Fourier transform (FFT).

import matplotlib.pyplot as plt
import numpy as np

[np.random.seed](https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html#numpy.random.seed "numpy.random.seed")
(0)

[dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 0.01  \# sampling interval
[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \= 1 / [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
  \# sampling frequency
[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.arange](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange "numpy.arange")
(0, 10, [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
)

\# generate noise:
[nse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html#numpy.random.randn "numpy.random.randn")
(len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
))
[r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.exp](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(\-[t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 / 0.05)
[cnse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [np.convolve](https://numpy.org/doc/stable/reference/generated/numpy.convolve.html#numpy.convolve "numpy.convolve")
([nse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [r](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) \* [dt](https://docs.python.org/3/library/functions.html#float "builtins.float")
[cnse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= [cnse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
\[:len([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")\
)\]

[s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 \= 0.1 \* [np.sin](https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")
(4 \* [np.pi](https://docs.python.org/3/library/functions.html#float "builtins.float")
 \* [t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
) + [cnse](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
  \# the signal

[fig](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "matplotlib.figure.Figure")
 \= [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html#matplotlib.pyplot.figure "matplotlib.pyplot.figure")
(figsize\=(7, 7), layout\='constrained')
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
 \= [fig.subplot\_mosaic](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.subplot_mosaic.html#matplotlib.figure.Figure.subplot_mosaic "matplotlib.figure.Figure.subplot_mosaic")
(\[\["signal", "signal"\],\
                          \["magnitude", "log\_magnitude"\],\
                          \["phase", "angle"\]\])

\# plot time signal:
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["signal"\].set\_title("Signal")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["signal"\].plot([t](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, color\='C0')
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["signal"\].set\_xlabel("Time (s)")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["signal"\].set\_ylabel("Amplitude")

\# plot different spectrum types:
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["magnitude"\].set\_title("Magnitude Spectrum")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["magnitude"\].magnitude\_spectrum([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
, color\='C1')

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["log\_magnitude"\].set\_title("Log. Magnitude Spectrum")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["log\_magnitude"\].magnitude\_spectrum([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
, scale\='dB', color\='C1')

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["phase"\].set\_title("Phase Spectrum ")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["phase"\].phase\_spectrum([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
, color\='C2')

[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["angle"\].set\_title("Angle Spectrum")
[axs](https://docs.python.org/3/library/stdtypes.html#dict "builtins.dict")
\["angle"\].angle\_spectrum([s](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
, [Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
\=[Fs](https://docs.python.org/3/library/functions.html#float "builtins.float")
, color\='C2')

[plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html#matplotlib.pyplot.show "matplotlib.pyplot.show")
()

![Signal, Magnitude Spectrum, Log. Magnitude Spectrum, Phase Spectrum , Angle Spectrum](https://matplotlib.org/stable/_images/sphx_glr_spectrum_demo_001_2_00x.png)

Tags: [domain: signal-processing](https://matplotlib.org/stable/_tags/domain-signal-processing.html)
 [plot-type: line](https://matplotlib.org/stable/_tags/plot-type-line.html)
 [level: beginner](https://matplotlib.org/stable/_tags/level-beginner.html)

**Total running time of the script:** (0 minutes 2.118 seconds)

[`Download Jupyter notebook: spectrum_demo.ipynb`](https://matplotlib.org/stable/_downloads/8326b90de4cd3b6b3b39684cb6d732f0/spectrum_demo.ipynb)

[`Download Python source code: spectrum_demo.py`](https://matplotlib.org/stable/_downloads/b8c57e62999229824f455e779d286772/spectrum_demo.py)

[`Download zipped: spectrum_demo.zip`](https://matplotlib.org/stable/_downloads/4d88498c7238b049792e0fda03c9a1e2/spectrum_demo.zip)

[Gallery generated by Sphinx-Gallery](https://sphinx-gallery.github.io/)