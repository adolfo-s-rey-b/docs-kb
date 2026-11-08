*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#mdn-search)
    

`background-origin` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-origin`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the background's origin: from the border start, inside the border, or inside the padding.

Note that `background-origin` is ignored when [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
 is `fixed`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#try_it)

---------------------------------------------------------------------------------------------------------

    background-origin: border-box;
    background-repeat: no-repeat;
    

    background-origin: padding-box;
    background-repeat: no-repeat;
    

    background-origin: content-box;
    background-repeat: no-repeat;
    

    <section id="default-example">
      <div id="example-element">This is the content of the element.</div>
    </section>
    

    #example-element {
      background-image: url("/shared-assets/images/examples/leopard.jpg");
      color: #d73611;
      text-shadow: 2px 2px black;
      padding: 20px;
      border: 10px dashed #333333;
      font-size: 2em;
      font-weight: bold;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-origin: border-box;
    background-origin: padding-box;
    background-origin: content-box;
    
    /* Global values */
    background-origin: inherit;
    background-origin: initial;
    background-origin: revert;
    background-origin: revert-layer;
    background-origin: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#values)

This property is specified as one of the following keyword values:

[`border-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#border-box)

The background is positioned relative to the border box.

[`padding-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#padding-box)

The background is positioned relative to the padding box. Default value.

[`content-box`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#content-box)

The background is positioned relative to the content box.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `padding-box` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

background-origin =   
  <visual-box>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<visual-box> =   
  content-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  padding-box  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  border-box     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#examples)

-------------------------------------------------------------------------------------------------------------

### [Setting background origins](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#setting_background_origins)

css

    .example {
      border: 10px double;
      padding: 10px;
      background: url("image.jpg");
      background-position: center left;
      background-origin: content-box;
    }
    

css

    #example2 {
      border: 4px solid black;
      padding: 10px;
      background: url("image.gif");
      background-repeat: no-repeat;
      background-origin: border-box;
    }
    

css

    div {
      background-image:
        url("logo.jpg"), url("main-back.png"); /* Applies two images to the background */
      background-position:
        top right,
        0px 0px;
      background-origin: content-box, padding-box;
    }
    

### [Using two gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#using_two_gradients)

In this example the box has a thick dotted border. The first gradient uses the `padding-box` as the `background-origin` and therefore the background sits inside the border. The second uses the `content-box` and so only displays behind the content.

css

    .box {
      margin: 10px 0;
      color: white;
      background:
        linear-gradient(
          90deg,
          rgb(131 58 180 / 100%) 0%,
          rgb(253 29 29 / 60%) 60%,
          rgb(252 176 69 / 100%) 100%
        ),
        radial-gradient(circle, white 0%, black 28%);
      border: 20px dashed black;
      padding: 20px;
      width: 400px;
      background-origin: padding-box, content-box;
      background-repeat: no-repeat;
    }
    

html

    <div class="box">Hello!</div>
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-origin](https://drafts.csswg.org/css-backgrounds/#background-origin) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-origin/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-origin (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-origin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-origin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-origin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-origin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")