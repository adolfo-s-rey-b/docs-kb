*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#mdn-search)
    

`<meta name="color-scheme">` HTML attribute value
=================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color-scheme`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element indicates a suggested color scheme that user agents should use for a page. If specified, you define the color scheme using a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute in the `<meta>` element with a valid CSS [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
 value.

The theme color works at the _document level_ in the same way that the CSS [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
 property specifies the preferred and accepted color schemes of _individual elements_. The primary use for `<meta name="color-scheme">` is to indicate compatibility and order of preference for light and dark color modes. For example, to indicate that a document prefers dark mode but also supports light mode:

Your styles can adapt to the current color scheme using the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 CSS media feature.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#usage_notes)

-----------------------------------------------------------------------------------------------------------------------

A `<meta name="color-scheme">` element has the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

A `<meta>` element with `name=color-scheme` must have a `content` attribute that defines the color scheme as a CSS [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
 value. The `content` attribute may be one of the following:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#normal)

The document is unaware of color schemes and should be rendered using the default color palette.

[`light`, `dark`, `light dark`, `dark light`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#light)

One or more color schemes supported by the document. Multiple color schemes indicates that the first scheme is preferred by the document, but that the second scheme is acceptable if the user prefers it. Specifying the same color scheme multiple times has the same effect as specifying it once.

[`only light`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#only_light)

Indicates that the document _only_ supports light mode, with a light background and dark foreground colors. `only dark` _is invalid_, because forcing a document to render in dark mode when it isn't compatible can result in unreadable content and all major browsers default to light mode if not otherwise configured.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#examples)

-----------------------------------------------------------------------------------------------------------------

### [Using a color-scheme keyword](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#using_a_color-scheme_keyword)

The following example indicates to the browser that the page supports both light and dark themes. Whether the light or dark color scheme is used depends on user preferences such as OS-level settings or the browser settings:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# meta-color-scheme](https://html.spec.whatwg.org/multipage/semantics.html#meta-color-scheme) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     CSS property
*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
     media query

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/color-scheme/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/color-scheme (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Fcolor-scheme&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Fcolor-scheme%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Fcolor-scheme%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Fcolor-scheme%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3a7da595860e07c871e243e58a8fe8b7043e305a%0A*+Document+last+modified%3A+2026-08-18T03%3A46%3A56.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")