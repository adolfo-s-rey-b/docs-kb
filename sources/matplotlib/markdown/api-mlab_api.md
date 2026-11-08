[Skip to main content](https://matplotlib.org/stable/api/mlab_api.html#main-content)

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
    

`matplotlib.mlab`[#](https://matplotlib.org/stable/api/mlab_api.html#module-matplotlib.mlab "Link to this heading")

====================================================================================================================

Numerical Python functions written for compatibility with MATLAB commands with the same names. Most numerical Python functions can be found in the [NumPy](https://numpy.org/)
 and [SciPy](https://www.scipy.org/)
 libraries. What remains here is code for performing spectral computations and kernel density estimations.

Spectral functions[#](https://matplotlib.org/stable/api/mlab_api.html#spectral-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

[`cohere`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.cohere "matplotlib.mlab.cohere")

Coherence (normalized cross spectral density)

[`csd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")

Cross spectral density using Welch's average periodogram

[`detrend`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "matplotlib.mlab.detrend")

Remove the mean or best fit line from an array

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

Power spectral density using Welch's average periodogram

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

Spectrogram (spectrum over segments of time)

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

Return the complex-valued frequency spectrum of a signal

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

Return the magnitude of the frequency spectrum of a signal

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

Return the angle (wrapped phase) of the frequency spectrum of a signal

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

Return the phase (unwrapped angle) of the frequency spectrum of a signal

[`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")

Remove the mean from a line.

[`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")

Remove the best fit line from a line.

[`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")

Return the original line.

class matplotlib.mlab.GaussianKDE(_dataset_, _bw\_method\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L788-L931)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Representation of a kernel-density estimate using Gaussian kernels.

Parameters:

**dataset**array-like

Datapoints to estimate from. In case of univariate data this is a 1-D array, otherwise a 2D array with shape (# of dims, # of data).

**bw\_method**{'scott', 'silverman'} or float or callable, optional

The method used to calculate the estimator bandwidth. If a float, this will be used directly as `kde.factor`. If a callable, it should take a [`GaussianKDE`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE "matplotlib.mlab.GaussianKDE")
 instance as only parameter and return a float. If None (default), 'scott' is used.

Attributes:

**dataset**ndarray

The dataset passed to the constructor.

**dim**int

Number of dimensions.

**num\_dp**int

Number of datapoints.

**factor**float

The bandwidth factor, obtained from [`covariance_factor`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE.covariance_factor "matplotlib.mlab.GaussianKDE.covariance_factor")
, with which the covariance matrix is multiplied.

**covariance**ndarray

The covariance matrix of _dataset_, scaled by the calculated bandwidth (`kde.factor`).

**inv\_cov**ndarray

The inverse of _covariance_.

Methods

|     |     |
| --- | --- |
| **kde.evaluate(points)** | (ndarray) Evaluate the estimated pdf on a provided set of points. |
| **kde(points)** | (ndarray) Same as kde.evaluate(points) |

covariance\_factor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L872-L873)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE.covariance_factor "Link to this definition")

evaluate(_points_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L882-L929)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE.evaluate "Link to this definition")

Evaluate the estimated pdf on a set of points.

Parameters:

**points**(# of dimensions, # of points)-array

Alternatively, a (# of dimensions,) vector can be passed in and treated as a single point.

Returns:

(# of points,)-array

The values at each point.

Raises:

**ValueError**if the dimensionality of the input points is different

than the dimensionality of the KDE.

scotts\_factor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L872-L873)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE.scotts_factor "Link to this definition")

silverman\_factor()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L875-L877)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.GaussianKDE.silverman_factor "Link to this definition")

matplotlib.mlab.angle\_spectrum(_x_, _Fs\=None_, _window\=None_, _pad\_to\=None_, _sides\=None_)[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "Link to this definition")

Compute the angle of the frequency spectrum (wrapped phase spectrum) of _x_. Data is padded to a length of _pad\_to_ and the windowing function _window_ is applied to the signal.

Parameters:

**x**1-D array or sequence

Array or sequence containing the data

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

The number of points to which the data segment is padded when performing the FFT. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the _n_ parameter in the call to [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "(in NumPy v2.5)")
. The default is None, which sets _pad\_to_ equal to the length of the input signal (i.e. no padding).

Returns:

**spectrum**1-D array

The angle of the frequency spectrum (wrapped phase spectrum).

**freqs**1-D array

The frequencies corresponding to the elements in _spectrum_.

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

Returns the power spectral density.

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

Returns the complex-valued frequency spectrum.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

Returns the absolute value of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

Returns the angle of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

Returns the phase (unwrapped angle) of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

Can return the complex spectrum of segments within the signal.

matplotlib.mlab.cohere(_x_, _y_, _NFFT\=256_, _Fs\=2_, _detrend\=<function detrend\_none>_, _window\=<function window\_hanning>_, _noverlap\=0_, _pad\_to\=None_, _sides\='default'_, _scale\_by\_freq\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L738-L785)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.cohere "Link to this definition")

The coherence between _x_ and _y_. Coherence is the normalized cross spectral density:

\\\[C\_{xy} = \\frac{|P\_{xy}|^2}{P\_{xx}P\_{yy}}\\\]

Parameters:

**x, y**

Array or sequence containing the data

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

**noverlap**int, default: 0 (no overlap)

The number of points of overlap between segments.

Returns:

**Cxy**1-D array

The coherence vector.

**freqs**1-D array

The frequencies for the elements in _Cxy_.

See also

[`psd()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")
, [`csd()`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")

For information about the methods used to compute \\(P\_{xy}\\), \\(P\_{xx}\\) and \\(P\_{yy}\\).

matplotlib.mlab.complex\_spectrum(_x_, _Fs\=None_, _window\=None_, _pad\_to\=None_, _sides\=None_)[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "Link to this definition")

Compute the complex-valued frequency spectrum of _x_. Data is padded to a length of _pad\_to_ and the windowing function _window_ is applied to the signal.

Parameters:

**x**1-D array or sequence

Array or sequence containing the data

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

The number of points to which the data segment is padded when performing the FFT. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the _n_ parameter in the call to [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "(in NumPy v2.5)")
. The default is None, which sets _pad\_to_ equal to the length of the input signal (i.e. no padding).

Returns:

**spectrum**1-D array

The complex-valued frequency spectrum.

**freqs**1-D array

The frequencies corresponding to the elements in _spectrum_.

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

Returns the power spectral density.

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

Returns the complex-valued frequency spectrum.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

Returns the absolute value of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

Returns the angle of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

Returns the phase (unwrapped angle) of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

Can return the complex spectrum of segments within the signal.

matplotlib.mlab.csd(_x_, _y_, _NFFT\=None_, _Fs\=None_, _detrend\=None_, _window\=None_, _noverlap\=None_, _pad\_to\=None_, _sides\=None_, _scale\_by\_freq\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L535-L596)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "Link to this definition")

Compute the cross-spectral density.

The cross spectral density \\(P\_{xy}\\) by Welch's average periodogram method. The vectors _x_ and _y_ are divided into _NFFT_ length segments. Each segment is detrended by function _detrend_ and windowed by function _window_. _noverlap_ gives the length of the overlap between segments. The product of the direct FFTs of _x_ and _y_ are averaged over each segment to compute \\(P\_{xy}\\), with a scaling to correct for power loss due to windowing.

If len(_x_) < _NFFT_ or len(_y_) < _NFFT_, they will be zero padded to _NFFT_.

Parameters:

**x, y**1-D arrays or sequences

Arrays or sequences containing the data

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

**noverlap**int, default: 0 (no overlap)

The number of points of overlap between segments.

Returns:

**Pxy**1-D array

The values for the cross spectrum \\(P\_{xy}\\) before scaling (real valued)

**freqs**1-D array

The frequencies corresponding to the elements in _Pxy_

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

equivalent to setting `y = x`.

References

Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John Wiley & Sons (1986)

matplotlib.mlab.detrend(_x_, _key\=None_, _axis\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L81-L127)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "Link to this definition")

Return _x_ with its trend removed.

Parameters:

**x**array or sequence

Array or sequence containing the data.

**key**{'default', 'constant', 'mean', 'linear', 'none'} or function

The detrending algorithm to use. 'default', 'mean', and 'constant' are the same as [`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")
. 'linear' is the same as [`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")
. 'none' is the same as [`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")
. The default is 'mean'. See the corresponding functions for more details regarding the algorithms. Can also be a function that carries out the detrend operation.

**axis**int

The axis along which to do the detrending.

See also

[`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")

Implementation of the 'mean' algorithm.

[`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")

Implementation of the 'linear' algorithm.

[`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")

Implementation of the 'none' algorithm.

matplotlib.mlab.detrend\_linear(_y_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L180-L211)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "Link to this definition")

Return _x_ minus best fit line; 'linear' detrending.

Parameters:

**y**0-D or 1-D array or sequence

Array or sequence containing the data

See also

[`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")

Another detrend algorithm.

[`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")

Another detrend algorithm.

[`detrend`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "matplotlib.mlab.detrend")

A wrapper around all the detrend algorithms.

matplotlib.mlab.detrend\_mean(_x_, _axis\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L130-L155)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "Link to this definition")

Return _x_ minus the mean(_x_).

Parameters:

**x**array or sequence

Array or sequence containing the data Can have any dimensionality

**axis**int

The axis along which to take the mean. See [`numpy.mean`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html#numpy.mean "(in NumPy v2.5)")
 for a description of this argument.

See also

[`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")

Another detrend algorithm.

[`detrend_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "matplotlib.mlab.detrend_none")

Another detrend algorithm.

[`detrend`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "matplotlib.mlab.detrend")

A wrapper around all the detrend algorithms.

matplotlib.mlab.detrend\_none(_x_, _axis\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L158-L177)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_none "Link to this definition")

Return _x_: no detrending.

Parameters:

**x**any object

An object containing the data

**axis**int

This parameter is ignored. It is included for compatibility with detrend\_mean

See also

[`detrend_mean`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_mean "matplotlib.mlab.detrend_mean")

Another detrend algorithm.

[`detrend_linear`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend_linear "matplotlib.mlab.detrend_linear")

Another detrend algorithm.

[`detrend`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.detrend "matplotlib.mlab.detrend")

A wrapper around all the detrend algorithms.

matplotlib.mlab.magnitude\_spectrum(_x_, _Fs\=None_, _window\=None_, _pad\_to\=None_, _sides\=None_)[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "Link to this definition")

Compute the magnitude (absolute value) of the frequency spectrum of _x_. Data is padded to a length of _pad\_to_ and the windowing function _window_ is applied to the signal.

Parameters:

**x**1-D array or sequence

Array or sequence containing the data

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

The number of points to which the data segment is padded when performing the FFT. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the _n_ parameter in the call to [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "(in NumPy v2.5)")
. The default is None, which sets _pad\_to_ equal to the length of the input signal (i.e. no padding).

Returns:

**spectrum**1-D array

The magnitude (absolute value) of the frequency spectrum.

**freqs**1-D array

The frequencies corresponding to the elements in _spectrum_.

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

Returns the power spectral density.

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

Returns the complex-valued frequency spectrum.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

Returns the absolute value of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

Returns the angle of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

Returns the phase (unwrapped angle) of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

Can return the complex spectrum of segments within the signal.

matplotlib.mlab.phase\_spectrum(_x_, _Fs\=None_, _window\=None_, _pad\_to\=None_, _sides\=None_)[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "Link to this definition")

Compute the phase of the frequency spectrum (unwrapped phase spectrum) of _x_. Data is padded to a length of _pad\_to_ and the windowing function _window_ is applied to the signal.

Parameters:

**x**1-D array or sequence

Array or sequence containing the data

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

The number of points to which the data segment is padded when performing the FFT. While not increasing the actual resolution of the spectrum (the minimum distance between resolvable peaks), this can give more points in the plot, allowing for more detail. This corresponds to the _n_ parameter in the call to [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "(in NumPy v2.5)")
. The default is None, which sets _pad\_to_ equal to the length of the input signal (i.e. no padding).

Returns:

**spectrum**1-D array

The phase of the frequency spectrum (unwrapped phase spectrum).

**freqs**1-D array

The frequencies corresponding to the elements in _spectrum_.

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

Returns the power spectral density.

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

Returns the complex-valued frequency spectrum.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

Returns the absolute value of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

Returns the angle of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

Returns the phase (unwrapped angle) of the [`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")
.

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

Can return the complex spectrum of segments within the signal.

matplotlib.mlab.psd(_x_, _NFFT\=None_, _Fs\=None_, _detrend\=None_, _window\=None_, _noverlap\=None_, _pad\_to\=None_, _sides\=None_, _scale\_by\_freq\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L479-L532)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "Link to this definition")

Compute the power spectral density.

The power spectral density \\(P\_{xx}\\) by Welch's average periodogram method. The vector _x_ is divided into _NFFT_ length segments. Each segment is detrended by function _detrend_ and windowed by function _window_. _noverlap_ gives the length of the overlap between segments. The \\(|\\mathrm{fft}(i)|^2\\) of each segment \\(i\\) are averaged to compute \\(P\_{xx}\\).

If len(_x_) < _NFFT_, it will be zero padded to _NFFT_.

Parameters:

**x**1-D array or sequence

Array or sequence containing the data

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

**noverlap**int, default: 0 (no overlap)

The number of points of overlap between segments.

Returns:

**Pxx**1-D array

The values for the power spectrum \\(P\_{xx}\\) (real valued)

**freqs**1-D array

The frequencies corresponding to the elements in _Pxx_

See also

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")

[`specgram`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "matplotlib.mlab.specgram")
 differs in the default overlap; in not returning the mean of the segment periodograms; and in returning the times of the segments.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

returns the magnitude spectrum.

[`csd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.csd "matplotlib.mlab.csd")

returns the spectral density between two signals.

References

Bendat & Piersol -- Random Data: Analysis and Measurement Procedures, John Wiley & Sons (1986)

matplotlib.mlab.specgram(_x_, _NFFT\=None_, _Fs\=None_, _detrend\=None_, _window\=None_, _noverlap\=None_, _pad\_to\=None_, _sides\=None_, _scale\_by\_freq\=None_, _mode\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L655-L735)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.specgram "Link to this definition")

Compute a spectrogram.

Compute and plot a spectrogram of data in _x_. Data are split into _NFFT_ length segments and the spectrum of each section is computed. The windowing function _window_ is applied to each segment, and the amount of overlap of each segment is specified with _noverlap_.

Parameters:

**x**array-like

1-D array or sequence.

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

**noverlap**int, default: 128

The number of points of overlap between blocks.

**mode**str, default: 'psd'

What sort of spectrum to use:

'psd'

Returns the power spectral density.

'complex'

Returns the complex-valued frequency spectrum.

'magnitude'

Returns the magnitude spectrum.

'angle'

Returns the phase spectrum without unwrapping.

'phase'

Returns the phase spectrum with unwrapping.

Returns:

**spectrum**array-like

2D array, columns are the periodograms of successive segments.

**freqs**array-like

1-D array, frequencies corresponding to the rows in _spectrum_.

**t**array-like

1-D array, the times corresponding to midpoints of segments (i.e the columns in _spectrum_).

See also

[`psd`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.psd "matplotlib.mlab.psd")

differs in the overlap and in the return values.

[`complex_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.complex_spectrum "matplotlib.mlab.complex_spectrum")

similar, but with complex valued frequencies.

[`magnitude_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.magnitude_spectrum "matplotlib.mlab.magnitude_spectrum")

similar single segment when _mode_ is 'magnitude'.

[`angle_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.angle_spectrum "matplotlib.mlab.angle_spectrum")

similar to single segment when _mode_ is 'angle'.

[`phase_spectrum`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.phase_spectrum "matplotlib.mlab.phase_spectrum")

similar to single segment when _mode_ is 'phase'.

Notes

_detrend_ and _scale\_by\_freq_ only apply when _mode_ is set to 'psd'.

matplotlib.mlab.window\_hanning(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L59-L67)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_hanning "Link to this definition")

Return _x_ times the Hanning (or Hann) window of len(_x_).

See also

[`window_none`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_none "matplotlib.mlab.window_none")

Another window algorithm.

matplotlib.mlab.window\_none(_x_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/mlab.py#L70-L78)
[#](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_none "Link to this definition")

No window function; simply return _x_.

See also

[`window_hanning`](https://matplotlib.org/stable/api/mlab_api.html#matplotlib.mlab.window_hanning "matplotlib.mlab.window_hanning")

Another window algorithm.

On this page