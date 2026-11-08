[Skip to main content](https://numpy.org/doc/stable/building/understanding_meson.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/understanding_meson.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/understanding_meson.html)
[2.4](https://numpy.org/doc/2.4/building/understanding_meson.html)
[2.3](https://numpy.org/doc/2.3/building/understanding_meson.html)
[2.2](https://numpy.org/doc/2.2/building/understanding_meson.html)
[2.1](https://numpy.org/doc/2.1/building/understanding_meson.html)
[2.0](https://numpy.org/doc/2.0/building/understanding_meson.html)
[1.26](https://numpy.org/doc/1.26/building/understanding_meson.html)
[1.25](https://numpy.org/doc/1.25/building/understanding_meson.html)
[1.24](https://numpy.org/doc/1.24/building/understanding_meson.html)
[1.23](https://numpy.org/doc/1.23/building/understanding_meson.html)
[1.22](https://numpy.org/doc/1.22/building/understanding_meson.html)
[1.21](https://numpy.org/doc/1.21/building/understanding_meson.html)
[1.20](https://numpy.org/doc/1.20/building/understanding_meson.html)
[1.19](https://numpy.org/doc/1.19/building/understanding_meson.html)
[1.18](https://numpy.org/doc/1.18/building/understanding_meson.html)
[1.17](https://numpy.org/doc/1.17/building/understanding_meson.html)
[1.16](https://numpy.org/doc/1.16/building/understanding_meson.html)
[1.15](https://numpy.org/doc/1.15/building/understanding_meson.html)
[1.14](https://numpy.org/doc/1.14/building/understanding_meson.html)
[1.13](https://numpy.org/doc/1.13/building/understanding_meson.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Understanding Meson[#](https://numpy.org/doc/stable/building/understanding_meson.html#understanding-meson "Link to this heading")

==================================================================================================================================

Building NumPy relies on the following tools, which can be considered part of the build system:

*   `meson`: the Meson build system, installable as a pure Python package from PyPI or conda-forge
    
*   `ninja`: the build tool invoked by Meson to do the actual building (e.g. invoking compilers). Installable also from PyPI (on all common platforms) or conda-forge.
    
*   `pkg-config`: the tool used for discovering dependencies (in particular BLAS/LAPACK). Available on conda-forge (and Homebrew, Chocolatey, and Linux package managers), but not packaged on PyPI.
    
*   `meson-python`: the Python build backend (i.e., the thing that gets invoked via a hook in `pyproject.toml` by a build frontend like `pip` or `pypa/build`). This is a thin layer on top of Meson, with as main roles (a) interface with build frontends, and (b) produce sdists and wheels with valid file names and metadata.
    

Warning

As of Dec’23, NumPy vendors a custom version of Meson, which is needed for SIMD and BLAS/LAPACK features that are not yet available in upstream Meson. Hence, using the `meson` executable directly is not possible. Instead, wherever instructions say `meson xxx`, use `python vendored-meson/meson/meson.py xxx` instead.

Building with Meson happens in stages:

*   A configure stage (`meson setup`) to detect compilers, dependencies and build options, and create the build directory and `build.ninja` file,
    
*   A compile stage (`meson compile` or `ninja`), where the extension modules that are part of a built NumPy package get compiled,
    
*   An install stage (`meson install`) to install the installable files from the source and build directories to the target install directory,
    

Meson has a good build dependency tracking system, so invoking a build for a second time will rebuild only targets for which any sources or dependencies have changed.

To learn more about Meson[#](https://numpy.org/doc/stable/building/understanding_meson.html#to-learn-more-about-meson "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Meson has [very good documentation](https://mesonbuild.com/)
; it pays off to read it, and is often the best source of answers for “how to do X”. Furthermore, an extensive pdf book on Meson can be obtained for free at [https://nibblestew.blogspot.com/2021/12/this-year-receive-gift-of-free-meson.html](https://nibblestew.blogspot.com/2021/12/this-year-receive-gift-of-free-meson.html)

To learn more about the design principles Meson uses, the recent talks linked from [mesonbuild.com/Videos](https://mesonbuild.com/Videos.html)
 are also a good resource.

Explanation of build stages[#](https://numpy.org/doc/stable/building/understanding_meson.html#explanation-of-build-stages "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

_This is for teaching purposes only; there should be no need to execute these stages separately!_

Assume we’re starting from a clean repo and a fully set up conda environment:

git clone git@github.com:numpy/numpy.git
git submodule update \--init
mamba env create \-f environment.yml
mamba activate numpy\-dev

Copy to clipboard

To now run the configure stage of the build and instruct Meson to put the build artifacts in `build/` and a local install under `build-install/` relative to the root of the repo, do:

meson setup build --prefix=$PWD/build-install

Copy to clipboard

To then run the compile stage of the build, do:

ninja \-C build

Copy to clipboard

In the command above, `-C` is followed by the name of the build directory. You can have multiple build directories at the same time. Meson is fully out-of-place, so those builds will not interfere with each other. You can for example have a GCC build, a Clang build and a debug build in different directories.

To then install NumPy into the prefix (`build-install/` here, but note that that’s just an arbitrary name we picked here):

meson install \-C build

Copy to clipboard

It will then install to `build-install/lib/python3.12/site-packages/numpy`, which is not on your Python path, so to add it do (_again, this is for learning purposes, using \`\`PYTHONPATH\`\` explicitly is typically not the best idea_):

export PYTHONPATH=$PWD/build-install/lib/python3.12/site-packages/

Copy to clipboard

Now we should be able to import `numpy` and run the tests. Remembering that we need to move out of the root of the repo to ensure we pick up the package and not the local `numpy/` source directory:

cd doc
python \-c "import numpy as np; np.test()"

Copy to clipboard

The above runs the “fast” numpy test suite. Other ways of running the tests should also work, for example:

pytest \--pyargs numpy

Copy to clipboard

The full test suite should pass, without any build warnings on Linux (with the GCC version for which `-Werror` is enforced in CI at least) and with at most a moderate amount of warnings on other platforms.

On this page