[Skip to main content](https://numpy.org/doc/stable/reference/random/examples/cython/meson.build.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/random/examples/cython/meson.build.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/random/examples/cython/meson.build.html)
[2.4](https://numpy.org/doc/2.4/reference/random/examples/cython/meson.build.html)
[2.3](https://numpy.org/doc/2.3/reference/random/examples/cython/meson.build.html)
[2.2](https://numpy.org/doc/2.2/reference/random/examples/cython/meson.build.html)
[2.1](https://numpy.org/doc/2.1/reference/random/examples/cython/meson.build.html)
[2.0](https://numpy.org/doc/2.0/reference/random/examples/cython/meson.build.html)
[1.26](https://numpy.org/doc/1.26/reference/random/examples/cython/meson.build.html)
[1.25](https://numpy.org/doc/1.25/reference/random/examples/cython/meson.build.html)
[1.24](https://numpy.org/doc/1.24/reference/random/examples/cython/meson.build.html)
[1.23](https://numpy.org/doc/1.23/reference/random/examples/cython/meson.build.html)
[1.22](https://numpy.org/doc/1.22/reference/random/examples/cython/meson.build.html)
[1.21](https://numpy.org/doc/1.21/reference/random/examples/cython/meson.build.html)
[1.20](https://numpy.org/doc/1.20/reference/random/examples/cython/meson.build.html)
[1.19](https://numpy.org/doc/1.19/reference/random/examples/cython/meson.build.html)
[1.18](https://numpy.org/doc/1.18/reference/random/examples/cython/meson.build.html)
[1.17](https://numpy.org/doc/1.17/reference/random/examples/cython/meson.build.html)
[1.16](https://numpy.org/doc/1.16/reference/random/examples/cython/meson.build.html)
[1.15](https://numpy.org/doc/1.15/reference/random/examples/cython/meson.build.html)
[1.14](https://numpy.org/doc/1.14/reference/random/examples/cython/meson.build.html)
[1.13](https://numpy.org/doc/1.13/reference/random/examples/cython/meson.build.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

meson.build[#](https://numpy.org/doc/stable/reference/random/examples/cython/meson.build.html#meson-build "Link to this heading")

==================================================================================================================================

project('random-build-examples', 'c', 'cpp', 'cython')

py\_mod \= import('python')
py3 \= py\_mod.find\_installation(pure: false)

cc \= meson.get\_compiler('c')
cy \= meson.get\_compiler('cython')

\# Keep synced with pyproject.toml
if not cy.version().version\_compare('>=3.0.6')
  error('tests requires Cython >= 3.0.6')
endif

base\_cython\_args \= \[\]
if cy.version().version\_compare('>=3.1.0')
  base\_cython\_args += \['-Xfreethreading\_compatible=True'\]
endif

\_numpy\_abs \= run\_command(py3, \['-c',\
               'import os; os.chdir(".."); import numpy; print(os.path.abspath(numpy.get\_include() + "../../.."))'\],
                         check: true).stdout().strip()

npymath\_path \= \_numpy\_abs / '\_core' / 'lib'
npy\_include\_path \= \_numpy\_abs / '\_core' / 'include'
npyrandom\_path \= \_numpy\_abs / 'random' / 'lib'
npymath\_lib \= cc.find\_library('npymath', dirs: npymath\_path)
npyrandom\_lib \= cc.find\_library('npyrandom', dirs: npyrandom\_path)

py3.extension\_module(
    'extending\_distributions',
    'extending\_distributions.pyx',
    install: false,
    include\_directories: \[npy\_include\_path\],
    dependencies: \[npyrandom\_lib, npymath\_lib\],
    cython\_args: base\_cython\_args,
)
py3.extension\_module(
    'extending',
    'extending.pyx',
    install: false,
    include\_directories: \[npy\_include\_path\],
    dependencies: \[npyrandom\_lib, npymath\_lib\],
    cython\_args: base\_cython\_args,
)
py3.extension\_module(
    'extending\_cpp',
    'extending\_distributions.pyx',
    install: false,
    override\_options : \['cython\_language=cpp'\],
    cython\_args: base\_cython\_args + \['--module-name', 'extending\_cpp'\],
    include\_directories: \[npy\_include\_path\],
    dependencies: \[npyrandom\_lib, npymath\_lib\],
)

Copy to clipboard