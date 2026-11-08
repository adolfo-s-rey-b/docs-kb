[Skip to main content](https://scikit-learn.org/stable/modules/preprocessing_targets.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/preprocessing_targets.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/preprocessing_targets.html)
[1.8.0](https://scikit-learn.org/1.8/modules/preprocessing_targets.html)
[1.7.2](https://scikit-learn.org/1.7/modules/preprocessing_targets.html)
[1.6.1](https://scikit-learn.org/1.6/modules/preprocessing_targets.html)
[1.5.2](https://scikit-learn.org/1.5/modules/preprocessing_targets.html)
[1.4.2](https://scikit-learn.org/1.4/modules/preprocessing_targets.html)

Collapse Sidebar Expand Sidebar

8.9. Transforming the prediction target (`y`)[#](https://scikit-learn.org/stable/modules/preprocessing_targets.html#transforming-the-prediction-target-y "Link to this heading")

=================================================================================================================================================================================

These are transformers that are not intended to be used on features, only on supervised learning targets. See also [Transforming target in regression](https://scikit-learn.org/stable/modules/compose.html#transformed-target-regressor)
 if you want to transform the prediction target for learning, but evaluate the model in the original (untransformed) space.

8.9.1. Label binarization[#](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-binarization "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

### 8.9.1.1. LabelBinarizer[#](https://scikit-learn.org/stable/modules/preprocessing_targets.html#labelbinarizer "Link to this heading")

[`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
 is a utility class to help create a [label indicator matrix](https://scikit-learn.org/stable/glossary.html#term-label-indicator-matrix)
 from a list of [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 labels:

\>>> from sklearn import preprocessing
\>>> lb \= preprocessing.LabelBinarizer()
\>>> lb.fit(\[1, 2, 6, 4, 2\])
LabelBinarizer()
\>>> lb.classes\_
array(\[1, 2, 4, 6\])
\>>> lb.transform(\[1, 6\])
array(\[\[1, 0, 0, 0\],\
       \[0, 0, 0, 1\]\])

Copy to clipboard

Using this format can enable multiclass classification in estimators that support the label indicator matrix format.

Warning

LabelBinarizer is not needed if you are using an estimator that already supports [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 data.

For more information about multiclass classification, refer to [Multiclass classification](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification)
.

### 8.9.1.2. MultiLabelBinarizer[#](https://scikit-learn.org/stable/modules/preprocessing_targets.html#multilabelbinarizer "Link to this heading")

In [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 learning, the joint set of binary classification tasks is expressed with a label binary indicator array: each sample is one row of a 2d array of shape (n\_samples, n\_classes) with binary values where the one, i.e. the non zero elements, corresponds to the subset of labels for that sample. An array such as `np.array([[1, 0, 0], [0, 1, 1], [0, 0, 0]])` represents label 0 in the first sample, labels 1 and 2 in the second sample, and no labels in the third sample.

Producing multilabel data as a list of sets of labels may be more intuitive. The [`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
 transformer can be used to convert between a collection of collections of labels and the indicator format:

\>>> from sklearn.preprocessing import MultiLabelBinarizer
\>>> y \= \[\[2, 3, 4\], \[2\], \[0, 1, 3\], \[0, 1, 2, 3, 4\], \[0, 1, 2\]\]
\>>> MultiLabelBinarizer().fit\_transform(y)
array(\[\[0, 0, 1, 1, 1\],\
       \[0, 0, 1, 0, 0\],\
       \[1, 1, 0, 1, 0\],\
       \[1, 1, 1, 1, 1\],\
       \[1, 1, 1, 0, 0\]\])

Copy to clipboard

For more information about multilabel classification, refer to [Multilabel classification](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification)
.

8.9.2. Label encoding[#](https://scikit-learn.org/stable/modules/preprocessing_targets.html#label-encoding "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

[`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
 is a utility class to help normalize labels such that they contain only values between 0 and n\_classes-1. This is sometimes useful for writing efficient Cython routines. [`LabelEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder "sklearn.preprocessing.LabelEncoder")
 can be used as follows:

\>>> from sklearn import preprocessing
\>>> le \= preprocessing.LabelEncoder()
\>>> le.fit(\[1, 2, 2, 6\])
LabelEncoder()
\>>> le.classes\_
array(\[1, 2, 6\])
\>>> le.transform(\[1, 1, 2, 6\])
array(\[0, 0, 1, 2\])
\>>> le.inverse\_transform(\[0, 0, 1, 2\])
array(\[1, 1, 2, 6\])

Copy to clipboard

It can also be used to transform non-numerical labels (as long as they are hashable and comparable) to numerical labels:

\>>> le \= preprocessing.LabelEncoder()
\>>> le.fit(\["paris", "paris", "tokyo", "amsterdam"\])
LabelEncoder()
\>>> list(le.classes\_)
\[np.str\_('amsterdam'), np.str\_('paris'), np.str\_('tokyo')\]
\>>> le.transform(\["tokyo", "tokyo", "paris"\])
array(\[2, 2, 1\])
\>>> list(le.inverse\_transform(\[2, 2, 1\]))
\[np.str\_('tokyo'), np.str\_('tokyo'), np.str\_('paris')\]

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)