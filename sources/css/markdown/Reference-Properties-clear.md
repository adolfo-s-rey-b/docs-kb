*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#mdn-search)
    

`clear` CSS property
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`clear`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether an element must be moved below (cleared) [floating](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
 elements that precede it. The `clear` property applies to floating and non-floating elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#try_it)

---------------------------------------------------------------------------------------------

    clear: none;
    

    clear: left;
    

    clear: right;
    

    clear: both;
    

    <section class="default-example" id="default-example">
      <div class="example-container">
        <div class="floated-left">Left</div>
        <div class="floated-right">Right</div>
        <div class="transition-all" id="example-element">
          As much mud in the streets as if the waters had but newly retired from the
          face of the earth, and it would not be wonderful to meet a Megalosaurus,
          forty feet long or so, waddling like an elephantine lizard up Holborn
          Hill.
        </div>
      </div>
    </section>
    

    .example-container {
      border: 1px solid #c5c5c5;
      padding: 0.75em;
      text-align: left;
      line-height: normal;
    }
    
    .floated-left {
      border: solid 10px #ffc129;
      background-color: rgb(81 81 81 / 0.6);
      padding: 1em;
      float: left;
    }
    
    .floated-right {
      border: solid 10px #ffc129;
      background-color: rgb(81 81 81 / 0.6);
      padding: 1em;
      float: right;
      height: 150px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#syntax)

---------------------------------------------------------------------------------------------

css

    /* Keyword values */
    clear: none;
    clear: left;
    clear: right;
    clear: both;
    clear: inline-start;
    clear: inline-end;
    
    /* Global values */
    clear: inherit;
    clear: initial;
    clear: revert;
    clear: revert-layer;
    clear: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#none)

Is a keyword indicating that the element is _not_ moved down to clear past floating elements.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#left)

Is a keyword indicating that the element is moved down to clear past _left_ floats.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#right)

Is a keyword indicating that the element is moved down to clear past _right_ floats.

[`both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#both)

Is a keyword indicating that the element is moved down to clear past _both_ left and right floats.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#inline-start)

Is a keyword indicating that the element is moved down to clear floats on _start side of its containing block_, that is the _left_ floats on ltr scripts and the _right_ floats on rtl scripts.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#inline-end)

Is a keyword indicating that the element is moved down to clear floats on _end side of its containing block_, that is the _right_ floats on ltr scripts and the _left_ floats on rtl scripts.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#description)

-------------------------------------------------------------------------------------------------------

When applied to non-floating blocks, it moves the [border edge](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#border_area)
 of the element down until it is below the [margin edge](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction#margin_area)
 of all relevant floats. The non-floated block's top margin collapses.

Vertical margins between two floated elements on the other hand will not collapse. When applied to floating elements, the margin edge of the bottom element is moved below the margin edge of all relevant floats. This affects the position of later floats, since later floats cannot be positioned higher than earlier ones.

The floats that are relevant to be cleared are the earlier floats within the same [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
.

**Note:** If an element contains only floated elements, its height collapses to nothing. If you want it to always be able to resize, so that it contains floating elements inside it, set the value of the element's [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to [`flow-root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display#flow-root)
.

css

    #container {
      display: flow-root;
    }
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#formal_definition)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | block-level elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#formal_syntax)

-----------------------------------------------------------------------------------------------------------

clear =   
  inline-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-start   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-end     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  left          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  right         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  top           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bottom        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both-inline   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both-block    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none            

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#examples)

-------------------------------------------------------------------------------------------------

### [clear: left](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#clear_left)

#### HTML

html

    <div class="wrapper">
      <p class="black">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus sit amet
        diam. Duis mattis varius dui. Suspendisse eget dolor.
      </p>
      <p class="red">Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
      <p class="left">This paragraph clears left.</p>
    </div>
    

#### CSS

css

    .wrapper {
      border: 1px solid black;
      padding: 10px;
    }
    .left {
      border: 1px solid black;
      clear: left;
    }
    .black {
      float: left;
      margin: 0;
      background-color: black;
      color: white;
      width: 20%;
    }
    .red {
      float: left;
      margin: 0;
      background-color: pink;
      width: 20%;
    }
    p {
      width: 50%;
    }
    

### [clear: right](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#clear_right)

#### HTML

html

    <div class="wrapper">
      <p class="black">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus sit amet
        diam. Duis mattis varius dui. Suspendisse eget dolor.
      </p>
      <p class="red">Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
      <p class="right">This paragraph clears right.</p>
    </div>
    

#### CSS

css

    .wrapper {
      border: 1px solid black;
      padding: 10px;
    }
    .right {
      border: 1px solid black;
      clear: right;
    }
    .black {
      float: right;
      margin: 0;
      background-color: black;
      color: white;
      width: 20%;
    }
    .red {
      float: right;
      margin: 0;
      background-color: pink;
      width: 20%;
    }
    p {
      width: 50%;
    }
    

### [clear: both](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#clear_both)

#### HTML

html

    <div class="wrapper">
      <p class="black">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus sit amet
        diam. Duis mattis varius dui. Suspendisse eget dolor. Fusce pulvinar lacus
        ac dui.
      </p>
      <p class="red">
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus sit amet
        diam. Duis mattis varius dui. Suspendisse eget dolor.
      </p>
      <p class="both">This paragraph clears both.</p>
    </div>
    

#### CSS

css

    .wrapper {
      border: 1px solid black;
      padding: 10px;
    }
    .both {
      border: 1px solid black;
      clear: both;
    }
    .black {
      float: left;
      margin: 0;
      background-color: black;
      color: white;
      width: 20%;
    }
    .red {
      float: right;
      margin: 0;
      background-color: pink;
      width: 20%;
    }
    p {
      width: 45%;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Cascading Style Sheets Level 2  <br>\# propdef-clear](https://drafts.csswg.org/css2/#propdef-clear) |
| [CSS Logical Properties and Values Module Level 1  <br>\# float-clear](https://drafts.csswg.org/css-logical/#float-clear) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear#see_also)

-------------------------------------------------------------------------------------------------

*   [CSS basic box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/clear/index.md?plain=1 "Folder: en-us/web/css/reference/properties/clear (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclear&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclear%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fclear%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fclear%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")