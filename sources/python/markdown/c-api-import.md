### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/marshal.html "Data marshalling support")
     |
*   [previous](https://docs.python.org/3/c-api/sys.html "Operating System Utilities")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Importing Modules](https://docs.python.org/3/c-api/import.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Importing Modules[¶](https://docs.python.org/3/c-api/import.html#importing-modules "Link to this heading")

===========================================================================================================

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModule(const char \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a wrapper around [`PyImport_Import()`](https://docs.python.org/3/c-api/import.html#c.PyImport_Import "PyImport_Import")
 which takes a const char\* as an argument instead of a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
\*.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModuleEx(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*fromlist)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleEx "Link to this definition")
  

_Return value: New reference._

Import a module. This is best described by referring to the built-in Python function [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
.

The return value is a new reference to the imported module or top-level package, or `NULL` with an exception set on failure. Like for [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
, the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty _fromlist_ was given.

Failing imports remove incomplete module objects, like with [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModuleLevelObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*fromlist, int level)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevelObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Import a module. This is best described by referring to the built-in Python function [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
, as the standard `__import__()` function calls this function directly.

The return value is a new reference to the imported module or top-level package, or `NULL` with an exception set on failure. Like for [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
, the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty _fromlist_ was given.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModuleLevel(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*fromlist, int level)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevel "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyImport_ImportModuleLevelObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleLevelObject "PyImport_ImportModuleLevelObject")
, but the name is a UTF-8 encoded string instead of a Unicode object.

Changed in version 3.3: Negative values for _level_ are no longer accepted.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_Import([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_Import "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a higher-level interface that calls the current “import hook function” (with an explicit _level_ of 0, meaning absolute import). It invokes the [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
 function from the `__builtins__` of the current globals. This means that the import is done using whatever import hooks are installed in the current environment.

This function always uses absolute imports.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ReloadModule([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*m)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ReloadModule "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Reload a module. Return a new reference to the reloaded module, or `NULL` with an exception set on failure (the module still exists in this case).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_AddModuleRef(const char \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.13._

Return the module object corresponding to a module name.

The _name_ argument may be of the form `package.module`. First check the modules dictionary if there’s one there, and if not, create a new one and insert it in the modules dictionary.

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the module on success. Return `NULL` with an exception set on failure.

The module name _name_ is decoded from UTF-8.

This function does not load or import the module; if the module wasn’t already loaded, you will get an empty module object. Use [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
 or one of its variants to import a module. Package structures implied by a dotted name for _name_ are not created if not already present.

Added in version 3.13.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_AddModuleObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleObject "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Similar to [`PyImport_AddModuleRef()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef")
, but return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
 and _name_ is a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object.

Added in version 3.3.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_AddModule(const char \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModule "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyImport_AddModuleRef()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AddModuleRef "PyImport_AddModuleRef")
, but return a [borrowed reference](https://docs.python.org/3/glossary.html#term-borrowed-reference)
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ExecCodeModule(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModule "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Given a module name (possibly of the form `package.module`) and a code object read from a Python bytecode file or obtained from the built-in function [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
, load the module. Return a new reference to the module object, or `NULL` with an exception set if an error occurred. _name_ is removed from [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
 in error cases, even if _name_ was already in `sys.modules` on entry to [`PyImport_ExecCodeModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModule "PyImport_ExecCodeModule")
. Leaving incompletely initialized modules in `sys.modules` is dangerous, as imports of such modules have no way to know that the module object is an unknown (and probably damaged with respect to the module author’s intents) state.

The module’s [`__spec__`](https://docs.python.org/3/reference/datamodel.html#module.__spec__ "module.__spec__")
 and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
 will be set, if not set already, with the appropriate values. The spec’s loader will be set to the module’s `__loader__` (if set) and to an instance of [`SourceFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader "importlib.machinery.SourceFileLoader")
 otherwise.

The module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
 attribute will be set to the code object’s [`co_filename`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_filename "codeobject.co_filename")
.

This function will reload the module if it was already imported. See [`PyImport_ReloadModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ReloadModule "PyImport_ReloadModule")
 for the intended way to reload a module.

If _name_ points to a dotted name of the form `package.module`, any package structures not already created will still not be created.

See also [`PyImport_ExecCodeModuleEx()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleEx "PyImport_ExecCodeModuleEx")
 and [`PyImport_ExecCodeModuleWithPathnames()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleWithPathnames "PyImport_ExecCodeModuleWithPathnames")
.

Changed in version 3.12: The setting of `__cached__` and [`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")
 is deprecated. See [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 for alternatives.

Changed in version 3.15: The `__cached__` attribute is no longer set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ExecCodeModuleEx(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, const char \*pathname)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleEx "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Like [`PyImport_ExecCodeModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModule "PyImport_ExecCodeModule")
, but the [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")
 attribute of the module object is set to _pathname_ if it is non-`NULL`.

See also [`PyImport_ExecCodeModuleWithPathnames()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleWithPathnames "PyImport_ExecCodeModuleWithPathnames")
.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ExecCodeModuleObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*pathname, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*cpathname)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleObject "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Like [`PyImport_ExecCodeModuleEx()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleEx "PyImport_ExecCodeModuleEx")
, but the path to any compiled file via _cpathname_ is used appropriately when non-`NULL`. Of the three functions, this is the preferred one to use.

Added in version 3.3.

Changed in version 3.12: Setting `__cached__` is deprecated. See [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 for alternatives.

Changed in version 3.15: The `__cached__` attribute no longer set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ExecCodeModuleWithPathnames(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, const char \*pathname, const char \*cpathname)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleWithPathnames "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Like [`PyImport_ExecCodeModuleObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExecCodeModuleObject "PyImport_ExecCodeModuleObject")
, but _name_, _pathname_ and _cpathname_ are UTF-8 encoded strings. Attempts are also made to figure out what the value for _pathname_ should be from _cpathname_ if the former is set to `NULL`.

Added in version 3.2.

Changed in version 3.3: Uses `imp.source_from_cache()` in calculating the source path if only the bytecode path is provided.

Changed in version 3.12: No longer uses the removed `imp` module.

long PyImport\_GetMagicNumber()[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetMagicNumber "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the magic number for Python bytecode files (a.k.a. `.pyc` file). The magic number should be present in the first four bytes of the bytecode file, in little-endian byte order. Returns `-1` on error.

Changed in version 3.3: Return value of `-1` upon failure.

const char \*PyImport\_GetMagicTag()[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetMagicTag "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the magic tag string for [**PEP 3147**](https://peps.python.org/pep-3147/)
 format Python bytecode file names. Keep in mind that the value at `sys.implementation.cache_tag` is authoritative and should be used instead of this function.

Added in version 3.2.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_GetModuleDict()[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetModuleDict "Link to this definition")
  

_Return value: Borrowed reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return the dictionary used for the module administration (a.k.a. `sys.modules`). Note that this is a per-interpreter variable.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_GetModule([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetModule "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.8._

Return the already imported module with the given name. If the module has not been imported yet then returns `NULL` but does not set an error. Returns `NULL` and sets an error if the lookup failed.

Added in version 3.7.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_GetImporter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*path)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetImporter "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Return a finder object for a [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
/`pkg.__path__` item _path_, possibly by fetching it from the [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache")
 dict. If it wasn’t yet cached, traverse [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks")
 until a hook is found that can handle the path item. Return `None` if no hook could; this tells our caller that the [path based finder](https://docs.python.org/3/glossary.html#term-path-based-finder)
 could not find a finder for this path item. Cache the result in `sys.path_importer_cache`. Return a new reference to the finder object.

int PyImport\_ImportFrozenModuleObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportFrozenModuleObject "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
 since version 3.7._

Load a frozen module named _name_. Return `1` for success, `0` if the module is not found, and `-1` with an exception set if the initialization failed. To access the imported module on a successful load, use [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule")
. (Note the misnomer — this function would reload the module if it was already imported.)

Added in version 3.3.

Changed in version 3.4: The `__file__` attribute is no longer set on the module.

int PyImport\_ImportFrozenModule(const char \*name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportFrozenModule "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Similar to [`PyImport_ImportFrozenModuleObject()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportFrozenModuleObject "PyImport_ImportFrozenModuleObject")
, but the name is a UTF-8 encoded string instead of a Unicode object.

struct \_frozen[¶](https://docs.python.org/3/c-api/import.html#c._frozen "Link to this definition")
  

This is the structure type definition for frozen module descriptors, as generated by the **freeze** utility (see `Tools/freeze/` in the Python source distribution). Its definition, found in `Include/import.h`, is:

struct \_frozen {
    const char \*name;                 /\* ASCII encoded string \*/
    const unsigned char \*code;
    int size;
    int is\_package;
};

Changed in version 3.11: The new `is_package` field indicates whether the module is a package or not. This replaces setting the `size` field to a negative value.

const struct [\_frozen](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen")
 \*PyImport\_FrozenModules[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_FrozenModules "Link to this definition")
  

This pointer is initialized to point to an array of [`_frozen`](https://docs.python.org/3/c-api/import.html#c._frozen "_frozen")
 records, terminated by one whose members are all `NULL` or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.

int PyImport\_AppendInittab(const char \*name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*initfunc)(void))[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Add a single module to the existing table of built-in modules. This is a convenience wrapper around [`PyImport_ExtendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "PyImport_ExtendInittab")
, returning `-1` if the table could not be extended. The new module can be imported by the name _name_, and uses the function _initfunc_ as the initialization function called on the first attempted import. This should be called before [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
.

struct \_inittab[¶](https://docs.python.org/3/c-api/import.html#c._inittab "Link to this definition")
  

Structure describing a single entry in the list of built-in modules. Programs which embed Python may use an array of these structures in conjunction with [`PyImport_ExtendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "PyImport_ExtendInittab")
 to provide additional built-in modules. The structure consists of two members:

const char \*name[¶](https://docs.python.org/3/c-api/import.html#c._inittab.name "Link to this definition")
  

The module name, as an ASCII encoded string.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*initfunc)(void)[¶](https://docs.python.org/3/c-api/import.html#c._inittab.initfunc "Link to this definition")
  

Initialization function for a module built into the interpreter.

Note that the inittab uses “`PyInit`” [initialization functions](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
; there is currently no way to include “`PyModExport_`” [export hooks](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
.

int PyImport\_ExtendInittab(struct [\_inittab](https://docs.python.org/3/c-api/import.html#c._inittab "_inittab")
 \*newtab)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "Link to this definition")
  

Add a collection of modules to the table of built-in modules. The _newtab_ array must end with a sentinel entry which contains `NULL` for the [`name`](https://docs.python.org/3/c-api/import.html#c._inittab.name "_inittab.name")
 field; failure to provide the sentinel value can result in a memory fault. Returns `0` on success or `-1` if insufficient memory could be allocated to extend the internal table. In the event of failure, no modules are added to the internal table. This must be called before [`Py_Initialize()`](https://docs.python.org/3/c-api/interp-lifecycle.html#c.Py_Initialize "Py_Initialize")
.

If Python is initialized multiple times, [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
 or [`PyImport_ExtendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "PyImport_ExtendInittab")
 must be called before each Python initialization.

struct [\_inittab](https://docs.python.org/3/c-api/import.html#c._inittab "_inittab")
 \*PyImport\_Inittab[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_Inittab "Link to this definition")
  

The table of built-in modules used by Python initialization. Do not use this directly; use [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
 and [`PyImport_ExtendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ExtendInittab "PyImport_ExtendInittab")
 instead.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModuleAttr([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*mod\_name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*attr\_name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleAttr "Link to this definition")
  

_Return value: New reference._

Import the module _mod\_name_ and get its attribute _attr\_name_.

Names must be Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 objects.

Helper function combining [`PyImport_Import()`](https://docs.python.org/3/c-api/import.html#c.PyImport_Import "PyImport_Import")
 and [`PyObject_GetAttr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetAttr "PyObject_GetAttr")
. For example, it can raise [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError "ImportError")
 if the module is not found, and [`AttributeError`](https://docs.python.org/3/builtins/exceptions.html#AttributeError "AttributeError")
 if the attribute doesn’t exist.

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_ImportModuleAttrString(const char \*mod\_name, const char \*attr\_name)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleAttrString "Link to this definition")
  

_Return value: New reference._

Similar to [`PyImport_ImportModuleAttr()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModuleAttr "PyImport_ImportModuleAttr")
, but names are UTF-8 encoded strings instead of Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 objects.

Added in version 3.14.

[PyImport\_LazyImportsMode](https://docs.python.org/3/c-api/import.html#c.PyImport_LazyImportsMode "PyImport_LazyImportsMode")
 PyImport\_GetLazyImportsMode()[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetLazyImportsMode "Link to this definition")
  

Gets the current lazy imports mode.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_GetLazyImportsFilter()[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_GetLazyImportsFilter "Link to this definition")
  

Return a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference)
 to the current lazy imports filter, or `NULL` if none exists. This function always succeeds.

Added in version 3.15.

int PyImport\_SetLazyImportsMode([PyImport\_LazyImportsMode](https://docs.python.org/3/c-api/import.html#c.PyImport_LazyImportsMode "PyImport_LazyImportsMode")
 mode)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_SetLazyImportsMode "Link to this definition")
  

Sets the current lazy imports mode.

This function always returns `0`.

Added in version 3.15.

int PyImport\_SetLazyImportsFilter([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filter)[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_SetLazyImportsFilter "Link to this definition")
  

Sets the current lazy imports filter. The _filter_ should be a callable that will receive `(importing_module_name, imported_module_name, [fromlist])` when an import can potentially be lazy. The `imported_module_name` value is the resolved module name, so `lazy from .spam import eggs` passes `package.spam`. The callable must return `True` if the import should be lazy and `False` otherwise.

Return `0` on success and `-1` with an exception set otherwise.

Added in version 3.15.

type PyImport\_LazyImportsMode[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_LazyImportsMode "Link to this definition")
  

Enumeration of possible lazy import modes.

enumerator PyImport\_LAZY\_NORMAL[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_LazyImportsMode.PyImport_LAZY_NORMAL "Link to this definition")
  

Respect the `lazy` keyword in source code. This is the default mode.

enumerator PyImport\_LAZY\_ALL[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_LazyImportsMode.PyImport_LAZY_ALL "Link to this definition")
  

Make all imports lazy by default.

Added in version 3.15.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyImport\_CreateModuleFromInitfunc([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*spec, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*(\*initfunc)(void))[¶](https://docs.python.org/3/c-api/import.html#c.PyImport_CreateModuleFromInitfunc "Link to this definition")
  

This function is a building block that enables embedders to implement the [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module")
 step of custom static extension importers (e.g. of statically-linked extensions).

_spec_ must be a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
 object.

_initfunc_ must be an [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-pyinit)
, the same as for [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
.

On success, create and return a module object. This module will not be initialized; call [`PyModule_Exec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "PyModule_Exec")
 to initialize it. (Custom importers should do this in their [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")
 method.)

On error, return NULL with an exception set.

For modules using [legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
, most of the import process is done in this function, rather than in extra steps that importers typically take after [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module")
. Specifically:

*   The module is added to [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")
     under the _spec_’s [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name")
     as part of initialization.
    
*   If a single-phase module was previously imported under the same [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name")
     by this function or as a built-in module (for example, one registered with [`PyImport_AppendInittab()`](https://docs.python.org/3/c-api/import.html#c.PyImport_AppendInittab "PyImport_AppendInittab")
    ), Python may reuse the previous module’s contents instead of calling _initfunc_ again.
    
*   The module will be fully initialized by _initfunc_. Calling [`PyModule_Exec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Exec "PyModule_Exec")
     on it will have no effect, though it is still recommended, in case the module later switches to [multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
    .
    
*   Also, if the _spec_’s `name` contains dots, this name is used for prepending a parent package to the new module’s [`__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")
    .
    

Added in version 3.15.

#### Previous topic

[Operating System Utilities](https://docs.python.org/3/c-api/sys.html "previous chapter")

#### Next topic

[Data marshalling support](https://docs.python.org/3/c-api/marshal.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Importing+Modules&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fimport.html&pagesource=c-api%2Fimport.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/import.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/marshal.html "Data marshalling support")
     |
*   [previous](https://docs.python.org/3/c-api/sys.html "Operating System Utilities")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [Utilities](https://docs.python.org/3/c-api/utilities.html)
     »
*   [Importing Modules](https://docs.python.org/3/c-api/import.html)
    
*    
    
    |
*   Theme Auto Light Dark |