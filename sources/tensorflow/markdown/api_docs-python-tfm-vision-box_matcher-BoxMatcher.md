[Skip to main content](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#main-content)

[![TensorFlow](https://www.gstatic.com/devrel-devsite/prod/v0bdbebc1f01a38de21004f32be4e375582bd633675ce8e19f11ee677174d47b4/tensorflow/images/lockup.svg)](https://www.tensorflow.org/)

/

*   [English](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher)
    
*   [中文 – 简体](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher?hl=zh-cn)
    

[GitHub](https://github.com/tensorflow)
 Sign in

*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#__call__)
        

*   [TensorFlow](https://www.tensorflow.org/)
    
*   [API](https://www.tensorflow.org/api)
    
*   [TensorFlow v2.21.0](https://www.tensorflow.org/api_docs)
    
*   [More](https://www.tensorflow.org/api_docs/more)
    

tfm.vision.box\_matcher.BoxMatcher Stay organized with collections Save and categorize content based on your preferences.
=========================================================================================================================

*   On this page
*   [Args](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#args)
    
*   [Raises](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#raises)
    
*   [Methods](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#methods)
    *   [\_\_call\_\_](https://www.tensorflow.org/api_docs/python/tfm/vision/box_matcher/BoxMatcher#__call__)
        

 [![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_matcher.py#L22-L202)

Matcher based on highest value.

tfm.vision.box_matcher.BoxMatcher(
        thresholds: List[float],
        indicators: List[int],
        force_match_for_each_col: bool = False
    )

This class computes matches from a similarity matrix. Each column is matched to a single row.

To support object detection target assignment this class enables setting both positive\_threshold (upper threshold) and negative\_threshold (lower thresholds) defining three categories of similarity which define whether examples are positive, negative, or ignored, for example: (1) thresholds=\[negative\_threshold, positive\_threshold\], and indicators=\[negative\_value, ignore\_value, positive\_value\]: The similarity metrics below negative\_threshold will be assigned with negative\_value, the metrics between negative\_threshold and positive\_threshold will be assigned ignore\_value, and the metrics above positive\_threshold will be assigned positive\_value. (2) thresholds=\[negative\_threshold, positive\_threshold\], and indicators=\[ignore\_value, negative\_value, positive\_value\]: The similarity metric below negative\_threshold will be assigned with ignore\_value, the metrics between negative\_threshold and positive\_threshold will be assigned negative\_value, and the metrics above positive\_threshold will be assigned positive\_value.

|     |     |
| --- | --- |
| Args<br>---- |     |
| `thresholds` | A list of thresholds to classify the matches into different types (e.g. positive or negative or ignored match). The list needs to be sorted, and will be prepended with -Inf and appended with +Inf. |
| `indicators` | A list of values representing match types (e.g. positive or negative or ignored match). len(`indicators`) must equal to len(`thresholds`) + 1. |
| `force_match_for_each_col` | If True, ensures that each column is matched to at least one row (which is not guaranteed otherwise if the positive\_threshold is high). Defaults to False. If True, all force matched row will be assigned to `indicators[-1]`. |

|     |     |
| --- | --- |
| Raises<br>------ |     |
| `ValueError` | If `threshold` not sorted, or len(indicators) != len(threshold) + 1 |

Methods
-------

### `__call__`

[View source](https://github.com/tensorflow/models/blob/v2.20.0/official/vision/ops/box_matcher.py#L81-L188)

__call__(
        similarity_matrix: tf.Tensor
    ) -> Tuple[tf.Tensor, tf.Tensor]

Tries to match each column of the similarity matrix to a row.

|     |     |
| --- | --- |
| Args |     |
| `similarity_matrix` | A float tensor of shape \[num\_rows, num\_cols\] or \[batch\_size, num\_rows, num\_cols\] representing any similarity metric. |

|     |     |
| --- | --- |
| Returns |     |
| `matched_columns` | An integer tensor of shape \[num\_rows\] or \[batch\_size, num\_rows\] storing the index of the matched column for each row. |
| `match_indicators` | An integer tensor of shape \[num\_rows\] or \[batch\_size, num\_rows\] storing the match type indicator (e.g. positive or negative or ignored match). |

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
, and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
. For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies)
. Java is a registered trademark of Oracle and/or its affiliates. Some content is licensed under the [numpy license](https://numpy.org/doc/stable/license.html)
.

Last updated 2026-11-06 UTC.