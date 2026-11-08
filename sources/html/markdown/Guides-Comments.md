*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#mdn-search)
    

Using HTML comments <!-- … -->
==============================

An HTML **comment** is used to add explanatory notes to the markup or to prevent the browser from interpreting specific parts of the document.

Comments start with the string `<!--` and end with the string `-->`, generally with text in between. This text cannot start with the string `>` or `->`, cannot contain the strings `-->` or `--!>`, nor end with the string `<!-`, though `<!` is allowed.

The browser ignores comments as it renders the code. In other words, they are not visible on the page - just in the code. HTML comments are a way for you to write helpful notes about your code or logic.

The above is true for [XML](https://developer.mozilla.org/en-US/docs/Web/XML)
 comments as well. In addition, in XML, such as in [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 or [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
 markup, a comment cannot contain the character sequence `--`.

Comments can be used on a single line, or span multiple lines. They can be used in the following places:

*   Before and after the [Doctype](https://developer.mozilla.org/en-US/docs/Glossary/Doctype)
    
*   Before and after the [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
     element
*   As the content of most elements except: [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    , [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    , [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
    , [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    , because these elements interpret their content as raw text

**Note:** While `<script>` elements should not have HTML comments and should use [JavaScript comments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)
 instead, there was a legacy practice to enclose the whole script content in an HTML comment so ancient browsers that don't support JavaScript don't render it as text. This is now a [legacy feature of JavaScript itself](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features#html_comments)
 and you should not rely on it.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#syntax)

-----------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#examples)

---------------------------------------------------------------------------------------

[Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#notes)

---------------------------------------------------------------------------------

HTML comments are only permitted as content. You cannot use it within a tag, such as before an HTML [attribute](https://developer.mozilla.org/en-US/docs/Glossary/Attribute)
.

As with most programming languages that use the `<!-- -->` comment syntax, comments cannot be nested. In other words, the first instance of `-->` that follows an instance of `<!--` closes the comment.

While comments do start with a `<` and end in a `>`, a comment is not an HTML element.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#specifications)

---------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# comments](https://html.spec.whatwg.org/multipage/syntax.html#comments) |

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments#see_also)

---------------------------------------------------------------------------------------

*   [Comments in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#comments)
    
*   [Comments in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments)
    
*   [`Comment`](https://developer.mozilla.org/en-US/docs/Web/API/Comment)
     API (`Comment` inherits from [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node)
    )

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Comments/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/guides/comments/index.md?plain=1 "Folder: en-us/web/html/guides/comments (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FComments&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fguides%2Fcomments%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FGuides%2FComments%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fguides%2Fcomments%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")