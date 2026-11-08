[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed#arguments)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.keras.utils.set\_random\_seed Stay organized with collections Save and categorize content based on your preferences.
=======================================================================================================================

*   On this page
*   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed#used-in-the-notebooks)
    
*   [Arguments](https://www.tensorflow.org/api_docs/python/tf/keras/utils/set_random_seed#arguments)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/keras-team/keras/tree/v3.15.1/keras/src/utils/rng_utils.py#L14-L70)

Sets all random seeds (Python, NumPy, and backend framework, e.g. TF).

tf.keras.utils.set_random_seed(
        seed
    )

### Used in the notebooks

| Used in the guide | Used in the tutorials |
| --- | --- |
| *   [Use TF1.x models in TF2 workflows](https://www.tensorflow.org/guide/migrate/model_mapping) | *   [Using DTensors with Keras](https://www.tensorflow.org/tutorials/distribute/dtensor_keras_tutorial) |

You can use this utility to make almost any Keras program fully deterministic. Some limitations apply in cases where network communications are involved (e.g. parameter server distribution), which creates additional sources of randomness, or when certain non-deterministic cuDNN ops are involved.

Calling this utility does the following:

import random
    random.seed(seed)
    
    import numpy as np
    np.random.seed(seed)
    
    import tensorflow as tf  # Only if TF is installed
    tf.random.set_seed(seed)
    
    import torch  # Only if the backend is 'torch'
    torch.manual_seed(seed)

Additionally, it resets the global Keras `SeedGenerator`, which is used by [`keras.random`](https://www.tensorflow.org/api_docs/python/tf/keras/random)
 functions when the `seed` is not provided.

Note that the TensorFlow seed is set even if you're not using TensorFlow as your backend framework, since many workflows leverage [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
 pipelines (which feature random shuffling). Likewise many workflows might leverage NumPy APIs.

|     |     |
| --- | --- |
| Arguments<br>--------- |     |
| `seed` | Integer, the random seed to use. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.