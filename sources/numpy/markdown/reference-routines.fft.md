[Skip to main content](https://numpy.org/doc/stable/reference/routines.fft.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.fft.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.fft.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.fft.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.fft.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.fft.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.fft.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.fft.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.fft.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.fft.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.fft.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.fft.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.fft.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.fft.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.fft.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.fft.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.fft.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.fft.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.fft.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.fft.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.fft.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.fft.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Discrete Fourier Transform[#](https://numpy.org/doc/stable/reference/routines.fft.html#discrete-fourier-transform "Link to this heading")

==========================================================================================================================================

The SciPy module [`scipy.fft`](https://docs.scipy.org/doc/scipy/reference/fft.html#module-scipy.fft "(in SciPy v1.18.0)")
 is a more comprehensive superset of [`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
, which includes only a basic set of routines.

Standard FFTs[#](https://numpy.org/doc/stable/reference/routines.fft.html#standard-ffts "Link to this heading")

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`fft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html#numpy.fft.fft "numpy.fft.fft")<br>(a\[, n, axis, norm, out\]) | Compute the one-dimensional discrete Fourier Transform. |
| [`ifft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft "numpy.fft.ifft")<br>(a\[, n, axis, norm, out\]) | Compute the one-dimensional inverse discrete Fourier Transform. |
| [`fft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2 "numpy.fft.fft2")<br>(a\[, s, axes, norm, out\]) | Compute the 2-dimensional discrete Fourier Transform. |
| [`ifft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifft2.html#numpy.fft.ifft2 "numpy.fft.ifft2")<br>(a\[, s, axes, norm, out\]) | Compute the 2-dimensional inverse discrete Fourier Transform. |
| [`fftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftn.html#numpy.fft.fftn "numpy.fft.fftn")<br>(a\[, s, axes, norm, out\]) | Compute the N-dimensional discrete Fourier Transform. |
| [`ifftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftn.html#numpy.fft.ifftn "numpy.fft.ifftn")<br>(a\[, s, axes, norm, out\]) | Compute the N-dimensional inverse discrete Fourier Transform. |

Real FFTs[#](https://numpy.org/doc/stable/reference/routines.fft.html#real-ffts "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")<br>(a\[, n, axis, norm, out\]) | Compute the one-dimensional discrete Fourier Transform for real input. |
| [`irfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft.html#numpy.fft.irfft "numpy.fft.irfft")<br>(a\[, n, axis, norm, out\]) | Computes the inverse of [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")<br>. |
| [`rfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#numpy.fft.rfft2 "numpy.fft.rfft2")<br>(a\[, s, axes, norm, out\]) | Compute the 2-dimensional FFT of a real array. |
| [`irfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfft2.html#numpy.fft.irfft2 "numpy.fft.irfft2")<br>(a\[, s, axes, norm, out\]) | Computes the inverse of [`rfft2`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft2.html#numpy.fft.rfft2 "numpy.fft.rfft2")<br>. |
| [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")<br>(a\[, s, axes, norm, out\]) | Compute the N-dimensional discrete Fourier Transform for real input. |
| [`irfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.irfftn.html#numpy.fft.irfftn "numpy.fft.irfftn")<br>(a\[, s, axes, norm, out\]) | Computes the inverse of [`rfftn`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftn.html#numpy.fft.rfftn "numpy.fft.rfftn")<br>. |

Hermitian FFTs[#](https://numpy.org/doc/stable/reference/routines.fft.html#hermitian-ffts "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")<br>(a\[, n, axis, norm, out\]) | Compute the FFT of a signal that has Hermitian symmetry, i.e., a real spectrum. |
| [`ihfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ihfft.html#numpy.fft.ihfft "numpy.fft.ihfft")<br>(a\[, n, axis, norm, out\]) | Compute the inverse FFT of a signal that has Hermitian symmetry. |

Helper routines[#](https://numpy.org/doc/stable/reference/routines.fft.html#helper-routines "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`fftfreq`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftfreq.html#numpy.fft.fftfreq "numpy.fft.fftfreq")<br>(n\[, d, device\]) | Return the Discrete Fourier Transform sample frequencies. |
| [`rfftfreq`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfftfreq.html#numpy.fft.rfftfreq "numpy.fft.rfftfreq")<br>(n\[, d, device\]) | Return the Discrete Fourier Transform sample frequencies (for usage with rfft, irfft). |
| [`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")<br>(x\[, axes\]) | Shift the zero-frequency component to the center of the spectrum. |
| [`ifftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.ifftshift.html#numpy.fft.ifftshift "numpy.fft.ifftshift")<br>(x\[, axes\]) | The inverse of [`fftshift`](https://numpy.org/doc/stable/reference/generated/numpy.fft.fftshift.html#numpy.fft.fftshift "numpy.fft.fftshift")<br>. |

Background information[#](https://numpy.org/doc/stable/reference/routines.fft.html#background-information "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

Fourier analysis is fundamentally a method for expressing a function as a sum of periodic components, and for recovering the function from those components. When both the function and its Fourier transform are replaced with discretized counterparts, it is called the discrete Fourier transform (DFT). The DFT has become a mainstay of numerical computing in part because of a very fast algorithm for computing it, called the Fast Fourier Transform (FFT), which was known to Gauss (1805) and was brought to light in its current form by Cooley and Tukey [\[CT\]](https://numpy.org/doc/stable/reference/routines.fft.html#rfb1dc64dd6a5-ct)
. Press et al. [\[NR\]](https://numpy.org/doc/stable/reference/routines.fft.html#rfb1dc64dd6a5-nr)
 provide an accessible introduction to Fourier analysis and its applications.

Because the discrete Fourier transform separates its input into components that contribute at discrete frequencies, it has a great number of applications in digital signal processing, e.g., for filtering, and in this context the discretized input to the transform is customarily referred to as a _signal_, which exists in the _time domain_. The output is called a _spectrum_ or _transform_ and exists in the _frequency domain_.

Implementation details[#](https://numpy.org/doc/stable/reference/routines.fft.html#implementation-details "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

There are many ways to define the DFT, varying in the sign of the exponent, normalization, etc. In this implementation, the DFT is defined as

\\\[A\_k = \\sum\_{m=0}^{n-1} a\_m \\exp\\left\\{-2\\pi i{mk \\over n}\\right\\} \\qquad k = 0,\\ldots,n-1.\\\]

The DFT is in general defined for complex inputs and outputs, and a single-frequency component at linear frequency \\(f\\) is represented by a complex exponential \\(a\_m = \\exp\\{2\\pi i\\,f m\\Delta t\\}\\), where \\(\\Delta t\\) is the sampling interval.

The values in the result follow so-called “standard” order: If `A = fft(a, n)`, then `A[0]` contains the zero-frequency term (the sum of the signal), which is always purely real for real inputs. Then `A[1:n/2]` contains the positive-frequency terms, and `A[n/2+1:]` contains the negative-frequency terms, in order of decreasingly negative frequency. For an even number of input points, `A[n/2]` represents both positive and negative Nyquist frequency, and is also purely real for real input. For an odd number of input points, `A[(n-1)/2]` contains the largest positive frequency, while `A[(n+1)/2]` contains the largest negative frequency. The routine `np.fft.fftfreq(n)` returns an array giving the frequencies of corresponding elements in the output. The routine `np.fft.fftshift(A)` shifts transforms and their frequencies to put the zero-frequency components in the middle, and `np.fft.ifftshift(A)` undoes that shift.

When the input _a_ is a time-domain signal and `A = fft(a)`, `np.abs(A)` is its amplitude spectrum and `np.abs(A)**2` is its power spectrum. The phase spectrum is obtained by `np.angle(A)`.

The inverse DFT is defined as

\\\[a\_m = \\frac{1}{n}\\sum\_{k=0}^{n-1}A\_k\\exp\\left\\{2\\pi i{mk\\over n}\\right\\} \\qquad m = 0,\\ldots,n-1.\\\]

It differs from the forward transform by the sign of the exponential argument and the default normalization by \\(1/n\\).

Type Promotion[#](https://numpy.org/doc/stable/reference/routines.fft.html#type-promotion "Link to this heading")

------------------------------------------------------------------------------------------------------------------

[`numpy.fft`](https://numpy.org/doc/stable/reference/routines.fft.html#module-numpy.fft "numpy.fft")
 promotes `float32` and `complex64` arrays to `float64` and `complex128` arrays respectively. For an FFT implementation that does not promote input arrays, see [`scipy.fftpack`](https://docs.scipy.org/doc/scipy/reference/fftpack.html#module-scipy.fftpack "(in SciPy v1.18.0)")
.

Normalization[#](https://numpy.org/doc/stable/reference/routines.fft.html#normalization "Link to this heading")

----------------------------------------------------------------------------------------------------------------

The argument `norm` indicates which direction of the pair of direct/inverse transforms is scaled and with what normalization factor. The default normalization (`"backward"`) has the direct (forward) transforms unscaled and the inverse (backward) transforms scaled by \\(1/n\\). It is possible to obtain unitary transforms by setting the keyword argument `norm` to `"ortho"` so that both direct and inverse transforms are scaled by \\(1/\\sqrt{n}\\). Finally, setting the keyword argument `norm` to `"forward"` has the direct transforms scaled by \\(1/n\\) and the inverse transforms unscaled (i.e. exactly opposite to the default `"backward"`). _None_ is an alias of the default option `"backward"` for backward compatibility.

Real and Hermitian transforms[#](https://numpy.org/doc/stable/reference/routines.fft.html#real-and-hermitian-transforms "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

When the input is purely real, its transform is Hermitian, i.e., the component at frequency \\(f\_k\\) is the complex conjugate of the component at frequency \\(-f\_k\\), which means that for real inputs there is no information in the negative frequency components that is not already available from the positive frequency components. The family of [`rfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.rfft.html#numpy.fft.rfft "numpy.fft.rfft")
 functions is designed to operate on real inputs, and exploits this symmetry by computing only the positive frequency components, up to and including the Nyquist frequency. Thus, `n` input points produce `n/2+1` complex output points. The inverses of this family assumes the same symmetry of its input, and for an output of `n` points uses `n/2+1` input points.

Correspondingly, when the spectrum is purely real, the signal is Hermitian. The [`hfft`](https://numpy.org/doc/stable/reference/generated/numpy.fft.hfft.html#numpy.fft.hfft "numpy.fft.hfft")
 family of functions exploits this symmetry by using `n/2+1` complex points in the input (time) domain for `n` real points in the frequency domain.

In higher dimensions, FFTs are used, e.g., for image analysis and filtering. The computational efficiency of the FFT means that it can also be a faster way to compute large convolutions, using the property that a convolution in the time domain is equivalent to a point-by-point multiplication in the frequency domain.

Higher dimensions[#](https://numpy.org/doc/stable/reference/routines.fft.html#higher-dimensions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

In two dimensions, the DFT is defined as

\\\[A\_{kl} = \\sum\_{m=0}^{M-1} \\sum\_{n=0}^{N-1} a\_{mn}\\exp\\left\\{-2\\pi i \\left({mk\\over M}+{nl\\over N}\\right)\\right\\} \\qquad k = 0, \\ldots, M-1;\\quad l = 0, \\ldots, N-1,\\\]

which extends in the obvious way to higher dimensions, and the inverses in higher dimensions also extend in the same way.

References[#](https://numpy.org/doc/stable/reference/routines.fft.html#references "Link to this heading")

----------------------------------------------------------------------------------------------------------

\[[CT](https://numpy.org/doc/stable/reference/routines.fft.html#id1)\
\]

Cooley, James W., and John W. Tukey, 1965, “An algorithm for the machine calculation of complex Fourier series,” _Math. Comput._ 19: 297-301.

\[[NR](https://numpy.org/doc/stable/reference/routines.fft.html#id2)\
\]

Press, W., Teukolsky, S., Vetterline, W.T., and Flannery, B.P., 2007, _Numerical Recipes: The Art of Scientific Computing_, ch. 12-13. Cambridge Univ. Press, Cambridge, UK.

Examples[#](https://numpy.org/doc/stable/reference/routines.fft.html#examples "Link to this heading")

------------------------------------------------------------------------------------------------------

For examples, see the various functions.

On this page