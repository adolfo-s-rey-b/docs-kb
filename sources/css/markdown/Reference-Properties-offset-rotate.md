*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#mdn-search)
    

`offset-rotate` CSS property
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`offset-rotate`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the orientation/direction of the element as it is positioned along the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#try_it)

-----------------------------------------------------------------------------------------------------

    offset-rotate: auto;
    

    offset-rotate: 90deg;
    

    offset-rotate: auto 90deg;
    

    offset-rotate: reverse;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element"></div>
      <button id="playback" type="button">Play</button>
    </section>
    

    #example-element {
      width: 24px;
      height: 24px;
      background: #2bc4a2;
      offset-path: path("M-70,-40 C-70,70 70,70 70,-40");
      animation: distance 8000ms infinite linear;
      animation-play-state: paused;
      clip-path: polygon(0% 0%, 70% 0%, 100% 50%, 70% 100%, 0% 100%, 30% 50%);
    }
    
    #example-element.running {
      animation-play-state: running;
    }
    
    #playback {
      position: absolute;
      top: 0;
      left: 0;
      font-size: 1em;
    }
    
    @keyframes distance {
      0% {
        offset-distance: 0%;
      }
      100% {
        offset-distance: 100%;
      }
    }
    
    /* Provides a reference image of what path the element is following */
    #default-example {
      position: relative;
      background-position: calc(50% - 12px) calc(50% + 14px);
      background-repeat: no-repeat;
      background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="-75 -45 150 140" width="150" height="140"><path d="M-70,-40 C-70,70 70,70 70,-40" fill="none" stroke="lightgrey" stroke-width="2" stroke-dasharray="4.5"/></svg>');
    }
    

    const example = document.getElementById("example-element");
    const button = document.getElementById("playback");
    
    button.addEventListener("click", () => {
      if (example.classList.contains("running")) {
        example.classList.remove("running");
        button.textContent = "Play";
      } else {
        example.classList.add("running");
        button.textContent = "Pause";
      }
    });
    

**Note:** Early versions of the spec called this property `motion-rotation`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Follow the path direction, with optional additional angle */
    offset-rotate: auto;
    offset-rotate: auto 45deg;
    
    /* Follow the path direction but facing the opposite direction of `auto` */
    offset-rotate: reverse;
    
    /* Keep a constant rotation regardless the position on the path */
    offset-rotate: 90deg;
    offset-rotate: 0.5turn;
    
    /* Global values */
    offset-rotate: inherit;
    offset-rotate: initial;
    offset-rotate: revert;
    offset-rotate: revert-layer;
    offset-rotate: unset;
    

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#auto)

The element is rotated by the angle of the direction of the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
, relative to the positive x-axis. This is the default value.

[`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)

The element has a constant clockwise rotation transformation applied to it by the specified rotation angle.

[`auto <angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#auto_angle)

If `auto` is followed by an [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
, the computed value of the angle is added to the computed value of `auto`.

[`reverse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#reverse)

The element is rotated similar to `auto`, except it faces the opposite direction. It is the same as specifying a value of `auto 180deg`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | transformable elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as <angle>, <basic-shape> or <path()> |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

offset-rotate =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 reverse [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<angle>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
               

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#examples)

---------------------------------------------------------------------------------------------------------

### [Setting element orientation along its offset path](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#setting_element_orientation_along_its_offset_path)

#### HTML

html

    <div></div>
    <div></div>
    <div></div>
    

#### CSS

css

    div {
      width: 40px;
      height: 40px;
      background: #2bc4a2;
      margin: 20px;
      clip-path: polygon(0% 0%, 70% 0%, 100% 50%, 70% 100%, 0% 100%, 30% 50%);
      animation: move 5000ms infinite alternate ease-in-out;
    
      offset-path: path("M20,20 C20,50 180,-10 180,20");
    }
    div:nth-child(1) {
      offset-rotate: auto;
    }
    div:nth-child(2) {
      offset-rotate: auto 90deg;
    }
    div:nth-child(3) {
      offset-rotate: 30deg;
    }
    
    @keyframes move {
      100% {
        offset-distance: 100%;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Motion Path Module Level 1  <br>\# offset-rotate-property](https://drafts.csswg.org/motion/#offset-rotate-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate#see_also)

---------------------------------------------------------------------------------------------------------

*   [`offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`offset-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
    
*   [`offset-distance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
    
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [`offset-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/offset-rotate/index.md?plain=1 "Folder: en-us/web/css/reference/properties/offset-rotate (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-rotate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-rotate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Foffset-rotate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Foffset-rotate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")