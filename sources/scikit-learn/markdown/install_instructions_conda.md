[Skip to main content](https://scikit-learn.org/stable/install_instructions_conda.html#main-content)

Back to top Ctrl+K

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/scikit-learn/scikit-learn)
    

1.9.1 (stable)

[1.10.dev0 (dev)](https://scikit-learn.org/dev/install_instructions_conda.html)
[1.9.1 (stable)](https://scikit-learn.org/stable/install_instructions_conda.html)
[1.8.0](https://scikit-learn.org/1.8/install_instructions_conda.html)
[1.7.2](https://scikit-learn.org/1.7/install_instructions_conda.html)
[1.6.1](https://scikit-learn.org/1.6/install_instructions_conda.html)
[1.5.2](https://scikit-learn.org/1.5/install_instructions_conda.html)
[1.4.2](https://scikit-learn.org/1.4/install_instructions_conda.html)

Install conda using the [conda-forge installers](https://conda-forge.org/download/)
 (no administrator permission required). Then run:

conda create \-n sklearn-env \-c conda-forge scikit-learn
conda activate sklearn-env

Copy to clipboard

In order to check your installation, you can use:

conda list scikit-learn  \# show scikit-learn version and location
conda list               \# show all installed packages in the environment
python \-c "import sklearn; sklearn.show\_versions()"

Copy to clipboard

On this page

* * *

scikit-learn is [financially supported](https://scikit-learn.org/stable/institutional_support.html#funding)
 by Probabl and other institutions.

[![](https://scikit-learn.org/stable/_static/probabl.png "Probabl")\
\
Enterprise-grade solutions and services](https://probabl.ai/lp/scikit-learn)