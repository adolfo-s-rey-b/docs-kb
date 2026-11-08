[Skip to main content](https://numpy.org/doc/stable/building/distutils_equivalents.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/distutils_equivalents.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/distutils_equivalents.html)
[2.4](https://numpy.org/doc/2.4/building/distutils_equivalents.html)
[2.3](https://numpy.org/doc/2.3/building/distutils_equivalents.html)
[2.2](https://numpy.org/doc/2.2/building/distutils_equivalents.html)
[2.1](https://numpy.org/doc/2.1/building/distutils_equivalents.html)
[2.0](https://numpy.org/doc/2.0/building/distutils_equivalents.html)
[1.26](https://numpy.org/doc/1.26/building/distutils_equivalents.html)
[1.25](https://numpy.org/doc/1.25/building/distutils_equivalents.html)
[1.24](https://numpy.org/doc/1.24/building/distutils_equivalents.html)
[1.23](https://numpy.org/doc/1.23/building/distutils_equivalents.html)
[1.22](https://numpy.org/doc/1.22/building/distutils_equivalents.html)
[1.21](https://numpy.org/doc/1.21/building/distutils_equivalents.html)
[1.20](https://numpy.org/doc/1.20/building/distutils_equivalents.html)
[1.19](https://numpy.org/doc/1.19/building/distutils_equivalents.html)
[1.18](https://numpy.org/doc/1.18/building/distutils_equivalents.html)
[1.17](https://numpy.org/doc/1.17/building/distutils_equivalents.html)
[1.16](https://numpy.org/doc/1.16/building/distutils_equivalents.html)
[1.15](https://numpy.org/doc/1.15/building/distutils_equivalents.html)
[1.14](https://numpy.org/doc/1.14/building/distutils_equivalents.html)
[1.13](https://numpy.org/doc/1.13/building/distutils_equivalents.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Meson and `distutils` ways of doing things[#](https://numpy.org/doc/stable/building/distutils_equivalents.html#meson-and-distutils-ways-of-doing-things "Link to this heading")

================================================================================================================================================================================

_Old workflows (numpy.distutils based, no longer relevant):_

1.  `python runtests.py`
    
2.  `python setup.py build_ext -i` + `export PYTHONPATH=/home/username/path/to/numpy/reporoot` (and then edit pure Python code in NumPy and run it with `python some_script.py`).
    
3.  `python setup.py develop` - this is similar to (2), except in-place build is made permanently visible in env.
    
4.  `python setup.py bdist_wheel` + `pip install dist/numpy*.whl` - build wheel in current env and install it.
    
5.  `pip install .` - build wheel in an isolated build env against deps in `pyproject.toml` and install it. _Note: be careful, this is usually not the correct command for development installs - typically you want to use (4) or_ `pip install . -v --no-build-isolation`.
    

_New workflows (Meson and meson-python based):_

1.  `spin test`
    
2.  `pip install -e . --no-build-isolation` (note: only for working on NumPy itself - for more details, see [IDE support & editable installs](https://numpy.org/doc/stable/building/index.html#meson-editable-installs)
    )
    
3.  the same as (2)
    
4.  `python -m build --no-isolation` + `pip install dist/numpy*.whl` - see [pypa/build](https://pypa-build.readthedocs.io/en/latest/)
    .
    
5.  `pip install .`