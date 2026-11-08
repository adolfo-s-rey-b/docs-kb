[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)

[Sign in](https://www.tensorflow.org/_d/signin?continue=https%3A%2F%2Fwww.tensorflow.org%2Fapi_docs%2Fpython%2Ftf%2Fcompat%2Fv1%2Fset_random_seed&prompt=select_account)

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#args)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

tf.compat.v1.set\_random\_seed Stay organized with collections Save and categorize content based on your preferences.
=====================================================================================================================

*   On this page
*   [Migrate to TF2](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#migrate-to-tf2)
    
*   [Description](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#description)
    *   [Used in the notebooks](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#used-in-the-notebooks)
        
*   [Args](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed#args)
    

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/tensorflow/blob/v2.21.0/tensorflow/python/framework/random_seed.py#L96-L207)

Sets the graph-level random seed for the default graph.

#### View aliases

**Compat aliases for migration**

See [Migration guide](https://www.tensorflow.org/guide/migrate)
 for more details.

[`tf.compat.v1.random.set_random_seed`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/set_random_seed)

tf.compat.v1.set_random_seed(
        seed
    )

Migrate to TF2
--------------

'tf.compat.v1.set\_random\_seed' is compatible with eager mode. However, in eager mode this API will set the global seed instead of the graph-level seed of the default graph. In TF2 this API is changed to [tf.random.set\_seed](https://www.tensorflow.org/api_docs/python/tf/random/set_seed)
.

Description
-----------

### Used in the notebooks

| Used in the tutorials |
| --- |
| *   [TensorFlow Constrained Optimization Example Using CelebA Dataset](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_CelebA_Case_Study)<br>    <br>*   [Wiki Talk Comments Toxicity Prediction](https://www.tensorflow.org/responsible_ai/fairness_indicators/tutorials/Fairness_Indicators_TFCO_Wiki_Case_Study)<br>    <br>*   [Fitting Dirichlet Process Mixture Model Using Preconditioned Stochastic Gradient Langevin Dynamics](https://www.tensorflow.org/probability/examples/Fitting_DPMM_Using_pSGLD) |

Operations that rely on a random seed actually derive it from two seeds: the graph-level and operation-level seeds. This sets the graph-level seed.

Its interactions with operation-level seeds is as follows:

1.  If neither the graph-level nor the operation seed is set: A random seed is used for this op.
2.  If the graph-level seed is set, but the operation seed is not: The system deterministically picks an operation seed in conjunction with the graph-level seed so that it gets a unique random sequence. Within the same version of tensorflow and user code, this sequence is deterministic. However across different versions, this sequence might change. If the code depends on particular seeds to work, specify both graph-level and operation-level seeds explicitly.
3.  If the graph-level seed is not set, but the operation seed is set: A default graph-level seed and the specified operation seed are used to determine the random sequence.
4.  If both the graph-level and the operation seed are set: Both seeds are used in conjunction to determine the random sequence.

To illustrate the user-visible effects, consider these examples:

To generate different sequences across sessions, set neither graph-level nor op-level seeds:

a = tf.random.uniform([1])
    b = tf.random.normal([1])
    
    print("Session 1")
    with tf.compat.v1.Session() as sess1:
      print(sess1.run(a))  # generates 'A1'
      print(sess1.run(a))  # generates 'A2'
      print(sess1.run(b))  # generates 'B1'
      print(sess1.run(b))  # generates 'B2'
    
    print("Session 2")
    with tf.compat.v1.Session() as sess2:
      print(sess2.run(a))  # generates 'A3'
      print(sess2.run(a))  # generates 'A4'
      print(sess2.run(b))  # generates 'B3'
      print(sess2.run(b))  # generates 'B4'

To generate the same repeatable sequence for an op across sessions, set the seed for the op:

a = tf.random.uniform([1], seed=1)
    b = tf.random.normal([1])
    
    # Repeatedly running this block with the same graph will generate the same
    # sequence of values for 'a', but different sequences of values for 'b'.
    print("Session 1")
    with tf.compat.v1.Session() as sess1:
      print(sess1.run(a))  # generates 'A1'
      print(sess1.run(a))  # generates 'A2'
      print(sess1.run(b))  # generates 'B1'
      print(sess1.run(b))  # generates 'B2'
    
    print("Session 2")
    with tf.compat.v1.Session() as sess2:
      print(sess2.run(a))  # generates 'A1'
      print(sess2.run(a))  # generates 'A2'
      print(sess2.run(b))  # generates 'B3'
      print(sess2.run(b))  # generates 'B4'

To make the random sequences generated by all ops be repeatable across sessions, set a graph-level seed:

tf.compat.v1.random.set_random_seed(1234)
    a = tf.random.uniform([1])
    b = tf.random.normal([1])
    
    # Repeatedly running this block with the same graph will generate the same
    # sequences of 'a' and 'b'.
    print("Session 1")
    with tf.compat.v1.Session() as sess1:
      print(sess1.run(a))  # generates 'A1'
      print(sess1.run(a))  # generates 'A2'
      print(sess1.run(b))  # generates 'B1'
      print(sess1.run(b))  # generates 'B2'
    
    print("Session 2")
    with tf.compat.v1.Session() as sess2:
      print(sess2.run(a))  # generates 'A1'
      print(sess2.run(a))  # generates 'A2'
      print(sess2.run(b))  # generates 'B1'
      print(sess2.run(b))  # generates 'B2'

|     |     |
| --- | --- |
| Args<br>---- |     |
| `seed` | integer. |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.