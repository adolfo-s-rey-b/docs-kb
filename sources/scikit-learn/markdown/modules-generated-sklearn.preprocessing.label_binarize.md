[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.preprocessing.label_binarize.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.preprocessing.label_binarize.html)

Collapse Sidebar Expand Sidebar

label\_binarize[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#label-binarize "Link to this heading")

======================================================================================================================================================

sklearn.preprocessing.label\_binarize(_y_, _\*_, _classes_, _neg\_label\=0_, _pos\_label\=1_, _sparse\_output\=False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/preprocessing/_label.py#L465)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#sklearn.preprocessing.label_binarize "Link to this definition")

Binarize labels in a one-vs-all fashion.

Several regression and binary classification algorithms are available in scikit-learn. A simple way to extend these algorithms to the multi-class classification case is to use the so-called one-vs-all scheme.

This function makes it possible to compute this transformation for a fixed set of class labels known ahead of time.

Parameters:

**y**array-like or sparse matrix

Sequence of integer labels or multilabel data to encode.

**classes**array-like of shape (n\_classes,)

Uniquely holds the label for each class.

**neg\_label**int, default=0

Value with which negative labels must be encoded.

**pos\_label**int, default=1

Value with which positive labels must be encoded.

**sparse\_output**bool, default=False,

Set to true if output binary array is desired in CSR sparse format.

Returns:

**Y**{ndarray, sparse matrix} of shape (n\_samples, n\_classes)

Shape will be (n\_samples, 1) for binary problems. Sparse matrix will be of CSR format.

See also

[`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")

Class used to wrap the functionality of label\_binarize and allow for fitting to classes independently of the transform operation.

Examples

\>>> from sklearn.preprocessing import label\_binarize
\>>> label\_binarize(\[1, 6\], classes\=\[1, 2, 4, 6\])
array(\[\[1, 0, 0, 0\],\
       \[0, 0, 0, 1\]\])

Copy to clipboard

The class ordering is preserved:

\>>> label\_binarize(\[1, 6\], classes\=\[1, 6, 4, 2\])
array(\[\[1, 0, 0, 0\],\
       \[0, 1, 0, 0\]\])

Copy to clipboard

Binary targets transform to a column vector

\>>> label\_binarize(\['yes', 'no', 'no', 'yes'\], classes\=\['no', 'yes'\])
array(\[\[1\],\
       \[0\],\
       \[0\],\
       \[1\]\])

Copy to clipboard

Gallery examples[#](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.label_binarize.html#gallery-examples "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_face_recognition_thumb.png)

[Faces recognition example using eigenfaces and kernel approximation](https://scikit-learn.org/stable/auto_examples/applications/plot_face_recognition.html)

Faces recognition example using eigenfaces and kernel approximation

![](https://scikit-learn.org/stable/_images/sphx_glr_plot_precision_recall_thumb.png)

[Precision-Recall](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)

Precision-Recall

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)