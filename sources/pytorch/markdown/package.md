Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/package.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/package.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/package.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/package.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/package.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/package.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/package.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/package.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/package.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/package.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/package.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/package.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/package.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/package.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/package.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/package.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/package.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/package.html)
[v1.13](https://docs.pytorch.org/docs/1.13/package.html)
[v1.12](https://docs.pytorch.org/docs/1.12/package.html)
[v1.11](https://docs.pytorch.org/docs/1.11/package.html)
[v1.10](https://docs.pytorch.org/docs/1.10/package.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/package.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/package.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/package.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/package.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/package.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/package.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/package.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/package.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/package.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/package.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/package.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/package.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/package.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/package.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/package.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/package.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/package.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/package.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/package.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/package.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/package.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/package.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

torch.package[#](https://docs.pytorch.org/docs/2.15/package.html#torch-package "Link to this heading")

=======================================================================================================

Created On: Jun 10, 2025 | Last Updated On: Apr 13, 2026

`torch.package` adds support for creating packages containing both artifacts and arbitrary PyTorch code. These packages can be saved, shared, used to load and execute models at a later date or on a different machine, and can even be deployed to production using `torch::deploy`.

This document contains tutorials, how-to guides, explanations, and an API reference that will help you learn more about `torch.package` and how to use it.

Warning

This module depends on the `pickle` module which is not secure. Only unpackage data you trust.

It is possible to construct malicious pickle data which will **execute arbitrary code during unpickling**. Never unpackage data that could have come from an untrusted source, or that could have been tampered with.

For more information, review the [documentation](https://docs.python.org/3/library/pickle.html)
 for the `pickle` module.

[Tutorials](https://docs.pytorch.org/docs/2.15/package.html#id1)
[#](https://docs.pytorch.org/docs/2.15/package.html#tutorials "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

### [Packaging your first model](https://docs.pytorch.org/docs/2.15/package.html#id2)
[#](https://docs.pytorch.org/docs/2.15/package.html#packaging-your-first-model "Link to this heading")

A tutorial that guides you through packaging and unpackaging a simple model is available [on Colab](https://colab.research.google.com/drive/1lFZkLyViGfXxB-m3jqlyTQuYToo3XLo-)
. After completing this exercise, you will be familiar with the basic API for creating and using Torch packages.

[How do I…](https://docs.pytorch.org/docs/2.15/package.html#id3)
[#](https://docs.pytorch.org/docs/2.15/package.html#how-do-i "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

### [See what is inside a package?](https://docs.pytorch.org/docs/2.15/package.html#id4)
[#](https://docs.pytorch.org/docs/2.15/package.html#see-what-is-inside-a-package "Link to this heading")

#### Treat the package like a ZIP archive[#](https://docs.pytorch.org/docs/2.15/package.html#treat-the-package-like-a-zip-archive "Link to this heading")

The container format for a `torch.package` is ZIP, so any tools that work with standard ZIP files should work for exploring the contents. Some common ways to interact with ZIP files:

*   `unzip my_package.pt` will unzip the `torch.package` archive to disk, where you can freely inspect its contents.
    

$ unzip my\_package.pt && tree my\_package
my\_package
├── .data
│   ├── 94304870911616.storage
│   ├── 94304900784016.storage
│   ├── extern\_modules
│   └── version
├── models
│   └── model\_1.pkl
└── torchvision
    └── models
        ├── resnet.py
        └── utils.py
~ cd my\_package && cat torchvision/models/resnet.py
...

Copy to clipboard

*   The Python `zipfile` module provides a standard way to read and write ZIP archive contents.
    

from zipfile import ZipFile
with ZipFile("my\_package.pt") as myzip:
    file\_bytes \= myzip.read("torchvision/models/resnet.py")
    \# edit file\_bytes in some way
    myzip.writestr("torchvision/models/resnet.py", new\_file\_bytes)

Copy to clipboard

*   vim has the ability to natively read ZIP archives. You can even edit files and :`write` them back into the archive!
    

\# add this to your .vimrc to treat \`\*.pt\` files as zip files
au BufReadCmd \*.pt call zip#Browse(expand("<amatch>"))

~ vi my\_package.pt

Copy to clipboard

#### Use the `file_structure()` API[#](https://docs.pytorch.org/docs/2.15/package.html#use-the-file-structure-api "Link to this heading")

[`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 provides a `file_structure()` method, which will return a printable and queryable [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
 object. The [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
 object is a simple directory structure that you can use to explore the current contents of a `torch.package`.

The [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
 object itself is directly printable and will print out a file tree representation. To filter what is returned, use the glob-style `include` and `exclude` filtering arguments.

with PackageExporter('my\_package.pt') as pe:
    pe.save\_pickle('models', 'model\_1.pkl', mod)

importer \= PackageImporter('my\_package.pt')
\# can limit printed items with include/exclude args
print(importer.file\_structure(include\=\["\*\*/utils.py", "\*\*/\*.pkl"\], exclude\="\*\*/\*.storage"))
print(importer.file\_structure()) \# will print out all files

Copy to clipboard

Output:

\# filtered with glob pattern:
#    include=\["\*\*/utils.py", "\*\*/\*.pkl"\], exclude="\*\*/\*.storage"
─── my\_package.pt
    ├── models
    │   └── model\_1.pkl
    └── torchvision
        └── models
            └── utils.py

# all files
─── my\_package.pt
    ├── .data
    │   ├── 94304870911616.storage
    │   ├── 94304900784016.storage
    │   ├── extern\_modules
    │   └── version
    ├── models
    │   └── model\_1.pkl
    └── torchvision
        └── models
            ├── resnet.py
            └── utils.py

Copy to clipboard

You can also query [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
 objects with the `has_file()` method.

importer\_file\_structure \= importer.file\_structure()
found: bool \= importer\_file\_structure.has\_file("package\_a/subpackage.py")

Copy to clipboard

### [See why a given module was included as a dependency?](https://docs.pytorch.org/docs/2.15/package.html#id5)
[#](https://docs.pytorch.org/docs/2.15/package.html#see-why-a-given-module-was-included-as-a-dependency "Link to this heading")

Say there is a given module `foo`, and you want to know why your [`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
 is pulling in `foo` as a dependency.

[`PackageExporter.get_rdeps()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.get_rdeps "torch.package.PackageExporter.get_rdeps")
 will return all modules that directly depend on `foo`.

If you would like to see how a given module `src` depends on `foo`, the [`PackageExporter.all_paths()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.all_paths "torch.package.PackageExporter.all_paths")
 method will return a DOT-formatted graph showing all the dependency paths between `src` and `foo`.

If you would just like to see the whole dependency graph of your :class:`PackageExporter`, you can use [`PackageExporter.dependency_graph_string()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.dependency_graph_string "torch.package.PackageExporter.dependency_graph_string")
.

### [Include arbitrary resources with my package and access them later?](https://docs.pytorch.org/docs/2.15/package.html#id6)
[#](https://docs.pytorch.org/docs/2.15/package.html#include-arbitrary-resources-with-my-package-and-access-them-later "Link to this heading")

[`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
 exposes three methods, `save_pickle`, `save_text` and `save_binary` that allow you to save Python objects, text, and binary data to a package.

with torch.PackageExporter("package.pt") as exporter:
    \# Pickles the object and saves to \`my\_resources/tensor.pkl\` in the archive.
    exporter.save\_pickle("my\_resources", "tensor.pkl", torch.randn(4))
    exporter.save\_text("config\_stuff", "words.txt", "a sample string")
    exporter.save\_binary("raw\_data", "binary", my\_bytes)

Copy to clipboard

[`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 exposes complementary methods named `load_pickle`, `load_text` and `load_binary` that allow you to load Python objects, text and binary data from a package.

importer \= torch.PackageImporter("package.pt")
my\_tensor \= importer.load\_pickle("my\_resources", "tensor.pkl")
text \= importer.load\_text("config\_stuff", "words.txt")
binary \= importer.load\_binary("raw\_data", "binary")

Copy to clipboard

### [Customize how a class is packaged?](https://docs.pytorch.org/docs/2.15/package.html#id7)
[#](https://docs.pytorch.org/docs/2.15/package.html#customize-how-a-class-is-packaged "Link to this heading")

`torch.package` allows for the customization of how classes are packaged. This behavior is accessed through defining the method `__reduce_package__` on a class and by defining a corresponding de-packaging function. This is similar to defining `__reduce__` for Python’s normal pickling process.

Steps:

1.  Define the method `__reduce_package__(self, exporter: PackageExporter)` on the target class. This method should do the work to save the class instance inside of the package, and should return a tuple of the corresponding de-packaging function with the arguments needed to invoke the de-packaging function. This method is called by the `PackageExporter` when it encounters an instance of the target class.
    
2.  Define a de-packaging function for the class. This de-packaging function should do the work to reconstruct and return an instance of the class. The function signature’s first parameter should be a `PackageImporter` instance, and the rest of the parameters are user defined.
    

\# foo.py \[Example of customizing how class Foo is packaged\]
from torch.package import PackageExporter, PackageImporter
import time

class Foo:
    def \_\_init\_\_(self, my\_string: str):
        super().\_\_init\_\_()
        self.my\_string \= my\_string
        self.time\_imported \= 0
        self.time\_exported \= 0

    def \_\_reduce\_package\_\_(self, exporter: PackageExporter):
        """
        Called by \`\`torch.package.PackageExporter\`\`'s Pickler's \`\`persistent\_id\`\` when
        saving an instance of this object. This method should do the work to save this
        object inside of the \`\`torch.package\`\` archive.

        Returns function w/ arguments to load the object from a
        \`\`torch.package.PackageImporter\`\`'s Pickler's \`\`persistent\_load\`\` function.
        """

        \# use this pattern to ensure no naming conflicts with normal dependencies,
        \# anything saved under this module name shouldn't conflict with other
        \# items in the package
        generated\_module\_name \= f"foo-generated.\_{exporter.get\_unique\_id()}"
        exporter.save\_text(
            generated\_module\_name,
            "foo.txt",
            self.my\_string + ", with exporter modification!",
        )
        time\_exported \= time.clock\_gettime(1)

        \# returns de-packaging function w/ arguments to invoke with
        return (unpackage\_foo, (generated\_module\_name, time\_exported,))

def unpackage\_foo(
    importer: PackageImporter, generated\_module\_name: str, time\_exported: float
) \-> Foo:
    """
    Called by \`\`torch.package.PackageImporter\`\`'s Pickler's \`\`persistent\_load\`\` function
    when depickling a Foo object.
    Performs work of loading and returning a Foo instance from a \`\`torch.package\`\` archive.
    """
    time\_imported \= time.clock\_gettime(1)
    foo \= Foo(importer.load\_text(generated\_module\_name, "foo.txt"))
    foo.time\_imported \= time\_imported
    foo.time\_exported \= time\_exported
    return foo

Copy to clipboard

\# example of saving instances of class Foo

import torch
from torch.package import PackageImporter, PackageExporter
import foo

foo\_1 \= foo.Foo("foo\_1 initial string")
foo\_2 \= foo.Foo("foo\_2 initial string")
with PackageExporter('foo\_package.pt') as pe:
    \# save as normal, no extra work necessary
    pe.save\_pickle('foo\_collection', 'foo1.pkl', foo\_1)
    pe.save\_pickle('foo\_collection', 'foo2.pkl', foo\_2)

pi \= PackageImporter('foo\_package.pt')
print(pi.file\_structure())
imported\_foo \= pi.load\_pickle('foo\_collection', 'foo1.pkl')
print(f"foo\_1 string: '{imported\_foo.my\_string}'")
print(f"foo\_1 export time: {imported\_foo.time\_exported}")
print(f"foo\_1 import time: {imported\_foo.time\_imported}")

Copy to clipboard

\# output of running above script
─── foo\_package
    ├── foo-generated
    │   ├── \_0
    │   │   └── foo.txt
    │   └── \_1
    │       └── foo.txt
    ├── foo\_collection
    │   ├── foo1.pkl
    │   └── foo2.pkl
    └── foo.py

foo\_1 string: 'foo\_1 initial string, with reduction modification!'
foo\_1 export time: 9857706.650140837
foo\_1 import time: 9857706.652698385

Copy to clipboard

### [Test in my source code whether or not it is executing inside a package?](https://docs.pytorch.org/docs/2.15/package.html#id8)
[#](https://docs.pytorch.org/docs/2.15/package.html#test-in-my-source-code-whether-or-not-it-is-executing-inside-a-package "Link to this heading")

A [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 will add the attribute `__torch_package__` to every module that it initializes. Your code can check for the presence of this attribute to determine whether it is executing in a packaged context or not.

\# In foo/bar.py:

if "\_\_torch\_package\_\_" in dir():  \# true if the code is being loaded from a package
    def is\_in\_package():
        return True

    UserException \= Exception
else:
    def is\_in\_package():
        return False

    UserException \= UnpackageableException

Copy to clipboard

Now, the code will behave differently depending on whether it’s imported normally through your Python environment or imported from a `torch.package`.

from foo.bar import is\_in\_package

print(is\_in\_package())  \# False

loaded\_module \= PackageImporter(my\_package).import\_module("foo.bar")
loaded\_module.is\_in\_package()  \# True

Copy to clipboard

**Warning**: in general, it’s bad practice to have code that behaves differently depending on whether it’s packaged or not. This can lead to hard-to-debug issues that are sensitive to how you imported your code. If your package is intended to be heavily used, consider restructuring your code so that it behaves the same way no matter how it was loaded.

### [Patch code into a package?](https://docs.pytorch.org/docs/2.15/package.html#id9)
[#](https://docs.pytorch.org/docs/2.15/package.html#patch-code-into-a-package "Link to this heading")

[`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
 offers a `save_source_string()` method that allows one to save arbitrary Python source code to a module of your choosing.

with PackageExporter(f) as exporter:
    \# Save the my\_module.foo available in your current Python environment.
    exporter.save\_module("my\_module.foo")

    \# This saves the provided string to my\_module/foo.py in the package archive.
    \# It will override the my\_module.foo that was previously saved.
    exporter.save\_source\_string("my\_module.foo", textwrap.dedent(
        """\\
        def my\_function():
            print('hello world')
        """
    ))

    \# If you want to treat my\_module.bar as a package
    \# (e.g. save to \`my\_module/bar/\_\_init\_\_.py\` instead of \`my\_module/bar.py)
    \# pass is\_package=True,
    exporter.save\_source\_string("my\_module.bar",
                                "def foo(): print('hello')\\n",
                                is\_package\=True)

importer \= PackageImporter(f)
importer.import\_module("my\_module.foo").my\_function()  \# prints 'hello world'

Copy to clipboard

### [Access package contents from packaged code?](https://docs.pytorch.org/docs/2.15/package.html#id10)
[#](https://docs.pytorch.org/docs/2.15/package.html#access-package-contents-from-packaged-code "Link to this heading")

[`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 implements the [`importlib.resources`](https://docs.python.org/3/library/importlib.html#module-importlib.resources)
 API for accessing resources from inside a package.

with PackageExporter(f) as exporter:
    \# saves text to my\_resource/a.txt in the archive
    exporter.save\_text("my\_resource", "a.txt", "hello world!")
    \# saves the tensor to my\_pickle/obj.pkl
    exporter.save\_pickle("my\_pickle", "obj.pkl", torch.ones(2, 2))

    \# see below for module contents
    exporter.save\_module("foo")
    exporter.save\_module("bar")

Copy to clipboard

The `importlib.resources` API allows access to resources from within packaged code.

\# foo.py:
import importlib.resources
import my\_resource

\# returns "hello world!"
def get\_my\_resource():
    return importlib.resources.read\_text(my\_resource, "a.txt")

Copy to clipboard

Using `importlib.resources` is the recommended way to access package contents from within packaged code, since it complies with the Python standard. However, it is also possible to access the parent :class:`PackageImporter` instance itself from within packaged code.

\# bar.py:
import torch\_package\_importer \# this is the PackageImporter that imported this module.

\# Prints "hello world!", equivalent to importlib.resources.read\_text
def get\_my\_resource():
    return torch\_package\_importer.load\_text("my\_resource", "a.txt")

\# You also do things that the importlib.resources API does not support, like loading
\# a pickled object from the package.
def get\_my\_pickle():
    return torch\_package\_importer.load\_pickle("my\_pickle", "obj.pkl")

Copy to clipboard

### [Distinguish between packaged code and non-packaged code?](https://docs.pytorch.org/docs/2.15/package.html#id11)
[#](https://docs.pytorch.org/docs/2.15/package.html#distinguish-between-packaged-code-and-non-packaged-code "Link to this heading")

To tell if an object’s code is from a `torch.package`, use the `torch.package.is_from_package()` function. Note: if an object is from a package but its definition is from a module marked `extern` or from `stdlib`, this check will return `False`.

importer \= PackageImporter(f)
mod \= importer.import\_module('foo')
obj \= importer.load\_pickle('model', 'model.pkl')
txt \= importer.load\_text('text', 'my\_test.txt')

assert is\_from\_package(mod)
assert is\_from\_package(obj)
assert not is\_from\_package(txt) \# str is from stdlib, so this will return False

Copy to clipboard

### [Re-export an imported object?](https://docs.pytorch.org/docs/2.15/package.html#id12)
[#](https://docs.pytorch.org/docs/2.15/package.html#re-export-an-imported-object "Link to this heading")

To re-export an object that was previously imported by a [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
, you must make the new [`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
 aware of the original [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 so that it can find source code for your object’s dependencies.

importer \= PackageImporter(f)
obj \= importer.load\_pickle("model", "model.pkl")

\# re-export obj in a new package
with PackageExporter(f2, importer\=(importer, sys\_importer)) as exporter:
    exporter.save\_pickle("model", "model.pkl", obj)

Copy to clipboard

[Explanation](https://docs.pytorch.org/docs/2.15/package.html#id13)
[#](https://docs.pytorch.org/docs/2.15/package.html#explanation "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

### [`torch.package` Format Overview](https://docs.pytorch.org/docs/2.15/package.html#id14)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch-package-format-overview "Link to this heading")

A `torch.package` file is a ZIP archive which conventionally uses the `.pt` extension. Inside the ZIP archive, there are two kinds of files:

*   Framework files, which are placed in the `.data/`.
    
*   User files, which is everything else.
    

As an example, this is what a fully packaged ResNet model from `torchvision` looks like:

resnet
├── .data  # All framework-specific data is stored here.
│   │      # It's named to avoid conflicts with user-serialized code.
│   ├── 94286146172688.storage  # tensor data
│   ├── 94286146172784.storage
│   ├── extern\_modules  # text file with names of extern modules (e.g. 'torch')
│   ├── version         # version metadata
│   ├── ...
├── model  # the pickled model
│   └── model.pkl
└── torchvision  # all code dependencies are captured as source files
    └── models
        ├── resnet.py
        └── utils.py

Copy to clipboard

#### Framework files[#](https://docs.pytorch.org/docs/2.15/package.html#framework-files "Link to this heading")

The `.data/` directory is owned by torch.package, and its contents are considered to be a private implementation detail. The `torch.package` format makes no guarantees about the contents of `.data/`, but any changes made will be backward compatible (that is, newer version of PyTorch will always be able to load older `torch.packages`).

Currently, the `.data/` directory contains the following items:

*   `version`: a version number for the serialized format, so that the `torch.package` import infrastructures knows how to load this package.
    
*   `extern_modules`: a list of modules that are considered `extern`. `extern` modules will be imported using the loading environment’s system importer.
    
*   `*.storage`: serialized tensor data.
    

.data
├── 94286146172688.storage
├── 94286146172784.storage
├── extern\_modules
├── version
├── ...

Copy to clipboard

#### User files[#](https://docs.pytorch.org/docs/2.15/package.html#user-files "Link to this heading")

All other files in the archive were put there by a user. The layout is identical to a Python [regular package](https://docs.python.org/3/reference/import.html#regular-packages)
. For a deeper dive in how Python packaging works, please consult [this essay](https://www.python.org/doc/essays/packages/)
 (it’s slightly out of date, so double-check implementation details with the [Python reference documentation](https://docs.python.org/3/library/importlib.html)
.

<package root>
├── model  # the pickled model
│   └── model.pkl
├── another\_package
│   ├── \_\_init\_\_.py
│   ├── foo.txt         # a resource file , see importlib.resources
│   └── ...
└── torchvision
    └── models
        ├── resnet.py   # torchvision.models.resnet
        └── utils.py    # torchvision.models.utils

Copy to clipboard

### [How `torch.package` finds your code’s dependencies](https://docs.pytorch.org/docs/2.15/package.html#id15)
[#](https://docs.pytorch.org/docs/2.15/package.html#how-torch-package-finds-your-code-s-dependencies "Link to this heading")

#### Analyzing an object’s dependencies[#](https://docs.pytorch.org/docs/2.15/package.html#analyzing-an-object-s-dependencies "Link to this heading")

When you issue a `save_pickle(obj, ...)` call, [`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
 will pickle the object normally. Then, it uses the `pickletools` standard library module to parse the pickle bytecode.

In a pickle, an object is saved along with a `GLOBAL` opcode that describes where to find the implementation of the object’s type, like:

GLOBAL 'torchvision.models.resnet Resnet\`

Copy to clipboard

The dependency resolver will gather up all `GLOBAL` ops and mark them as dependencies of your pickled object. For more information about pickling and the pickle format, please consult [the Python docs](https://docs.python.org/3/library/pickle.html)
.

#### Analyzing a module’s dependencies[#](https://docs.pytorch.org/docs/2.15/package.html#analyzing-a-module-s-dependencies "Link to this heading")

When a Python module is identified as a dependency, `torch.package` walks the module’s python AST representation and looks for import statements with full support for the standard forms: `from x import y`, `import z`, `from w import v as u`, etc. When one of these import statements are encountered, `torch.package` registers the imported modules as dependencies that are then themselves parsed in the same AST walking way.

**Note**: AST parsing has limited support for the `__import__(...)` syntax and does not support `importlib.import_module` calls. In general, you should not expect dynamic imports to be detected by `torch.package`.

### [Dependency Management](https://docs.pytorch.org/docs/2.15/package.html#id16)
[#](https://docs.pytorch.org/docs/2.15/package.html#dependency-management "Link to this heading")

`torch.package` automatically finds the Python modules that your code and objects depend on. This process is called dependency resolution. For each module that the dependency resolver finds, you must specify an _action_ to take.

The allowed actions are:

*   `intern`: put this module into the package.
    
*   `extern`: declare this module as an external dependency of the package.
    
*   `mock`: stub out this module.
    
*   `deny`: depending on this module will raise an error during package export.
    

Finally, there is one more important action that is not technically part of `torch.package`:

*   Refactoring: remove or change the dependencies in your code.
    

Note that actions are only defined on entire Python modules. There is no way to package “just” a function or class from a module and leave the rest out. This is by design. Python does not offer clean boundaries between objects defined in a module. The only defined unit of dependency organization is a module, so that’s what `torch.package` uses.

Actions are applied to modules using patterns. Patterns can either be module names (`"foo.bar"`) or globs (like `"foo.**"`). You associate a pattern with an action using methods on [`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
, e.g.

my\_exporter.intern("torchvision.\*\*")
my\_exporter.extern("numpy")

Copy to clipboard

If a module matches a pattern, the corresponding action is applied to it. For a given module, patterns will be checked in the order that they were defined, and the first action will be taken.

#### `intern`[#](https://docs.pytorch.org/docs/2.15/package.html#intern "Link to this heading")

If a module is `intern`\-ed, it will be placed into the package.

This action is your model code, or any related code you want to package. For example, if you are trying to package a ResNet from `torchvision`, you will need to `intern` the module torchvision.models.resnet.

On package import, when your packaged code tries to import an `intern`\-ed module, PackageImporter will look inside your package for that module. If it can’t find that module, an error will be raised. This ensures that each [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 is isolated from the loading environment—even if you have `my_interned_module` available in both your package and the loading environment, [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 will only use the version in your package.

**Note**: Only Python source modules can be `intern`\-ed. Other kinds of modules, like C extension modules and bytecode modules, will raise an error if you attempt to `intern` them. These kinds of modules need to be `mock`\-ed or `extern`\-ed.

#### `extern`[#](https://docs.pytorch.org/docs/2.15/package.html#extern "Link to this heading")

If a module is `extern`\-ed, it will not be packaged. Instead, it will be added to a list of external dependencies for this package. You can find this list on `package_exporter.extern_modules`.

On package import, when the packaged code tries to import an `extern`\-ed module, [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 will use the default Python importer to find that module, as if you did `importlib.import_module("my_externed_module")`. If it can’t find that module, an error will be raised.

In this way, you can depend on third-party libraries like `numpy` and `scipy` from within your package without having to package them too.

**Warning**: If any external library changes in a backwards-incompatible way, your package may fail to load. If you need long-term reproducibility for your package, try to limit your use of `extern`.

#### `mock`[#](https://docs.pytorch.org/docs/2.15/package.html#mock "Link to this heading")

If a module is `mock`\-ed, it will not be packaged. Instead a stub module will be packaged in its place. The stub module will allow you to retrieve objects from it (so that `from my_mocked_module import foo` will not error), but any use of that object will raise a `NotImplementedError`.

`mock` should be used for code that you “know” will not be needed in the loaded package, but you still want available for use in non-packaged contents. For example, initialization/configuration code, or code only used for debugging/training.

**Warning**: In general, `mock` should be used as a last resort. It introduces behavioral differences between packaged code and non-packaged code, which may lead to later confusion. Prefer instead to refactor your code to remove unwanted dependencies.

#### Refactoring[#](https://docs.pytorch.org/docs/2.15/package.html#refactoring "Link to this heading")

The best way to manage dependencies is to not have dependencies at all! Often, code can be refactored to remove unnecessary dependencies. Here are some guidelines for writing code with clean dependencies (which are also generally good practices!):

**Include only what you use**. Do not leave unused imports in your code. The dependency resolver is not smart enough to tell that they are indeed unused, and will try to process them.

**Qualify your imports**. For example, instead of writing import foo and later using `foo.bar.baz`, prefer to write `from foo.bar import baz`. This more precisely specifies your real dependency (`foo.bar`) and lets the dependency resolver know you don’t need all of `foo`.

**Split up large files with unrelated functionality into smaller ones**. If your `utils` module contains a hodge-podge of unrelated functionality, any module that depends on `utils` will need to pull in lots of unrelated dependencies, even if you only needed a small part of it. Prefer instead to define single-purpose modules that can be packaged independently of one another.

#### Patterns[#](https://docs.pytorch.org/docs/2.15/package.html#patterns "Link to this heading")

Patterns allow you to specify groups of modules with a convenient syntax. The syntax and behavior of patterns follows the Bazel/Buck [glob()](https://docs.bazel.build/versions/master/be/functions.html#glob)
.

A module that we are trying to match against a pattern is called a candidate. A candidate is composed of a list of segments separated by a separator string, e.g. `foo.bar.baz`.

A pattern contains one or more segments. Segments can be:

*   A literal string (e.g. `foo`), which matches exactly.
    
*   A string containing a wildcard (e.g. `torch`, or `foo*baz*`). The wildcard matches any string, including the empty string.
    
*   A double wildcard (`**`). This matches against zero or more complete segments.
    

Examples:

*   `torch.**`: matches `torch` and all its submodules, e.g. `torch.nn` and `torch.nn.functional`.
    
*   `torch.*`: matches `torch.nn` or `torch.functional`, but not `torch.nn.functional` or `torch`
    
*   `torch*.**`: matches `torch`, `torchvision`, and all of their submodules
    

When specifying actions, you can pass multiple patterns, e.g.

exporter.intern(\["torchvision.models.\*\*", "torchvision.utils.\*\*"\])

Copy to clipboard

A module will match against this action if it matches any of the patterns.

You can also specify patterns to exclude, e.g.

exporter.mock("\*\*", exclude\=\["torchvision.\*\*"\])

Copy to clipboard

A module will not match against this action if it matches any of the exclude patterns. In this example, we are mocking all modules except `torchvision` and its submodules.

When a module could potentially match against multiple actions, the first action defined will be taken.

### [`torch.package` sharp edges](https://docs.pytorch.org/docs/2.15/package.html#id17)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch-package-sharp-edges "Link to this heading")

#### Avoid global state in your modules[#](https://docs.pytorch.org/docs/2.15/package.html#avoid-global-state-in-your-modules "Link to this heading")

Python makes it really easy to bind objects and run code at module-level scope. This is generally fine—after all, functions and classes are bound to names this way. However, things become more complicated when you define an object at module scope with the intention of mutating it, introducing mutable global state.

Mutable global state is quite useful—it can reduce boilerplate, allow for open registration into tables, etc. But unless employed very carefully, it can cause complications when used with `torch.package`.

Every [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 creates an independent environment for its contents. This is nice because it means we load multiple packages and ensure they are isolated from each other, but when modules are written in a way that assumes shared mutable global state, this behavior can create hard-to-debug errors.

#### Types are not shared between packages and the loading environment[#](https://docs.pytorch.org/docs/2.15/package.html#types-are-not-shared-between-packages-and-the-loading-environment "Link to this heading")

Any class that you import from a [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 will be a version of the class specific to that importer. For example:

from foo import MyClass

my\_class\_instance \= MyClass()

with PackageExporter(f) as exporter:
    exporter.save\_module("foo")

importer \= PackageImporter(f)
imported\_MyClass \= importer.import\_module("foo").MyClass

assert isinstance(my\_class\_instance, MyClass)  \# works
assert isinstance(my\_class\_instance, imported\_MyClass)  \# ERROR!

Copy to clipboard

In this example, `MyClass` and `imported_MyClass` are _not the same type_. In this specific example, `MyClass` and `imported_MyClass` have exactly the same implementation, so you might think it’s okay to consider them the same class. But consider the situation where `imported_MyClass` is coming from an older package with an entirely different implementation of `MyClass` — in that case, it’s unsafe to consider them the same class.

Under the hood, each importer has a prefix that allows it to uniquely identify classes:

print(MyClass.\_\_name\_\_)  \# prints "foo.MyClass"
print(imported\_MyClass.\_\_name\_\_)  \# prints <torch\_package\_0>.foo.MyClass

Copy to clipboard

That means you should not expect `isinstance` checks to work when one of the arguments is from a package and the other is not. If you need this functionality, consider the following options:

*   Doing duck typing (just using the class instead of explicitly checking that it is of a given type).
    
*   Make the typing relationship an explicit part of the class contract. For example, you can add an attribute tag `self.handler = "handle_me_this_way"` and have client code check for the value of `handler` instead of checking the type directly.
    

### [How `torch.package` keeps packages isolated from each other](https://docs.pytorch.org/docs/2.15/package.html#id18)
[#](https://docs.pytorch.org/docs/2.15/package.html#how-torch-package-keeps-packages-isolated-from-each-other "Link to this heading")

Each [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 instance creates an independent, isolated environment for its modules and objects. Modules in a package can only import other packaged modules, or modules marked `extern`. If you use multiple [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 instances to load a single package, you will get multiple independent environments that do not interact.

This is achieved by extending Python’s import infrastructure with a custom importer. [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 provides the same core API as the `importlib` importer; namely, it implements the `import_module` and `__import__` methods.

When you invoke [`PackageImporter.import_module()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.import_module "torch.package.PackageImporter.import_module")
, [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 will construct and return a new module, much as the system importer does. However, [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 patches the returned module to use `self` (i.e. that [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 instance) to fulfill future import requests by looking in the package rather than searching the user’s Python environment.

#### Mangling[#](https://docs.pytorch.org/docs/2.15/package.html#mangling "Link to this heading")

To avoid confusion (“is this `foo.bar` object the one from my package, or the one from my Python environment?”), [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 mangles the `__name__` and `__file__` of all imported modules, by adding a _mangle prefix_ to them.

For `__name__`, a name like `torchvision.models.resnet18` becomes `<torch_package_0>.torchvision.models.resnet18`.

For `__file__`, a name like `torchvision/models/resnet18.py` becomes `<torch_package_0>.torchvision/modules/resnet18.py`.

Name mangling helps avoid inadvertent punning of module names between different packages, and helps you debug by making stack traces and print statements more clearly show whether they are referring to packaged code or not. For developer-facing details about mangling, consult `mangling.md` in `torch/package/`.

[API Reference](https://docs.pytorch.org/docs/2.15/package.html#id19)
[#](https://docs.pytorch.org/docs/2.15/package.html#api-reference "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ torch.package.PackagingError(_dependency\_graph_, _debug\=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L118)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackagingError "Link to this definition")

This exception is raised when there is an issue with exporting a package. `PackageExporter` will attempt to gather up all the errors and present them to you at once.

_class_ torch.package.EmptyMatchError[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L112)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.EmptyMatchError "Link to this definition")

This is an exception that is thrown when a mock or extern is marked as `allow_empty=False`, and is not matched with any module during packaging.

_class_ torch.package.PackageExporter(_f_, _importer=<torch.package.importer.\_SysImporter object>_, _debug=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L175)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "Link to this definition")

Exporters allow you to write packages of code, pickled Python data, and arbitrary binary and text resources into a self-contained package.

Imports can load this code in a hermetic way, such that code is loaded from the package rather than the normal Python import system. This allows for the packaging of PyTorch model code and data so that it can be run on a server or used in the future for transfer learning.

The code contained in packages is copied file-by-file from the original source when it is created, and the file format is a specially organized zip file. Future users of the package can unzip the package, and edit the code in order to perform custom modifications to it.

The importer for packages ensures that code in the module can only be loaded from within the package, except for modules explicitly listed as external using [`extern()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.extern "torch.package.PackageExporter.extern")
. The file `extern_modules` in the zip archive lists all the modules that a package externally depends on. This prevents “implicit” dependencies where the package runs locally because it is importing a locally-installed package, but then fails when the package is copied to another machine.

When source code is added to the package, the exporter can optionally scan it for further code dependencies (`dependencies=True`). It looks for import statements, resolves relative references to qualified module names, and performs an action specified by the user (See: [`extern()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.extern "torch.package.PackageExporter.extern")
, [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
, and [`intern()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.intern "torch.package.PackageExporter.intern")
).

\_\_init\_\_(_f_, _importer=<torch.package.importer.\_SysImporter object>_, _debug=False_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L206)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.__init__ "Link to this definition")

Create an exporter.

Parameters:

*   **f** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_IO_](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.15)")
    _\[_[_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
    _\]_) – The location to export to. Can be a `string`/`Path` object containing a filename or a binary I/O object.
    
*   **importer** (_Importer_ _|_ [_Sequence_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.15)")
    _\[__Importer__\]_) – If a single Importer is passed, use that to search for modules. If a sequence of importers are passed, an `OrderedImporter` will be constructed out of them.
    
*   **debug** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – If set to True, add path of broken modules to PackagingErrors.
    

add\_dependency(_module\_name_, _dependencies\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L455)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.add_dependency "Link to this definition")

Given a module, add it to the dependency graph according to patterns specified by the user.

all\_paths(_src_, _dst_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1186)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.all_paths "Link to this definition")

Return a dot representation of the subgraph

that has all paths from src to dst.

Returns:

A dot representation containing all paths from src to dst. ([https://graphviz.org/doc/info/lang.html](https://graphviz.org/doc/info/lang.html)
)

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

close()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1089)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.close "Link to this definition")

Write the package to the filesystem. Any calls after [`close()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.close "torch.package.PackageExporter.close")
 are now invalid. It is preferable to use resource guard syntax instead:

with PackageExporter("file.zip") as e:
    ...

Copy to clipboard

denied\_modules()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1166)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.denied_modules "Link to this definition")

Return all modules that are currently denied.

Returns:

A list containing the names of modules which will be denied in this package.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

deny(_include_, _\*_, _exclude\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L912)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.deny "Link to this definition")

Blocklist modules whose names match the given glob patterns from the list of modules the package can import. If a dependency on any matching packages is found, a [`PackagingError`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackagingError "torch.package.PackagingError")
 is raised.

Parameters:

*   **include** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A string e.g. `"my_package.my_subpackage"`, or list of strings for the names of the modules to be externed. This can also be a glob-style pattern, as described in [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
    .
    
*   **exclude** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional pattern that excludes some patterns that match the include string.
    

dependency\_graph\_string()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1120)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.dependency_graph_string "Link to this definition")

Returns digraph string representation of dependencies in package.

Returns:

A string representation of dependencies in package.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

extern(_include_, _\*_, _exclude\=()_, _allow\_empty\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L881)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.extern "Link to this definition")

Include `module` in the list of external modules the package can import. This will prevent dependency discovery from saving it in the package. The importer will load an external module directly from the standard import system. Code for extern modules must also exist in the process loading the package.

Parameters:

*   **include** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A string e.g. `"my_package.my_subpackage"`, or list of strings for the names of the modules to be externed. This can also be a glob-style pattern, as described in [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
    .
    
*   **exclude** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional pattern that excludes some patterns that match the include string.
    
*   **allow\_empty** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – An optional flag that specifies whether the extern modules specified by this call to the `extern` method must be matched to some module during packaging. If an extern module glob pattern is added with `allow_empty=False`, and [`close()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.close "torch.package.PackageExporter.close")
     is called (either explicitly or via `__exit__`) before any modules match that pattern, an exception is thrown. If `allow_empty=True`, no such exception is thrown.
    

externed\_modules()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1139)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.externed_modules "Link to this definition")

Return all modules that are currently externed.

Returns:

A list containing the names of modules which will be externed in this package.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

get\_rdeps(_module\_name_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1175)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.get_rdeps "Link to this definition")

Return a list of all modules which depend on the module `module_name`.

Returns:

A list containing the names of modules which depend on `module_name`.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

get\_unique\_id()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L319)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.get_unique_id "Link to this definition")

Get an id. This id is guaranteed to only be handed out once for this package.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

intern(_include_, _\*_, _exclude\=()_, _allow\_empty\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L814)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.intern "Link to this definition")

Specify modules that should be packaged. A module must match some `intern` pattern in order to be included in the package and have its dependencies processed recursively.

Parameters:

*   **include** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A string e.g. “my\_package.my\_subpackage”, or list of strings for the names of the modules to be externed. This can also be a glob-style pattern, as described in [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
    .
    
*   **exclude** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional pattern that excludes some patterns that match the include string.
    
*   **allow\_empty** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – An optional flag that specifies whether the intern modules specified by this call to the `intern` method must be matched to some module during packaging. If an `intern` module glob pattern is added with `allow_empty=False`, and [`close()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.close "torch.package.PackageExporter.close")
     is called (either explicitly or via `__exit__`) before any modules match that pattern, an exception is thrown. If `allow_empty=True`, no such exception is thrown.
    

interned\_modules()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1148)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.interned_modules "Link to this definition")

Return all modules that are currently interned.

Returns:

A list containing the names of modules which will be interned in this package.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

mock(_include_, _\*_, _exclude\=()_, _allow\_empty\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L840)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "Link to this definition")

Replace some required modules with a mock implementation. Mocked modules will return a fake object for any attribute accessed from it. Because we copy file-by-file, the dependency resolution will sometimes find files that are imported by model files but whose functionality is never used (e.g. custom serialization code or training helpers). Use this function to mock this functionality out without having to modify the original code.

Parameters:

*   **include** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) –
    
    A string e.g. `"my_package.my_subpackage"`, or list of strings for the names of the modules to be mocked out. Strings can also be a glob-style pattern string that may match multiple modules. Any required dependencies that match this pattern string will be mocked out automatically.
    
    Examples :
    
    `'torch.**'` – matches `torch` and all submodules of torch, e.g. `'torch.nn'` and `'torch.nn.functional'`
    
    `'torch.*'` – matches `'torch.nn'` or `'torch.functional'`, but not `'torch.nn.functional'`
    
*   **exclude** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional pattern that excludes some patterns that match the include string. e.g. `include='torch.**', exclude='torch.foo'` will mock all torch packages except `'torch.foo'`, Default: is `[]`.
    
*   **allow\_empty** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    ) – An optional flag that specifies whether the mock implementation(s) specified by this call to the [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
     method must be matched to some module during packaging. If a mock is added with `allow_empty=False`, and [`close()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.close "torch.package.PackageExporter.close")
     is called (either explicitly or via `__exit__`) and the mock has not been matched to a module used by the package being exported, an exception is thrown. If `allow_empty=True`, no such exception is thrown.
    

mocked\_modules()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L1157)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mocked_modules "Link to this definition")

Return all modules that are currently mocked.

Returns:

A list containing the names of modules which will be mocked in this package.

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

register\_extern\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L757)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.register_extern_hook "Link to this definition")

Registers an extern hook on the exporter.

The hook will be called each time a module matches against an [`extern()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.extern "torch.package.PackageExporter.extern")
 pattern. It should have the following signature:

hook(exporter: PackageExporter, module\_name: str) \-> None

Copy to clipboard

Hooks will be called in order of registration.

Returns:

A handle that can be used to remove the added hook by calling `handle.remove()`.

Return type:

`torch.utils.hooks.RemovableHandle`

register\_intern\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L795)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.register_intern_hook "Link to this definition")

Registers an intern hook on the exporter.

The hook will be called each time a module matches against an [`intern()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.intern "torch.package.PackageExporter.intern")
 pattern. It should have the following signature:

hook(exporter: PackageExporter, module\_name: str) \-> None

Copy to clipboard

Hooks will be called in order of registration.

Returns:

A handle that can be used to remove the added hook by calling `handle.remove()`.

Return type:

`torch.utils.hooks.RemovableHandle`

register\_mock\_hook(_hook_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L776)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.register_mock_hook "Link to this definition")

Registers a mock hook on the exporter.

The hook will be called each time a module matches against a [`mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
 pattern. It should have the following signature:

hook(exporter: PackageExporter, module\_name: str) \-> None

Copy to clipboard

Hooks will be called in order of registration.

Returns:

A handle that can be used to remove the added hook by calling `handle.remove()`.

Return type:

`torch.utils.hooks.RemovableHandle`

save\_binary(_package_, _resource_, _binary_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L746)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_binary "Link to this definition")

Save raw bytes to the package.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package this resource should go in (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A unique name for the resource, used to identify it to load.
    
*   **binary** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The data to save.
    

save\_module(_module\_name_, _dependencies\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L514)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_module "Link to this definition")

Save the code for `module` into the package. Code for the module is resolved using the `importers` path to find the module object, and then using its `__file__` attribute to find the source code.

Parameters:

*   **module\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
    
*   **dependencies** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, we scan the source for dependencies.
    

save\_pickle(_package_, _resource_, _obj_, _dependencies\=True_, _pickle\_protocol\=3_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L586)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_pickle "Link to this definition")

Save a python object to the archive using pickle. Equivalent to [`torch.save()`](https://docs.pytorch.org/docs/2.15/generated/torch.save.html#torch.save "torch.save")
 but saving into the archive rather than a stand-alone file. Standard pickle does not save the code, only the objects. If `dependencies` is true, this method will also scan the pickled objects for which modules are required to reconstruct them and save the relevant code.

To be able to save an object where `type(obj).__name__` is `my_module.MyObject`, `my_module.MyObject` must resolve to the class of the object according to the `importer` order. When saving objects that have previously been packaged, the importer’s `import_module` method will need to be present in the `importer` list for this to work.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package this resource should go in (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A unique name for the resource, used to identify it to load.
    
*   **obj** (_Any_) – The object to save, must be picklable.
    
*   **dependencies** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, we scan the source for dependencies.
    

save\_source\_file(_module\_name_, _file\_or\_directory_, _dependencies\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L265)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_source_file "Link to this definition")

Adds the local file system `file_or_directory` to the source package to provide the code for `module_name`.

Parameters:

*   **module\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – e.g. `"my_package.my_subpackage"`, code will be saved to provide code for this package.
    
*   **file\_or\_directory** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – the path to a file or directory of code. When a directory, all python files in the directory are recursively copied using [`save_source_file()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_source_file "torch.package.PackageExporter.save_source_file")
    . If a file is named `"/__init__.py"` the code is treated as a package.
    
*   **dependencies** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, we scan the source for dependencies.
    

save\_source\_string(_module\_name_, _src_, _is\_package\=False_, _dependencies\=True_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L374)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_source_string "Link to this definition")

Adds `src` as the source code for `module_name` in the exported package.

Parameters:

*   **module\_name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – e.g. `my_package.my_subpackage`, code will be saved to provide code for this package.
    
*   **src** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The Python source code to save for this package.
    
*   **is\_package** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, this module is treated as a package. Packages are allowed to have submodules (e.g. `my_package.my_subpackage.my_subsubpackage`), and resources can be saved inside them. Defaults to `False`.
    
*   **dependencies** ([_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")
    _,_ _optional_) – If `True`, we scan the source for dependencies.
    

save\_text(_package_, _resource_, _text_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_exporter.py#L736)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.save_text "Link to this definition")

Save text data to the package.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package this resource should go in (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – A unique name for the resource, used to identify it to load.
    
*   **text** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The contents to save.
    

_class_ torch.package.PackageImporter(_file\_or\_buffer_, _module\_allowed=<function PackageImporter.<lambda>>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L66)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "Link to this definition")

Importers allow you to load code written to packages by [`PackageExporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter "torch.package.PackageExporter")
. Code is loaded in a hermetic way, using files from the package rather than the normal python import system. This allows for the packaging of PyTorch model code and data so that it can be run on a server or used in the future for transfer learning.

The importer for packages ensures that code in the module can only be loaded from within the package, except for modules explicitly listed as external during export. The file `extern_modules` in the zip archive lists all the modules that a package externally depends on. This prevents “implicit” dependencies where the package runs locally because it is importing a locally-installed package, but then fails when the package is copied to another machine.

\_\_init\_\_(_file\_or\_buffer_, _module\_allowed=<function PackageImporter.<lambda>>_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L86)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.__init__ "Link to this definition")

Open `file_or_buffer` for importing. This checks that the imported package only requires modules allowed by `module_allowed`

Parameters:

*   **file\_or\_buffer** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
     _|_ [_PathLike_](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_IO_](https://docs.python.org/3/library/typing.html#typing.IO "(in Python v3.15)")
    _\[_[_bytes_](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")\
    _\]_ _|_ _PyTorchFileReader_) – a file-like object (has to implement `read()`, `readline()`, `tell()`, and `seek()`), a string, or an `os.PathLike` object containing a filename.
    
*   **module\_allowed** (_Callable__\[__\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]__,_ [_bool_](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")\
    _\]__,_ _optional_) – A method to determine if a externally provided module should be allowed. Can be used to ensure packages loaded do not depend on modules that the server does not support. Defaults to allowing anything.
    

Raises:

[**ImportError**](https://docs.python.org/3/builtins/exceptions.html#ImportError "(in Python v3.15)")
 – If the package will use a disallowed module.

file\_structure(_\*_, _include\='\*\*'_, _exclude\=()_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L326)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.file_structure "Link to this definition")

Returns a file structure representation of package’s zipfile.

Parameters:

*   **include** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional string e.g. `"my_package.my_subpackage"`, or optional list of strings for the names of the files to be included in the zipfile representation. This can also be a glob-style pattern, as described in [`PackageExporter.mock()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageExporter.mock "torch.package.PackageExporter.mock")
    
*   **exclude** ([_list_](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
    _\[_[_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
    _\]_ _|_ [_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – An optional pattern that excludes files whose name match the pattern.
    

Returns:

[`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")

Return type:

[_Directory_](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.file_structure_representation.Directory")

id()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L317)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.id "Link to this definition")

Returns internal identifier that torch.package uses to distinguish [`PackageImporter`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter "torch.package.PackageImporter")
 instances. Looks like:

<torch\_package\_0\>

Copy to clipboard

import\_module(_name_, _package\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L158)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.import_module "Link to this definition")

Load a module from the package if it hasn’t already been loaded, and then return the module. Modules are loaded locally to the importer and will appear in `self.modules` rather than `sys.modules`.

Parameters:

*   **name** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – Fully qualified name of the module to load.
    
*   **package** (_\[_[_type_](https://docs.python.org/3/builtins/functions.html#type "(in Python v3.15)")\
    _\]__,_ _optional_) – Unused, but present to match the signature of importlib.import\_module. Defaults to `None`.
    

Returns:

The (possibly already) loaded module.

Return type:

[types.ModuleType](https://docs.python.org/3/library/types.html#types.ModuleType "(in Python v3.15)")

load\_binary(_package_, _resource_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L181)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.load_binary "Link to this definition")

Load raw bytes.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The unique name for the resource.
    

Returns:

The loaded data.

Return type:

[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes "(in Python v3.15)")

load\_pickle(_package_, _resource_, _map\_location\=None_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L216)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.load_pickle "Link to this definition")

Unpickles the resource from the package, loading any modules that are needed to construct the objects using [`import_module()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.import_module "torch.package.PackageImporter.import_module")
.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The unique name for the resource.
    
*   **map\_location** – Passed to torch.load to determine how tensors are mapped to devices. Defaults to `None`.
    

Returns:

The unpickled object.

Return type:

Any

load\_text(_package_, _resource_, _encoding\='utf-8'_, _errors\='strict'_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L195)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.load_text "Link to this definition")

Load a string.

Parameters:

*   **package** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The name of module package (e.g. `"my_package.my_subpackage"`).
    
*   **resource** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    ) – The unique name for the resource.
    
*   **encoding** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Passed to `decode`. Defaults to `'utf-8'`.
    
*   **errors** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
    _,_ _optional_) – Passed to `decode`. Defaults to `'strict'`.
    

Returns:

The loaded text.

Return type:

[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")

python\_version()[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/package_importer.py#L345)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.python_version "Link to this definition")

Returns the version of python that was used to create this package.

Note: this function is experimental and not Forward Compatible. The plan is to move this into a lock file later on.

Returns:

`str | None` a python version e.g. 3.8.9 or None if no version was stored with this package

_class_ torch.package.Directory(_name_, _is\_dir_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/file_structure_representation.py#L9)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "Link to this definition")

A file structure representation. Organized as Directory nodes that have lists of their Directory children. Directories for a package are created by calling [`PackageImporter.file_structure()`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackageImporter.file_structure "torch.package.PackageImporter.file_structure")
.

has\_file(_filename_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/file_structure_representation.py#L47)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory.has_file "Link to this definition")

Checks if a file is present in a [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
.

Parameters:

**filename** ([_str_](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")
) – Path of file to search for.

Returns:

If a [`Directory`](https://docs.pytorch.org/docs/2.15/package.html#torch.package.Directory "torch.package.Directory")
 contains the specified file.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

[Analysis Utilities](https://docs.pytorch.org/docs/2.15/package.html#id20)
[#](https://docs.pytorch.org/docs/2.15/package.html#module-torch.package.analyze.find_first_use_of_broken_modules "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

torch.package.analyze.find\_first\_use\_of\_broken\_modules.find\_first\_use\_of\_broken\_modules(_exc_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/analyze/find_first_use_of_broken_modules.py#L7)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.analyze.find_first_use_of_broken_modules.find_first_use_of_broken_modules "Link to this definition")

Find all broken modules in a PackagingError, and for each one, return the dependency path in which the module was first encountered.

E.g. broken module m.n.o was added to a dependency graph while processing a.b.c, then re-encountered while processing d.e.f. This method would return {‘m.n.o’: \[‘a’, ‘b’, ‘c’\]}

Parameters:

**exc** ([_PackagingError_](https://docs.pytorch.org/docs/2.15/package.html#torch.package.PackagingError "torch.package.package_exporter.PackagingError")
) – a PackagingError

Return type:

[dict](https://docs.python.org/3/builtins/stdtypes.html#dict "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
, [list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")\
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]\]

Returns: A dict from broken module names to lists of module names in the path.

torch.package.analyze.is\_from\_package.is\_from\_package(_obj_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/analyze/is_from_package.py#L7)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.analyze.is_from_package.is_from_package "Link to this definition")

Return whether an object was loaded from a package.

Note: packaged objects from externed modules will return `False`.

Return type:

[bool](https://docs.python.org/3/builtins/functions.html#bool "(in Python v3.15)")

torch.package.analyze.trace\_dependencies.trace\_dependencies(_callable_, _inputs_)[\[source\]](https://github.com/pytorch/pytorch/blob/v2.15.0/torch/package/analyze/trace_dependencies.py#L10)
[#](https://docs.pytorch.org/docs/2.15/package.html#torch.package.analyze.trace_dependencies.trace_dependencies "Link to this definition")

Trace the execution of a callable in order to determine which modules it uses.

Parameters:

*   **callable** ([_Callable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.15)")
    _\[__\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]__,_ [_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _\]_) – The callable to execute and trace.
    
*   **inputs** ([_Iterable_](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.15)")
    _\[_[_tuple_](https://docs.python.org/3/builtins/stdtypes.html#tuple "(in Python v3.15)")\
    _\[_[_Any_](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.15)")\
    _,_ _...__\]__\]_) – The input to use during tracing. The modules used by ‘callable’ when invoked by each set of inputs are union-ed to determine all modules used by the callable for the purposes of packaging.
    

Return type:

[list](https://docs.python.org/3/builtins/stdtypes.html#list "(in Python v3.15)")
\[[str](https://docs.python.org/3/builtins/stdtypes.html#str "(in Python v3.15)")\
\]

Returns: A list of the names of all modules used during callable execution.

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/package.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/package.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |