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
 / Einops ops

Einops ops
==========

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/ops/einops.py#L106)

### `rearrange` function

Copied!

`keras.ops.rearrange(tensor, pattern, **axes_lengths)`

Rearranges the axes of a Keras tensor according to a specified pattern, einops-style.

**Arguments**

*   **tensor**: Input Keras tensor.
*   **pattern**: String describing the rearrangement in einops notation.
*   **\*\*axes\_lengths**: Keyword arguments specifying lengths of axes when axes decomposition is used.

**Returns**

*   **Tensor**: A Keras tensor with rearranged axes.

Follows the logic of:

1.  If decomposition is needed, reshape to match decomposed dimensions.
2.  Permute known and inferred axes to match the form of the output.
3.  Reshape to match the desired output shape.

Example Usage:

Copied!

` ```python >>> import numpy as np >>> from keras.ops import rearrange >>> images = np.random.rand(32, 30, 40, 3) # BHWC format `

Reordering to BCHW
==================

Copied!

`>>> rearrange(images, 'b h w c -> b c h w').shape TensorShape([32, 3, 30, 40])`

"Merge" along first axis - concat images from a batch
=====================================================

Copied!

`>>> rearrange(images, 'b h w c -> (b h) w c').shape TensorShape([960, 40, 3])`

"Merge" along second axis - concat images horizontally
======================================================

Copied!

`>>> rearrange(images, 'b h w c -> h (b w) c').shape TensorShape([30, 1280, 3])`

Flatten images into a CHW vector
================================

Copied!

`>>> rearrange(images, 'b h w c -> b (c h w)').shape TensorShape([32, 3600])`

Decompose H and W axes into 4 smaller patches
=============================================

Copied!

`>>> rearrange(images, 'b (h1 h) (w1 w) c -> (b h1 w1) h w c', h1=2, w1=2).shape TensorShape([128, 15, 20, 3])`

Space-to-depth decomposition of input axes
==========================================

Copied!

`>>> rearrange(images, 'b (h h1) (w w1) c -> b h w (c h1 w1)', h1=2, w1=2).shape TensorShape([32, 15, 20, 12])`

\`\`\`

* * *

[Einops ops](https://keras.io/api/ops/einops/#einops-ops)

[`rearrange` function](https://keras.io/api/ops/einops/#rearrange-function)