*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#mdn-search)
    

`text-align-last` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`text-align-last`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how the last line of a block or a line, right before a forced line break, is aligned.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#try_it)

-------------------------------------------------------------------------------------------------------

    text-align-last: right;
    

    text-align-last: center;
    

    text-align-last: left;
    

    <section id="default-example">
      <div>
        <p id="example-element">
          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
      </div>
    </section>
    

    section {
      font-size: 1.5em;
    }
    
    #default-example > div {
      width: 250px;
    }
    
    #example-element {
      text-align: justify;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    text-align-last: auto;
    text-align-last: start;
    text-align-last: end;
    text-align-last: left;
    text-align-last: right;
    text-align-last: center;
    text-align-last: justify;
    
    /* Global values */
    text-align-last: inherit;
    text-align-last: initial;
    text-align-last: revert;
    text-align-last: revert-layer;
    text-align-last: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#auto)

The affected line is aligned per the value of [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
, unless [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 is `justify`, in which case the effect is the same as setting `text-align-last` to `start`.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#start)

The same as `left` if direction is left-to-right and `right` if direction is right-to-left.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#end)

The same as `right` if direction is left-to-right and `left` if direction is right-to-left.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#left)

The inline contents are aligned to the left edge of the line box.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#right)

The inline contents are aligned to the right edge of the line box.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#center)

The inline contents are centered within the line box.

[`justify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#justify)

The text is justified. Text should line up their left and right edges to the left and right content edges of the paragraph.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | block containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

text-align-last =   
  auto          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  center        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  justify       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  match-parent    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#examples)

-----------------------------------------------------------------------------------------------------------

### [Justifying the last line](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#justifying_the_last_line)

    <p>
      Integer elementum massa at nulla placerat varius. Suspendisse in libero risus,
      in interdum massa. Vestibulum ac leo vitae metus faucibus gravida ac in neque.
      Nullam est eros, suscipit sed dictum quis, accumsan a ligula.
    </p>
    

#### CSS

css

    p {
      font-size: 1.4em;
      text-align: justify;
      text-align-last: center;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# text-align-last-property](https://drafts.csswg.org/css-text/#text-align-last-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-align-last/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-align-last (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-align-last&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-align-last%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-align-last%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-align-last%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")