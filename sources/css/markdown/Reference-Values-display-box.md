*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#mdn-search)
    

`<display-box>` CSS type
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/296)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

These keywords define whether an element generates display boxes at all.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#syntax)

-----------------------------------------------------------------------------------------------

Valid `<display-box>` values:

[`contents`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#contents)

These elements don't produce a specific box by themselves. They are replaced by their pseudo-box and their child boxes. Please note that the CSS Display Level 3 spec defines how the `contents` value should affect "unusual elements" — elements that aren't rendered purely by CSS box concepts such as replaced elements. See [Appendix B: Effects of display: contents on Unusual Elements](https://drafts.csswg.org/css-display/#unbox "External link (opens in new tab)")
 for more details.

_Due to a bug in browsers this will currently remove the element from the accessibility tree — screen readers will not look at what's inside. See the [Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#accessibility)
 section below for more details._

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#none)

Turns off the display of an element so that it has no effect on layout (the document is rendered as though the element did not exist). All descendant elements also have their display turned off. To have an element take up the space that it would normally take, but without actually rendering anything, use the [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
 property instead.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#accessibility)

-------------------------------------------------------------------------------------------------------------

Current implementations in most browsers will remove from the [accessibility tree](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility#accessibility_apis)
 any element with a `display` value of `contents`. This will cause the element — and in some browser versions, its descendant elements — to no longer be announced by screen reading technology. This is incorrect behavior according to the [CSSWG specification](https://drafts.csswg.org/css-display/#the-display-properties "External link (opens in new tab)")
.

*   [More accessible markup with display: contents | Hidde de Vries](https://hidde.blog/more-accessible-markup-with-display-contents/ "External link (opens in new tab)")
    
*   [Display: Contents Is Not a CSS Reset | Adrian Roselli](https://adrianroselli.com/2018/05/display-contents-is-not-a-css-reset.html "External link (opens in new tab)")
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#formal_syntax)

-------------------------------------------------------------------------------------------------------------

<display-box> =   
  contents  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none        

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#examples)

---------------------------------------------------------------------------------------------------

In this first example, the paragraph with a class of secret is set to `display: none`; the box and any content is now not rendered.

### [display: none](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#display_none)

#### HTML

html

    <p>Visible text</p>
    <p class="secret">Invisible text</p>
    

#### CSS

css

    p.secret {
      display: none;
    }
    

#### Result

### [display: contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#display_contents)

In this example the outer [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 has a 2-pixel red border and a width of 300px. However it also has `display: contents` specified therefore this `<div>` will not be rendered, the border and width will no longer apply, and the child element will be displayed as if the parent had never existed.

#### HTML

html

    <div class="outer">
      <div>Inner div.</div>
    </div>
    

#### CSS

css

    .outer {
      border: 2px solid red;
      width: 300px;
      display: contents;
    }
    
    .outer > div {
      border: 1px solid green;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Display Module Level 3  <br>\# valdef-display-contents](https://drafts.csswg.org/css-display/#valdef-display-contents) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box#see_also)

---------------------------------------------------------------------------------------------------

*   [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    *   [`<display-outside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
        
    *   [`<display-inside>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
        
    *   [`<display-listitem>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
        
    *   [`<display-internal>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
        
    *   [`<display-legacy>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
        
*   [Display: Contents Is Not a CSS Reset | Adrian Roselli](https://adrianroselli.com/2018/05/display-contents-is-not-a-css-reset.html "External link (opens in new tab)")
    
*   [More accessible markup with display: contents](https://hidde.blog/more-accessible-markup-with-display-contents/ "External link (opens in new tab)")
     by Hidde de Vries (2018)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/display-box/index.md?plain=1 "Folder: en-us/web/css/reference/values/display-box (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-box&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-box%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdisplay-box%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdisplay-box%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")