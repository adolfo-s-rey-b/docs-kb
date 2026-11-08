[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fdata%2Fexperimental%2Fget_single_element&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#raises)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.data.experimental.get\_single\_element Stay organized with collections Save and categorize content based on your preferences.
================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#returns)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element#raises)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/data/experimental/ops/get_single_element.py#L21-L109)

Returns the single element of the `dataset` as a nested structure of tensors. (deprecated)

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.data.experimental.get_single_element`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element)

tf.data.experimental.get_single_element(
        dataset
    )

The function enables you to use a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 in a stateless "tensor-in tensor-out" expression, without creating an iterator. This facilitates the ease of data transformation on tensors using the optimized [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 abstraction on top of them.

For example, lets consider a `preprocessing_fn` which would take as an input the raw features and returns the processed feature along with it's label.

def preprocessing_fn(raw_feature):
      # ... the raw_feature is preprocessed as per the use-case
      return feature
    
    raw_features = ...  # input batch of BATCH_SIZE elements.
    dataset = (tf.data.Dataset.from_tensor_slices(raw_features)
               .map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)
               .batch(BATCH_SIZE))
    
    processed_features = tf.data.experimental.get_single_element(dataset)

In the above example, the `raw_features` tensor of length=BATCH\_SIZE was converted to a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
. Next, each of the `raw_feature` was mapped using the `preprocessing_fn` and the processed features were grouped into a single batch. The final `dataset` contains only one element which is a batch of all the processed features.

Now, instead of creating an iterator for the `dataset` and retrieving the batch of features, the [`tf.data.experimental.get_single_element()`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/get_single_element)
 function is used to skip the iterator creation process and directly output the batch of features.

This can be particularly useful when your tensor transformations are expressed as [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)
 operations, and you want to use those transformations while serving your model.

Keras
=====

model = ... # A pre-built or custom model
    
    class PreprocessingModel(tf.keras.Model):
      def __init__(self, model):
        super().__init__(self)
        self.model = model
    
      @tf.function(input_signature=[...])
      def serving_fn(self, data):
        ds = tf.data.Dataset.from_tensor_slices(data)
        ds = ds.map(preprocessing_fn, num_parallel_calls=BATCH_SIZE)
        ds = ds.batch(batch_size=BATCH_SIZE)
        return tf.argmax(
          self.model(tf.data.experimental.get_single_element(ds)),
          axis=-1
        )
    
    preprocessing_model = PreprocessingModel(model)
    your_exported_model_dir = ... # save the model to this path.
    tf.saved_model.save(preprocessing_model, your_exported_model_dir,
                  signatures={'serving_default': preprocessing_model.serving_fn})

|     |     |
| --- | --- |
| Args<br>---- |     |
| `dataset` | A [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object containing a single element. |

|     |
| --- |
| Returns<br>------- |     |
| A nested structure of [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)<br> objects, corresponding to the single element of `dataset`. |     |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `TypeError` | if `dataset` is not a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)<br> object. |
| `InvalidArgumentError` | (at runtime) if `dataset` does not contain exactly one element. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.