[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fkeras%2Futils%2FFeatureSpace%3Fversion%3Dstable&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#methods_2)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#adapt)
        
    *   [cross](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#cross)
        
    *   [feature](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#feature)
        
    *   [float](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float)
        
    *   [float\_discretized](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_discretized)
        
    *   [float\_normalized](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_normalized)
        
    *   [float\_rescaled](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_rescaled)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#from_config)
        
    *   [get\_encoded\_features](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#get_encoded_features)
        
    *   [get\_inputs](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#get_inputs)
        
    *   [integer\_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#integer_categorical)
        
    *   [integer\_hashed](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#integer_hashed)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#save)
        
    *   [string\_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#string_categorical)
        
    *   [string\_hashed](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#string_hashed)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.FeatureSpace Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

*   On this page
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#arguments_1)
    
*   [Attributes](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#attributes_1)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#methods_2)
    *   [adapt](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#adapt)
        
    *   [cross](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#cross)
        
    *   [feature](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#feature)
        
    *   [float](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float)
        
    *   [float\_discretized](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_discretized)
        
    *   [float\_normalized](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_normalized)
        
    *   [float\_rescaled](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#float_rescaled)
        
    *   [from\_config](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#from_config)
        
    *   [get\_encoded\_features](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#get_encoded_features)
        
    *   [get\_inputs](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#get_inputs)
        
    *   [integer\_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#integer_categorical)
        
    *   [integer\_hashed](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#integer_hashed)
        
    *   [save](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#save)
        
    *   [string\_categorical](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#string_categorical)
        
    *   [string\_hashed](https://www.tensorflow.org/api_docs/python/tf/keras/utils/FeatureSpace?version=stable#string_hashed)
        

See Stable See Nightly

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L81-L818)

One-stop utility for preprocessing and encoding structured data.

Inherits From: [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/Layer)
, [`Operation`](https://www.tensorflow.org/api_docs/python/tf/keras/Operation)

tf.keras.utils.FeatureSpace(
        features,
        output_mode='concat',
        crosses=None,
        crossing_dim=32,
        hashing_dim=32,
        num_discretization_bins=32,
        name=None
    )

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `feature_names` | Dict mapping the names of your features to their type specification, e.g. `{"my_feature": "integer_categorical"}` or `{"my_feature": FeatureSpace.integer_categorical()}`. For a complete list of all supported types, see "Available feature types" paragraph below. |
| `output_mode` | One of `"concat"` or `"dict"`. In concat mode, all features get concatenated together into a single vector. In dict mode, the FeatureSpace returns a dict of individually encoded features (with the same keys as the input dict keys). |
| `crosses` | List of features to be crossed together, e.g. `crosses=[("feature_1", "feature_2")]`. The features will be "crossed" by hashing their combined value into a fixed-length vector. |
| `crossing_dim` | Default vector size for hashing crossed features. Defaults to `32`. |
| `hashing_dim` | Default vector size for hashing features of type `"integer_hashed"` and `"string_hashed"`. Defaults to `32`. |
| `num_discretization_bins` | Default number of bins to be used for discretizing features of type `"float_discretized"`. Defaults to `32`. |

**Available feature types:**

Note that all features can be referred to by their string name, e.g. `"integer_categorical"`. When using the string name, the default argument values are used.

# Plain float values.
    FeatureSpace.float(name=None)
    
    # Float values to be preprocessed via featurewise standardization
    # (i.e. via a `keras.layers.Normalization` layer).
    FeatureSpace.float_normalized(name=None)
    
    # Float values to be preprocessed via linear rescaling
    # (i.e. via a `keras.layers.Rescaling` layer).
    FeatureSpace.float_rescaled(scale=1., offset=0., name=None)
    
    # Float values to be discretized. By default, the discrete
    # representation will then be one-hot encoded.
    FeatureSpace.float_discretized(
        num_bins, bin_boundaries=None, output_mode="one_hot", name=None)
    
    # Integer values to be indexed. By default, the discrete
    # representation will then be one-hot encoded.
    FeatureSpace.integer_categorical(
        max_tokens=None, num_oov_indices=1, output_mode="one_hot", name=None)
    
    # String values to be indexed. By default, the discrete
    # representation will then be one-hot encoded.
    FeatureSpace.string_categorical(
        max_tokens=None, num_oov_indices=1, output_mode="one_hot", name=None)
    
    # Integer values to be hashed into a fixed number of bins.
    # By default, the discrete representation will then be one-hot encoded.
    FeatureSpace.integer_hashed(num_bins, output_mode="one_hot", name=None)
    
    # String values to be hashed into a fixed number of bins.
    # By default, the discrete representation will then be one-hot encoded.
    FeatureSpace.string_hashed(num_bins, output_mode="one_hot", name=None)

#### Examples:

**Basic usage with a dict of input data:**

raw_data = {
        "float_values": [0.0, 0.1, 0.2, 0.3],
        "string_values": ["zero", "one", "two", "three"],
        "int_values": [0, 1, 2, 3],
    }
    dataset = tf.data.Dataset.from_tensor_slices(raw_data)
    
    feature_space = FeatureSpace(
        features={
            "float_values": "float_normalized",
            "string_values": "string_categorical",
            "int_values": "integer_categorical",
        },
        crosses=[("string_values", "int_values")],
        output_mode="concat",
    )
    # Before you start using the FeatureSpace,
    # you must `adapt()` it on some data.
    feature_space.adapt(dataset)
    
    # You can call the FeatureSpace on a dict of data (batched or unbatched).
    output_vector = feature_space(raw_data)

**Basic usage with [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
:**

# Unlabeled data
    preprocessed_ds = unlabeled_dataset.map(feature_space)
    
    # Labeled data
    preprocessed_ds = labeled_dataset.map(lambda x, y: (feature_space(x), y))

**Basic usage with the Keras Functional API:**

# Retrieve a dict Keras Input objects
    inputs = feature_space.get_inputs()
    # Retrieve the corresponding encoded Keras tensors
    encoded_features = feature_space.get_encoded_features()
    # Build a Functional model
    outputs = keras.layers.Dense(1, activation="sigmoid")(encoded_features)
    model = keras.Model(inputs, outputs)

**Customizing each feature or feature cross:**

feature_space = FeatureSpace(
        features={
            "float_values": FeatureSpace.float_normalized(),
            "string_values": FeatureSpace.string_categorical(max_tokens=10),
            "int_values": FeatureSpace.integer_categorical(max_tokens=10),
        },
        crosses=[\
            FeatureSpace.cross(("string_values", "int_values"), crossing_dim=32)\
        ],
        output_mode="concat",
    )

**Returning a dict of integer-encoded features:**

feature_space = FeatureSpace(
        features={
            "string_values": FeatureSpace.string_categorical(output_mode="int"),
            "int_values": FeatureSpace.integer_categorical(output_mode="int"),
        },
        crosses=[\
            FeatureSpace.cross(\
                feature_names=("string_values", "int_values"),\
                crossing_dim=32,\
                output_mode="int",\
            )\
        ],
        output_mode="dict",
    )

**Specifying your own Keras preprocessing layer:**

# Let's say that one of the features is a short text paragraph that
    # we want to encode as a vector (one vector per paragraph) via TF-IDF.
    data = {
        "text": ["1st string", "2nd string", "3rd string"],
    }
    
    # There's a Keras layer for this: TextVectorization.
    custom_layer = layers.TextVectorization(output_mode="tf_idf")
    
    # We can use FeatureSpace.feature to create a custom feature
    # that will use our preprocessing layer.
    feature_space = FeatureSpace(
        features={
            "text": FeatureSpace.feature(
                preprocessor=custom_layer, dtype="string", output_mode="float"
            ),
        },
        output_mode="concat",
    )
    feature_space.adapt(tf.data.Dataset.from_tensor_slices(data))
    output_vector = feature_space(data)

**Retrieving the underlying Keras preprocessing layers:**

# The preprocessing layer of each feature is available in `.preprocessors`.
    preprocessing_layer = feature_space.preprocessors["feature1"]
    
    # The crossing layer of each feature cross is available in `.crossers`.
    # It's an instance of keras.layers.HashedCrossing.
    crossing_layer = feature_space.crossers["feature1_X_feature2"]

**Saving and reloading a FeatureSpace:**

feature_space.save("featurespace.keras")
    reloaded_feature_space = keras.models.load_model("featurespace.keras")

|     |     |
| --- | --- |
| Attributes<br>---------- |     |
| `input` | Retrieves the input tensor(s) of a symbolic operation.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |
| `output` | Retrieves the output tensor(s) of a layer.<br><br>Only returns the tensor(s) corresponding to the _first time_ the operation was called. |

Methods
-------

### `adapt`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L510-L548)

adapt(
        dataset
    )

### `cross`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L280-L282)

@classmethod

### `feature`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L284-L286)

@classmethod

### `float`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L288-L294)

@classmethod

### `float_discretized`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L316-L328)

@classmethod

### `float_normalized`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L306-L314)

@classmethod

### `float_rescaled`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L296-L304)

@classmethod

### `from_config`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L785-L787)

@classmethod

Creates an operation from its config.

This method is the reverse of `get_config`, capable of instantiating the same operation from the config dictionary.

if "dtype" in config and isinstance(config["dtype"], dict):
        policy = dtype_policies.deserialize(config["dtype"])

|     |     |
| --- | --- |
| Args |     |
| `config` | A Python dictionary, typically the output of `get_config`. |

|     |
| --- |
| Returns |     |
| An operation instance. |     |

### `get_encoded_features`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L554-L564)

get_encoded_features()

### `get_inputs`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L550-L552)

get_inputs()

### `integer_categorical`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L330-L346)

@classmethod

### `integer_hashed`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L376-L384)

@classmethod

### `save`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L802-L812)

save(
        filepath
    )

Save the `FeatureSpace` instance to a `.keras` file.

You can reload it via [`keras.models.load_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/load_model)
:

feature_space.save("featurespace.keras")
    reloaded_fs = keras.models.load_model("featurespace.keras")

### `string_categorical`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L348-L364)

@classmethod

### `string_hashed`

[View source](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/layers/preprocessing/feature_space.py#L366-L374)

@classmethod

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.