[Skip to main content](https://matplotlib.org/stable/api/_api_api.html#main-content)

Back to top Ctrl+K

*   [Plot types](https://matplotlib.org/stable/plot_types/index.html)
    
*   [User guide](https://matplotlib.org/stable/users/index.html)
    
*   [Tutorials](https://matplotlib.org/stable/tutorials/index.html)
    
*   [Examples](https://matplotlib.org/stable/gallery/index.html)
    
*   [Reference](https://matplotlib.org/stable/api/index.html)
    
*   [Contribute](https://matplotlib.org/stable/devel/index.html)
    
*   [Releases](https://matplotlib.org/stable/users/release_notes.html)
    

Choose version

*   [Gitter](https://gitter.im/matplotlib/matplotlib "Gitter")
    
*   [Discourse](https://discourse.matplotlib.org/ "Discourse")
    
*   [GitHub](https://github.com/matplotlib/matplotlib "GitHub")
    

`matplotlib._api`[#](https://matplotlib.org/stable/api/_api_api.html#module-matplotlib._api "Link to this heading")

====================================================================================================================

Helper functions for managing the Matplotlib API.

This documentation is only relevant for Matplotlib developers, not for users.

Warning

This module and its submodules are for internal use only. Do not use them in your own code. We may change the API at any time with no warning.

exception matplotlib.\_api.UnsupportedError[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L38-L44)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.UnsupportedError "Link to this definition")

Bases: [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "(in Python v3.14)")

Raised on inherited methods if the child class does not support the functionality of the base class.

See [`unsupported_method`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.unsupported_method "matplotlib._api.unsupported_method")
 for details.

matplotlib.\_api.caching\_module\_getattr(_cls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L289-L321)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.caching_module_getattr "Link to this definition")

Helper decorator for implementing module-level `__getattr__` as a class.

This decorator must be used at the module toplevel as follows:

@caching\_module\_getattr
class \_\_getattr\_\_:  \# The class \*must\* be named \`\`\_\_getattr\_\_\`\`.
    @property  \# Only properties are taken into account.
    def name(self): ...

The `__getattr__` class will be replaced by a `__getattr__` function such that trying to access `name` on the module will resolve the corresponding property (which may be decorated e.g. with `_api.deprecated` for deprecating module globals). The properties are all implicitly cached. Moreover, a suitable AttributeError is generated and raised if no property with the given name exists.

matplotlib.\_api.check\_in\_list(_values_, _/_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L188-L227)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.check_in_list "Link to this definition")

For each _key, value_ pair in _kwargs_, check that _value_ is in _values_; if not, raise an appropriate ValueError.

Parameters:

**values**iterable

Sequence of values to check on.

Note: All values must support == comparisons. This means in particular the entries must not be numpy arrays.

**\*\*kwargs**dict

_key, value_ pairs as keyword arguments to find in _values_.

Raises:

ValueError

If any _value_ in _kwargs_ is not found in _values_.

Examples

\>>> \_api.check\_in\_list(\["foo", "bar"\], arg\=arg, other\_arg\=other\_arg)

matplotlib.\_api.check\_isinstance(_types_, _/_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L123-L155)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.check_isinstance "Link to this definition")

For each _key, value_ pair in _kwargs_, check that _value_ is an instance of one of _types_; if not, raise an appropriate TypeError.

As a special case, a `None` entry in _types_ is treated as NoneType.

Examples

\>>> \_api.check\_isinstance((SomeClass, None), arg\=arg)

matplotlib.\_api.check\_shape(_shape_, _/_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L230-L262)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.check_shape "Link to this definition")

For each _key, value_ pair in _kwargs_, check that _value_ has the shape _shape_; if not, raise an appropriate ValueError.

_None_ in the shape is treated as a "free" size that can have any length. e.g. (None, 2) -> (N, 2)

The values checked must be numpy arrays.

Examples

To check for (N, 2) shaped arrays

\>>> \_api.check\_shape((None, 2), arg\=arg, other\_arg\=other\_arg)

class matplotlib.\_api.classproperty(_fget_, _fset\=None_, _fdel\=None_, _doc\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L86-L117)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.classproperty "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Like [`property`](https://docs.python.org/3/library/functions.html#property "(in Python v3.14)")
, but also triggers on access via the class, and it is the _class_ that's passed as argument.

Examples

class C:
    @classproperty
    def foo(cls):
        return cls.\_\_name\_\_

assert C.foo \== "C"

property fget[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.classproperty.fget "Link to this definition")

matplotlib.\_api.define\_aliases(_alias\_d_, _cls\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L324-L379)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.define_aliases "Link to this definition")

Class decorator for defining property aliases.

Use as

@\_api.define\_aliases({"property": \["alias", ...\], ...})
class C: ...

For each property, if the corresponding `get_property` is defined in the class so far, an alias named `get_alias` will be defined; the same will be done for setters. If neither the getter nor the setter exists, an exception will be raised.

The alias map is stored as the `_alias_to_prop` attribute under the format [\`\`](https://matplotlib.org/stable/api/_api_api.html#id1)
{"alias": "property", ...}\` on the class, and can be used by [`normalize_kwargs`](https://matplotlib.org/stable/api/cbook_api.html#matplotlib.cbook.normalize_kwargs "matplotlib.cbook.normalize_kwargs")
.

matplotlib.\_api.getitem\_checked(_mapping_, _/_, _\_error\_cls\=<class 'ValueError'>_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L265-L286)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.getitem_checked "Link to this definition")

_kwargs_ must consist of a single _key, value_ pair. If _key_ is in _mapping_, return `mapping[value]`; else, raise an appropriate ValueError.

Parameters:

**\_error\_cls**

Class of error to raise.

Examples

\>>> \_api.getitem\_checked({"foo": "bar"}, arg\=arg)

matplotlib.\_api.kwarg\_error(_name_, _kw_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L440-L454)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.kwarg_error "Link to this definition")

Generate a TypeError to be raised by function calls with wrong kwarg.

Parameters:

**name**str

The name of the calling function.

**kw**str or Iterable\[str\]

Either the invalid keyword argument name, or an iterable yielding invalid keyword arguments (e.g., a `kwargs` dict).

matplotlib.\_api.list\_suggestion\_error\_msg(_name_, _potential_, _values_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L158-L185)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.list_suggestion_error_msg "Link to this definition")

Generate an error message that a potential setting is not an acceptable value.

If the acceptable values are all strings, and sufficiently large, then add just a few suggestions to the end of the message. Otherwise list the supported values.

Parameters:

**name**str

The name of the setting, keyword argument, etc. to generate the message for.

**potential**

The potential value from the user that is not a valid choice.

**values**iterable

Sequence of values to check on.

matplotlib.\_api.nargs\_error(_name_, _takes_, _given_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L434-L437)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.nargs_error "Link to this definition")

Generate a TypeError to be raised by function calls with wrong arity.

matplotlib.\_api.recursive\_subclasses(_cls_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L457-L461)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.recursive_subclasses "Link to this definition")

Yield _cls_ and direct and indirect subclasses of _cls_.

matplotlib.\_api.select\_matching\_signature(_funcs_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L382-L431)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.select_matching_signature "Link to this definition")

Select and call the function that accepts `*args, **kwargs`.

_funcs_ is a list of functions which should not raise any exception (other than [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 if the arguments passed do not match their signature).

[`select_matching_signature`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.select_matching_signature "matplotlib._api.select_matching_signature")
 tries to call each of the functions in _funcs_ with `*args, **kwargs` (in the order in which they are given). Calls that fail with a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 are silently skipped. As soon as a call succeeds, [`select_matching_signature`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.select_matching_signature "matplotlib._api.select_matching_signature")
 returns its return value. If no function accepts `*args, **kwargs`, then the [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 raised by the last failing call is re-raised.

Callers should normally make sure that any `*args, **kwargs` can only bind a single _func_ (to avoid any ambiguity), although this is not checked by [`select_matching_signature`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.select_matching_signature "matplotlib._api.select_matching_signature")
.

Notes

[`select_matching_signature`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.select_matching_signature "matplotlib._api.select_matching_signature")
 is intended to help implementing signature-overloaded functions. In general, such functions should be avoided, except for back-compatibility concerns. A typical use pattern is

def my\_func(\*args, \*\*kwargs):
    params \= select\_matching\_signature(
        \[lambda old1, old2: locals(), lambda new: locals()\],
        \*args, \*\*kwargs)
    if "old1" in params:
        warn\_deprecated(...)
        old1, old2 \= params.values()  \# note that locals() is ordered.
    else:
        new, \= params.values()
    \# do things with params

which allows _my\_func_ to be called either with two parameters (_old1_ and _old2_) or a single one (_new_). Note that the new signature is given last, so that callers get a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.14)")
 corresponding to the new signature if the arguments they passed in do not match any signature.

class matplotlib.\_api.unsupported\_method(_\*_, _append\_message\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L47-L83)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.unsupported_method "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Descriptor that creates a method raising [`UnsupportedError`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.UnsupportedError "matplotlib._api.UnsupportedError")
.

Historically, we have quite a few cases of inheritance hierarchies that do not fully respect the Liskov Substitution Principle, e.g. Axes and Artist. Some of the methods of a base class may not be implemented in the child class. In that case, we override the method in the child class to raise [`UnsupportedError`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.UnsupportedError "matplotlib._api.UnsupportedError")
.

Use in a class body to mark inherited methods as unsupported:

class Axes3D(Axes):
    twinx \= \_api.unsupported\_method()

Calling `Axes3D().twinx()` will raise "UnsupportedError: Axes3D does not support 'twinx'."

Parameters:

**append\_message**str

Optional additional text to be appended to the error message.

matplotlib.\_api.warn\_external(_message_, _category\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/__init__.py#L464-L494)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.warn_external "Link to this definition")

[`warnings.warn`](https://docs.python.org/3/library/warnings.html#warnings.warn "(in Python v3.14)")
 wrapper that sets _stacklevel_ to "outside Matplotlib".

The original emitter of the warning can be obtained by patching this function back to [`warnings.warn`](https://docs.python.org/3/library/warnings.html#warnings.warn "(in Python v3.14)")
, i.e. `_api.warn_external = warnings.warn` (or `functools.partial(warnings.warn, stacklevel=2)`, etc.).

Helper functions for deprecating parts of the Matplotlib API.

This documentation is only relevant for Matplotlib developers, not for users.

Warning

This module is for internal use only. Do not use it in your own code. We may change the API at any time with no warning.

exception matplotlib.\_api.deprecation.MatplotlibDeprecationWarning[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L20-L21)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.MatplotlibDeprecationWarning "Link to this definition")

Bases: [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "(in Python v3.14)")

A class for issuing deprecation warnings for Matplotlib users.

matplotlib.\_api.deprecation.delete\_parameter(_since_, _name_, _func\=None_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L317-L416)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.delete_parameter "Link to this definition")

Decorator indicating that parameter _name_ of _func_ is being deprecated.

The actual implementation of _func_ should keep the _name_ parameter in its signature, or accept a `**kwargs` argument (through which _name_ would be passed).

Parameters that come after the deprecated parameter effectively become keyword-only (as they cannot be passed positionally without triggering the DeprecationWarning on the deprecated parameter), and should be marked as such after the deprecation period has passed and the deprecated parameter is removed.

Parameters other than _since_, _name_, and _func_ are keyword-only and forwarded to [`warn_deprecated`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.warn_deprecated "matplotlib._api.deprecation.warn_deprecated")
.

Examples

@\_api.delete\_parameter("3.1", "unused")
def func(used\_arg, other\_arg, unused, more\_args): ...

matplotlib.\_api.deprecation.deprecate\_method\_override(_method_, _obj_, _\*_, _allow\_empty\=False_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L487-L526)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.deprecate_method_override "Link to this definition")

Return `obj.method` with a deprecation if it was overridden, else None.

Parameters:

**method**

An unbound method, i.e. an expression of the form `Class.method_name`. Remember that within the body of a method, one can always use `__class__` to refer to the class that is currently being defined.

**obj**

Either an object of the class where _method_ is defined, or a subclass of that class.

**allow\_empty**bool, default: False

Whether to allow overrides by "empty" methods without emitting a warning.

**\*\*kwargs**

Additional parameters passed to [`warn_deprecated`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.warn_deprecated "matplotlib._api.deprecation.warn_deprecated")
 to generate the deprecation warning; must at least include the "since" key.

class matplotlib.\_api.deprecation.deprecate\_privatize\_attribute(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L222-L245)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.deprecate_privatize_attribute "Link to this definition")

Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

Helper to deprecate public access to an attribute (or method).

This helper should only be used at class scope, as follows:

class Foo:
    attr \= \_deprecate\_privatize\_attribute(\*args, \*\*kwargs)

where _all_ parameters are forwarded to [`deprecated`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.deprecated "matplotlib._api.deprecation.deprecated")
. This form makes `attr` a property which forwards read and write access to `self._attr` (same name but with a leading underscore), with a deprecation warning. Note that the attribute name is derived from _the name this helper is assigned to_. This helper also works for deprecating methods.

matplotlib.\_api.deprecation.deprecated(_since_, _\*_, _message\=''_, _name\=''_, _alternative\=''_, _pending\=False_, _obj\_type\=None_, _addendum\=''_, _removal\=''_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L97-L219)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.deprecated "Link to this definition")

Decorator to mark a function, a class, or a property as deprecated.

When deprecating a classmethod, a staticmethod, or a property, the `@deprecated` decorator should go _under_ `@classmethod` and `@staticmethod` (i.e., [`deprecated`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.deprecated "matplotlib._api.deprecation.deprecated")
 should directly decorate the underlying callable), but _over_ `@property`.

When deprecating a class `C` intended to be used as a base class in a multiple inheritance hierarchy, `C` _must_ define an `__init__` method (if `C` instead inherited its `__init__` from its own base class, then `@deprecated` would mess up `__init__` inheritance when installing its own (deprecation-emitting) `C.__init__`).

Parameters are the same as for [`warn_deprecated`](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.warn_deprecated "matplotlib._api.deprecation.warn_deprecated")
, except that _obj\_type_ defaults to 'class' if decorating a class, 'attribute' if decorating a property, and 'function' otherwise.

Examples

@deprecated('1.4.0')
def the\_function\_to\_deprecate():
    pass

matplotlib.\_api.deprecation.make\_keyword\_only(_since_, _name_, _func\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L419-L484)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.make_keyword_only "Link to this definition")

Decorator indicating that passing parameter _name_ (or any of the following ones) positionally to _func_ is being deprecated.

When used on a method that has a pyplot wrapper, this should be the outermost decorator, so that `boilerplate.py` can access the original signature.

Examples

Assume we want to only allow _dataset_ and _positions_ as positional parameters on the method

def violinplot(self, dataset, positions\=None, vert\=None, ...)

Introduce the deprecation by adding the decorator

@\_api.make\_keyword\_only("3.10", "vert")
def violinplot(self, dataset, positions\=None, vert\=None, ...)

When the deprecation expires, switch to

def violinplot(self, dataset, positions\=None, \*, vert\=None, ...)

matplotlib.\_api.deprecation.rename\_parameter(_since_, _old_, _new_, _func\=None_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L256-L306)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.rename_parameter "Link to this definition")

Decorator indicating that parameter _old_ of _func_ is renamed to _new_.

The actual implementation of _func_ should use _new_, not _old_. If _old_ is passed to _func_, a DeprecationWarning is emitted, and its value is used, even if _new_ is also passed by keyword (this is to simplify pyplot wrapper functions, which always pass _new_ explicitly to the Axes method). If _new_ is also passed but positionally, a TypeError will be raised by the underlying function during argument binding.

Examples

@\_api.rename\_parameter("3.1", "bad\_name", "good\_name")
def func(good\_name): ...

matplotlib.\_api.deprecation.suppress\_matplotlib\_deprecation\_warning()[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L529-L533)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.suppress_matplotlib_deprecation_warning "Link to this definition")

matplotlib.\_api.deprecation.warn\_deprecated(_since_, _\*_, _message\=''_, _name\=''_, _alternative\=''_, _pending\=False_, _obj\_type\=''_, _addendum\=''_, _removal\=''_)[\[source\]](https://github.com/matplotlib/matplotlib/blob/v3.11.2/lib/matplotlib/_api/deprecation.py#L48-L94)
[#](https://matplotlib.org/stable/api/_api_api.html#matplotlib._api.deprecation.warn_deprecated "Link to this definition")

Display a standardized deprecation.

Parameters:

**since**str

The release at which this API became deprecated.

**message**str, optional

Override the default deprecation message. The `%(since)s`, `%(name)s`, `%(alternative)s`, `%(obj_type)s`, `%(addendum)s`, and `%(removal)s` format specifiers will be replaced by the values of the respective arguments passed to this function.

**name**str, optional

The name of the deprecated object.

**alternative**str, optional

An alternative API that the user may use in place of the deprecated API. The deprecation warning will tell the user about this alternative if provided.

**pending**bool, optional

If True, uses a PendingDeprecationWarning instead of a DeprecationWarning. Cannot be used together with _removal_.

**obj\_type**str, optional

The object type being deprecated.

**addendum**str, optional

Additional text appended directly to the final message.

**removal**str, optional

The expected removal version. With the default (an empty string), a removal version is automatically computed from _since_. Set to other Falsy values to not schedule a removal date. Cannot be used together with _pending_.

Examples

\# To warn of the deprecation of "matplotlib.name\_of\_module"
warn\_deprecated('1.4.0', name\='matplotlib.name\_of\_module',
                obj\_type\='module')

On this page