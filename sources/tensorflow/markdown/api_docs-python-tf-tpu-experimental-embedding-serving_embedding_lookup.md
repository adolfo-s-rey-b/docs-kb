[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Ftpu%2Fexperimental%2Fembedding%2Fserving_embedding_lookup&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.tpu.experimental.embedding.serving\_embedding\_lookup Stay organized with collections Save and categorize content based on your preferences.
===============================================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup#args)
    
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/tpu/tpu_embedding_for_serving.py#L353-L483)

Apply standard lookup ops with [`tf.tpu.experimental.embedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding)
 configs.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.tpu.experimental.embedding.serving_embedding_lookup`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/serving_embedding_lookup)

tf.tpu.experimental.embedding.serving_embedding_lookup(
        inputs: Any,
        weights: Optional[Any],
        tables: Dict[tf.tpu.experimental.embedding.TableConfig, tf.Variable],
        feature_config: Union[tf.tpu.experimental.embedding.FeatureConfig, Iterable]
    ) -> Any

This function is a utility which allows using the [`tf.tpu.experimental.embedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding)
 config objects with standard lookup functions. This can be used when exporting a model which uses [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 for serving on CPU. In particular [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 only supports lookups on TPUs and should not be part of your serving graph.

Note that TPU specific options (such as `max_sequence_length`) in the configuration objects will be ignored.

In the following example we take a trained model (see the documentation for [`tf.tpu.experimental.embedding.TPUEmbedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding/TPUEmbedding)
 for the context) and create a saved model with a serving function that will perform the embedding lookup and pass the results to your model:

model = model_fn(...)
    embedding = tf.tpu.experimental.embedding.TPUEmbedding(
        feature_config=feature_config,
        batch_size=1024,
        optimizer=tf.tpu.experimental.embedding.SGD(0.1))
    checkpoint = tf.train.Checkpoint(model=model, embedding=embedding)
    checkpoint.restore(...)
    
    @tf.function(input_signature=[{'feature_one': tf.TensorSpec(...),\
                                   'feature_two': tf.TensorSpec(...),\
                                   'feature_three': tf.TensorSpec(...)}])
    def serve_tensors(embedding_features):
      embedded_features = tf.tpu.experimental.embedding.serving_embedding_lookup(
          embedding_features, None, embedding.embedding_tables,
          feature_config)
      return model(embedded_features)
    
    model.embedding_api = embedding
    tf.saved_model.save(model,
                        export_dir=...,
                        signatures={'serving_default': serve_tensors})

|     |     |
| --- | --- |
| Args<br>---- |     |
| `inputs` | a nested structure of Tensors, SparseTensors or RaggedTensors. |
| `weights` | a nested structure of Tensors, SparseTensors or RaggedTensors or None for no weights. If not None, structure must match that of inputs, but entries are allowed to be None. |
| `tables` | a dict of mapping TableConfig objects to Variables. |
| `feature_config` | a nested structure of FeatureConfig objects. The keys of feature\_config is a superset of inputs. |

|     |
| --- |
| Returns<br>------- |     |
| A nested structure of Tensors with the same structure as inputs. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.