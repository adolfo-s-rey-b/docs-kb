[Skip to main content](https://scikit-learn.org/stable/modules/multiclass.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/multiclass.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/multiclass.html)
[1.8.0](https://scikit-learn.org/1.8/modules/multiclass.html)
[1.7.2](https://scikit-learn.org/1.7/modules/multiclass.html)
[1.6.1](https://scikit-learn.org/1.6/modules/multiclass.html)
[1.5.2](https://scikit-learn.org/1.5/modules/multiclass.html)
[1.4.2](https://scikit-learn.org/1.4/modules/multiclass.html)

Collapse Sidebar Expand Sidebar

1.12. Multiclass and multioutput algorithms[#](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-and-multioutput-algorithms "Link to this heading")

=====================================================================================================================================================================

This section of the user guide covers functionality related to multi-learning problems, including [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
, [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
, and [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
 classification and regression.

The modules in this section implement [meta-estimators](https://scikit-learn.org/stable/glossary.html#term-meta-estimators)
, which require a base estimator to be provided in their constructor. Meta-estimators extend the functionality of the base estimator to support multi-learning problems, which is accomplished by transforming the multi-learning problem into a set of simpler problems, then fitting one estimator per problem.

This section covers two modules: [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
 and [`sklearn.multioutput`](https://scikit-learn.org/stable/api/sklearn.multioutput.html#module-sklearn.multioutput "sklearn.multioutput")
. The chart below demonstrates the problem types that each module is responsible for, and the corresponding meta-estimators that each module provides.

![../_images/multi_org_chart.png](https://scikit-learn.org/stable/_images/multi_org_chart.png)

The table below provides a quick reference on the differences between problem types. More detailed explanations can be found in subsequent sections of this guide.

|     | Number of targets | Target cardinality | Valid [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target") |
| --- | --- | --- | --- |
| Multiclass classification | 1   | \>2 | ‘multiclass’ |
| Multilabel classification | \>1 | 2 (0 or 1) | ‘multilabel-indicator’ |
| Multiclass-multioutput classification | \>1 | \>2 | ‘multiclass-multioutput’ |
| Multioutput regression | \>1 | Continuous | ‘continuous-multioutput’ |

Below is a summary of scikit-learn estimators that have multi-learning support built-in, grouped by strategy. You don’t need the meta-estimators provided by this section if you’re using one of these estimators. However, meta-estimators can provide additional strategies beyond what is built-in:

*   **Inherently multiclass:**
    
    *   [`naive_bayes.BernoulliNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB "sklearn.naive_bayes.BernoulliNB")
        
    *   [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
        
    *   [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
        
    *   [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
        
    *   [`naive_bayes.GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB "sklearn.naive_bayes.GaussianNB")
        
    *   [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
        
    *   [`semi_supervised.LabelPropagation`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html#sklearn.semi_supervised.LabelPropagation "sklearn.semi_supervised.LabelPropagation")
        
    *   [`semi_supervised.LabelSpreading`](https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelSpreading.html#sklearn.semi_supervised.LabelSpreading "sklearn.semi_supervised.LabelSpreading")
        
    *   [`discriminant_analysis.LinearDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html#sklearn.discriminant_analysis.LinearDiscriminantAnalysis "sklearn.discriminant_analysis.LinearDiscriminantAnalysis")
        
    *   [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
         (setting multi\_class=”crammer\_singer”)
        
    *   [`linear_model.LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression "sklearn.linear_model.LogisticRegression")
         (all solvers but “liblinear”)
        
    *   [`linear_model.LogisticRegressionCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html#sklearn.linear_model.LogisticRegressionCV "sklearn.linear_model.LogisticRegressionCV")
         (all solvers but “liblinear”)
        
    *   [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
        
    *   [`neighbors.NearestCentroid`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.NearestCentroid.html#sklearn.neighbors.NearestCentroid "sklearn.neighbors.NearestCentroid")
        
    *   [`discriminant_analysis.QuadraticDiscriminantAnalysis`](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis.html#sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis "sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis")
        
    *   [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
        
    *   [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
        
    *   [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
        
    *   [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
        
*   **Multiclass as One-Vs-One:**
    
    *   [`svm.NuSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC "sklearn.svm.NuSVC")
        
    *   [`svm.SVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC "sklearn.svm.SVC")
        .
        
    *   [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
         (setting multi\_class = “one\_vs\_one”)
        
*   **Multiclass as One-Vs-The-Rest:**
    
    *   [`ensemble.GradientBoostingClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier "sklearn.ensemble.GradientBoostingClassifier")
        
    *   [`gaussian_process.GaussianProcessClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessClassifier.html#sklearn.gaussian_process.GaussianProcessClassifier "sklearn.gaussian_process.GaussianProcessClassifier")
         (setting multi\_class = “one\_vs\_rest”)
        
    *   [`svm.LinearSVC`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC "sklearn.svm.LinearSVC")
         (setting multi\_class=”ovr”)
        
    *   [`linear_model.SGDClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier "sklearn.linear_model.SGDClassifier")
        
    *   [`linear_model.Perceptron`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron "sklearn.linear_model.Perceptron")
        
*   **Support multilabel:**
    
    *   [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
        
    *   [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
        
    *   [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
        
    *   [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
        
    *   [`neural_network.MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier "sklearn.neural_network.MLPClassifier")
        
    *   [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
        
    *   [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
        
    *   [`linear_model.RidgeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier "sklearn.linear_model.RidgeClassifier")
        
    *   [`linear_model.RidgeClassifierCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifierCV.html#sklearn.linear_model.RidgeClassifierCV "sklearn.linear_model.RidgeClassifierCV")
        
*   **Support multiclass-multioutput:**
    
    *   [`tree.DecisionTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier "sklearn.tree.DecisionTreeClassifier")
        
    *   [`tree.ExtraTreeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeClassifier.html#sklearn.tree.ExtraTreeClassifier "sklearn.tree.ExtraTreeClassifier")
        
    *   [`ensemble.ExtraTreesClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier "sklearn.ensemble.ExtraTreesClassifier")
        
    *   [`neighbors.KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier "sklearn.neighbors.KNeighborsClassifier")
        
    *   [`neighbors.RadiusNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsClassifier.html#sklearn.neighbors.RadiusNeighborsClassifier "sklearn.neighbors.RadiusNeighborsClassifier")
        
    *   [`ensemble.RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier "sklearn.ensemble.RandomForestClassifier")
        

1.12.1. Multiclass classification[#](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

Warning

All classifiers in scikit-learn do multiclass classification out-of-the-box. You don’t need to use the [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
 module unless you want to experiment with different multiclass strategies.

**Multiclass classification** is a classification task with more than two classes. Each sample can only be labeled as one class.

For example, classification using features extracted from a set of images of fruit, where each image may either be of an orange, an apple, or a pear. Each image is one sample and is labeled as one of the 3 possible classes. Multiclass classification makes the assumption that each sample is assigned to one and only one label - one sample cannot, for example, be both a pear and an apple.

While all scikit-learn classifiers are capable of multiclass classification, the meta-estimators offered by [`sklearn.multiclass`](https://scikit-learn.org/stable/api/sklearn.multiclass.html#module-sklearn.multiclass "sklearn.multiclass")
 permit changing the way they handle more than two classes because this may have an effect on classifier performance (either in terms of generalization error or required computational resources).

### 1.12.1.1. Target format[#](https://scikit-learn.org/stable/modules/multiclass.html#target-format "Link to this heading")

Valid [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 representations for [`type_of_target`](https://scikit-learn.org/stable/modules/generated/sklearn.utils.multiclass.type_of_target.html#sklearn.utils.multiclass.type_of_target "sklearn.utils.multiclass.type_of_target")
 (`y`) are:

*   1d or column vector containing more than two discrete values. An example of a vector `y` for 4 samples:
    
    \>>> import numpy as np
    \>>> y \= np.array(\['apple', 'pear', 'apple', 'orange'\])
    \>>> print(y)
    \['apple' 'pear' 'apple' 'orange'\]
    
    Copy to clipboard
    
*   Dense or sparse [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
     matrix of shape `(n_samples, n_classes)` with a single sample per row, where each column represents one class. An example of both a dense and sparse [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
     matrix `y` for 4 samples, where the columns, in order, are apple, orange, and pear:
    
    \>>> import numpy as np
    \>>> from sklearn.preprocessing import LabelBinarizer
    \>>> y \= np.array(\['apple', 'pear', 'apple', 'orange'\])
    \>>> y\_dense \= LabelBinarizer().fit\_transform(y)
    \>>> print(y\_dense)
    \[\[1 0 0\]\
     \[0 0 1\]\
     \[1 0 0\]\
     \[0 1 0\]\]
    \>>> from scipy import sparse
    \>>> y\_sparse \= sparse.csr\_array(y\_dense)
    \>>> print(y\_sparse)
    <Compressed Sparse Row sparse array of dtype 'int64'
      with 4 stored elements and shape (4, 3)>
      Coords Values
      (0, 0) 1
      (1, 2) 1
      (2, 0) 1
      (3, 1) 1
    
    Copy to clipboard
    

For more information about [`LabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer "sklearn.preprocessing.LabelBinarizer")
, refer to [Transforming the prediction target (y)](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
.

### 1.12.1.2. OneVsRestClassifier[#](https://scikit-learn.org/stable/modules/multiclass.html#onevsrestclassifier "Link to this heading")

The **one-vs-rest** strategy, also known as **one-vs-all**, is implemented in [`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
. The strategy consists in fitting one classifier per class. For each classifier, the class is fitted against all the other classes. In addition to its computational efficiency (only `n_classes` classifiers are needed), one advantage of this approach is its interpretability. Since each class is represented by one and only one classifier, it is possible to gain knowledge about the class by inspecting its corresponding classifier. This is the most commonly used strategy and is a fair default choice.

Below is an example of multiclass learning using OvR:

\>>> from sklearn import datasets
\>>> from sklearn.multiclass import OneVsRestClassifier
\>>> from sklearn.svm import LinearSVC
\>>> X, y \= datasets.load\_iris(return\_X\_y\=True)
\>>> OneVsRestClassifier(LinearSVC(random\_state\=0)).fit(X, y).predict(X)
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
       1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1,\
       1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2,\
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2\])

Copy to clipboard

[`OneVsRestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsRestClassifier.html#sklearn.multiclass.OneVsRestClassifier "sklearn.multiclass.OneVsRestClassifier")
 also supports multilabel classification. To use this feature, feed the classifier an indicator matrix, in which cell \[i, j\] indicates the presence of label j in sample i.

[![../_images/sphx_glr_plot_multilabel_001.png](https://scikit-learn.org/stable/_images/sphx_glr_plot_multilabel_001.png)](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html)

Examples

*   [Multilabel classification](https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_multilabel.html#sphx-glr-auto-examples-miscellaneous-plot-multilabel-py)
    
*   [Plot classification probability](https://scikit-learn.org/stable/auto_examples/classification/plot_classification_probability.html#sphx-glr-auto-examples-classification-plot-classification-probability-py)
    
*   [Decision Boundaries of Multinomial and One-vs-Rest Logistic Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_logistic_multinomial.html#sphx-glr-auto-examples-linear-model-plot-logistic-multinomial-py)
    

### 1.12.1.3. OneVsOneClassifier[#](https://scikit-learn.org/stable/modules/multiclass.html#onevsoneclassifier "Link to this heading")

[`OneVsOneClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OneVsOneClassifier.html#sklearn.multiclass.OneVsOneClassifier "sklearn.multiclass.OneVsOneClassifier")
 constructs one classifier per pair of classes. At prediction time, the class which received the most votes is selected. In the event of a tie (among two classes with an equal number of votes), it selects the class with the highest aggregate classification confidence by summing over the pair-wise classification confidence levels computed by the underlying binary classifiers.

Since it requires to fit `n_classes * (n_classes - 1) / 2` classifiers, this method is usually slower than one-vs-the-rest, due to its O(n\_classes^2) complexity. However, this method may be advantageous for algorithms such as kernel algorithms which don’t scale well with `n_samples`. This is because each individual learning problem only involves a small subset of the data whereas, with one-vs-the-rest, the complete dataset is used `n_classes` times. The decision function is the result of a monotonic transformation of the one-versus-one classification.

Below is an example of multiclass learning using OvO:

\>>> from sklearn import datasets
\>>> from sklearn.multiclass import OneVsOneClassifier
\>>> from sklearn.svm import LinearSVC
\>>> X, y \= datasets.load\_iris(return\_X\_y\=True)
\>>> OneVsOneClassifier(LinearSVC(random\_state\=0)).fit(X, y).predict(X)
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
       1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1,\
       1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2\])

Copy to clipboard

References

*   “Pattern Recognition and Machine Learning. Springer”, Christopher M. Bishop, page 183, (First Edition)
    

### 1.12.1.4. OutputCodeClassifier[#](https://scikit-learn.org/stable/modules/multiclass.html#outputcodeclassifier "Link to this heading")

Error-Correcting Output Code-based strategies are fairly different from one-vs-the-rest and one-vs-one. With these strategies, each class is represented in a Euclidean space, where each dimension can only be 0 or 1. Another way to put it is that each class is represented by a binary code (an array of 0 and 1). The matrix which keeps track of the location/code of each class is called the code book. The code size is the dimensionality of the aforementioned space. Intuitively, each class should be represented by a code as unique as possible and a good code book should be designed to optimize classification accuracy. In this implementation, we simply use a randomly-generated code book as advocated in [\[3\]](https://scikit-learn.org/stable/modules/multiclass.html#id3)
 although more elaborate methods may be added in the future.

At fitting time, one binary classifier per bit in the code book is fitted. At prediction time, the classifiers are used to project new points in the class space and the class closest to the points is chosen.

In [`OutputCodeClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multiclass.OutputCodeClassifier.html#sklearn.multiclass.OutputCodeClassifier "sklearn.multiclass.OutputCodeClassifier")
, the `code_size` attribute allows the user to control the number of classifiers which will be used. It is a percentage of the total number of classes.

A number between 0 and 1 will require fewer classifiers than one-vs-the-rest. In theory, `log2(n_classes) / n_classes` is sufficient to represent each class unambiguously. However, in practice, it may not lead to good accuracy since `log2(n_classes)` is much smaller than `n_classes`.

A number greater than 1 will require more classifiers than one-vs-the-rest. In this case, some classifiers will in theory correct for the mistakes made by other classifiers, hence the name “error-correcting”. In practice, however, this may not happen as classifier mistakes will typically be correlated. The error-correcting output codes have a similar effect to bagging.

Below is an example of multiclass learning using Output-Codes:

\>>> from sklearn import datasets
\>>> from sklearn.multiclass import OutputCodeClassifier
\>>> from sklearn.svm import LinearSVC
\>>> X, y \= datasets.load\_iris(return\_X\_y\=True)
\>>> clf \= OutputCodeClassifier(LinearSVC(random\_state\=0), code\_size\=2, random\_state\=0)
\>>> clf.fit(X, y).predict(X)
array(\[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\
       0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1,\
       1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1,\
       1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,\
       2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 2,\
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2\])

Copy to clipboard

References

*   “Solving multiclass learning problems via error-correcting output codes”, Dietterich T., Bakiri G., Journal of Artificial Intelligence Research 2, 1995.
    

*   “The Elements of Statistical Learning”, Hastie T., Tibshirani R., Friedman J., page 606 (second-edition), 2008.
    

1.12.2. Multilabel classification[#](https://scikit-learn.org/stable/modules/multiclass.html#multilabel-classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

**Multilabel classification** (closely related to **multioutput** **classification**) is a classification task labeling each sample with `m` labels from `n_classes` possible classes, where `m` can be 0 to `n_classes` inclusive. This can be thought of as predicting properties of a sample that are not mutually exclusive. Formally, a binary output is assigned to each class, for every sample. Positive classes are indicated with 1 and negative classes with 0 or -1. It is thus comparable to running `n_classes` binary classification tasks, for example with [`MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
. This approach treats each label independently whereas multilabel classifiers _may_ treat the multiple classes simultaneously, accounting for correlated behavior among them.

For example, prediction of the topics relevant to a text document or video. The document or video may be about one of ‘religion’, ‘politics’, ‘finance’ or ‘education’, several of the topic classes or all of the topic classes.

### 1.12.2.1. Target format[#](https://scikit-learn.org/stable/modules/multiclass.html#id5 "Link to this heading")

A valid representation of [multilabel](https://scikit-learn.org/stable/glossary.html#term-multilabel)
 `y` is an either dense or sparse [binary](https://scikit-learn.org/stable/glossary.html#term-binary)
 matrix of shape `(n_samples, n_classes)`. Each column represents a class. The `1`’s in each row denote the positive classes a sample has been labeled with. An example of a dense matrix `y` for 3 samples:

\>>> y \= np.array(\[\[1, 0, 0, 1\], \[0, 0, 1, 1\], \[0, 0, 0, 0\]\])
\>>> print(y)
\[\[1 0 0 1\]\
 \[0 0 1 1\]\
 \[0 0 0 0\]\]

Copy to clipboard

Dense binary matrices can also be created using [`MultiLabelBinarizer`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html#sklearn.preprocessing.MultiLabelBinarizer "sklearn.preprocessing.MultiLabelBinarizer")
. For more information, refer to [Transforming the prediction target (y)](https://scikit-learn.org/stable/modules/preprocessing_targets.html#preprocessing-targets)
.

An example of the same `y` in sparse matrix form:

\>>> y\_sparse \= sparse.csr\_array(y)
\>>> print(y\_sparse)
<Compressed Sparse Row sparse array of dtype 'int64'
  with 4 stored elements and shape (3, 4)>
  Coords Values
  (0, 0) 1
  (0, 3) 1
  (1, 2) 1
  (1, 3) 1

Copy to clipboard

### 1.12.2.2. MultiOutputClassifier[#](https://scikit-learn.org/stable/modules/multiclass.html#multioutputclassifier "Link to this heading")

Multilabel classification support can be added to any classifier with [`MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
. This strategy consists of fitting one classifier per target. This allows multiple target variable classifications. The purpose of this class is to extend estimators to be able to estimate a series of target functions (f1,f2,f3…,fn) that are trained on a single X predictor matrix to predict a series of responses (y1,y2,y3…,yn).

You can find a usage example for [`MultiOutputClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputClassifier.html#sklearn.multioutput.MultiOutputClassifier "sklearn.multioutput.MultiOutputClassifier")
 as part of the section on [Multiclass-multioutput classification](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-multioutput-classification)
 since it is a generalization of multilabel classification to multiclass outputs instead of binary outputs.

### 1.12.2.3. ClassifierChain[#](https://scikit-learn.org/stable/modules/multiclass.html#classifierchain "Link to this heading")

Classifier chains (see [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
) are a way of combining a number of binary classifiers into a single multi-label model that is capable of exploiting correlations among targets.

For a multi-label classification problem with N classes, N binary classifiers are assigned an integer between 0 and N-1. These integers define the order of models in the chain. Each classifier is then fit on the available training data plus the true labels of the classes whose models were assigned a lower number.

When predicting, the true labels will not be available. Instead the predictions of each model are passed on to the subsequent models in the chain to be used as features.

Clearly the order of the chain is important. The first model in the chain has no information about the other labels while the last model in the chain has features indicating the presence of all of the other labels. In general one does not know the optimal ordering of the models in the chain so typically many randomly ordered chains are fit and their predictions are averaged together.

References

*   Jesse Read, Bernhard Pfahringer, Geoff Holmes, Eibe Frank, “Classifier Chains for Multi-label Classification”, 2009.
    

1.12.3. Multiclass-multioutput classification[#](https://scikit-learn.org/stable/modules/multiclass.html#multiclass-multioutput-classification "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Multiclass-multioutput classification** (also known as **multitask classification**) is a classification task which labels each sample with a set of **non-binary** properties. Both the number of properties and the number of classes per property is greater than 2. A single estimator thus handles several joint classification tasks. This is both a generalization of the multi_label_ classification task, which only considers binary attributes, as well as a generalization of the multi_class_ classification task, where only one property is considered.

For example, classification of the properties “type of fruit” and “colour” for a set of images of fruit. The property “type of fruit” has the possible classes: “apple”, “pear” and “orange”. The property “colour” has the possible classes: “green”, “red”, “yellow” and “orange”. Each sample is an image of a fruit, a label is output for both properties and each label is one of the possible classes of the corresponding property.

Note that all classifiers handling multiclass-multioutput (also known as multitask classification) tasks, support the multilabel classification task as a special case. Multitask classification is similar to the multioutput classification task with different model formulations. For more information, see the relevant estimator documentation.

Below is an example of multiclass-multioutput classification:

\>>> from sklearn.datasets import make\_classification
\>>> from sklearn.multioutput import MultiOutputClassifier
\>>> from sklearn.ensemble import RandomForestClassifier
\>>> from sklearn.utils import shuffle
\>>> import numpy as np
\>>> X, y1 \= make\_classification(n\_samples\=10, n\_features\=100,
...                             n\_informative\=30, n\_classes\=3,
...                             random\_state\=1)
\>>> y2 \= shuffle(y1, random\_state\=1)
\>>> y3 \= shuffle(y1, random\_state\=2)
\>>> Y \= np.vstack((y1, y2, y3)).T
\>>> n\_samples, n\_features \= X.shape \# 10,100
\>>> n\_outputs \= Y.shape\[1\] \# 3
\>>> n\_classes \= 3
\>>> forest \= RandomForestClassifier(random\_state\=1)
\>>> multi\_target\_forest \= MultiOutputClassifier(forest, n\_jobs\=2)
\>>> multi\_target\_forest.fit(X, Y).predict(X)
array(\[\[2, 2, 0\],\
       \[1, 2, 1\],\
       \[2, 1, 0\],\
       \[0, 0, 2\],\
       \[0, 2, 1\],\
       \[0, 0, 2\],\
       \[1, 1, 0\],\
       \[1, 1, 1\],\
       \[0, 0, 2\],\
       \[2, 0, 0\]\])

Copy to clipboard

Warning

At present, no metric in [`sklearn.metrics`](https://scikit-learn.org/stable/api/sklearn.metrics.html#module-sklearn.metrics "sklearn.metrics")
 supports the multiclass-multioutput classification task.

### 1.12.3.1. Target format[#](https://scikit-learn.org/stable/modules/multiclass.html#id8 "Link to this heading")

A valid representation of [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
 `y` is a dense matrix of shape `(n_samples, n_classes)` of class labels. A column wise concatenation of 1d [multiclass](https://scikit-learn.org/stable/glossary.html#term-multiclass)
 variables. An example of `y` for 3 samples:

\>>> y \= np.array(\[\['apple', 'green'\], \['orange', 'orange'\], \['pear', 'green'\]\])
\>>> print(y)
\[\['apple' 'green'\]\
 \['orange' 'orange'\]\
 \['pear' 'green'\]\]

Copy to clipboard

1.12.4. Multioutput regression[#](https://scikit-learn.org/stable/modules/multiclass.html#multioutput-regression "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

**Multioutput regression** predicts multiple numerical properties for each sample. Each property is a numerical variable and the number of properties to be predicted for each sample is greater than or equal to 2. Some estimators that support multioutput regression are faster than just running `n_output` estimators.

For example, prediction of both wind speed and wind direction, in degrees, using data obtained at a certain location. Each sample would be data obtained at one location and both wind speed and direction would be output for each sample.

The following regressors natively support multioutput regression:

*   [`cross_decomposition.CCA`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.CCA.html#sklearn.cross_decomposition.CCA "sklearn.cross_decomposition.CCA")
    
*   [`tree.DecisionTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor "sklearn.tree.DecisionTreeRegressor")
    
*   [`dummy.DummyRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyRegressor.html#sklearn.dummy.DummyRegressor "sklearn.dummy.DummyRegressor")
    
*   [`linear_model.ElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.ElasticNet.html#sklearn.linear_model.ElasticNet "sklearn.linear_model.ElasticNet")
    
*   [`tree.ExtraTreeRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.ExtraTreeRegressor.html#sklearn.tree.ExtraTreeRegressor "sklearn.tree.ExtraTreeRegressor")
    
*   [`ensemble.ExtraTreesRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesRegressor.html#sklearn.ensemble.ExtraTreesRegressor "sklearn.ensemble.ExtraTreesRegressor")
    
*   [`gaussian_process.GaussianProcessRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.gaussian_process.GaussianProcessRegressor.html#sklearn.gaussian_process.GaussianProcessRegressor "sklearn.gaussian_process.GaussianProcessRegressor")
    
*   [`neighbors.KNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html#sklearn.neighbors.KNeighborsRegressor "sklearn.neighbors.KNeighborsRegressor")
    
*   [`kernel_ridge.KernelRidge`](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_ridge.KernelRidge.html#sklearn.kernel_ridge.KernelRidge "sklearn.kernel_ridge.KernelRidge")
    
*   [`linear_model.Lars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lars.html#sklearn.linear_model.Lars "sklearn.linear_model.Lars")
    
*   [`linear_model.Lasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html#sklearn.linear_model.Lasso "sklearn.linear_model.Lasso")
    
*   [`linear_model.LassoLars`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoLars.html#sklearn.linear_model.LassoLars "sklearn.linear_model.LassoLars")
    
*   [`linear_model.LinearRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression "sklearn.linear_model.LinearRegression")
    
*   [`multioutput.MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
    
*   [`linear_model.MultiTaskElasticNet`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNet.html#sklearn.linear_model.MultiTaskElasticNet "sklearn.linear_model.MultiTaskElasticNet")
    
*   [`linear_model.MultiTaskElasticNetCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskElasticNetCV.html#sklearn.linear_model.MultiTaskElasticNetCV "sklearn.linear_model.MultiTaskElasticNetCV")
    
*   [`linear_model.MultiTaskLasso`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLasso.html#sklearn.linear_model.MultiTaskLasso "sklearn.linear_model.MultiTaskLasso")
    
*   [`linear_model.MultiTaskLassoCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.MultiTaskLassoCV.html#sklearn.linear_model.MultiTaskLassoCV "sklearn.linear_model.MultiTaskLassoCV")
    
*   [`linear_model.OrthogonalMatchingPursuit`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.OrthogonalMatchingPursuit.html#sklearn.linear_model.OrthogonalMatchingPursuit "sklearn.linear_model.OrthogonalMatchingPursuit")
    
*   [`cross_decomposition.PLSCanonical`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSCanonical.html#sklearn.cross_decomposition.PLSCanonical "sklearn.cross_decomposition.PLSCanonical")
    
*   [`cross_decomposition.PLSRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.cross_decomposition.PLSRegression.html#sklearn.cross_decomposition.PLSRegression "sklearn.cross_decomposition.PLSRegression")
    
*   [`linear_model.RANSACRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RANSACRegressor.html#sklearn.linear_model.RANSACRegressor "sklearn.linear_model.RANSACRegressor")
    
*   [`neighbors.RadiusNeighborsRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.RadiusNeighborsRegressor.html#sklearn.neighbors.RadiusNeighborsRegressor "sklearn.neighbors.RadiusNeighborsRegressor")
    
*   [`ensemble.RandomForestRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor "sklearn.ensemble.RandomForestRegressor")
    
*   [`multioutput.RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
    
*   [`linear_model.Ridge`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html#sklearn.linear_model.Ridge "sklearn.linear_model.Ridge")
    
*   [`linear_model.RidgeCV`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV "sklearn.linear_model.RidgeCV")
    
*   [`compose.TransformedTargetRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.TransformedTargetRegressor.html#sklearn.compose.TransformedTargetRegressor "sklearn.compose.TransformedTargetRegressor")
    

### 1.12.4.1. Target format[#](https://scikit-learn.org/stable/modules/multiclass.html#id10 "Link to this heading")

A valid representation of [multioutput](https://scikit-learn.org/stable/glossary.html#term-multioutput)
 `y` is a dense matrix of shape `(n_samples, n_output)` of floats. A column wise concatenation of [continuous](https://scikit-learn.org/stable/glossary.html#term-continuous)
 variables. An example of `y` for 3 samples:

\>>> y \= np.array(\[\[31.4, 94\], \[40.5, 109\], \[25.0, 30\]\])
\>>> print(y)
\[\[ 31.4  94. \]\
 \[ 40.5 109. \]\
 \[ 25.   30. \]\]

Copy to clipboard

### 1.12.4.2. MultiOutputRegressor[#](https://scikit-learn.org/stable/modules/multiclass.html#multioutputregressor "Link to this heading")

Multioutput regression support can be added to any regressor with [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
. This strategy consists of fitting one regressor per target. Since each target is represented by exactly one regressor it is possible to gain knowledge about the target by inspecting its corresponding regressor. As [`MultiOutputRegressor`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html#sklearn.multioutput.MultiOutputRegressor "sklearn.multioutput.MultiOutputRegressor")
 fits one regressor per target it can not take advantage of correlations between targets.

Below is an example of multioutput regression:

\>>> from sklearn.datasets import make\_regression
\>>> from sklearn.multioutput import MultiOutputRegressor
\>>> from sklearn.ensemble import GradientBoostingRegressor
\>>> X, y \= make\_regression(n\_samples\=10, n\_targets\=3, random\_state\=1)
\>>> MultiOutputRegressor(GradientBoostingRegressor(random\_state\=0)).fit(X, y).predict(X)
array(\[\[-154.75474165, -147.03498585,  -50.03812219\],\
       \[   7.12165031,    5.12914884,  -81.46081961\],\
       \[-187.8948621 , -100.44373091,   13.88978285\],\
       \[-141.62745778,   95.02891072, -191.48204257\],\
       \[  97.03260883,  165.34867495,  139.52003279\],\
       \[ 123.92529176,   21.25719016,   -7.84253   \],\
       \[-122.25193977,  -85.16443186, -107.12274212\],\
       \[ -30.170388  ,  -94.80956739,   12.16979946\],\
       \[ 140.72667194,  176.50941682,  -17.50447799\],\
       \[ 149.37967282,  -81.15699552,   -5.72850319\]\])

Copy to clipboard

### 1.12.4.3. RegressorChain[#](https://scikit-learn.org/stable/modules/multiclass.html#regressorchain "Link to this heading")

Regressor chains (see [`RegressorChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.RegressorChain.html#sklearn.multioutput.RegressorChain "sklearn.multioutput.RegressorChain")
) is analogous to [`ClassifierChain`](https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.ClassifierChain.html#sklearn.multioutput.ClassifierChain "sklearn.multioutput.ClassifierChain")
 as a way of combining a number of regressions into a single multi-target model that is capable of exploiting correlations among targets.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)