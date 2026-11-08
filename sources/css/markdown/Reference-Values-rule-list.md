*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#mdn-search)
    

`<rule-list>` CSS type
======================

The **`<rule-list>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 represents a sequence of **zero or more CSS rules**. It is used to define places in CSS where multiple rules may appear, such as the top level of a stylesheet or inside grouping at-rules like `@media` or `@supports`.

A `<rule-list>` is not written directly. Instead, it describes how the CSS parser collects and interprets rules inside a block or stylesheet.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#syntax)

---------------------------------------------------------------------------------------------

A `<rule-list>` is defined as a sequence of **zero or more**:

*   **Style rules** (e.g., `p { color: red; }`).
*   **Qualified at-rules** (e.g., `@media (width < 600px) { ... }`).
*   **Ignored statements** (e.g., parse errors handled by the parser, which the parser automatically skips).

All whitespace, comments, and invalid or malformed constructs are handled according to the CSS parser rules.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#description)

-------------------------------------------------------------------------------------------------------

The `<rule-list>` type appears in the specification anywhere CSS is defined to contain a "list of rules."

Examples include:

*   The **top level** of a stylesheet.
*   The body of **grouping at-rules** like `@media`, `@custom-media`, `@supports`, `@layer`, `@container`.
*   The contents of **nesting selectors** (CSS Nesting).

Although authors cannot explicitly write `<rule-list>`, understanding it is crucial when interpreting how CSS parses nested structures, how invalid rules are dropped, and how the cascade forms within conditional blocks.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#examples)

-------------------------------------------------------------------------------------------------

### [A `<rule-list>` in a stylesheet](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#a_rule-list_in_a_stylesheet)

The following stylesheet is treated as a `<rule-list>` containing two style rules and an at-rule.

css

    p {
      margin: 0;
    }
    
    h1 {
      font-size: 2rem;
    }
    
    @media (width < 600px) {
      body {
        background: lightgray;
      }
    }
    

### [A `<rule-list>` inside `@media` at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#a_rule-list_inside_media_at-rule)

The block contained inside an `@media` at-rule is a `<rule-list>` containing one or more style rules. The following example contains two style rules.

css

    @media (prefers-color-scheme: dark) {
      main {
        background: black;
        color: white;
      }
    
      a {
        color: skyblue;
      }
    }
    

### [Invalid rules inside a `<rule-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#invalid_rules_inside_a_rule-list)

The invalid token sequence (`!invalid-rule`) is ignored by the parser. The rest of the rules form a valid `<rule-list>`.

body {
  color: black;
}

!invalid-rule

@supports (display: grid) {
  section {
    display: grid;
  }
}

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Syntax Module Level 3  <br>\# typedef-rule-list](https://drafts.csswg.org/css-syntax-3/#typedef-rule-list) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list#see_also)

-------------------------------------------------------------------------------------------------

*   CSS [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
     at-rule
*   CSS [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     at-rule
*   CSS [`@custom-media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media)
     at-rule

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/rule-list/index.md?plain=1 "Folder: en-us/web/css/reference/values/rule-list (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frule-list&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frule-list%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frule-list%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frule-list%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")