*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#mdn-search)
    

`background-blend-mode` CSS property
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-blend-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how an element's background images should blend with each other and with the element's background color.

Blending modes should be defined in the same order as the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property. If the blending modes' and background images' list lengths are not equal, it will be repeated and/or truncated until lengths match.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#try_it)

-------------------------------------------------------------------------------------------------------------

    background-blend-mode: normal;
    

    background-blend-mode: multiply;
    

    background-blend-mode: hard-light;
    

    background-blend-mode: difference;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="transition-all" id="example-element"></div>
      </div>
    </section>
    

    #example-element {
      background-color: green;
      background-image: url("/shared-assets/images/examples/balloon.jpg");
      width: 250px;
      height: 305px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* One value */
    background-blend-mode: normal;
    
    /* Two values, one per background */
    background-blend-mode: darken, luminosity;
    
    /* Global values */
    background-blend-mode: inherit;
    background-blend-mode: initial;
    background-blend-mode: revert;
    background-blend-mode: revert-layer;
    background-blend-mode: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#values)

[`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)

The blending mode to be applied. There can be several values, separated by commas.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | All elements. In SVG, it applies to container elements, graphics elements, and graphics referencing elements.. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

background-blend-mode =   
  [<'mix-blend-mode'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<mix-blend-mode>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
 =   
  <blend-mode>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  plus-lighter    
  
[<blend-mode>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
 =   
  normal       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  darken       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  multiply     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-burn   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  lighten      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  screen       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color-dodge  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  overlay      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  soft-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hard-light   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  difference   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  exclusion    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hue          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  saturation   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  color        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  luminosity     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#basic_example)

css

    .item {
      width: 300px;
      height: 300px;
      background: url("image1.png"), url("image2.png");
      background-blend-mode: screen;
    }
    

### [Try out different blend modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#try_out_different_blend_modes)

    <div id="div"></div>
    <select id="select">
      <option>normal</option>
      <option>multiply</option>
      <option selected>screen</option>
      <option>overlay</option>
      <option>darken</option>
      <option>lighten</option>
      <option>color-dodge</option>
      <option>color-burn</option>
      <option>hard-light</option>
      <option>soft-light</option>
      <option>difference</option>
      <option>exclusion</option>
      <option>hue</option>
      <option>saturation</option>
      <option>color</option>
      <option>luminosity</option>
    </select>
    

    #div {
      width: 300px;
      height: 300px;
      background: url("br.png"), url("tr.png");
      background-blend-mode: screen;
    }
    

    document.getElementById("select").onchange = (event) => {
      document.getElementById("div").style.backgroundBlendMode =
        document.getElementById("select").selectedOptions[0].innerHTML;
    };
    console.log(document.getElementById("div"));
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compositing and Blending Module Level 2  <br>\# background-blend-mode](https://drafts.csswg.org/compositing/#background-blend-mode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`<blend-mode>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
    
*   [`mix-blend-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-blend-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-blend-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-blend-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-blend-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-blend-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-blend-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")