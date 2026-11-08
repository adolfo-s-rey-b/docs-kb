*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#mdn-search)
    

`outline-offset` CSS property
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`outline-offset`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the amount of space between an [outline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 and the edge or border of an element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#try_it)

------------------------------------------------------------------------------------------------------

    outline-offset: 4px;
    

    outline-offset: 0.6rem;
    

    outline-offset: 12px;
    outline: 5px dashed blue;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        This is a box with an outline around it.
      </div>
    </section>
    

    #example-element {
      border: 2px solid crimson;
      outline: 0.75em solid;
      padding: 0.75em;
      width: 80%;
      height: 100px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#syntax)

------------------------------------------------------------------------------------------------------

css

    /* <length> values */
    outline-offset: 3px;
    outline-offset: 0.2em;
    
    /* Global values */
    outline-offset: inherit;
    outline-offset: initial;
    outline-offset: revert;
    outline-offset: revert-layer;
    outline-offset: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#values)

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The width of the space between the element and its outline. A negative value places the outline inside the element. A value of `0` places the outline so that there is no space between it and the element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#description)

----------------------------------------------------------------------------------------------------------------

An outline is a line that is drawn around an element, outside the border edge. The space between an element and its outline is transparent. In other words, it is the same as the parent element's background.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the absolute [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br>, snapped as a line width |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

outline-offset =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#examples)

----------------------------------------------------------------------------------------------------------

### [Setting outline offset in pixels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#setting_outline_offset_in_pixels)

#### HTML

html

    <p>Gallia est omnis divisa in partes tres.</p>
    

#### CSS

css

    p {
      outline: 1px dashed red;
      outline-offset: 10px;
      background: yellow;
      border: 1px solid blue;
      margin: 15px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# outline-offset](https://drafts.csswg.org/css-ui/#outline-offset) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset#see_also)

----------------------------------------------------------------------------------------------------------

*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/outline-offset/index.md?plain=1 "Folder: en-us/web/css/reference/properties/outline-offset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-offset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-offset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foutline-offset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foutline-offset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")