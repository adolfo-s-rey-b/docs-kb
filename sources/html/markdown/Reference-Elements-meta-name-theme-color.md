*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#mdn-search)
    

`<meta name="theme-color">` HTML attribute value
================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/145)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`theme-color`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element indicates a suggested color that user agents should use to customize the display of the page or of the surrounding user interface. If specified, you define a theme color using a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute in the `<meta>` element as a CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

For example, to indicate that a document should use `cornflowerblue` as a theme color, set the `<meta>` as:

To set the media to which the theme color metadata applies, include the [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#media)
 attribute with a valid media query list (see the [`theme-color` media query example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#using_a_media_query_with_theme-color)
).

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#usage_notes)

----------------------------------------------------------------------------------------------------------------------

A `<meta name="theme-color">` element has the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

A `<meta>` element with `name=theme-color` must have a `content` attribute that defines the theme color. The value of `content` attribute is as follows:

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value

A valid color value, such as hexadecimal, RGB, named color, etc.

[`media` Optional](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#media)

Any valid media type or query. If provided, the options for the document's theme color defined in the `content` attribute are suggested to the browser when the media query matches.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#examples)

----------------------------------------------------------------------------------------------------------------

### [Setting a color value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#setting_a_color_value)

Consider the following code that uses `<meta>` to set a theme color:

The following image shows the effect of this setting in Chrome on an Android mobile device:

![Image showing the effect of using theme-color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color/theme-color.png)

_Image credit: from [Icons & Browser Colors](https://web.dev/articles/icons-and-browser-colors "External link (opens in new tab)")
, created and shared by Google and used according to terms described in the [Creative Commons 4.0 Attribution License](https://creativecommons.org/licenses/by/4.0/ "External link (opens in new tab)")
._

### [Using a media query with `theme-color`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#using_a_media_query_with_theme-color)

You can provide a media type or query inside the [`media`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#media)
 attribute. The `theme-color` will then only be set if the media condition is true. For example:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# meta-theme-color](https://html.spec.whatwg.org/multipage/semantics.html#meta-theme-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color#see_also)

----------------------------------------------------------------------------------------------------------------

*   `<meta>` `name` attribute [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme)
     value
*   [`color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
     CSS property
*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
     media query

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/theme-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/theme-color/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/theme-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Ftheme-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Ftheme-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Ftheme-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Ftheme-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf5017c389132af39b50106cf1763fa7106e87b4%0A*+Document+last+modified%3A+2026-04-22T15%3A05%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")