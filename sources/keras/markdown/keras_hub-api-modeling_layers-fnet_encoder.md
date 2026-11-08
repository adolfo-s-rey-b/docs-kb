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
 / [Modeling Layers](https://keras.io/keras_hub/api/modeling_layers/)
 / FNetEncoder layer

FNetEncoder layer
=================

[\[source\]](https://github.com/keras-team/keras-hub/tree/v0.33.0/keras_hub/src/layers/modeling/f_net_encoder.py#L8)

### `FNetEncoder` class

Copied!

`keras_hub.layers.FNetEncoder(     intermediate_dim,     dropout=0,     activation="relu",     layer_norm_epsilon=1e-05,     kernel_initializer="glorot_uniform",     bias_initializer="zeros",     **kwargs )`

FNet encoder.

This class follows the architecture of FNet encoder layer in the [FNet paper](https://arxiv.org/abs/2105.03824)
. Users can instantiate multiple instances of this class to stack up the encoder.

Note on masking: In the official FNet code, padding tokens are added to the the input. However, the padding masks are deleted, i.e., mixing of all tokens is done. This is because certain frequencies will be zeroed out if we apply padding masks in every encoder layer. Hence, we don't take padding mask as input in the call() function.

**Arguments**

*   **intermediate\_dim**: int. The hidden size of feedforward network.
*   **dropout**: float. The dropout value, applied in the feedforward network. Defaults to `0.`.
*   **activation**: string or `keras.activations`. The activation function of feedforward network. Defaults to `"relu"`.
*   **layer\_norm\_epsilon**: float. The epsilon value in layer normalization components. Defaults to `1e-5`.
*   **kernel\_initializer**: `str` or `keras.initializers` initializer. The kernel initializer for the dense layers. Defaults to `"glorot_uniform"`.
*   **bias\_initializer**: "string" or `keras.initializers` initializer. The bias initializer for the dense layers. Defaults to `"zeros"`.
*   **\*\*kwargs**: other keyword arguments passed to `keras.layers.Layer`, including `name`, `trainable`, `dtype` etc.

**Example**

Copied!

`# Create a single FNet encoder layer. encoder = keras_hub.layers.FNetEncoder(     intermediate_dim=64)  # Create a simple model containing the encoder. input = keras.Input(shape=(10, 64)) output = encoder(input) model = keras.Model(inputs=input, outputs=output)  # Call encoder on the inputs. input_data = np.random.uniform(size=(1, 10, 64)) output = model(input_data)`

**References**

*   [Lee-Thorp et al., 2021](https://arxiv.org/abs/2105.03824)
    

* * *

[FNetEncoder layer](https://keras.io/keras_hub/api/modeling_layers/fnet_encoder/#fnetencoder-layer)

[`FNetEncoder` class](https://keras.io/keras_hub/api/modeling_layers/fnet_encoder/#fnetencoder-class)