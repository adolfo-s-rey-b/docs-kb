*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#mdn-search)
    

SyntaxError: missing : after property id
========================================

The JavaScript exception "missing : after property id" occurs when objects are created using the [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 syntax. A colon (`:`) separates keys and values for the object's properties. Somehow, this colon is missing or misplaced.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#message)

----------------------------------------------------------------------------------------------------------------------------

SyntaxError: Invalid shorthand property initializer (V8-based)
SyntaxError: missing : after property id (Firefox)
SyntaxError: Unexpected token '='. Expected a ':' following the property name 'x'. (Safari)
SyntaxError: Unexpected token '+'. Expected an identifier as property name. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#error_type)

----------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------------------

When creating objects with the [object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
 syntax, a colon (`:`) separates keys and values for the object's properties.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#examples)

------------------------------------------------------------------------------------------------------------------------------

### [Colons vs. equal signs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#colons_vs._equal_signs)

This code fails, as the equal sign can't be used this way in this object initializer syntax.

Correct would be to use a colon, or to use square brackets to assign a new property after the object has been created already.

Or alternatively:

### [Computed properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#computed_properties)

If you create a property key from an expression, you need to use square brackets. Otherwise the property name can't be computed:

Put the expression in square brackets `[]`:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id#see_also)

------------------------------------------------------------------------------------------------------------------------------

*   [Object initializer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_colon_after_property_id/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/missing_colon_after_property_id/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/missing_colon_after_property_id (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_colon_after_property_id&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_colon_after_property_id%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_colon_after_property_id%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_colon_after_property_id%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")