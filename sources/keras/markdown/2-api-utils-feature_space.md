None

[Keras 3 API documentation](https://keras.io/api/)
 [Keras 2 API documentation](https://keras.io/2/api/)

[Models API](https://keras.io/2/api/models/)
 [Layers API](https://keras.io/2/api/layers/)
 [Callbacks API](https://keras.io/2/api/callbacks/)
 [Optimizers](https://keras.io/2/api/optimizers/)
 [Metrics](https://keras.io/2/api/metrics/)
 [Losses](https://keras.io/2/api/losses/)
 [Data loading](https://keras.io/2/api/data_loading/)
 [Built-in small datasets](https://keras.io/2/api/datasets/)
 [Keras Applications](https://keras.io/2/api/applications/)
 [Mixed precision](https://keras.io/2/api/mixed_precision/)
 [Utilities](https://keras.io/2/api/utils/)
 [Model plotting utilities](https://keras.io/2/api/utils/model_plotting_utils/)
 [Structured data preprocessing utilities](https://keras.io/2/api/utils/feature_space/)
 [Python & NumPy utilities](https://keras.io/2/api/utils/python_utils/)
 [Backend utilities](https://keras.io/2/api/utils/backend_utils/)

► [Keras 2 API documentation](https://keras.io/2/api/)
 / [Utilities](https://keras.io/2/api/utils/)
 / Structured data preprocessing utilities

Structured data preprocessing utilities
=======================================

[\[source\]](https://github.com/keras-team/tf-keras/tree/v2.20.0/tf_keras/utils/feature_space.py#L89)

### `FeatureSpace` class

Copied!

`tf_keras.utils.FeatureSpace(     features,     output_mode="concat",     crosses=None,     crossing_dim=32,     hashing_dim=32,     num_discretization_bins=32, )`

One-stop utility for preprocessing and encoding structured data.

**Arguments**

*   **feature\_names**: Dict mapping the names of your features to their type specification, e.g. `{"my_feature": "integer_categorical"}` or `{"my_feature": FeatureSpace.integer_categorical()}`. For a complete list of all supported types, see "Available feature types" paragraph below.
*   **output\_mode**: One of `"concat"` or `"dict"`. In concat mode, all features get concatenated together into a single vector. In dict mode, the FeatureSpace returns a dict of individually encoded features (with the same keys as the input dict keys).
*   **crosses**: List of features to be crossed together, e.g. `crosses=[("feature_1", "feature_2")]`. The features will be "crossed" by hashing their combined value into a fixed-length vector.
*   **crossing\_dim**: Default vector size for hashing crossed features. Defaults to `32`.
*   **hashing\_dim**: Default vector size for hashing features of type `"integer_hashed"` and `"string_hashed"`. Defaults to `32`.
*   **num\_discretization\_bins**: Default number of bins to be used for discretizing features of type `"float_discretized"`. Defaults to `32`.

**Available feature types:**

Note that all features can be referred to by their string name, e.g. `"integer_categorical"`. When using the string name, the default argument values are used.

Copied!

``# Plain float values. FeatureSpace.float(name=None)  # Float values to be preprocessed via featurewise standardization # (i.e. via a [`keras.layers.Normalization`](/api/layers/preprocessing_layers/numerical/normalization#normalization-class) layer). FeatureSpace.float_normalized(name=None)  # Float values to be preprocessed via linear rescaling # (i.e. via a [`keras.layers.Rescaling`](/api/layers/preprocessing_layers/image_preprocessing/rescaling#rescaling-class) layer). FeatureSpace.float_rescaled(scale=1., offset=0., name=None)  # Float values to be discretized. By default, the discrete # representation will then be one-hot encoded. FeatureSpace.float_discretized(     num_bins, bin_boundaries=None, output_mode="one_hot", name=None)  # Integer values to be indexed. By default, the discrete # representation will then be one-hot encoded. FeatureSpace.integer_categorical(     max_tokens=None, num_oov_indices=1, output_mode="one_hot", name=None)  # String values to be indexed. By default, the discrete # representation will then be one-hot encoded. FeatureSpace.string_categorical(     max_tokens=None, num_oov_indices=1, output_mode="one_hot", name=None)  # Integer values to be hashed into a fixed number of bins. # By default, the discrete representation will then be one-hot encoded. FeatureSpace.integer_hashed(num_bins, output_mode="one_hot", name=None)  # String values to be hashed into a fixed number of bins. # By default, the discrete representation will then be one-hot encoded. FeatureSpace.string_hashed(num_bins, output_mode="one_hot", name=None)``

**Examples**

**Basic usage with a dict of input data:**

Copied!

``raw_data = {     "float_values": [0.0, 0.1, 0.2, 0.3],     "string_values": ["zero", "one", "two", "three"],     "int_values": [0, 1, 2, 3], } dataset = tf.data.Dataset.from_tensor_slices(raw_data)  feature_space = FeatureSpace(     features={         "float_values": "float_normalized",         "string_values": "string_categorical",         "int_values": "integer_categorical",     },     crosses=[("string_values", "int_values")],     output_mode="concat", ) # Before you start using the FeatureSpace, # you must `adapt()` it on some data. feature_space.adapt(dataset)  # You can call the FeatureSpace on a dict of data (batched or unbatched). output_vector = feature_space(raw_data)``

**Basic usage with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
:**

Copied!

`# Unlabeled data preprocessed_ds = unlabeled_dataset.map(feature_space)  # Labeled data preprocessed_ds = labeled_dataset.map(lambda x, y: (feature_space(x), y))`

**Basic usage with the TF-Keras Functional API:**

Copied!

`# Retrieve a dict TF-Keras Input objects inputs = feature_space.get_inputs() # Retrieve the corresponding encoded TF-Keras tensors encoded_features = feature_space.get_encoded_features() # Build a Functional model outputs = keras.layers.Dense(1, activation="sigmoid")(encoded_features) model = keras.Model(inputs, outputs)`

**Customizing each feature or feature cross:**

Copied!

`feature_space = FeatureSpace(     features={         "float_values": FeatureSpace.float_normalized(),         "string_values": FeatureSpace.string_categorical(max_tokens=10),         "int_values": FeatureSpace.integer_categorical(max_tokens=10),     },     crosses=[         FeatureSpace.cross(("string_values", "int_values"), crossing_dim=32)     ],     output_mode="concat", )`

**Returning a dict of integer-encoded features:**

Copied!

`feature_space = FeatureSpace(     features={         "string_values": FeatureSpace.string_categorical(output_mode="int"),         "int_values": FeatureSpace.integer_categorical(output_mode="int"),     },     crosses=[         FeatureSpace.cross(             feature_names=("string_values", "int_values"),             crossing_dim=32,             output_mode="int",         )     ],     output_mode="dict", )`

**Specifying your own TF-Keras preprocessing layer:**

Copied!

`# Let's say that one of the features is a short text paragraph that # we want to encode as a vector (one vector per paragraph) via TF-IDF. data = {     "text": ["1st string", "2nd string", "3rd string"], }  # There's a TF-Keras layer for this: TextVectorization. custom_layer = layers.TextVectorization(output_mode="tf_idf")  # We can use FeatureSpace.feature to create a custom feature # that will use our preprocessing layer. feature_space = FeatureSpace(     features={         "text": FeatureSpace.feature(             preprocessor=custom_layer, dtype="string", output_mode="float"         ),     },     output_mode="concat", ) feature_space.adapt(tf.data.Dataset.from_tensor_slices(data)) output_vector = feature_space(data)`

**Retrieving the underlying TF-Keras preprocessing layers:**

Copied!

``# The preprocessing layer of each feature is available in `.preprocessors`. preprocessing_layer = feature_space.preprocessors["feature1"]  # The crossing layer of each feature cross is available in `.crossers`. # It's an instance of keras.layers.HashedCrossing. crossing_layer = feature_space.crossers["feature1_X_feature2"]``

**Saving and reloading a FeatureSpace:**

Copied!

`feature_space.save("myfeaturespace.keras") reloaded_feature_space = keras.models.load_model("myfeaturespace.keras")`

* * *

[Structured data preprocessing utilities](https://keras.io/2/api/utils/feature_space/#structured-data-preprocessing-utilities)

[`FeatureSpace` class](https://keras.io/2/api/utils/feature_space/#featurespace-class)