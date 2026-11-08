*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#mdn-search)
    

`<style>` HTML style information element
========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<style>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element contains style information for a document, or part of a document. It contains CSS, which is applied to the contents of the document containing the `<style>` element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#try_it)

--------------------------------------------------------------------------------------------

    <style>
      p {
        color: #26b72b;
      }
      code {
        font-weight: bold;
      }
    </style>
    
    <p>
      This text will be green. Inline styles take precedence over CSS included
      externally.
    </p>
    
    <p style="color: blue">
      The <code>style</code> attribute can override it, though.
    </p>
    

    p {
      color: red;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`blocking`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#blocking)

This attribute explicitly indicates that certain operations should be blocked on the fetching of critical subresources and the application of the stylesheet to the document. [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
\-ed stylesheets are generally considered as critical subresources, whereas [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 and fonts are not. The operations that are to be blocked must be a space-separated list of blocking tokens listed below. Currently there is only one token:

*   `render`: The rendering of content on the screen is blocked.

**Note:** Only `style` elements in the document's `<head>` can possibly block rendering. By default, a `style` element in the `<head>` blocks rendering when the browser discovers it during parsing. If such a `style` element is added dynamically via script, you must additionally set `blocking = "render"` for it to block rendering.

[`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#media)

This attribute defines which media the style should be applied to. Its value is a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
, which defaults to `all` if the attribute is missing.

[`nonce`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#nonce)

A cryptographic [nonce](https://developer.mozilla.org/en-US/docs/Glossary/Nonce)
 (number used once) used to allow inline styles in a [style-src Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/style-src)
. The server must generate a unique nonce value each time it transmits a policy. It is critical to provide a nonce that cannot be guessed as bypassing a resource's policy is otherwise trivial.

[`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#title)

This attribute specifies [alternative style sheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet)
 sets.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#deprecated_attributes)

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#type)

This attribute should not be provided: if it is, the only permitted values are the empty string or a case-insensitive match for `text/css`.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#usage_notes)

------------------------------------------------------------------------------------------------------

The `<style>` element is typically included inside the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 of the document. It can also be used in the [template contents](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement/content)
 of a [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 element, which can include any elements. In the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
, it can be used as the first child of its parent element (see [Using `<style>` in the body](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#using_style_in_the_body)
).

If you include multiple `<style>` and `<link>` elements in your document, they will be applied to the DOM in the order they are included in the document — make sure you include them in the correct order, to avoid unexpected cascade issues.

In the same manner as `<link>` elements, `<style>` elements can include `media` attributes that contain [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
, allowing you to selectively apply internal stylesheets to your document depending on media features such as viewport width.

### [Using `<style>` in the body](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#using_style_in_the_body)

A `<style>` element can be used where flow content is expected, such as in the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
, as long as it is the first child of its parent element and its stylesheet only styles that parent element and its descendants:

*   Every style rule must be inside an [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
     rule without a scope root selector, such as `@scope { ... }` or `@scope to (.x) { ... }`. Such an `@scope` rule is scoped to the `<style>` element's parent. It can itself be nested inside rules such as [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    , [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
    , [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
    , [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    , or [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
    .
*   An `@scope` rule with a scope root selector, such as `@scope (.card) { ... }`, must likewise be nested inside an `@scope` rule without a scope root selector.
*   The stylesheet must not contain [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
     rules.

Browsers apply any `<style>` element in the body, but one that doesn't follow these rules is invalid HTML. The rules ensure that a `<style>` element in the body can't restyle content that the browser might already have rendered, other than its parent element.

At-rules such as [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
, [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
, and [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 define names for the whole document. To avoid restyling content that might already have been rendered, only use such names within the `<style>` element's parent, and pick names that aren't used elsewhere in the document.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#examples)

------------------------------------------------------------------------------------------------

### [A basic stylesheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#a_basic_stylesheet)

In the following example, we apply a short stylesheet to a document:

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta charset="UTF-8" />
        <title>Test page</title>
        <style>
          p {
            color: red;
          }
        </style>
      </head>
      <body>
        <p>This is my paragraph.</p>
      </body>
    </html>
    

#### Result

### [Using `<style>` inside `<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#using_style_inside_template)

A `<style>` element can also be placed inside a [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
 element. The styles remain inactive until the template content is instantiated and inserted into the document.

html

    <template id="card-template">
      <style>
        .card {
          border: 1px solid #cccccc;
          padding: 1rem;
          border-radius: 0.5rem;
        }
      </style>
    
      <div class="card">Template content</div>
    </template>
    

### [Multiple style elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#multiple_style_elements)

In this example we've included two `<style>` elements — notice how the conflicting declarations in the later `<style>` element override those in the earlier one, if they have equal [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta charset="UTF-8" />
        <title>Test page</title>
        <style>
          p {
            color: white;
            background-color: blue;
            padding: 5px;
            border: 1px solid black;
          }
        </style>
        <style>
          p {
            color: blue;
            background-color: yellow;
          }
        </style>
      </head>
      <body>
        <p>This is my paragraph.</p>
      </body>
    </html>
    

#### Result

### [Including a media query](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#including_a_media_query)

In this example we build on the previous one, including a `media` attribute on the second `<style>` element so it is only applied when the viewport is less than 500px in width.

html

    <!doctype html>
    <html lang="en-US">
      <head>
        <meta charset="UTF-8" />
        <title>Test page</title>
        <style>
          p {
            color: white;
            background-color: blue;
            padding: 5px;
            border: 1px solid black;
          }
        </style>
        <style media="(width < 500px)">
          p {
            color: blue;
            background-color: yellow;
          }
        </style>
      </head>
      <body>
        <p>This is my paragraph.</p>
      </body>
    </html>
    

#### Result

### [Scoped styles in the body](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#scoped_styles_in_the_body)

In this example, a `<style>` element is the first child of an [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)
 element. Its rules are inside an `@scope` rule without a scope root selector, so they only apply to the `<aside>` and its descendants.

html

    <aside>
      <style>
        @scope {
          :scope {
            background-color: lightyellow;
            padding: 0 1rem;
          }
          p {
            font-weight: bold;
          }
        }
      </style>
      <p>Did you know? Octopuses have three hearts.</p>
    </aside>
    <p>This paragraph isn't styled, because it's outside the aside.</p>
    

Adding a rule such as `p { margin: 0; }` outside the `@scope` rule would make the HTML invalid, because it isn't limited to the `<aside>`.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>, [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Permitted content | Text content matching the `type` attribute, that is `text/css`. |
| Tag omission | Neither tag is omissible. |
| Permitted parents | Any element that accepts [metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>. Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, as its first child. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLStyleElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLStyleElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-style-element](https://html.spec.whatwg.org/multipage/semantics.html#the-style-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style#see_also)

------------------------------------------------------------------------------------------------

*   The [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
     element, which allows us to apply external stylesheets to a document.
*   [Alternative Style Sheets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/alternate_stylesheet)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/style/index.md?plain=1 "Folder: en-us/web/html/reference/elements/style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fstyle&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fstyle%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fstyle%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fstyle%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb58d84c261b9cfa66d46a070ba205c53e18ee3e0%0A*+Document+last+modified%3A+2026-10-27T23%3A22%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")