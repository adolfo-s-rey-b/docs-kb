*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#mdn-search)
    

Comments
========

A CSS **comment** is used to add explanatory notes to the code or to prevent the browser from interpreting specific parts of the style sheet. By design, comments have no effect on the layout of a document.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#syntax)

-----------------------------------------------------------------------------------------

Comments can be placed wherever white space is allowed within a style sheet. They can be used on a single line, or traverse multiple lines.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#examples)

---------------------------------------------------------------------------------------------

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#notes)

---------------------------------------------------------------------------------------

The `/* */` comment syntax is used for both single and multiline comments. There is no other way to specify comments in external style sheets. However, when using the [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 element, you may use `<!-- -->` to hide CSS from older browsers, although this is not recommended. As with most programming languages that use the `/* */` comment syntax, comments cannot be nested. In other words, the first instance of `*/` that follows an instance of `/*` closes the comment.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Syntax Module Level 3  <br>\# consume-comment](https://drafts.csswg.org/css-syntax-3/#consume-comment) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments#see_also)

---------------------------------------------------------------------------------------------

*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
     module
*   [Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
     guide
*   [CSS error handling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/syntax/comments/index.md?plain=1 "Folder: en-us/web/css/guides/syntax/comments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FComments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fcomments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FComments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fcomments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")