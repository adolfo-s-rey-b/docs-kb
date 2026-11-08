[Skip to main content](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver#classes)
    

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [Python](https://www.tensorflow.org/api_docs/python/tf)
    

Module: tf.distribute.cluster\_resolver Stay organized with collections Save and categorize content based on your preferences.
==============================================================================================================================

*   On this page
*   [Classes](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver#classes)
    

Public API for tf.\_api.v2.distribute.cluster\_resolver namespace

Classes
-------

[`class ClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/ClusterResolver)
: Abstract class for all implementations of ClusterResolvers.

[`class GCEClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/GCEClusterResolver)
: ClusterResolver for Google Compute Engine.

[`class KubernetesClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesClusterResolver)
: ClusterResolver for Kubernetes.

[`class KubernetesExecutableLocation`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/KubernetesExecutableLocation)
: Defines where the executable runs on.

[`class SimpleClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SimpleClusterResolver)
: Simple implementation of ClusterResolver that accepts all attributes.

[`class SlurmClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/SlurmClusterResolver)
: ClusterResolver for system with Slurm workload manager.

[`class TFConfigClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TFConfigClusterResolver)
: Implementation of a ClusterResolver which reads the TF\_CONFIG EnvVar.

[`class TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver)
: Cluster Resolver for Google Cloud TPUs.

[`class UnionResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/UnionResolver)
: Performs a union on underlying ClusterResolvers.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-10-31 UTC.