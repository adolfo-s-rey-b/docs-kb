None

[KerasHub: Pretrained Models](https://keras.io/keras_hub/)

[Getting started](https://keras.io/keras_hub/getting_started/)
 [Developer guides](https://keras.io/keras_hub/guides/)
 [API documentation](https://keras.io/keras_hub/api/)
 [Modeling API](https://keras.io/keras_hub/api/base_classes/)
 [Model Architectures](https://keras.io/keras_hub/api/models/)
 [Tokenizers](https://keras.io/keras_hub/api/tokenizers/)
 [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 [Samplers](https://keras.io/keras_hub/api/samplers/)
 [Metrics](https://keras.io/keras_hub/api/metrics/)
 [Pretrained models list](https://keras.io/keras_hub/presets/)

► [KerasHub: Pretrained Models](https://keras.io/keras_hub/)
 / [API documentation](https://keras.io/keras_hub/api/)
 / [Preprocessing Layers](https://keras.io/keras_hub/api/preprocessing_layers/)
 / RandomSwap layer

RandomSwap layer
================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/preprocessing/random_swap.py#L17)

### `RandomSwap` class

Copied!

`keras_hub.layers.RandomSwap(     rate,     max_swaps=None,     skip_list=None,     skip_fn=None,     skip_py_fn=None,     seed=None,     name=None,     dtype="int32",     **kwargs )`

Augments input by randomly swapping words.

This layer comes in handy when you need to generate new data using swap augmentations as described in the paper \[EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks\] (https://arxiv.org/pdf/1901.11196.pdf). The layer expects the inputs to be pre-split into token level inputs. This allows control over the level of augmentation, you can split by character for character level swaps, or by word for word level swaps.

Input data should be passed as tensors, [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
s, or lists. For batched input, inputs should be a list of lists or a rank two tensor. For unbatched inputs, each element should be a list or a rank one tensor.

This layer runs on a pure Python/NumPy code path by default, so it works inside a Grain pipeline and does not require TensorFlow. Randomness is derived from `seed` together with a stable hash of the record being augmented, so the output does not depend on how many Grain workers are running or on the order records are seen in. The tradeoff is that an identical record is augmented identically on every epoch. To vary the augmentation per epoch, pass your own generator as `rng`, for example from `grain.RandomMapTransform`, which derives one from the element index.

**Arguments**

*   **rate**: The probability of a given token being chosen to be swapped with another random token.
*   **max\_swaps**: The maximum number of swaps to be performed.
*   **skip\_list**: A list of token values that should not be considered candidates for deletion.
*   **skip\_fn**: A function that takes as input a scalar tensor token and returns as output a scalar tensor True/False value. A value of True indicates that the token should not be considered a candidate for deletion. This function must be tracable–it should consist of tensorflow operations. Setting this forces the layer onto the TensorFlow code path, which cannot run in a Grain worker; prefer `skip_py_fn`.
*   **skip\_py\_fn**: A function that takes as input a python token value and returns as output `True` or `False`. A value of True indicates that should not be considered a candidate for deletion. Unlike the `skip_fn` argument, this argument need not be tracable–it can be any python function.
*   **seed**: A seed for the random number generator.

**Call arguments**

*   **inputs**: The tokens to augment.
*   **rng**: Optional `np.random.Generator` used instead of the per record generator derived from `seed`. Only supported on the pure Python code path. With a batched input, every row draws from this one generator in order, so a row's augmentation depends on where it sits in the batch.

**Examples**

Word level usage.

Copied!

`>>> x = ["Hey I like", "Keras and Tensorflow"] >>> x = list(map(lambda x: x.split(), x)) >>> augmenter = keras_hub.layers.RandomSwap(rate=0.4, seed=9) >>> y = augmenter(x) >>> list(map(lambda y: " ".join(y), y)) ['I Hey like', 'and Tensorflow Keras']`

Character level usage.

Copied!

`>>> x = ["Hey Dude", "Speed Up"] >>> x = list(map(lambda x: list(x), x)) >>> augmenter = keras_hub.layers.RandomSwap(rate=0.4, seed=42) >>> y = augmenter(x) >>> list(map(lambda y: "".join(y), y)) ['Heyu edD', ' eedpUpS']`

Usage with skip\_list.

Copied!

`>>> x = ["Hey I like", "Keras and Tensorflow"] >>> x = list(map(lambda x: x.split(), x)) >>> augmenter = keras_hub.layers.RandomSwap(rate=0.4, ...     skip_list=["Keras"], seed=9) >>> y = augmenter(x) >>> list(map(lambda y: " ".join(y), y)) ['I Hey like', 'Keras Tensorflow and']`

Usage with skip\_fn.

Copied!

`>>> def skip_fn(word): ...     return tf.strings.regex_full_match(word, r"[I, a].*") >>> keras.utils.set_random_seed(1337) >>> x = ["Hey I like", "Keras and Tensorflow"] >>> x = list(map(lambda x: x.split(), x)) >>> augmenter = keras_hub.layers.RandomSwap(rate=0.9, max_swaps=3, ...     skip_fn=skip_fn, seed=11) >>> y = augmenter(x) >>> list(map(lambda y: " ".join(y), y)) ['like I Hey', 'Keras and Tensorflow']`

Usage with skip\_py\_fn.

Copied!

`>>> def skip_py_fn(word): ...     return len(word) < 4 >>> x = ["He was drifting along", "With the wind"] >>> x = list(map(lambda x: x.split(), x)) >>> augmenter = keras_hub.layers.RandomSwap(rate=0.8, max_swaps=2, ...     skip_py_fn=skip_py_fn, seed=15) >>> y = augmenter(x) >>> list(map(lambda y: " ".join(y), y)) ['He was along drifting', 'wind the With']`

Usage in a Grain pipeline, with per epoch variation. Grain derives the generator from its own seed and the element index, so a record that comes round again on the next epoch is augmented differently.

Copied!

`>>> import grain >>> x = [["Hey", "I", "like"], ["Keras", "and", "Tensorflow"]] >>> augmenter = keras_hub.layers.RandomSwap(rate=0.4, seed=9) >>> ds = grain.MapDataset.source(x).repeat(2).random_map( ...     lambda row, rng: augmenter(row, rng=rng), seed=1) >>> len(list(ds)) 4`

* * *

[RandomSwap layer](https://keras.io/keras_hub/api/preprocessing_layers/random_swap/#randomswap-layer)

[`RandomSwap` class](https://keras.io/keras_hub/api/preprocessing_layers/random_swap/#randomswap-class)