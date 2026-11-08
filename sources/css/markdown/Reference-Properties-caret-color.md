*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#mdn-search)
    

`caret-color` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`caret-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the color of the **insertion caret**, sometimes referred to as the **text input cursor**. This is the visible marker appearing at the insertion point where the next character typed will be added or where the next character deleted will be removed.

The `caret-color` property can also be set as part of the [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
 shorthand property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#try_it)

---------------------------------------------------------------------------------------------------

    caret-color: red;
    

    caret-color: auto;
    

    caret-color: transparent;
    

    <section class="default-example container" id="default-example">
      <div>
        <p>Enter text in the field to see the caret:</p>
        <p><input id="example-element" type="text" /></p>
      </div>
    </section>
    

    #example-element {
      font-size: 1.2rem;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    caret-color: auto;
    caret-color: transparent;
    caret-color: currentColor;
    
    /* <color> values */
    caret-color: red;
    caret-color: #5729e9;
    caret-color: rgb(0 200 0);
    caret-color: hsl(228deg 4% 24% / 80%);
    
    /* Global values */
    caret-color: inherit;
    caret-color: initial;
    caret-color: revert;
    caret-color: revert-layer;
    caret-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#values)

This property is specified as a single value from the following list:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#auto)

Generally resolves to [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
, the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 of the text that will be modified.

[`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

The color of the caret.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#description)

-------------------------------------------------------------------------------------------------------------

An insertion caret is a visible indicator of the spot within editable text — or within an element that accepts text input — where content will be inserted (or deleted) by the user. The caret is typically a thin vertical line indicating where the addition or deletion of characters will occur. It generally blinks (flashes on and off), so it is more noticeable. The caret only appears when the editable element has focus. By default, this caret is the color of the text. The `caret-color` property can be used to set the color of this caret to something other than the `currentColor`, or to reset a colored caret back to its default.

The `auto` value sets the insertion caret to `currentColor`, which is the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 of the text that is being added or deleted. User agents may choose a different color to ensure good visibility and contrast with the surrounding content, taking into account the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
, [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
, shadows, and other factors. In practice, however, all browsers use the current color by default, and when `caret-color` is set to `auto`. You can set any valid `<color>` as the value.

### [Understanding insertion carets](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#understanding_insertion_carets)

The insertion caret, and therefore this property, only applies to text or elements that can accept text input. The caret appears in focused user interface elements where users can update content, such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements that accept freeform text, the [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element, and elements with the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 attribute set.

The caret may appear in `<input>` elements of type `password`, `text`, `search`, `tel`, and `email`. No caret exists with date, `color`, `hidden`, `radio`, or `checkbox` input types. Some browsers display a caret with the `number` input type. It is possible in some browsers to make a caret appear in elements that never have text content — for example, by setting [`appearance: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 and adding the `contenteditable` attribute. However, this is not recommended.

A caret may be displayed in an editable element or its descendants, provided the editability is not disabled, for example by setting a descendant element's `contentEditable` attribute to `false`. If an element is not editable or selectable, for example if [`user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
 is set to `none`, the caret should not appear.

### [Caret versus cursor](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#caret_versus_cursor)

There are multiple types of carets. The insertion caret is the only type affected by the `caret-color` property.

Many browsers have a **navigation caret**, which acts similarly to an insertion caret but can be moved around in non-editable text.

The mouse cursor image shown for certain [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
 property values (for example, `auto` or `text`) may resemble a caret, but it's not. It's a cursor.

### [Animating from `auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#animating_from_auto)

Generally, when the `caret-color` is set to or defaults to `auto`, user agents use `currentColor`, which is animatable. However, `auto` is not an animatable value by default: when animating or transitioning the `caret-color` from `auto` to any color value, no interpolation happens. The animation is [discrete](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
; the color switches from or to the `currentColor` color at the midpoint of the [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
 or [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Text or elements that accept text input |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `auto` is computed as specified and `<color>` values are computed as defined for the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)<br> property. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

caret-color =   
  auto                         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#examples)

-------------------------------------------------------------------------------------------------------

### [Setting a custom caret color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#setting_a_custom_caret_color)

#### HTML

html

    <input value="This field uses a default caret." size="64" />
    <input class="custom" value="I have a custom caret color!" size="64" />
    <p contenteditable class="custom">
      This paragraph can be edited, and its caret has a custom color as well!
    </p>
    

#### CSS

css

    input {
      caret-color: auto;
      display: block;
      margin-bottom: 0.5em;
    }
    
    input.custom {
      caret-color: orange;
    }
    
    p.custom {
      caret-color: green;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# caret-color](https://drafts.csswg.org/css-ui/#caret-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color#see_also)

-------------------------------------------------------------------------------------------------------

*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    , [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    
*   [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
     shorthand
*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    
*   [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
    
*   [`text-emphasis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    
*   CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
     data type
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element
*   HTML [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/caret-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/caret-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")