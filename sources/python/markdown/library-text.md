### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/string.html "string — Common string operations")
     |
*   [previous](https://docs.python.org/3/library/intro.html "Introduction")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Text Processing Services[¶](https://docs.python.org/3/library/text.html#text-processing-services "Link to this heading")

=========================================================================================================================

The modules described in this chapter provide a wide range of string manipulation operations and other text processing services.

The [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.")
 module described under [Binary Data Services](https://docs.python.org/3/library/binary.html#binaryservices)
 is also highly relevant to text processing. In addition, see the documentation for Python’s built-in string type in [Text Sequence Type — str](https://docs.python.org/3/builtins/stdtypes.html#textseq)
.

*   [`string` — Common string operations](https://docs.python.org/3/library/string.html)
    *   [String constants](https://docs.python.org/3/library/string.html#string-constants)
        
    *   [Custom string formatting](https://docs.python.org/3/library/string.html#custom-string-formatting)
        
    *   [Format string syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
        *   [Format specification mini-language](https://docs.python.org/3/library/string.html#format-specification-mini-language)
            
        *   [Format examples](https://docs.python.org/3/library/string.html#format-examples)
            
    *   [Template strings ($-strings)](https://docs.python.org/3/library/string.html#template-strings-strings)
        
    *   [Helper functions](https://docs.python.org/3/library/string.html#helper-functions)
        
*   [`string.templatelib` — Support for template string literals](https://docs.python.org/3/library/string.templatelib.html)
    *   [Template strings](https://docs.python.org/3/library/string.templatelib.html#template-strings)
        
    *   [Types](https://docs.python.org/3/library/string.templatelib.html#types)
        
    *   [Helper functions](https://docs.python.org/3/library/string.templatelib.html#helper-functions)
        
*   [`re` — Regular expression operations](https://docs.python.org/3/library/re.html)
    *   [Regular expression syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax)
        *   [Special characters](https://docs.python.org/3/library/re.html#special-characters)
            
        *   [Special sequences](https://docs.python.org/3/library/re.html#special-sequences)
            
        *   [Standard escapes](https://docs.python.org/3/library/re.html#standard-escapes)
            
    *   [Module contents](https://docs.python.org/3/library/re.html#module-contents)
        *   [Flags](https://docs.python.org/3/library/re.html#flags)
            
        *   [Functions](https://docs.python.org/3/library/re.html#functions)
            
        *   [Exceptions](https://docs.python.org/3/library/re.html#exceptions)
            
    *   [Regular expression objects](https://docs.python.org/3/library/re.html#regular-expression-objects)
        
    *   [Match objects](https://docs.python.org/3/library/re.html#match-objects)
        
    *   [Regular expression examples](https://docs.python.org/3/library/re.html#regular-expression-examples)
        *   [Checking for a pair](https://docs.python.org/3/library/re.html#checking-for-a-pair)
            
        *   [Simulating scanf()](https://docs.python.org/3/library/re.html#simulating-scanf)
            
        *   [search() vs. prefixmatch()](https://docs.python.org/3/library/re.html#search-vs-prefixmatch)
            
        *   [prefixmatch() vs. match()](https://docs.python.org/3/library/re.html#prefixmatch-vs-match)
            
        *   [Making a phonebook](https://docs.python.org/3/library/re.html#making-a-phonebook)
            
        *   [Text munging](https://docs.python.org/3/library/re.html#text-munging)
            
        *   [Finding all adverbs](https://docs.python.org/3/library/re.html#finding-all-adverbs)
            
        *   [Finding all adverbs and their positions](https://docs.python.org/3/library/re.html#finding-all-adverbs-and-their-positions)
            
        *   [Raw string notation](https://docs.python.org/3/library/re.html#raw-string-notation)
            
        *   [Writing a tokenizer](https://docs.python.org/3/library/re.html#writing-a-tokenizer)
            
*   [`difflib` — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)
    *   [Junk heuristic](https://docs.python.org/3/library/difflib.html#junk-heuristic)
        
    *   [The `difflib` algorithm](https://docs.python.org/3/library/difflib.html#the-difflib-algorithm)
        
    *   [Diff generation](https://docs.python.org/3/library/difflib.html#diff-generation)
        
    *   [Junk definition functions](https://docs.python.org/3/library/difflib.html#junk-definition-functions)
        
    *   [SequenceMatcher objects](https://docs.python.org/3/library/difflib.html#sequencematcher-objects)
        
    *   [Examples](https://docs.python.org/3/library/difflib.html#examples)
        *   [SequenceMatcher examples](https://docs.python.org/3/library/difflib.html#sequencematcher-examples)
            
        *   [Differ example](https://docs.python.org/3/library/difflib.html#differ-example)
            
        *   [A command-line interface to difflib](https://docs.python.org/3/library/difflib.html#a-command-line-interface-to-difflib)
            
        *   [ndiff example](https://docs.python.org/3/library/difflib.html#ndiff-example)
            
*   [`textwrap` — Text wrapping and filling](https://docs.python.org/3/library/textwrap.html)
    
*   [`unicodedata` — Unicode Database](https://docs.python.org/3/library/unicodedata.html)
    
*   [`stringprep` — Internet String Preparation](https://docs.python.org/3/library/stringprep.html)
    
*   [`readline` — GNU readline interface](https://docs.python.org/3/library/readline.html)
    *   [Init file](https://docs.python.org/3/library/readline.html#init-file)
        
    *   [Line buffer](https://docs.python.org/3/library/readline.html#line-buffer)
        
    *   [History file](https://docs.python.org/3/library/readline.html#history-file)
        
    *   [History list](https://docs.python.org/3/library/readline.html#history-list)
        
    *   [Startup hooks](https://docs.python.org/3/library/readline.html#startup-hooks)
        
    *   [Completion](https://docs.python.org/3/library/readline.html#completion)
        
    *   [Example](https://docs.python.org/3/library/readline.html#example)
        
*   [`rlcompleter` — Completion function for GNU readline](https://docs.python.org/3/library/rlcompleter.html)
    

#### Previous topic

[Introduction](https://docs.python.org/3/library/intro.html "previous chapter")

#### Next topic

[`string` — Common string operations](https://docs.python.org/3/library/string.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Text+Processing+Services&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ftext.html&pagesource=library%2Ftext.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/text.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/string.html "string — Common string operations")
     |
*   [previous](https://docs.python.org/3/library/intro.html "Introduction")
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
*   [Text Processing Services](https://docs.python.org/3/library/text.html)
    
*    
    
    |
*   Theme Auto Light Dark |