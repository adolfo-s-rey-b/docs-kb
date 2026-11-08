[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#used-in-the-notebooks)
        
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#returns)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.global\_variables\_initializer Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#used-in-the-notebooks)
        
*   [Returns](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer#returns)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/ops/variables.py#L1968-L1984)

Returns an Op that initializes global variables.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.initializers.global_variables`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/global_variables_initializer)

tf.compat.v1.global_variables_initializer()

Migrate to TF2
--------------

In TF2, variables are initialized immediately when they are created. There is no longer a need to run variable initializers before using them.

Description
-----------

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Migrating model checkpoints](https://www.tensorflow.org/guide/migrate/migrating_checkpoints)<br>    <br>*   [Validating correctness & numerical equivalence](https://www.tensorflow.org/guide/migrate/validate_correctness)<br>    <br>*   [Debug a TensorFlow 2 migrated training pipeline](https://www.tensorflow.org/guide/migrate/migration_debugging) | *   [Universal Sentence Encoder-Lite demo](https://www.tensorflow.org/hub/tutorials/semantic_similarity_with_tf_hub_universal_encoder_lite)<br>    <br>*   [Generating Images with Little Data Using S3GAN](https://www.tensorflow.org/hub/tutorials/s3gan_generation_with_tf_hub)<br>    <br>*   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD)<br>    <br>*   [Generating Images with BigBiGAN](https://www.tensorflow.org/hub/tutorials/bigbigan_with_tf_hub)<br>    <br>*   [Generating Images with BigGAN](https://www.tensorflow.org/hub/tutorials/biggan_generation_with_tf_hub) |

This is just a shortcut for `variables_initializer(global_variables())`

|     |
| --- |
| Returns<br>------- |     |
| An Op that initializes global variables in the graph. |     |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.