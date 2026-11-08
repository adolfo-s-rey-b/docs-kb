*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#mdn-search)
    

`offset-distance` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`offset-distance`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a position along an [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 for an element to be placed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#try_it)

-------------------------------------------------------------------------------------------------------

    offset-distance: 0%;
    

    offset-distance: 80%;
    

    offset-distance: 50px;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #example-element {
      width: 24px;
      height: 24px;
      background: #2bc4a2;
      offset-path: path("M-70,-40 C-70,70 70,70 70,-40");
      clip-path: polygon(0% 0%, 70% 0%, 100% 50%, 70% 100%, 0% 100%, 30% 50%);
    }
    
    /* Provides a reference image of what path the element is following */
    #default-example {
      background-position: calc(50% - 12px) calc(50% + 14px);
      background-repeat: no-repeat;
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="-75 -45 150 140" width="150" height="140"><path d="M-70,-40 C-70,70 70,70 70,-40" fill="none" stroke="lightgrey" stroke-width="2" stroke-dasharray="4.5"/></svg>');
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Default value */
    offset-distance: 0;
    
    /* the middle of the offset-path */
    offset-distance: 50%;
    
    /* a fixed length positioned along the path */
    offset-distance: 40px;
    
    /* Global values */
    offset-distance: inherit;
    offset-distance: initial;
    offset-distance: revert;
    offset-distance: revert-layer;
    offset-distance: unset;
    

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

A length that specifies how far the element is along the path (defined with [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
).

100% represents the total length of the path (when the `offset-path` is defined as a basic shape or `path()`).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to the total path length |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | for [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)<br> the absolute value, otherwise a percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#interpolation "Values of the <length> CSS data type are interpolated as real, floating-point numbers.")<br>, [percentage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage#interpolation "Values of the <percentage> CSS data type are interpolated as real, floating-point numbers.")<br> or calc(); |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

offset-distance =   
  <length-percentage>    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#examples)

-----------------------------------------------------------------------------------------------------------

### [Using offset-distance in an animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#using_offset-distance_in_an_animation)

The motion aspect in CSS Motion Path typically comes from animating the `offset-distance` property. If you want to animate an element along its full path, you would define its [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 and then set up an animation that takes the `offset-distance` from `0%` to `100%`.

#### HTML

html

    <div id="motion-demo"></div>
    

#### CSS

css

    #motion-demo {
      offset-path: path("M20,20 C20,100 200,0 200,100");
      animation: move 3000ms infinite alternate ease-in-out;
      width: 40px;
      height: 40px;
      background: cyan;
    }
    
    @keyframes move {
      0% {
        offset-distance: 0%;
      }
      100% {
        offset-distance: 100%;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Motion Path Module Level 1  <br>\# offset-distance-property](https://drafts.csswg.org/motion/#offset-distance-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`offset-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
    
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [`offset-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position)
    
*   [`offset-rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/offset-distance/index.md?plain=1 "Folder: en-us/web/css/reference/properties/offset-distance (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-distance&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-distance%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-distance%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-distance%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")