*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#mdn-search)
    

`caret-animation` CSS property
==============================

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#browser_compatibility)
 carefully before using this in production.

The **`caret-animation`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to enable or disable the blinking behavior of the **insertion caret**, the visible marker that appears in editable elements to indicate where the next character will be inserted or deleted.

The `caret-animation` property can also be set as part of the [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
 shorthand property.

**Note:** When applying a custom animation to the caret, you should stop the default blinking so that it doesn't interfere with the animation.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#syntax)

-------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#auto)

The caret blinks on and off. This is the default (initial) value.

[`manual`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#manual)

The caret does not blink on and off.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Text or elements that accept text input |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

caret-animation =   
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  manual    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#examples)

-----------------------------------------------------------------------------------------------------------

### [Basic `caret-animation` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#basic_caret-animation_usage)

This example shows the difference between having `caret-animation` set to `auto` versus `manual` on an editable element.

#### HTML

The markup features two [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements with [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 set to make them editable.

#### CSS

The CSS sets the [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 value to `red`. It then gives the first paragraph a `caret-animation` value of `auto` and the second paragraph a `caret-animation` value of `manual`.

#### Result

The rendered result looks like so:

Try focusing the two paragraphs to see the difference in caret behavior.

### [Creating a custom caret animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#creating_a_custom_caret_animation)

In this example, a custom caret animation is applied to an editable paragraph and a text input.

#### HTML

The markup features a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element and two text [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. The `<p>` element has the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 attribute set on it to make it editable. The paragraph and first text input have a `class` of `custom-caret` set on them.

html

    <p contenteditable="true" class="custom-caret">
      This paragraph has a custom animation applied to it, plus
      <code>caret-animation: manual</code> to stop the default caret blinking and
      allow the smooth animation to be seen.
    </p>
    
    <input
      type="text"
      class="custom-caret"
      value="I've got a custom caret animation" />
    
    <input type="text" value="I've got the default blinking caret" />
    

#### CSS

We first define a set of [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 that change the [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 from `transparent` to `darkblue`.

css

    @keyframes custom-caret-animation {
      from {
        caret-color: transparent;
      }
    
      to {
        caret-color: darkblue;
      }
    }
    

We then style the `<p>` and the first `<input>` with the custom `@keyframes` animation, a [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
, and a `caret-animation` value of `manual` to turn the default caret blinking behavior off.

    body {
      display: flex;
      flex-direction: column;
    }
    
    input {
      margin-bottom: 20px;
    }
    

css

    .custom-caret {
      animation: custom-caret-animation infinite linear alternate 0.75s;
      caret-color: darkblue;
      caret-animation: manual;
    }
    
    p,
    input {
      font-size: 1.6rem;
    }
    

#### Result

The rendered result looks like so:

Try focusing the first two elements to see what the custom caret animation looks like. To compare it with the default blinking caret, you can focus the third element.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-caret-animation](https://drafts.csswg.org/css-ui/#propdef-caret-animation) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    
*   [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
     shorthand
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/caret-animation/index.md?plain=1 "Folder: en-us/web/css/reference/properties/caret-animation (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-animation&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-animation%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-animation%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-animation%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")