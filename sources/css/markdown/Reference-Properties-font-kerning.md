*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#mdn-search)
    

`font-kerning` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-kerning`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the use of the kerning information stored in a font.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#try_it)

----------------------------------------------------------------------------------------------------

    font-kerning: auto;
    

    font-kerning: normal;
    

    font-kerning: none;
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element">
        "We took Tracy to see 'THE WATERFALL' in W. Virginia."
      </div>
    </section>
    

    section {
      font-family: serif;
    }
    

_Kerning_ affects how letters are spaced. In _well-kerned_ fonts, this feature makes character spacing more uniform and pleasant to read by reducing white space between certain character combinations.

In the image below, for instance, the examples on the left do not use kerning, while the ones on the right do:

![Example of font-kerning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning/font-kerning.png)

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#syntax)

----------------------------------------------------------------------------------------------------

css

    font-kerning: auto;
    font-kerning: normal;
    font-kerning: none;
    
    /* Global values */
    font-kerning: inherit;
    font-kerning: initial;
    font-kerning: revert;
    font-kerning: revert-layer;
    font-kerning: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#auto)

The browser determines whether font kerning should be used or not. For example, some browsers will disable kerning on small fonts, since applying it could harm the readability of text.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#normal)

Font kerning information stored in the font must be applied.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#none)

Font kerning information stored in the font is disabled.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#formal_syntax)

------------------------------------------------------------------------------------------------------------------

font-kerning =   
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#examples)

--------------------------------------------------------------------------------------------------------

### [Enabling and disabling kerning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#enabling_and_disabling_kerning)

#### HTML

html

    <div id="kern"></div>
    <div id="no-kern"></div>
    <textarea id="input">AV T. ij</textarea>
    

#### CSS

css

    div {
      font-size: 2rem;
      font-family: serif;
    }
    
    #no-kern {
      font-kerning: none;
    }
    
    #kern {
      font-kerning: normal;
    }
    

#### JavaScript

js

    const input = document.getElementById("input");
    const kern = document.getElementById("kern");
    const noKern = document.getElementById("no-kern");
    
    input.addEventListener("keyup", () => {
      kern.textContent = input.value; /* Update content */
      noKern.textContent = input.value;
    });
    
    kern.textContent = input.value; /* Initialize content */
    noKern.textContent = input.value;
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-kerning-prop](https://drafts.csswg.org/css-fonts/#font-kerning-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning#see_also)

--------------------------------------------------------------------------------------------------------

*   [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    , [`font-variant-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    , [`font-variant-east-asian`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    , [`font-variant-caps`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    , [`font-variant-ligatures`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    , [`font-variant-numeric`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    , [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    , [`font-synthesis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    , [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-kerning/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-kerning (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-kerning&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-kerning%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-kerning%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-kerning%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")