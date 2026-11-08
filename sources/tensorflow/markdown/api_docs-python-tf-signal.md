[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/signal#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/signal)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/signal?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/signal#functions)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.signal Stay organized with collections Save and categorize content based on your preferences.
========================================================================================================

*   On this page
*   [Functions](https://www.tensorflow.org/api_docs/python/tf/signal#functions)
    

Public API for tf.\_api.v2.signal namespace

Functions
---------

[`dct(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/dct)
: Computes the 1D \[Discrete Cosine Transform (DCT)\]\[dct\] of `input`.

[`fft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/fft)
: Fast Fourier transform.

[`fft2d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/fft2d)
: 2D fast Fourier transform.

[`fft3d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/fft3d)
: 3D fast Fourier transform.

[`fftnd(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/fftnd)
: ND fast Fourier transform.

[`fftshift(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/fftshift)
: Shift the zero-frequency component to the center of the spectrum.

[`frame(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/frame)
: Expands `signal`'s `axis` dimension into frames of `frame_length`.

[`hamming_window(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/hamming_window)
: Generate a \[Hamming\]\[hamming\] window.

[`hann_window(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/hann_window)
: Generate a \[Hann window\]\[hann\].

[`idct(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/idct)
: Computes the 1D \[Inverse Discrete Cosine Transform (DCT)\]\[idct\] of `input`.

[`ifft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft)
: Inverse fast Fourier transform.

[`ifft2d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft2d)
: Inverse 2D fast Fourier transform.

[`ifft3d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/ifft3d)
: Inverse 3D fast Fourier transform.

[`ifftnd(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/ifftnd)
: ND inverse fast Fourier transform.

[`ifftshift(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/ifftshift)
: The inverse of fftshift.

[`inverse_mdct(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_mdct)
: Computes the inverse modified DCT of `mdcts`.

[`inverse_stft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft)
: Computes the inverse \[Short-time Fourier Transform\]\[stft\] of `stfts`.

[`inverse_stft_window_fn(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/inverse_stft_window_fn)
: Generates a window function that can be used in `inverse_stft`.

[`irfft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft)
: Inverse real-valued fast Fourier transform.

[`irfft2d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft2d)
: Inverse 2D real-valued fast Fourier transform.

[`irfft3d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/irfft3d)
: Inverse 3D real-valued fast Fourier transform.

[`irfftnd(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/irfftnd)
: ND inverse real fast Fourier transform.

[`kaiser_bessel_derived_window(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/kaiser_bessel_derived_window)
: Generate a \[Kaiser Bessel derived window\]\[kbd\].

[`kaiser_window(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/kaiser_window)
: Generate a \[Kaiser window\]\[kaiser\].

[`linear_to_mel_weight_matrix(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/linear_to_mel_weight_matrix)
: Returns a matrix to warp linear scale spectrograms to the \[mel scale\]\[mel\].

[`mdct(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/mdct)
: Computes the \[Modified Discrete Cosine Transform\]\[mdct\] of `signals`.

[`mfccs_from_log_mel_spectrograms(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/mfccs_from_log_mel_spectrograms)
: Computes \[MFCCs\]\[mfcc\] of `log_mel_spectrograms`.

[`overlap_and_add(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/overlap_and_add)
: Reconstructs a signal from a framed representation.

[`rfft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft)
: Real-valued fast Fourier transform.

[`rfft2d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft2d)
: 2D real-valued fast Fourier transform.

[`rfft3d(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/rfft3d)
: 3D real-valued fast Fourier transform.

[`rfftnd(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/rfftnd)
: ND fast real Fourier transform.

[`stft(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/stft)
: Computes the \[Short-time Fourier Transform\]\[stft\] of `signals`.

[`vorbis_window(...)`](https://www.tensorflow.org/api_docs/python/tf/signal/vorbis_window)
: Generate a \[Vorbis power complementary window\]\[vorbis\].

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2024-04-26 UTC.