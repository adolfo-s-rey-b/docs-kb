*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#mdn-search)
    

`element()` CSS function
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/297)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#browser_compatibility)
 carefully before using this in production.

The **`element()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 defines an [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value generated from an arbitrary HTML element. This image is live, meaning that if the HTML element is changed, the CSS properties using the resulting value are automatically updated.

A particularly useful scenario for using this would be to render an image in an HTML [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element, then use that as a background.

On Gecko browsers, you can use the non-standard [`document.mozSetImageElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/mozSetImageElement)
 method to change the element being used as the background for a given CSS background element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#syntax)

-------------------------------------------------------------------------------------------

css

    element(id)
    

where:

[_id_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#id)

The ID of an element to use as the background, specified using the HTML attribute #_id_ on the element.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#formal_syntax)

---------------------------------------------------------------------------------------------------------

<element()> =   
  element( <id-selector> )    
  
<id-selector> =   
  <hash-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#examples)

-----------------------------------------------------------------------------------------------

These examples work in builds of Firefox that support `-moz-element()`.

### [A somewhat realistic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#a_somewhat_realistic_example)

This example uses a hidden [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 as a background. The background element uses a gradient, but also includes text that is rendered as part of the background.

html

    <div id="target-box">
      <p>This box uses the element with the #my-background ID as its background!</p>
    </div>
    
    <div id="background-container">
      <div id="my-background">
        <p>This text is part of the background. Cool, huh?</p>
      </div>
    </div>
    

css

    #target-box {
      width: 400px;
      height: 400px;
      background: -moz-element(#my-background) no-repeat;
    }
    
    #background-container {
      overflow: hidden;
      height: 0;
    }
    
    #my-background {
      width: 1024px;
      height: 1024px;
      background-image: linear-gradient(to right, red, orange, yellow, white);
    }
    
    #my-background p {
      transform-origin: 0 0;
      rotate: 45deg;
      color: white;
    }
    

The [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with the ID "my-background" is used as the background for the content including the paragraph "This box uses the element with the #my-background ID as its background!".

### [Page Preview](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#page_preview)

This [example based on Vincent De Oliveira's](https://iamvdo.me/en/blog/css-element-function "External link (opens in new tab)")
 creates a preview of the `<div id="css-source">` inside `<div id="css-result">`.

#### HTML

html

    <div id="css-source">
      <h1>Page Preview</h1>
    </div>
    <div id="css-result"></div>
    

#### CSS

css

    #css-result {
      background: -moz-element(#css-source) no-repeat;
      width: 256px;
      height: 32px;
      background-size: 80%;
      border: dashed;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 4  <br>\# element-notation](https://drafts.csswg.org/css-images-4/#element-notation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element#see_also)

-----------------------------------------------------------------------------------------------

*   [`image()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`image-set()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`<gradient>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`cross-fade()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    
*   [`document.mozSetImageElement()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/mozSetImageElement)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/element/index.md?plain=1 "Folder: en-us/web/css/reference/values/element (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Felement&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Felement%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Felement%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Felement%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")