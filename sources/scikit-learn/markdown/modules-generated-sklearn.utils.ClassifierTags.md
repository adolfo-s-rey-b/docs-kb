[Skip to main content](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/modules/generated/sklearn.utils.ClassifierTags.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html)
[1.8.0](https://scikit-learn.org/1.8/modules/generated/sklearn.utils.ClassifierTags.html)
[1.7.2](https://scikit-learn.org/1.7/modules/generated/sklearn.utils.ClassifierTags.html)
[1.6.1](https://scikit-learn.org/1.6/modules/generated/sklearn.utils.ClassifierTags.html)
[1.5.2](https://scikit-learn.org/1.5/modules/generated/sklearn.utils.ClassifierTags.html)
[1.4.2](https://scikit-learn.org/1.4/modules/generated/sklearn.utils.ClassifierTags.html)

Collapse Sidebar Expand Sidebar

ClassifierTags[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#classifiertags "Link to this heading")

=============================================================================================================================================

class sklearn.utils.ClassifierTags(_poor\_score: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_, _multi\_class: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= True_, _multi\_label: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
 \= False_)[\[source\]](https://github.com/scikit-learn/scikit-learn/blob/afe5bcd80/sklearn/utils/_tags.py#L135)
[#](https://scikit-learn.org/stable/modules/generated/sklearn.utils.ClassifierTags.html#sklearn.utils.ClassifierTags "Link to this definition")

Tags for the classifier.

Parameters:

**poor\_score**bool, default=False

Whether the estimator fails to provide a “reasonable” test-set score, which currently for classification is an accuracy of 0.83 on `make_blobs(n_samples=300, random_state=0)`. The datasets and values are based on current estimators in scikit-learn and might be replaced by something more systematic.

**multi\_class**bool, default=True

Whether the classifier can handle multi-class classification. Note that all classifiers support binary classification. Therefore this flag indicates whether the classifier is a binary-classifier-only or not.

See [multi-class](https://scikit-learn.org/stable/glossary.html#term-multi-class)
 in the glossary.

**multi\_label**bool, default=False

Whether the classifier supports multi-label output: a data point can be predicted to belong to a variable number of classes.

See [multi-label](https://scikit-learn.org/stable/glossary.html#term-multi-label)
 in the glossary.

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)