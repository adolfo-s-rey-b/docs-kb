None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
 [The Operation class](https://keras.io/api/ops/operation/)
 [NumPy ops](https://keras.io/api/ops/numpy/)
 [NN ops](https://keras.io/api/ops/nn/)
 [Linear algebra ops](https://keras.io/api/ops/linalg/)
 [Core ops](https://keras.io/api/ops/core/)
 [Image ops](https://keras.io/api/ops/image/)
 [FFT ops](https://keras.io/api/ops/fft/)
 [Einops ops](https://keras.io/api/ops/einops/)
 [Math ops](https://keras.io/api/ops/math/)
 [Optimizers](https://keras.io/api/optimizers/)
 [Metrics](https://keras.io/api/metrics/)
 [Losses](https://keras.io/api/losses/)
 [Data loading](https://keras.io/api/data_loading/)
 [Tree API](https://keras.io/api/tree/)
 [Built-in small datasets](https://keras.io/api/datasets/)
 [Keras Applications](https://keras.io/api/applications/)
 [Mixed precision](https://keras.io/api/mixed_precision/)
 [Multi-device distribution](https://keras.io/api/distribution/)
 [RNG API](https://keras.io/api/random/)
 [Quantizers](https://keras.io/api/quantizers/)
 [Scope](https://keras.io/api/scope/)
 [Rematerialization](https://keras.io/api/rematerialization/)
 [Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

► [Keras 3 API documentation](https://keras.io/api/)
 / [Ops API](https://keras.io/api/ops/)
 / FFT ops

FFT ops
=======

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L533)

### `fft` function

Copied!

`keras.ops.fft(x)`

Computes the Fast Fourier Transform along last axis of input.

**Arguments**

*   **x**: Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type.

**Returns**

A tuple containing two tensors - the real and imaginary parts of the output tensor.

**Example**

Copied!

`>>> x = ( ...     keras.ops.convert_to_tensor([1., 2.]), ...     keras.ops.convert_to_tensor([0., 1.]), ... ) >>> fft(x) (array([ 3., -1.], dtype=float32), array([ 1., -1.], dtype=float32))`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L602)

### `fft2` function

Copied!

`keras.ops.fft2(x)`

Computes the 2D Fast Fourier Transform along the last two axes of input.

**Arguments**

*   **x**: Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type.

**Returns**

A tuple containing two tensors - the real and imaginary parts of the output.

**Example**

Copied!

`>>> x = ( ...     keras.ops.convert_to_tensor([[1., 2.], [2., 1.]]), ...     keras.ops.convert_to_tensor([[0., 1.], [1., 0.]]), ... ) >>> fft2(x) (array([[ 6.,  0.],     [ 0., -2.]], dtype=float32), array([[ 2.,  0.],     [ 0., -2.]], dtype=float32))`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L673)

### `ifft2` function

Copied!

`keras.ops.ifft2(x)`

Computes the 2D Inverse Fast Fourier Transform along the last two axes of input.

**Arguments**

*   **x**: Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type.

**Returns**

A tuple containing two tensors - the real and imaginary parts of the output.

**Example**

Copied!

`>>> x = ( ...     keras.ops.convert_to_tensor([[1., 2.], [2., 1.]]), ...     keras.ops.convert_to_tensor([[0., 1.], [1., 0.]]), ... ) >>> ifft2(x) (array([[ 6.,  0.],     [ 0., -2.]], dtype=float32), array([[ 2.,  0.],     [ 0., -2.]], dtype=float32))`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L814)

### `irfft` function

Copied!

`keras.ops.irfft(x, fft_length=None)`

Inverse real-valued Fast Fourier transform along the last axis.

Computes the inverse 1D Discrete Fourier Transform of a real-valued signal over the inner-most dimension of input.

The inner-most dimension of the input is assumed to be the result of RFFT: the `fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If `fft_length` is not provided, it is computed from the size of the inner-most dimension of the input `(fft_length = 2 * (inner - 1))`. If the FFT length used to compute is odd, it should be provided since it cannot be inferred properly.

Along the axis IRFFT is computed on, if `fft_length / 2 + 1` is smaller than the corresponding dimension of the input, the dimension is cropped. If it is larger, the dimension is padded with zeros.

**Arguments**

*   **x**: Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type.
*   **fft\_length**: An integer representing the number of the fft length. If not specified, it is inferred from the length of the last axis of `x`. Defaults to `None`.

**Returns**

A tensor containing the inverse real-valued Fast Fourier Transform along the last axis of `x`.

**Examples**

Copied!

`>>> real = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0]) >>> imag = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0]) >>> irfft((real, imag)) array([0.66666667, -0.9106836, 0.24401694])`

Copied!

`>>> irfft(rfft(real, 5), 5) array([0.0, 1.0, 2.0, 3.0, 4.0])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L1032)

### `istft` function

Copied!

`keras.ops.istft(     x,     sequence_length,     sequence_stride,     fft_length,     length=None,     window="hann",     center=True, )`

Inverse Short-Time Fourier Transform along the last axis of the input.

To reconstruct an original waveform, the parameters should be the same in `stft`.

**Arguments**

*   **x**: Tuple of the real and imaginary parts of the input tensor. Both tensors in the tuple should be of floating type.
*   **sequence\_length**: An integer representing the sequence length.
*   **sequence\_stride**: An integer representing the sequence hop size.
*   **fft\_length**: An integer representing the size of the FFT that produced `stft`. Should be of type `int32`.
*   **length**: An integer representing the output is clipped to exactly length. If not specified, no padding or clipping take place. Defaults to `None`.
*   **window**: A string, a tensor of the window or `None`. If `window` is a string, available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`.
*   **center**: Whether `x` was padded on both sides so that the t-th sequence is centered at time `t * sequence_stride`. Defaults to `True`.

**Returns**

A tensor containing the inverse Short-Time Fourier Transform along the last axis of `x`.

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0]) >>> istft(stft(x, 1, 1, 1), 1, 1, 1) array([0.0, 1.0, 2.0, 3.0, 4.0])`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L733)

### `rfft` function

Copied!

`keras.ops.rfft(x, fft_length=None)`

Real-valued Fast Fourier Transform along the last axis of the input.

Computes the 1D Discrete Fourier Transform of a real-valued signal over the inner-most dimension of input.

Since the Discrete Fourier Transform of a real-valued signal is Hermitian-symmetric, RFFT only returns the `fft_length / 2 + 1` unique components of the FFT: the zero-frequency term, followed by the `fft_length / 2` positive-frequency terms.

Along the axis RFFT is computed on, if `fft_length` is smaller than the corresponding dimension of the input, the dimension is cropped. If it is larger, the dimension is padded with zeros.

**Arguments**

*   **x**: Input tensor.
*   **fft\_length**: An integer representing the number of the fft length. If not specified, it is inferred from the length of the last axis of `x`. Defaults to `None`.

**Returns**

A tuple containing two tensors - the real and imaginary parts of the output.

**Examples**

Copied!

`>>> x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0]) >>> rfft(x) (array([10.0, -2.5, -2.5]), array([0.0, 3.4409548, 0.81229924]))`

Copied!

`>>> rfft(x, 3) (array([3.0, -1.5]), array([0.0, 0.8660254]))`

* * *

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/math.py#L903)

### `stft` function

Copied!

`keras.ops.stft(     x, sequence_length, sequence_stride, fft_length, window="hann", center=True )`

Short-Time Fourier Transform along the last axis of the input.

The STFT computes the Fourier transform of short overlapping windows of the input. This giving frequency components of the signal as they change over time.

**Arguments**

*   **x**: Input tensor.
*   **sequence\_length**: An integer representing the sequence length.
*   **sequence\_stride**: An integer representing the sequence hop size.
*   **fft\_length**: An integer representing the size of the FFT to apply. If not specified, uses the smallest power of 2 enclosing `sequence_length`.
*   **window**: A string, a tensor of the window or `None`. If `window` is a string, available values are `"hann"` and `"hamming"`. If `window` is a tensor, it will be used directly as the window and its length must be `sequence_length`. If `window` is `None`, no windowing is used. Defaults to `"hann"`.
*   **center**: Whether to pad `x` on both sides so that the t-th sequence is centered at time `t * sequence_stride`. Otherwise, the t-th sequence begins at time `t * sequence_stride`. Defaults to `True`.

**Returns**

A tuple containing two tensors - the real and imaginary parts of the STFT output.

**Example**

Copied!

`>>> x = keras.ops.convert_to_tensor([0.0, 1.0, 2.0, 3.0, 4.0]) >>> stft(x, 3, 2, 3) (array([[0.75, -0.375],    [3.75, -1.875],    [5.25, -2.625]]), array([[0.0, 0.64951905],    [0.0, 0.64951905],    [0.0, -0.64951905]]))`

* * *

[FFT ops](https://keras.io/api/ops/fft/#fft-ops)

[`fft` function](https://keras.io/api/ops/fft/#fft-function)

[`fft2` function](https://keras.io/api/ops/fft/#fft2-function)

[`ifft2` function](https://keras.io/api/ops/fft/#ifft2-function)

[`irfft` function](https://keras.io/api/ops/fft/#irfft-function)

[`istft` function](https://keras.io/api/ops/fft/#istft-function)

[`rfft` function](https://keras.io/api/ops/fft/#rfft-function)

[`stft` function](https://keras.io/api/ops/fft/#stft-function)