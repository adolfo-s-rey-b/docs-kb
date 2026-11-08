For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts.md)
.

n8n provides built-in methods and variables for working with data and accessing n8n data. This section provides a reference of available methods and variables for use in expressions, with a short description.

**Availability in the expressions editor and the Code node**

Not every method and variable in this reference works in the [Code node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
. The Code node runs plain JavaScript against native Luxon, not n8n's expression engine, so any entry marked **Source: Custom n8n functionality** on a reference page (for example, [`DateTime.format()`](https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime#datetimeformat)
) is an n8n-only extension that may not exist, or may behave differently, in the Code node.

If code in the Code node throws `... is not a function`, or silently produces the wrong result:

*   Check whether the method's reference entry is tagged **Custom n8n functionality**.
    
*   Look for a native Luxon or JavaScript equivalent. For example, use [`toFormat()`](https://moment.github.io/luxon/api-docs/index.html#datetimetoformat)
     instead of the n8n-only `DateTime.format()`.
    
*   Watch for methods that exist in both places but with different signatures, such as `DateTime.plus()`/`minus()`: n8n's expression version accepts `(amount, unit)`, while native Luxon's version only accepts a single Duration-like object (`{ days: 7 }`). Using the expression-style signature in the Code node won't error, but won't produce the expected result either.
    

All data transformation functions (the top-level helper functions listed in this section, such as `$if()` or `$jmespath()`) are only available in the expressions editor, not the Code node.

The [Cookbook](https://docs.n8n.io/build/code-in-n8n)
 contains examples for some common tasks, including some [Code node only](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
 functions.

In this section[](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts#in-this-section)

------------------------------------------------------------------------------------------------

*   [JMESPath](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath)
    : use the JMESPath library in n8n.
    
*   [HTTP node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/http-node)
    : methods for common tasks in HTTP Request node expressions.
    
*   [LangChain Code node](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/langchain-code-node)
    : methods for common tasks in the LangChain Code node.
    
*   [n8n metadata](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata)
    : methods for working with n8n metadata.
    

Related resources[](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts#related-resources)

----------------------------------------------------------------------------------------------------

*   [Code in n8n](https://docs.n8n.io/build/code-in-n8n)
    
*   [Using the Code node](https://docs.n8n.io/build/code-in-n8n/using-the-code-node)
    
*   [Get coding help from AI](https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai)
    
*   [Define custom variables](https://docs.n8n.io/build/code-in-n8n/define-custom-variables)
    
*   [Cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook)
    

[PreviousGet coding help from AI](https://docs.n8n.io/build/code-in-n8n/get-coding-help-from-ai)
[NextJMESPath](https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/jmespath)

Last updated 10 days ago

Was this helpful?