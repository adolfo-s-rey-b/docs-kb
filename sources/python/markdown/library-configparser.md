### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tomllib.html "tomllib — Parse TOML files")
     |
*   [previous](https://docs.python.org/3/library/csv.html "csv — CSV file reading and writing")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [File Formats](https://docs.python.org/3/library/fileformats.html)
     »
*   [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`configparser` — Configuration file parser[¶](https://docs.python.org/3/library/configparser.html#module-configparser "Link to this heading")

==============================================================================================================================================

**Source code:** [Lib/configparser.py](https://github.com/python/cpython/tree/3.15/Lib/configparser.py)

* * *

This module provides the [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.

Note

This library does _not_ interpret or write the value-type prefixes used in the Windows Registry extended version of INI syntax.

Warning

Be cautious when parsing data from untrusted sources. A malicious INI file may cause the decoder to consume considerable CPU and memory resources. Limiting the size of data to be parsed is recommended.

See also

Module [`tomllib`](https://docs.python.org/3/library/tomllib.html#module-tomllib "tomllib: Parse TOML files.")

TOML is a well-specified format for application configuration files. It is specifically designed to be an improved version of INI.

Module [`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.")

Support for creating Unix shell-like mini-languages which can also be used for application configuration files.

Module [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")

The `json` module implements a subset of JavaScript syntax which is sometimes used for configuration, but does not support comments.

Quick Start[¶](https://docs.python.org/3/library/configparser.html#quick-start "Link to this heading")

-------------------------------------------------------------------------------------------------------

Let’s take a very basic configuration file that looks like this:

\[DEFAULT\]
ServerAliveInterval \= 45
Compression \= yes
CompressionLevel \= 9
ForwardX11 \= yes

\[forge.example\]
User \= hg

\[topsecret.server.example\]
Port \= 50022
ForwardX11 \= no

The structure of INI files is described [in the following section](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure)
. Essentially, the file consists of sections, each of which contains keys with values. `configparser` classes can read and write such files. Let’s start by creating the above configuration file programmatically.

Copy

\>>> import configparser
\>>> config \= configparser.ConfigParser()
\>>> config\['DEFAULT'\] \= {'ServerAliveInterval': '45',
...                      'Compression': 'yes',
...                      'CompressionLevel': '9'}
\>>> config\['forge.example'\] \= {}
\>>> config\['forge.example'\]\['User'\] \= 'hg'
\>>> config\['topsecret.server.example'\] \= {}
\>>> topsecret \= config\['topsecret.server.example'\]
\>>> topsecret\['Port'\] \= '50022'     \# mutates the parser
\>>> topsecret\['ForwardX11'\] \= 'no'  \# same here
\>>> config\['DEFAULT'\]\['ForwardX11'\] \= 'yes'
\>>> with open('example.ini', 'w') as configfile:
...   config.write(configfile)
...

As you can see, we can treat a config parser much like a dictionary. There are differences, [outlined later](https://docs.python.org/3/library/configparser.html#mapping-protocol-access)
, but the behavior is very close to what you would expect from a dictionary.

Now that we have created and saved a configuration file, let’s read it back and explore the data it holds.

Copy

\>>> config \= configparser.ConfigParser()
\>>> config.sections()
\[\]
\>>> config.read('example.ini')
\['example.ini'\]
\>>> config.sections()
\['forge.example', 'topsecret.server.example'\]
\>>> 'forge.example' in config
True
\>>> 'python.org' in config
False
\>>> config\['forge.example'\]\['User'\]
'hg'
\>>> config\['DEFAULT'\]\['Compression'\]
'yes'
\>>> topsecret \= config\['topsecret.server.example'\]
\>>> topsecret\['ForwardX11'\]
'no'
\>>> topsecret\['Port'\]
'50022'
\>>> for key in config\['forge.example'\]:
...     print(key)
user
compressionlevel
serveraliveinterval
compression
forwardx11
\>>> config\['forge.example'\]\['ForwardX11'\]
'yes'

As we can see above, the API is pretty straightforward. The only bit of magic involves the `DEFAULT` section which provides default values for all other sections [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
. Note also that keys in sections are case-insensitive and stored in lowercase [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
.

It is possible to read several configurations into a single [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
, where the most recently added configuration has the highest priority. Any conflicting keys are taken from the more recent configuration while the previously existing keys are retained. The example below reads in an `override.ini` file, which will override any conflicting keys from the `example.ini` file.

\[DEFAULT\]
ServerAliveInterval \= \-1

Copy

\>>> config\_override \= configparser.ConfigParser()
\>>> config\_override\['DEFAULT'\] \= {'ServerAliveInterval': '-1'}
\>>> with open('override.ini', 'w') as configfile:
...     config\_override.write(configfile)
...
\>>> config\_override \= configparser.ConfigParser()
\>>> config\_override.read(\['example.ini', 'override.ini'\])
\['example.ini', 'override.ini'\]
\>>> print(config\_override.get('DEFAULT', 'ServerAliveInterval'))
\-1

This behaviour is equivalent to a [`ConfigParser.read()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "configparser.ConfigParser.read")
 call with several files passed to the _filenames_ parameter.

Supported Datatypes[¶](https://docs.python.org/3/library/configparser.html#supported-datatypes "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Config parsers do not guess datatypes of values in configuration files, always storing them internally as strings. This means that if you need other datatypes, you should convert on your own:

Copy

\>>> int(topsecret\['Port'\])
50022
\>>> float(topsecret\['CompressionLevel'\])
9.0

Since this task is so common, config parsers provide a range of handy getter methods to handle integers, floats and booleans. The last one is the most interesting because simply passing the value to `bool()` would do no good since `bool('False')` is still `True`. This is why config parsers also provide [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean")
. This method is case-insensitive and recognizes Boolean values from `'yes'`/`'no'`, `'on'`/`'off'`, `'true'`/`'false'` and `'1'`/`'0'` [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
. For example:

Copy

\>>> topsecret.getboolean('ForwardX11')
False
\>>> config\['forge.example'\].getboolean('ForwardX11')
True
\>>> config.getboolean('forge.example', 'Compression')
True

Apart from [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean")
, config parsers also provide equivalent [`getint()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "configparser.ConfigParser.getint")
 and [`getfloat()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "configparser.ConfigParser.getfloat")
 methods. You can register your own converters and customize the provided ones. [\[1\]](https://docs.python.org/3/library/configparser.html#id16)

Fallback Values[¶](https://docs.python.org/3/library/configparser.html#fallback-values "Link to this heading")

---------------------------------------------------------------------------------------------------------------

As with a dictionary, you can use a section’s [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 method to provide fallback values:

Copy

\>>> topsecret.get('Port')
'50022'
\>>> topsecret.get('CompressionLevel')
'9'
\>>> topsecret.get('Cipher')
\>>> topsecret.get('Cipher', '3des-cbc')
'3des-cbc'

Please note that default values have precedence over fallback values. For instance, in our example the `'CompressionLevel'` key was specified only in the `'DEFAULT'` section. If we try to get it from the section `'topsecret.server.example'`, we will always get the default, even if we specify a fallback:

Copy

\>>> topsecret.get('CompressionLevel', '3')
'9'

One more thing to be aware of is that the parser-level [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 method provides a custom, more complex interface, maintained for backwards compatibility. When using this method, a fallback value can be provided via the `fallback` keyword-only argument:

Copy

\>>> config.get('forge.example', 'monster',
...            fallback\='No such things as monsters')
'No such things as monsters'

The same `fallback` argument can be used with the [`getint()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "configparser.ConfigParser.getint")
, [`getfloat()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "configparser.ConfigParser.getfloat")
 and [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean")
 methods, for example:

Copy

\>>> 'BatchMode' in topsecret
False
\>>> topsecret.getboolean('BatchMode', fallback\=True)
True
\>>> config\['DEFAULT'\]\['BatchMode'\] \= 'no'
\>>> topsecret.getboolean('BatchMode', fallback\=True)
False

Supported INI File Structure[¶](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

A configuration file consists of sections, each led by a `[section]` header, followed by key/value entries separated by a specific string (`=` or `:` by default [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
). By default, section names are case sensitive but keys are not [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
. Leading and trailing whitespace is removed from keys and values. Values can be omitted if the parser is configured to allow it [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
, in which case the key/value delimiter may also be left out. Values can also span multiple lines, as long as they are indented deeper than the first line of the value. Depending on the parser’s mode, blank lines may be treated as parts of multiline values or ignored.

By default, a valid section name can be any string that does not contain ‘\\n’. To change this, see [`ConfigParser.SECTCRE`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.SECTCRE "configparser.ConfigParser.SECTCRE")
.

The first section name may be omitted if the parser is configured to allow an unnamed top level section with `allow_unnamed_section=True`. In this case, the keys/values may be retrieved by [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
 as in `config[UNNAMED_SECTION]`.

Configuration files may include comments, prefixed by specific characters (`#` and `;` by default [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
). Comments may appear on their own on an otherwise empty line, possibly indented. [\[1\]](https://docs.python.org/3/library/configparser.html#id16)

For example:

\[Simple Values\]
key\=value
spaces in keys\=allowed
spaces in values\=allowed as well
spaces around the delimiter \= obviously
you can also use : to delimit keys from values

\[All Values Are Strings\]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

\[Multiline Values\]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

\[No Values\]
key\_without\_value
empty string value here \=

\[You can use comments\]
\# like this
; or this

\# By default only in an empty line.
\# Inline comments can be harmful because they prevent users
\# from using the delimiting characters as parts of values.
\# That being said, this can be customized.

    \[Sections Can Be Indented\]
        can\_values\_be\_as\_well \= True
        does\_that\_mean\_anything\_special \= False
        purpose \= formatting for readability
        multiline\_values \= are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        \# Did I mention we can indent comments, too?

Unnamed Sections[¶](https://docs.python.org/3/library/configparser.html#unnamed-sections "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

The name of the first section (or unique) may be omitted and values retrieved by the [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
 attribute.

Copy

\>>> config \= """
... option = value
...
... \[  Section 2  \]
... another = val
... """
\>>> unnamed \= configparser.ConfigParser(allow\_unnamed\_section\=True)
\>>> unnamed.read\_string(config)
\>>> unnamed.get(configparser.UNNAMED\_SECTION, 'option')
'value'

Interpolation of values[¶](https://docs.python.org/3/library/configparser.html#interpolation-of-values "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

On top of the core functionality, [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 supports interpolation. This means values can be preprocessed before returning them from `get()` calls.

class configparser.BasicInterpolation[¶](https://docs.python.org/3/library/configparser.html#configparser.BasicInterpolation "Link to this definition")

The default implementation used by [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
. It enables values to contain format strings which refer to other values in the same section, or values in the special default section [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
. Additional default values can be provided on initialization.

For example:

\[Paths\]
home\_dir: /Users
my\_dir: %(home\_dir)s/lumberjack
my\_pictures: %(my\_dir)s/Pictures

\[Escape\]
\# use a %% to escape the % sign (% is the only character that needs to be escaped):
gain: 80%%

In the example above, [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 with _interpolation_ set to `BasicInterpolation()` would resolve `%(home_dir)s` to the value of `home_dir` (`/Users` in this case). `%(my_dir)s` in effect would resolve to `/Users/lumberjack`. All interpolations are done on demand so keys used in the chain of references do not have to be specified in any specific order in the configuration file.

With `interpolation` set to `None`, the parser would simply return `%(my_dir)s/Pictures` as the value of `my_pictures` and `%(home_dir)s/lumberjack` as the value of `my_dir`.

class configparser.ExtendedInterpolation[¶](https://docs.python.org/3/library/configparser.html#configparser.ExtendedInterpolation "Link to this definition")

An alternative handler for interpolation which implements a more advanced syntax, used for instance in `zc.buildout`. Extended interpolation is using `${section:option}` to denote a value from a foreign section. Interpolation can span multiple levels. For convenience, if the `section:` part is omitted, interpolation defaults to the current section (and possibly the default values from the special section).

For example, the configuration specified above with basic interpolation, would look like this with extended interpolation:

\[Paths\]
home\_dir: /Users
my\_dir: ${home\_dir}/lumberjack
my\_pictures: ${my\_dir}/Pictures

\[Escape\]
\# use a $$ to escape the $ sign ($ is the only character that needs to be escaped):
cost: $$80

Values from other sections can be fetched as well:

\[Common\]
home\_dir: /Users
library\_dir: /Library
system\_dir: /System
macports\_dir: /opt/local

\[Frameworks\]
Python: 3.2
path: ${Common:system\_dir}/Library/Frameworks/

\[Arthur\]
nickname: Two Sheds
last\_name: Jackson
my\_dir: ${Common:home\_dir}/twosheds
my\_pictures: ${my\_dir}/Pictures
python\_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}

Mapping Protocol Access[¶](https://docs.python.org/3/library/configparser.html#mapping-protocol-access "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

Added in version 3.2.

Mapping protocol access is a generic name for functionality that enables using custom objects as if they were dictionaries. In case of `configparser`, the mapping interface implementation is using the `parser['section']['option']` notation.

`parser['section']` in particular returns a proxy for the section’s data in the parser. This means that the values are not copied but they are taken from the original parser on demand. What’s even more important is that when values are changed on a section proxy, they are actually mutated in the original parser.

`configparser` objects behave as close to actual dictionaries as possible. The mapping interface is complete and adheres to the [`MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping")
 ABC. However, there are a few differences that should be taken into account:

*   By default, all keys in sections are accessible in a case-insensitive manner [\[1\]](https://docs.python.org/3/library/configparser.html#id16)
    . E.g. `for option in parser["section"]` yields only `optionxform`’ed option key names. This means lowercased keys by default. At the same time, for a section that holds the key `'a'`, both expressions return `True`:
    
    Copy
    
    "a" in parser\["section"\]
    "A" in parser\["section"\]
    
*   All sections include `DEFAULTSECT` values as well which means that `.clear()` on a section may not leave the section visibly empty. This is because default values cannot be deleted from the section (because technically they are not there). If they are overridden in the section, deleting causes the default value to be visible again. Trying to delete a default value causes a [`KeyError`](https://docs.python.org/3/builtins/exceptions.html#KeyError "KeyError")
    .
    
*   `DEFAULTSECT` cannot be removed from the parser:
    
    *   trying to delete it raises [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
        ,
        
    *   `parser.clear()` leaves it intact,
        
    *   `parser.popitem()` never returns it.
        
*   `parser.get(section, option, **kwargs)` - the second argument is **not** a fallback value. Note however that the section-level `get()` methods are compatible both with the mapping protocol and the classic configparser API.
    
*   `parser.items()` is compatible with the mapping protocol (returns a list of _section\_name_, _section\_proxy_ pairs including the DEFAULTSECT). However, this method can also be invoked with arguments: `parser.items(section, raw, vars)`. The latter call returns a list of _option_, _value_ pairs for a specified `section`, with all interpolations expanded (unless `raw=True` is provided).
    

The mapping protocol is implemented on top of the existing legacy API so that subclasses overriding the original interface still should have mappings working as expected.

Customizing Parser Behaviour[¶](https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

There are nearly as many INI format variants as there are applications using it. `configparser` goes a long way to provide support for the largest sensible set of INI styles available. The default functionality is mainly dictated by historical background and it’s very likely that you will want to customize some of the features.

The most common way to change the way a specific config parser works is to use the `__init__()` options:

*   _defaults_, default value: `None`
    
    This option accepts a dictionary of key-value pairs which will be initially put in the `DEFAULT` section. This makes for an elegant way to support concise configuration files that don’t specify values which are the same as the documented default.
    
    Hint: if you want to specify default values for a specific section, use [`read_dict()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict "configparser.ConfigParser.read_dict")
     before you read the actual file.
    
*   _dict\_type_, default value: [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
    
    This option has a major impact on how the mapping protocol will behave and how the written configuration files look. With the standard dictionary, every section is stored in the order they were added to the parser. Same goes for options within sections.
    
    An alternative dictionary type can be used for example to sort sections and options on write-back.
    
    Please note: there are ways to add a set of key-value pairs in a single operation. When you use a regular dictionary in those operations, the order of the keys will be ordered. For example:
    
    Copy
    
    \>>> parser \= configparser.ConfigParser()
    \>>> parser.read\_dict({'section1': {'key1': 'value1',
    ...                                'key2': 'value2',
    ...                                'key3': 'value3'},
    ...                   'section2': {'keyA': 'valueA',
    ...                                'keyB': 'valueB',
    ...                                'keyC': 'valueC'},
    ...                   'section3': {'foo': 'x',
    ...                                'bar': 'y',
    ...                                'baz': 'z'}
    ... })
    \>>> parser.sections()
    \['section1', 'section2', 'section3'\]
    \>>> \[option for option in parser\['section3'\]\]
    \['foo', 'bar', 'baz'\]
    
*   _allow\_no\_value_, default value: `False`
    
    Some configuration files are known to include settings without values, but which otherwise conform to the syntax supported by `configparser`. The _allow\_no\_value_ parameter to the constructor can be used to indicate that such values should be accepted:
    
    Copy
    
    \>>> import configparser
    
    \>>> sample\_config \= """
    ... \[mysqld\]
    ...   user = mysql
    ...   pid-file = /var/run/mysqld/mysqld.pid
    ...   skip-external-locking
    ...   old\_passwords = 1
    ...   skip-bdb
    ...   # we don't need ACID today
    ...   skip-innodb
    ... """
    \>>> config \= configparser.ConfigParser(allow\_no\_value\=True)
    \>>> config.read\_string(sample\_config)
    
    \>>> \# Settings with values are treated as before:
    \>>> config\["mysqld"\]\["user"\]
    'mysql'
    
    \>>> \# Settings without values provide None:
    \>>> config\["mysqld"\]\["skip-bdb"\]
    
    \>>> \# Settings which aren't specified still raise an error:
    \>>> config\["mysqld"\]\["does-not-exist"\]
    Traceback (most recent call last):
      ...
    KeyError: 'does-not-exist'
    
*   _delimiters_, default value: `('=', ':')`
    
    Delimiters are substrings that delimit keys from values within a section. The first occurrence of a delimiting substring on a line is considered a delimiter. This means values (but not keys) can contain the delimiters.
    
    See also the _space\_around\_delimiters_ argument to [`ConfigParser.write()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.write "configparser.ConfigParser.write")
    .
    
*   _comment\_prefixes_, default value: `('#', ';')`
    
*   _inline\_comment\_prefixes_, default value: `None`
    
    Comment prefixes are strings that indicate the start of a valid comment within a config file. _comment\_prefixes_ are used only on otherwise empty lines (optionally indented) whereas _inline\_comment\_prefixes_ can be used after every valid value (e.g. section names, options and empty lines as well). By default inline comments are disabled and `'#'` and `';'` are used as prefixes for whole line comments.
    
    Changed in version 3.2: In previous versions of `configparser` behaviour matched `comment_prefixes=('#',';')` and `inline_comment_prefixes=(';',)`.
    
    Please note that config parsers don’t support escaping of comment prefixes so using _inline\_comment\_prefixes_ may prevent users from specifying option values with characters used as comment prefixes. When in doubt, avoid setting _inline\_comment\_prefixes_. In any circumstances, the only way of storing comment prefix characters at the beginning of a line in multiline values is to interpolate the prefix, for example:
    
    Copy
    
    \>>> from configparser import ConfigParser, ExtendedInterpolation
    \>>> parser \= ConfigParser(interpolation\=ExtendedInterpolation())
    \>>> \# the default BasicInterpolation could be used as well
    \>>> parser.read\_string("""
    ... \[DEFAULT\]
    ... hash = #
    ...
    ... \[hashes\]
    ... shebang =
    ...   ${hash}!/usr/bin/env python
    ...   ${hash} -\*- coding: utf-8 -\*-
    ...
    ... extensions =
    ...   enabled\_extension
    ...   another\_extension
    ...   #disabled\_by\_comment
    ...   yet\_another\_extension
    ...
    ... interpolation not necessary = if # is not at line start
    ... even in multiline values = line #1
    ...   line #2
    ...   line #3
    ... """)
    \>>> print(parser\['hashes'\]\['shebang'\])
    
    #!/usr/bin/env python
    \# -\*- coding: utf-8 -\*-
    \>>> print(parser\['hashes'\]\['extensions'\])
    
    enabled\_extension
    another\_extension
    yet\_another\_extension
    \>>> print(parser\['hashes'\]\['interpolation not necessary'\])
    if # is not at line start
    \>>> print(parser\['hashes'\]\['even in multiline values'\])
    line #1
    line #2
    line #3
    
*   _strict_, default value: `True`
    
    When set to `True`, the parser will not allow for any section or option duplicates while reading from a single source (using [`read_file()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_file "configparser.ConfigParser.read_file")
    , [`read_string()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_string "configparser.ConfigParser.read_string")
     or [`read_dict()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict "configparser.ConfigParser.read_dict")
    ). It is recommended to use strict parsers in new applications.
    
    Changed in version 3.2: In previous versions of `configparser` behaviour matched `strict=False`.
    
*   _empty\_lines\_in\_values_, default value: `True`
    
    In config parsers, values can span multiple lines as long as they are indented more than the key that holds them. By default parsers also let empty lines to be parts of values. At the same time, keys can be arbitrarily indented themselves to improve readability. In consequence, when configuration files get big and complex, it is easy for the user to lose track of the file structure. Take for instance:
    
    \[Section\]
    key \= multiline
      value with a gotcha
    
     this \= is still a part of the multiline value of 'key'
    
    This can be especially problematic for the user to see if she’s using a proportional font to edit the file. That is why when your application does not need values with empty lines, you should consider disallowing them. This will make empty lines split keys every time. In the example above, it would produce two keys, `key` and `this`.
    
*   _default\_section_, default value: `configparser.DEFAULTSECT` (that is: `"DEFAULT"`)
    
    The convention of allowing a special section of default values for other sections or interpolation purposes is a powerful concept of this library, letting users create complex declarative configurations. This section is normally called `"DEFAULT"` but this can be customized to point to any other valid section name. Some typical values include: `"general"` or `"common"`. The name provided is used for recognizing default sections when reading from any source and is used when writing configuration back to a file. Its current value can be retrieved using the `parser_instance.default_section` attribute and may be modified at runtime (i.e. to convert files from one format to another).
    
*   _interpolation_, default value: `configparser.BasicInterpolation`
    
    Interpolation behaviour may be customized by providing a custom handler through the _interpolation_ argument. `None` can be used to turn off interpolation completely, `ExtendedInterpolation()` provides a more advanced variant inspired by `zc.buildout`. More on the subject in the [dedicated documentation section](https://docs.python.org/3/library/configparser.html#interpolation-of-values)
    . [`RawConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "configparser.RawConfigParser")
     has a default value of `None`.
    
*   _converters_, default value: not set
    
    Config parsers provide option value getters that perform type conversion. By default [`getint()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "configparser.ConfigParser.getint")
    , [`getfloat()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "configparser.ConfigParser.getfloat")
    , and [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean")
     are implemented. Should other getters be desirable, users may define them in a subclass or pass a dictionary where each key is a name of the converter and each value is a callable implementing said conversion. For instance, passing `{'decimal': decimal.Decimal}` would add `getdecimal()` on both the parser object and all section proxies. In other words, it will be possible to write both `parser_instance.getdecimal('section', 'key', fallback=0)` and `parser_instance['section'].getdecimal('key', 0)`.
    
    If the converter needs to access the state of the parser, it can be implemented as a method on a config parser subclass. If the name of this method starts with `get`, it will be available on all section proxies, in the dict-compatible form (see the `getdecimal()` example above).
    

More advanced customization may be achieved by overriding default values of these parser attributes. The defaults are defined on the classes, so they may be overridden by subclasses or by attribute assignment.

ConfigParser.BOOLEAN\_STATES[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.BOOLEAN_STATES "Link to this definition")

By default when using [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean")
, config parsers consider the following values `True`: `'1'`, `'yes'`, `'true'`, `'on'` and the following values `False`: `'0'`, `'no'`, `'false'`, `'off'`. You can override this by specifying a custom dictionary of strings and their Boolean outcomes. For example:

Copy

\>>> custom \= configparser.ConfigParser()
\>>> custom\['section1'\] \= {'funky': 'nope'}
\>>> custom\['section1'\].getboolean('funky')
Traceback (most recent call last):
...
ValueError: Not a boolean: nope
\>>> custom.BOOLEAN\_STATES \= {'sure': True, 'nope': False}
\>>> custom\['section1'\].getboolean('funky')
False

Other typical Boolean pairs include `accept`/`reject` or `enabled`/`disabled`.

ConfigParser.optionxform(_option_)

This method transforms option names on every read, get, or set operation. The default converts the name to lowercase. This also means that when a configuration file gets written, all keys will be lowercase. Override this method if that’s unsuitable. For example:

Copy

\>>> config \= """
... \[Section1\]
... Key = Value
...
... \[Section2\]
... AnotherKey = Value
... """
\>>> typical \= configparser.ConfigParser()
\>>> typical.read\_string(config)
\>>> list(typical\['Section1'\].keys())
\['key'\]
\>>> list(typical\['Section2'\].keys())
\['anotherkey'\]
\>>> custom \= configparser.RawConfigParser()
\>>> custom.optionxform \= lambda option: option
\>>> custom.read\_string(config)
\>>> list(custom\['Section1'\].keys())
\['Key'\]
\>>> list(custom\['Section2'\].keys())
\['AnotherKey'\]

Note

The optionxform function transforms option names to a canonical form. This should be an idempotent function: if the name is already in canonical form, it should be returned unchanged.

ConfigParser.SECTCRE[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.SECTCRE "Link to this definition")

A compiled regular expression used to parse section headers. The default matches `[section]` to the name `"section"`. Whitespace is considered part of the section name, thus `[  larch  ]` will be read as a section of name `"  larch  "`. Override this attribute if that’s unsuitable. For example:

Copy

\>>> import re
\>>> config \= """
... \[Section 1\]
... option = value
...
... \[  Section 2  \]
... another = val
... """
\>>> typical \= configparser.ConfigParser()
\>>> typical.read\_string(config)
\>>> typical.sections()
\['Section 1', '  Section 2  '\]
\>>> custom \= configparser.ConfigParser()
\>>> custom.SECTCRE \= re.compile(r"\\\[ \*(?P<header>\[^\]\]+?) \*\\\]")
\>>> custom.read\_string(config)
\>>> custom.sections()
\['Section 1', 'Section 2'\]

Note

While ConfigParser objects also use an `OPTCRE` attribute for recognizing option lines, it’s not recommended to override it because that would interfere with constructor options _allow\_no\_value_ and _delimiters_.

Legacy API Examples[¶](https://docs.python.org/3/library/configparser.html#legacy-api-examples "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Mainly because of backwards compatibility concerns, `configparser` provides also a legacy API with explicit `get`/`set` methods. While there are valid use cases for the methods outlined below, mapping protocol access is preferred for new projects. The legacy API is at times more advanced, low-level and downright counterintuitive.

An example of writing to a configuration file:

Copy

import configparser

config \= configparser.RawConfigParser()

\# Please note that using RawConfigParser's set functions, you can assign
\# non-string values to keys internally, but will receive an error when
\# attempting to write to a file or when you get it in non-raw mode. Setting
\# values using the mapping protocol or ConfigParser's set() does not allow
\# such assignments to take place.
config.add\_section('Section1')
config.set('Section1', 'an\_int', '15')
config.set('Section1', 'a\_bool', 'true')
config.set('Section1', 'a\_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

\# Writing our configuration file to 'example.cfg'
with open('example.cfg', 'w') as configfile:
    config.write(configfile)

An example of reading the configuration file again:

Copy

import configparser

config \= configparser.RawConfigParser()
config.read('example.cfg')

\# getfloat() raises an exception if the value is not a float
\# getint() and getboolean() also do this for their respective types
a\_float \= config.getfloat('Section1', 'a\_float')
an\_int \= config.getint('Section1', 'an\_int')
print(a\_float + an\_int)

\# Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
\# This is because we are using a RawConfigParser().
if config.getboolean('Section1', 'a\_bool'):
    print(config.get('Section1', 'foo'))

To get interpolation, use [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
:

Copy

import configparser

cfg \= configparser.ConfigParser()
cfg.read('example.cfg')

\# Set the optional \*raw\* argument of get() to True if you wish to disable
\# interpolation in a single get operation.
print(cfg.get('Section1', 'foo', raw\=False))  \# -> "Python is fun!"
print(cfg.get('Section1', 'foo', raw\=True))   \# -> "%(bar)s is %(baz)s!"

\# The optional \*vars\* argument is a dict with members that will take
\# precedence in interpolation.
print(cfg.get('Section1', 'foo', vars\={'bar': 'Documentation',
                                       'baz': 'evil'}))

\# The optional \*fallback\* argument can be used to provide a fallback value
print(cfg.get('Section1', 'foo'))
      \# -> "Python is fun!"

print(cfg.get('Section1', 'foo', fallback\='Monty is not.'))
      \# -> "Python is fun!"

print(cfg.get('Section1', 'monster', fallback\='No such things as monsters.'))
      \# -> "No such things as monsters."

\# A bare print(cfg.get('Section1', 'monster')) would raise NoOptionError
\# but we can also use:

print(cfg.get('Section1', 'monster', fallback\=None))
      \# -> None

Default values are available in both types of ConfigParsers. They are used in interpolation if an option used is not defined elsewhere.

Copy

import configparser

\# New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
config \= configparser.ConfigParser({'bar': 'Life', 'baz': 'hard'})
config.read('example.cfg')

print(config.get('Section1', 'foo'))     \# -> "Python is fun!"
config.remove\_option('Section1', 'bar')
config.remove\_option('Section1', 'baz')
print(config.get('Section1', 'foo'))     \# -> "Life is hard!"

ConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#configparser-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

class configparser.ConfigParser(_defaults\=None_, _dict\_type\=dict_, _allow\_no\_value\=False_, _\*_, _delimiters\=('=', ':')_, _comment\_prefixes\=('#', ';')_, _inline\_comment\_prefixes\=None_, _strict\=True_, _empty\_lines\_in\_values\=True_, _default\_section\=configparser.DEFAULTSECT_, _interpolation\=BasicInterpolation()_, _converters\={}_, _allow\_unnamed\_section\=False_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "Link to this definition")

The main configuration parser. When _defaults_ is given, it is initialized into the dictionary of intrinsic defaults. When _dict\_type_ is given, it will be used to create the dictionary objects for the list of sections, for the options within a section, and for the default values.

When _delimiters_ is given, it is used as the set of substrings that divide keys from values. When _comment\_prefixes_ is given, it will be used as the set of substrings that prefix comments in otherwise empty lines. Comments can be indented. When _inline\_comment\_prefixes_ is given, it will be used as the set of substrings that prefix comments in non-empty lines.

When _strict_ is `True` (the default), the parser won’t allow for any section or option duplicates while reading from a single source (file, string or dictionary), raising [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError")
 or [`DuplicateOptionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateOptionError "configparser.DuplicateOptionError")
. When _empty\_lines\_in\_values_ is `False` (default: `True`), each empty line marks the end of an option. Otherwise, internal empty lines of a multiline option are kept as part of the value. When _allow\_no\_value_ is `True` (default: `False`), options without values are accepted; the value held for these is `None` and they are serialized without the trailing delimiter.

When _default\_section_ is given, it specifies the name for the special section holding default values for other sections and interpolation purposes (normally named `"DEFAULT"`). This value can be retrieved and changed at runtime using the `default_section` instance attribute. This won’t re-evaluate an already parsed config file, but will be used when writing parsed settings to a new config file.

Interpolation behaviour may be customized by providing a custom handler through the _interpolation_ argument. `None` can be used to turn off interpolation completely, `ExtendedInterpolation()` provides a more advanced variant inspired by `zc.buildout`. More on the subject in the [dedicated documentation section](https://docs.python.org/3/library/configparser.html#interpolation-of-values)
.

All option names used in interpolation will be passed through the [`optionxform()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.optionxform "configparser.ConfigParser.optionxform")
 method just like any other option name reference. For example, using the default implementation of `optionxform()` (which converts option names to lower case), the values `foo %(bar)s` and `foo %(BAR)s` are equivalent.

When _converters_ is given, it should be a dictionary where each key represents the name of a type converter and each value is a callable implementing the conversion from string to the desired datatype. Every converter gets its own corresponding `get*()` method on the parser object and section proxies.

When _allow\_unnamed\_section_ is `True` (default: `False`), the first section name can be omitted. See the [“Unnamed Sections” section](https://docs.python.org/3/library/configparser.html#unnamed-sections)
.

It is possible to read several configurations into a single `ConfigParser`, where the most recently added configuration has the highest priority. Any conflicting keys are taken from the more recent configuration while the previously existing keys are retained. The example below reads in an `override.ini` file, which will override any conflicting keys from the `example.ini` file.

\[DEFAULT\]
ServerAliveInterval \= \-1

Copy

\>>> config\_override \= configparser.ConfigParser()
\>>> config\_override\['DEFAULT'\] \= {'ServerAliveInterval': '-1'}
\>>> with open('override.ini', 'w') as configfile:
...     config\_override.write(configfile)
...
\>>> config\_override \= configparser.ConfigParser()
\>>> config\_override.read(\['example.ini', 'override.ini'\])
\['example.ini', 'override.ini'\]
\>>> print(config\_override.get('DEFAULT', 'ServerAliveInterval'))
\-1

Changed in version 3.1: The default _dict\_type_ is [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict")
.

Changed in version 3.2: _allow\_no\_value_, _delimiters_, _comment\_prefixes_, _strict_, _empty\_lines\_in\_values_, _default\_section_ and _interpolation_ were added.

Changed in version 3.5: The _converters_ argument was added.

Changed in version 3.7: The _defaults_ argument is read with [`read_dict()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict "configparser.ConfigParser.read_dict")
, providing consistent behavior across the parser: non-string keys and values are implicitly converted to strings.

Changed in version 3.8: The default _dict\_type_ is [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, since it now preserves insertion order.

Changed in version 3.13: Raise a [`MultilineContinuationError`](https://docs.python.org/3/library/configparser.html#configparser.MultilineContinuationError "configparser.MultilineContinuationError")
 when _allow\_no\_value_ is `True`, and a key without a value is continued with an indented line.

Changed in version 3.13: The _allow\_unnamed\_section_ argument was added.

defaults()[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.defaults "Link to this definition")

Return a dictionary containing the instance-wide defaults.

sections()[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.sections "Link to this definition")

Return a list of the sections available; the _default section_ is not included in the list.

add\_section(_section_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.add_section "Link to this definition")

Add a section named _section_ to the instance. If a section by the given name already exists, [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError")
 is raised. If the _default section_ name is passed, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. The name of the section must be a string; if not, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

Changed in version 3.2: Non-string section names raise [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
.

has\_section(_section_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.has_section "Link to this definition")

Indicates whether the named _section_ is present in the configuration. The _default section_ is not acknowledged.

options(_section_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.options "Link to this definition")

Return a list of options available in the specified _section_.

has\_option(_section_, _option_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.has_option "Link to this definition")

If the given _section_ exists, and contains the given _option_, return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
; otherwise return [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
. If the specified _section_ is [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 or an empty string, DEFAULT is assumed.

read(_filenames_, _encoding\=None_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "Link to this definition")

Attempt to read and parse an iterable of filenames, returning a list of filenames which were successfully parsed.

If _filenames_ is a string, a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object or a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
, it is treated as a single filename. If a file named in _filenames_ cannot be opened, that file will be ignored. This is designed so that you can specify an iterable of potential configuration file locations (for example, the current directory, the user’s home directory, and some system-wide directory), and all existing configuration files in the iterable will be read.

If none of the named files exist, the `ConfigParser` instance will contain an empty dataset. An application which requires initial values to be loaded from a file should load the required file or files using [`read_file()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_file "configparser.ConfigParser.read_file")
 before calling `read()` for any optional files:

Copy

import configparser, os

config \= configparser.ConfigParser()
config.read\_file(open('defaults.cfg'))
config.read(\['site.cfg', os.path.expanduser('~/.myapp.cfg')\],
            encoding\='cp1250')

Changed in version 3.2: Added the _encoding_ parameter. Previously, all files were read using the default encoding for [`open()`](https://docs.python.org/3/builtins/functions.html#open "open")
.

Changed in version 3.6.1: The _filenames_ parameter accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)
.

Changed in version 3.7: The _filenames_ parameter accepts a [`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
 object.

read\_file(_f_, _source\=None_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_file "Link to this definition")

Read and parse configuration data from _f_ which must be an iterable yielding Unicode strings (for example files opened in text mode).

Optional argument _source_ specifies the name of the file being read. If not given and _f_ has a `name` attribute, that is used for _source_; the default is `'<???>'`.

Added in version 3.2: Replaces `readfp()`.

read\_string(_string_, _source\='<string>'_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_string "Link to this definition")

Parse configuration data from a string.

Optional argument _source_ specifies a context-specific name of the string passed. If not given, `'<string>'` is used. This should commonly be a filesystem path or a URL.

Added in version 3.2.

read\_dict(_dictionary_, _source\='<dict>'_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict "Link to this definition")

Load configuration from any object that provides a dict-like `items()` method. Keys are section names, values are dictionaries with keys and values that should be present in the section. If the used dictionary type preserves order, sections and their keys will be added in order. Values are automatically converted to strings.

Optional argument _source_ specifies a context-specific name of the dictionary passed. If not given, `<dict>` is used.

This method can be used to copy state between parsers.

Added in version 3.2.

get(_section_, _option_, _\*_, _raw\=False_, _vars\=None_\[, _fallback_\])[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "Link to this definition")

Get an _option_ value for the named _section_. If _vars_ is provided, it must be a dictionary. The _option_ is looked up in _vars_ (if provided), _section_, and in _DEFAULTSECT_ in that order. If the key is not found and _fallback_ is provided, it is used as a fallback value. `None` can be provided as a _fallback_ value.

All the `'%'` interpolations are expanded in the return values, unless the _raw_ argument is true. Values for interpolation keys are looked up in the same manner as the option.

Changed in version 3.2: Arguments _raw_, _vars_ and _fallback_ are keyword only to protect users from trying to use the third argument as the _fallback_ fallback (especially when using the mapping protocol).

getint(_section_, _option_, _\*_, _raw\=False_, _vars\=None_\[, _fallback_\])[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "Link to this definition")

A convenience method which coerces the _option_ in the specified _section_ to an integer. See [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 for explanation of _raw_, _vars_ and _fallback_.

getfloat(_section_, _option_, _\*_, _raw\=False_, _vars\=None_\[, _fallback_\])[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "Link to this definition")

A convenience method which coerces the _option_ in the specified _section_ to a floating-point number. See [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 for explanation of _raw_, _vars_ and _fallback_.

getboolean(_section_, _option_, _\*_, _raw\=False_, _vars\=None_\[, _fallback_\])[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "Link to this definition")

A convenience method which coerces the _option_ in the specified _section_ to a Boolean value. Note that the accepted values for the option are `'1'`, `'yes'`, `'true'`, and `'on'`, which cause this method to return `True`, and `'0'`, `'no'`, `'false'`, and `'off'`, which cause it to return `False`. These string values are checked in a case-insensitive manner. Any other value will cause it to raise [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
. See [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 for explanation of _raw_, _vars_ and _fallback_.

items(_raw\=False_, _vars\=None_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.items "Link to this definition")

items(_section_, _raw\=False_, _vars\=None_)

When _section_ is not given, return a list of _section\_name_, _section\_proxy_ pairs, including DEFAULTSECT.

Otherwise, return a list of _name_, _value_ pairs for the options in the given _section_. Optional arguments have the same meaning as for the [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 method.

Changed in version 3.8: Items present in _vars_ no longer appear in the result. The previous behaviour mixed actual parser options with variables provided for interpolation.

set(_section_, _option_, _value_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.set "Link to this definition")

If the given section exists, set the given option to the specified value; otherwise raise [`NoSectionError`](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "configparser.NoSectionError")
. _option_ and _value_ must be strings; if not, [`TypeError`](https://docs.python.org/3/builtins/exceptions.html#TypeError "TypeError")
 is raised.

write(_fileobject_, _space\_around\_delimiters\=True_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.write "Link to this definition")

Write a representation of the configuration to the specified [file object](https://docs.python.org/3/glossary.html#term-file-object)
, which must be opened in text mode (accepting strings). This representation can be parsed by a future [`read()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "configparser.ConfigParser.read")
 call. If _space\_around\_delimiters_ is true, delimiters between keys and values are surrounded by spaces.

Changed in version 3.14: Raises InvalidWriteError if this would write a representation which cannot be accurately parsed by a future [`read()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "configparser.ConfigParser.read")
 call from this parser.

Note

Comments in the original configuration file are not preserved when writing the configuration back. What is considered a comment, depends on the given values for _comment\_prefixes_ and _inline\_comment\_prefixes_.

remove\_option(_section_, _option_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.remove_option "Link to this definition")

Remove the specified _option_ from the specified _section_. If the section does not exist, raise [`NoSectionError`](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "configparser.NoSectionError")
. If the option existed to be removed, return [`True`](https://docs.python.org/3/builtins/constants.html#True "True")
; otherwise return [`False`](https://docs.python.org/3/builtins/constants.html#False "False")
.

remove\_section(_section_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.remove_section "Link to this definition")

Remove the specified _section_ from the configuration. If the section in fact existed, return `True`. Otherwise return `False`.

optionxform(_option_)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.optionxform "Link to this definition")

Transforms the option name _option_ as found in an input file or as passed in by client code to the form that should be used in the internal structures. The default implementation returns a lower-case version of _option_; subclasses may override this or client code can set an attribute of this name on instances to affect this behavior.

You don’t need to subclass the parser to use this method, you can also set it on an instance, to a function that takes a string argument and returns a string. Setting it to `str`, for example, would make option names case sensitive:

Copy

cfgparser \= ConfigParser()
cfgparser.optionxform \= str

Note that when reading configuration files, whitespace around the option names is stripped before `optionxform()` is called.

configparser.UNNAMED\_SECTION[¶](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "Link to this definition")

A special object representing a section name used to reference the unnamed section (see [Unnamed Sections](https://docs.python.org/3/library/configparser.html#unnamed-sections)
).

configparser.MAX\_INTERPOLATION\_DEPTH[¶](https://docs.python.org/3/library/configparser.html#configparser.MAX_INTERPOLATION_DEPTH "Link to this definition")

The maximum depth for recursive interpolation for [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get")
 when the _raw_ parameter is false. This is relevant only when the default _interpolation_ is used.

RawConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#rawconfigparser-objects "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

class configparser.RawConfigParser(_defaults\=None_, _dict\_type\=dict_, _allow\_no\_value\=False_, _\*_, _delimiters\=('=', ':')_, _comment\_prefixes\=('#', ';')_, _inline\_comment\_prefixes\=None_, _strict\=True_, _empty\_lines\_in\_values\=True_, _default\_section\=configparser.DEFAULTSECT_, _interpolation\=BasicInterpolation()_, _converters\={}_, _allow\_unnamed\_section\=False_)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "Link to this definition")

Legacy variant of the [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
. It has interpolation disabled by default and allows for non-string section names, option names, and values via its unsafe `add_section` and `set` methods, as well as the legacy `defaults=` keyword argument handling.

Changed in version 3.2: _allow\_no\_value_, _delimiters_, _comment\_prefixes_, _strict_, _empty\_lines\_in\_values_, _default\_section_ and _interpolation_ were added.

Changed in version 3.5: The _converters_ argument was added.

Changed in version 3.8: The default _dict\_type_ is [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict "dict")
, since it now preserves insertion order.

Changed in version 3.13: The _allow\_unnamed\_section_ argument was added.

Note

Consider using [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 instead which checks types of the values to be stored internally. If you don’t want interpolation, you can use `ConfigParser(interpolation=None)`.

add\_section(_section_)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser.add_section "Link to this definition")

Add a section named _section_ or [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
 to the instance.

If the given section already exists, [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError")
 is raised. If the _default section_ name is passed, [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError "ValueError")
 is raised. If [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
 is passed and support is disabled, [`UnnamedSectionDisabledError`](https://docs.python.org/3/library/configparser.html#configparser.UnnamedSectionDisabledError "configparser.UnnamedSectionDisabledError")
 is raised.

Type of _section_ is not checked which lets users create non-string named sections. This behaviour is unsupported and may cause internal errors.

Changed in version 3.14: Added support for [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
.

set(_section_, _option_, _value_)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser.set "Link to this definition")

If the given section exists, set the given option to the specified value; otherwise raise [`NoSectionError`](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "configparser.NoSectionError")
. While it is possible to use `RawConfigParser` (or [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser")
 with _raw_ parameters set to true) for _internal_ storage of non-string values, full functionality (including interpolation and output to files) can only be achieved using string values.

This method lets users assign non-string values to keys internally. This behaviour is unsupported and will cause errors when attempting to write to a file or get it in non-raw mode. **Use the mapping protocol API** which does not allow such assignments to take place.

Exceptions[¶](https://docs.python.org/3/library/configparser.html#exceptions "Link to this heading")

-----------------------------------------------------------------------------------------------------

exception configparser.Error[¶](https://docs.python.org/3/library/configparser.html#configparser.Error "Link to this definition")

Base class for all other `configparser` exceptions.

exception configparser.NoSectionError[¶](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "Link to this definition")

Exception raised when a specified section is not found.

exception configparser.DuplicateSectionError[¶](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "Link to this definition")

Exception raised if [`add_section()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.add_section "configparser.ConfigParser.add_section")
 is called with the name of a section that is already present or in strict parsers when a section if found more than once in a single input file, string or dictionary.

Changed in version 3.2: Added the optional _source_ and _lineno_ attributes and parameters to `__init__()`.

exception configparser.DuplicateOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.DuplicateOptionError "Link to this definition")

Exception raised by strict parsers if a single option appears twice during reading from a single file, string or dictionary. This catches misspellings and case sensitivity-related errors, e.g. a dictionary may have two keys representing the same case-insensitive configuration key.

exception configparser.NoOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.NoOptionError "Link to this definition")

Exception raised when a specified option is not found in the specified section.

exception configparser.InterpolationError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "Link to this definition")

Base class for exceptions raised when problems occur performing string interpolation.

exception configparser.InterpolationDepthError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationDepthError "Link to this definition")

Exception raised when string interpolation cannot be completed because the number of iterations exceeds [`MAX_INTERPOLATION_DEPTH`](https://docs.python.org/3/library/configparser.html#configparser.MAX_INTERPOLATION_DEPTH "configparser.MAX_INTERPOLATION_DEPTH")
. Subclass of [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError")
.

exception configparser.InterpolationMissingOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationMissingOptionError "Link to this definition")

Exception raised when an option referenced from a value does not exist. Subclass of [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError")
.

exception configparser.InterpolationSyntaxError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationSyntaxError "Link to this definition")

Exception raised when the source text into which substitutions are made does not conform to the required syntax. Subclass of [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError")
.

exception configparser.MissingSectionHeaderError[¶](https://docs.python.org/3/library/configparser.html#configparser.MissingSectionHeaderError "Link to this definition")

Exception raised when attempting to parse a file which has no section headers.

exception configparser.ParsingError[¶](https://docs.python.org/3/library/configparser.html#configparser.ParsingError "Link to this definition")

Exception raised when errors occur attempting to parse a file.

Changed in version 3.12: The `filename` attribute and `__init__()` constructor argument were removed. They have been available using the name `source` since 3.2.

exception configparser.MultilineContinuationError[¶](https://docs.python.org/3/library/configparser.html#configparser.MultilineContinuationError "Link to this definition")

Exception raised when a key without a corresponding value is continued with an indented line.

Added in version 3.13.

exception configparser.UnnamedSectionDisabledError[¶](https://docs.python.org/3/library/configparser.html#configparser.UnnamedSectionDisabledError "Link to this definition")

Exception raised when attempting to use the [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION")
 without enabling it.

> Added in version 3.14.

exception configparser.InvalidWriteError[¶](https://docs.python.org/3/library/configparser.html#configparser.InvalidWriteError "Link to this definition")

Exception raised when an attempted [`ConfigParser.write()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.write "configparser.ConfigParser.write")
 would not be parsed accurately with a future [`ConfigParser.read()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read "configparser.ConfigParser.read")
 call.

Ex: Writing a key beginning with the [`ConfigParser.SECTCRE`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.SECTCRE "configparser.ConfigParser.SECTCRE")
 pattern would parse as a section header when read. Attempting to write this will raise this exception.

Added in version 3.14.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html#)
    *   [Quick Start](https://docs.python.org/3/library/configparser.html#quick-start)
        
    *   [Supported Datatypes](https://docs.python.org/3/library/configparser.html#supported-datatypes)
        
    *   [Fallback Values](https://docs.python.org/3/library/configparser.html#fallback-values)
        
    *   [Supported INI File Structure](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure)
        
    *   [Unnamed Sections](https://docs.python.org/3/library/configparser.html#unnamed-sections)
        
    *   [Interpolation of values](https://docs.python.org/3/library/configparser.html#interpolation-of-values)
        
    *   [Mapping Protocol Access](https://docs.python.org/3/library/configparser.html#mapping-protocol-access)
        
    *   [Customizing Parser Behaviour](https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour)
        
    *   [Legacy API Examples](https://docs.python.org/3/library/configparser.html#legacy-api-examples)
        
    *   [ConfigParser Objects](https://docs.python.org/3/library/configparser.html#configparser-objects)
        
    *   [RawConfigParser Objects](https://docs.python.org/3/library/configparser.html#rawconfigparser-objects)
        
    *   [Exceptions](https://docs.python.org/3/library/configparser.html#exceptions)
        

#### Previous topic

[`csv` — CSV file reading and writing](https://docs.python.org/3/library/csv.html "previous chapter")

#### Next topic

[`tomllib` — Parse TOML files](https://docs.python.org/3/library/tomllib.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=configparser+%E2%80%94+Configuration+file+parser&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fconfigparser.html&pagesource=library%2Fconfigparser.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/configparser.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/tomllib.html "tomllib — Parse TOML files")
     |
*   [previous](https://docs.python.org/3/library/csv.html "csv — CSV file reading and writing")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [File Formats](https://docs.python.org/3/library/fileformats.html)
     »
*   [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html)
    
*    
    
    |
*   Theme Auto Light Dark |