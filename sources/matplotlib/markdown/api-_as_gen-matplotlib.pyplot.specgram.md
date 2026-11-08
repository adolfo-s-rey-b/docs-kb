[Skip to main content](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#main-content)

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
    

matplotlib.pyplot.specgram[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib-pyplot-specgram "Link to this heading")

===========================================================================================================================================================

matplotlib.pyplot.specgram(_x_, _\*_, _NFFT\=None_, _Fs\=None_, _Fc\=None_, _detrend\=None_, _window\=None_, _noverlap\=None_, _cmap\=None_, _xextent\=None_, _pad\_to\=None_, _sides\=None_, _scale\_by\_freq\=None_, _mode\=None_, _scale\=None_, _vmin\=None_, _vmax\=None_, _data\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/pyplot.py#L4163-L4208)
[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#matplotlib.pyplot.specgram "Link to this definition")

Plot a spectrogram.

Compute and plot a spectrogram of data in _x_. Data are split into _NFFT_ length segments and the spectrum of each section is computed. The windowing function _window_ is applied to each segment, and the amount of overlap of each segment is specified with _noverlap_. The spectrogram is plotted as a colormap (using imshow).

Parameters:

**x**1-D array or sequence

Array or sequence containing the data.

**Fs**float, default: 2

The sampling frequency (samples per time unit). It is used to calculate the Fourier frequencies, _freqs_, in cycles per time unit.

**window**callable or ndarray, default: [`window_hanning`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_hanning "matplotlib.mlab.window_hanning")

A function or a vector of length _NFFT_. To create window vectors see [`window_hanning`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_hanning "matplotlib.mlab.window_hanning")
, [`window_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_none "matplotlib.mlab.window_none")
, [`numpy.blackman`](https://numpy.org/doc/stable/reference/generated/numpy.blackman.html#numpy.blackman "(in NumPy v2.5)")
, [`numpy.hamming`](https://numpy.org/doc/stable/reference/generated/numpy.hamming.html#numpy.hamming "(in NumPy v2.5)")
, [`numpy.bartlett`](https://numpy.org/doc/stable/reference/generated/numpy.bartlett.html#numpy.bartlett "(in NumPy v2.5)")
, [`scipy.signal`](https://docs.scipy.org/doc/scipy/reference/signal.html#module-scipy.signal "(in SciPy v1.18.0)")
, [`scipy.signal.get_window`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html#scipy.signal.get_window "(in SciPy v1.18.0)")
, etc. If a function is passed as the argument, it must take a data segment as an argument and return the windowed version of the segment.

**sides**{'default', 'onesided', 'twosided'}, optional

Which sides of the spectrum to return. 'default' is one-sided for real data and two-sided for complex data. 'onesided' forces the return of a one-sided spectrum, while 'twosided' forces two-sided.

**pad\_to**int, optional

The number of points to which the data segment is padded when performing the FFT. This can be different from _NFFT_, which specifies the number of data points used. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the _n_ parameter in the call to [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "(in NumPy v2.5)")
. The default is None, which sets _pad\_to_ equal to _NFFT_

**NFFT**int, default: 256

The number of data points used in each block for the FFT. A power 2 is most efficient. This should _NOT_ be used to get zero padding, or the scaling of the result will be incorrect; use _pad\_to_ for this instead.

**detrend**{'none', 'mean', 'linear'} or callable, default: 'none'

The function applied to each segment before fft-ing, designed to remove the mean or linear trend. Unlike in MATLAB, where the _detrend_ parameter is a vector, in Matplotlib it is a function. The [`mlab`](https://matplotlib.org/stable/api/mlab_api.html#module-matplotlib.mlab "matplotlib.mlab")
 module defines [`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")
, [`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")
, and [`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")
, but you can use a custom function as well. You can also use a string to choose one of the functions: 'none' calls [`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")
. 'mean' calls [`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")
. 'linear' calls [`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")
.

**scale\_by\_freq**bool, default: True

Whether the resulting density values should be scaled by the scaling frequency, which gives density in units of 1/Hz. This allows for integration over the returned frequency values. The default is True for MATLAB compatibility.

**mode**{'default', 'psd', 'magnitude', 'angle', 'phase'}

What sort of spectrum to use. Default is 'psd', which takes the power spectral density. 'magnitude' returns the magnitude spectrum. 'angle' returns the phase spectrum without unwrapping. 'phase' returns the phase spectrum with unwrapping.

**noverlap**int, default: 128

The number of points of overlap between blocks.

**scale**{'default', 'linear', 'dB'}

The scaling of the values in the _spec_. 'linear' is no scaling. 'dB' returns the values in dB scale. When _mode_ is 'psd', this is dB power (10 \* log10). Otherwise, this is dB amplitude (20 \* log10). 'default' is 'dB' if _mode_ is 'psd' or 'magnitude' and 'linear' otherwise. This must be 'linear' if _mode_ is 'angle' or 'phase'.

**Fc**int, default: 0

The center frequency of _x_, which offsets the x extents of the plot to reflect the frequency range used when a signal is acquired and then filtered and downsampled to baseband.

**cmap**[`Colormap`](https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.Colormap.html#matplotlib.colors.Colormap "matplotlib.colors.Colormap")
, default: `[rcParams["image.cmap"]](https://matplotlib.org/stable/users/explain/configuration.html?highlight=image.cmap#rcparam-image-cmap) ` (default: `'viridis'`)

**xextent**_None_ or (xmin, xmax)

The image extent along the x-axis. The default sets _xmin_ to the left border of the first bin (_spectrum_ column) and _xmax_ to the right border of the last bin. Note that for _noverlap>0_ the width of the bins is smaller than those of the segments.

**data**indexable object, optional

If given, the following parameters also accept a string `s`, which is interpreted as `data[s]` if `s` is a key in `data`:

_x_

**vmin, vmax**float, optional

vmin and vmax define the data range that the colormap covers. By default, the colormap covers the complete value range of the data.

**\*\*kwargs**

Additional keyword arguments are passed on to [`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.imshow.html#matplotlib.axes.Axes.imshow "matplotlib.axes.Axes.imshow")
 which makes the specgram image. The origin keyword argument is not supported.

Returns:

**spectrum**2D array

Columns are the periodograms of successive segments.

**freqs**1-D array

The frequencies corresponding to the rows in _spectrum_.

**t**1-D array

The times corresponding to midpoints of segments (i.e., the columns in _spectrum_).

**im**[`AxesImage`](https://matplotlib.org/stable/api/image_api.html#matplotlib.image.AxesImage "matplotlib.image.AxesImage")

The image created by imshow containing the spectrogram.

See also

[`psd`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html#matplotlib.pyplot.psd "matplotlib.pyplot.psd")

Differs in the default overlap; in returning the mean of the segment periodograms; in not returning times; and in generating a line plot instead of colormap.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.magnitude_spectrum.html#matplotlib.pyplot.magnitude_spectrum "matplotlib.pyplot.magnitude_spectrum")

A single spectrum, similar to having a single segment when _mode_ is 'magnitude'. Plots a line instead of a colormap.

[`angle_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.angle_spectrum.html#matplotlib.pyplot.angle_spectrum "matplotlib.pyplot.angle_spectrum")

A single spectrum, similar to having a single segment when _mode_ is 'angle'. Plots a line instead of a colormap.

[`phase_spectrum`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.phase_spectrum.html#matplotlib.pyplot.phase_spectrum "matplotlib.pyplot.phase_spectrum")

A single spectrum, similar to having a single segment when _mode_ is 'phase'. Plots a line instead of a colormap.

Notes

Note

This is the [pyplot wrapper](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html#pyplot-interface)
 for [`axes.Axes.specgram`](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.specgram.html#matplotlib.axes.Axes.specgram "matplotlib.axes.Axes.specgram")
.

The parameters _detrend_ and _scale\_by\_freq_ do only apply when _mode_ is set to 'psd'.

Examples using `matplotlib.pyplot.specgram`[#](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.specgram.html#examples-using-matplotlib-pyplot-specgram "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://matplotlib.org/stable/_images/sphx_glr_specgram_demo_thumb.png)

[Spectrogram](https://matplotlib.org/stable/gallery/images_contours_and_fields/specgram_demo.html)

Spectrogram

On this page