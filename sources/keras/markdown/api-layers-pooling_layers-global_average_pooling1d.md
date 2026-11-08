None

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)
 [Layers API](https://keras.io/api/layers/)
 [The base Layer class](https://keras.io/api/layers/base_layer/)
 [Layer activations](https://keras.io/api/layers/activations/)
 [Layer weight initializers](https://keras.io/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/api/layers/constraints/)
 [Core layers](https://keras.io/api/layers/core_layers/)
 [Convolution layers](https://keras.io/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/api/layers/merging_layers/)
 [Activation layers](https://keras.io/api/layers/activation_layers/)
 [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)
 [Callbacks API](https://keras.io/api/callbacks/)
 [Ops API](https://keras.io/api/ops/)
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
 / [Layers API](https://keras.io/api/layers/)
 / [Pooling layers](https://keras.io/api/layers/pooling_layers/)
 / GlobalAveragePooling1D layer

GlobalAveragePooling1D layer
============================

[\[source\]](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/pooling/global_average_pooling1d.py#L6)

### `GlobalAveragePooling1D` class

Copied!

`keras.layers.GlobalAveragePooling1D(data_format=None, keepdims=False, **kwargs)`

Global average pooling operation for temporal data.

**Arguments**

*   **data\_format**: string, either `"channels_last"` or `"channels_first"`. The ordering of the dimensions in the inputs. `"channels_last"` corresponds to inputs with shape `(batch, steps, features)` while `"channels_first"` corresponds to inputs with shape `(batch, features, steps)`. It defaults to the `image_data_format` value found in your Keras config file at `~/.keras/keras.json`. If you never set it, then it will be `"channels_last"`.
*   **keepdims**: A boolean, whether to keep the temporal dimension or not. If `keepdims` is `False` (default), the rank of the tensor is reduced for spatial dimensions. If `keepdims` is `True`, the temporal dimension are retained with length 1. The behavior is the same as for [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/reduce_mean)
     or `np.mean`.

**Call arguments**

*   **inputs**: A 3D tensor.
*   **mask**: Binary tensor of shape `(batch_size, steps)` indicating whether a given step should be masked (excluded from the average).

**Input shape**

*   If `data_format='channels_last'`: 3D tensor with shape: `(batch_size, steps, features)`
*   If `data_format='channels_first'`: 3D tensor with shape: `(batch_size, features, steps)`

**Output shape**

*   If `keepdims=False`: 2D tensor with shape `(batch_size, features)`.
*   If `keepdims=True`: - If `data_format="channels_last"`: 3D tensor with shape `(batch_size, 1, features)` - If `data_format="channels_first"`: 3D tensor with shape `(batch_size, features, 1)`

**Example**

Copied!

`>>> x = np.random.rand(2, 3, 4) >>> y = keras.layers.GlobalAveragePooling1D()(x) >>> y.shape (2, 4)`

**Guides and examples using `GlobalAveragePooling1D`**

*   [Pretraining a Transformer from scratch](https://keras.io/keras_hub/guides/transformer_pretraining/)
    
*   [Text Classification using FNet](https://keras.io/examples/nlp/fnet_classification_with_keras_hub/)
    
*   [Sentence embeddings using Siamese RoBERTa-networks](https://keras.io/examples/nlp/sentence_embeddings_with_sbert/)
    
*   [Timeseries classification from scratch](https://keras.io/examples/timeseries/timeseries_classification_from_scratch/)
    
*   [Float8 training and inference with a simple Transformer model](https://keras.io/examples/keras_recipes/float8_training_and_inference_with_transformer/)
    
*   [Deep Recommenders](https://keras.io/keras_rs/examples/deep_recommender/)
    

* * *

[GlobalAveragePooling1D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling1d/#globalaveragepooling1d-layer)

[`GlobalAveragePooling1D` class](https://keras.io/api/layers/pooling_layers/global_average_pooling1d/#globalaveragepooling1d-class)