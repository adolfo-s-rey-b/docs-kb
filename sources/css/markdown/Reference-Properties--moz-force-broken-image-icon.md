*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#mdn-search)
    

`-moz-force-broken-image-icon` CSS property
===========================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`-moz-force-broken-image-icon`** extended CSS property can be used to force the broken image icon to be shown even when a broken image has an `alt` attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#syntax)

--------------------------------------------------------------------------------------------------------------------

css

    -moz-force-broken-image-icon: 1;
    -moz-force-broken-image-icon: 0;
    
    /* Global values */
    -moz-force-broken-image-icon: inherit;
    -moz-force-broken-image-icon: initial;
    -moz-force-broken-image-icon: revert;
    -moz-force-broken-image-icon: revert-layer;
    -moz-force-broken-image-icon: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#values)

This property is specified as the following value:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

A value of `1` means that the broken image icon is shown even if the image has an [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alt)
 attribute. When the value `0` is used, the image will act as usual and only display the `alt` attribute.

**Note:** Even if the value is set to `1` the `alt` attribute will still be displayed, alongside the broken image icon.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | images |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------------

\-moz-force-broken-image-icon =   
  <integer>    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#examples)

------------------------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#html)

html

    <img src="/broken/image/link.png" alt="Broken image link" />
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#css)

css

    img {
      -moz-force-broken-image-icon: 1;
      height: 100px;
      width: 100px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#result)

**Note:** The alt text may not be visible if `-moz-force-broken-image-icon` is set to `1` and the image has no (or too small) `height` or `width` set.

[Notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#notes)

------------------------------------------------------------------------------------------------------------------

*   This property will only work in Gecko-based browsers.
*   The use of this property is not recommended. A proper `alt` attribute should be used instead.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#specifications)

------------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon#see_also)

------------------------------------------------------------------------------------------------------------------------

*   [Firefox bug 58646](https://bugzil.la/58646 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-moz-force-broken-image-icon/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-moz-force-broken-image-icon (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-force-broken-image-icon&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-force-broken-image-icon%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-force-broken-image-icon%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-force-broken-image-icon%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")