None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [The base Layer class](https://keras.io/2/api/layers/base_layer/)
 [Layer activations](https://keras.io/2/api/layers/activations/)
 [Layer weight initializers](https://keras.io/2/api/layers/initializers/)
 [Layer weight regularizers](https://keras.io/2/api/layers/regularizers/)
 [Layer weight constraints](https://keras.io/2/api/layers/constraints/)
 [Core layers](https://keras.io/2/api/layers/core_layers/)
 [Convolution layers](https://keras.io/2/api/layers/convolution_layers/)
 [Pooling layers](https://keras.io/2/api/layers/pooling_layers/)
 [Recurrent layers](https://keras.io/2/api/layers/recurrent_layers/)
 [Preprocessing layers](https://keras.io/2/api/layers/preprocessing_layers/)
 [Normalization layers](https://keras.io/2/api/layers/normalization_layers/)
 [Regularization layers](https://keras.io/2/api/layers/regularization_layers/)
 [Attention layers](https://keras.io/2/api/layers/attention_layers/)
 [Reshaping layers](https://keras.io/2/api/layers/reshaping_layers/)
 [Merging layers](https://keras.io/2/api/layers/merging_layers/)
 [Activation layers](https://keras.io/2/api/layers/activation_layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Layers API](https://keras.io/2/api/layers/)
 / [Core layers](https://keras.io/2/api/layers/core_layers/)
 / Embedding layer

Embedding layer
===============

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/layers/core/embedding.py#L34)

### `Embedding` class

Copied!

`tf_keras.layers.Embedding(     input_dim,     output_dim,     embeddings_initializer="uniform",     embeddings_regularizer=None,     activity_regularizer=None,     embeddings_constraint=None,     mask_zero=False,     input_length=None,     sparse=False,     **kwargs )`

Turns positive integers (indexes) into dense vectors of fixed size.

e.g. `[[4], [20]] -> [[0.25, 0.1], [0.6, -0.2]]`

This layer can only be used on positive integer inputs of a fixed range. The [`tf.keras.layers.TextVectorization`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization)
, [`tf.keras.layers.StringLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/StringLookup)
, and [`tf.keras.layers.IntegerLookup`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/IntegerLookup)
 preprocessing layers can help prepare inputs for an `Embedding` layer.

This layer accepts [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
, [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
 and [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/SparseTensor)
 input.

**Example**

Copied!

``>>> model = tf.keras.Sequential() >>> model.add(tf.keras.layers.Embedding(1000, 64, input_length=10)) >>> # The model will take as input an integer matrix of size (batch, >>> # input_length), and the largest integer (i.e. word index) in the input >>> # should be no larger than 999 (vocabulary size). >>> # Now model.output_shape is (None, 10, 64), where `None` is the batch >>> # dimension. >>> input_array = np.random.randint(1000, size=(32, 10)) >>> model.compile('rmsprop', 'mse') >>> output_array = model.predict(input_array) >>> print(output_array.shape) (32, 10, 64)``

**Arguments**

*   **input\_dim**: Integer. Size of the vocabulary, i.e. maximum integer index + 1.
*   **output\_dim**: Integer. Dimension of the dense embedding.
*   **embeddings\_initializer**: Initializer for the `embeddings` matrix (see `keras.initializers`).
*   **embeddings\_regularizer**: Regularizer function applied to the `embeddings` matrix (see `keras.regularizers`).
*   **embeddings\_constraint**: Constraint function applied to the `embeddings` matrix (see `keras.constraints`).
*   **mask\_zero**: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out. This is useful when using recurrent layers which may take variable length input. If this is `True`, then all subsequent layers in the model need to support masking or an exception will be raised. If mask\_zero is set to True, as a consequence, index 0 cannot be used in the vocabulary (input\_dim should equal size of vocabulary + 1).
*   **input\_length**: Length of input sequences, when it is constant. This argument is required if you are going to connect `Flatten` then `Dense` layers upstream (without it, the shape of the dense outputs cannot be computed).
*   **sparse**: If True, calling this layer returns a [`tf.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/SparseTensor)
    . If False, the layer returns a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)
    . For an entry with no features in a sparse tensor (entry with value 0), the embedding vector of index 0 is returned by default.

**Input shape**

2D tensor with shape: `(batch_size, input_length)`.

**Output shape**

3D tensor with shape: `(batch_size, input_length, output_dim)`.

**Note on variable placement:** By default, if a GPU is available, the embedding matrix will be placed on the GPU. This achieves the best performance, but it might cause issues:

*   You may be using an optimizer that does not support sparse GPU kernels. In this case you will see an error upon training your model.
*   Your embedding matrix may be too large to fit on your GPU. In this case you will see an Out Of Memory (OOM) error.

In such cases, you should place the embedding matrix on the CPU memory. You can do so with a device scope, as such:

Copied!

`with tf.device('cpu:0'):   embedding_layer = Embedding(...)   embedding_layer.build()`

The pre-built `embedding_layer` instance can then be added to a `Sequential` model (e.g. `model.add(embedding_layer)`), called in a Functional model (e.g. `x = embedding_layer(x)`), or used in a subclassed model.

* * *

[Embedding layer](https://keras.io/2/api/layers/core_layers/embedding/#embedding-layer)

[`Embedding` class](https://keras.io/2/api/layers/core_layers/embedding/#embedding-class)