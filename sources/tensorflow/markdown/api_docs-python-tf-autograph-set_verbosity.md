[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/autograph/set_verbosity#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   English
*   中文 – 简体

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.autograph.set\_verbosity Stay organized with collections Save and categorize content based on your preferences.
==================================================================================================================

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/autograph/utils/ag_logging.py#L36-L84)

Sets the AutoGraph verbosity level.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.autograph.set_verbosity`](https://www.tensorflow.org/api_docs/python/tf/autograph/set_verbosity)

tf.autograph.set_verbosity(
        level, alsologtostdout=False
    )

_Debug logging in AutoGraph_

More verbose logging is useful to enable when filing bug reports or doing more in-depth debugging.

There are two means to control the logging verbosity:

*   The `set_verbosity` function
    
*   The `AUTOGRAPH_VERBOSITY` environment variable
    

`set_verbosity` takes precedence over the environment variable.

#### For example:

import os
    import tensorflow as tf
    
    os.environ['AUTOGRAPH_VERBOSITY'] = '5'
    # Verbosity is now 5
    
    tf.autograph.set_verbosity(0)
    # Verbosity is now 0
    
    os.environ['AUTOGRAPH_VERBOSITY'] = '1'
    # No effect, because set_verbosity was already called.

Logs entries are output to [absl](https://abseil.io/)
's [default output](https://abseil.io/docs/python/guides/logging)
, with `INFO` level. Logs can be mirrored to stdout by using the `alsologtostdout` argument. Mirroring is enabled by default when Python runs in interactive mode.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `level` | int, the verbosity level; larger values specify increased verbosity; 0 means no logging. When reporting bugs, it is recommended to set this value to a larger number, like 10. |
| `alsologtostdout` | bool, whether to also output log messages to `sys.stdout`. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.