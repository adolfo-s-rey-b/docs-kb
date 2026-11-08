*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#mdn-search)
    

`field-sizing` CSS property
===========================

Baseline 2026

Newly available

Since June 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`field-sizing`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables you to control the sizing behavior of elements that are given a default preferred size, such as form control elements. This property enables you to override the default sizing behavior, allowing form controls to adjust in size to fit their contents.

This property is typically used to style text [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements to allow them to shrinkwrap their content as well as grow when more text is entered into the form control.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    field-sizing: content;
    field-sizing: fixed;
    
    /* Global values */
    field-sizing: inherit;
    field-sizing: initial;
    field-sizing: revert;
    field-sizing: revert-layer;
    field-sizing: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#values)

This property is specified as one of the following keyword values:

[`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#content)

Allows the element to adjust its size to fit its contents.

[`fixed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#fixed)

Sets a fixed size for the element. This is the default value.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#description)

--------------------------------------------------------------------------------------------------------------

`field-sizing: content` overrides the default preferred sizing of form elements. This setting provides a way to configure text inputs to shrinkwrap their content and grow as more text is entered. They stop expanding when they reach maximum size limits (defined by the size of their containing element or set via CSS), at which point scrolling is required to view all the content.

### [Elements affected by `field-sizing: content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#elements_affected_by_field-sizing_content)

Specifically, `field-sizing` to `content` affects the following elements:

*   Form input types that accept direct text input from users. This includes [`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
    , [`number`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
    , [`password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
    , [`search`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
    , [`tel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
    , [`text`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
    , and [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
     types.
    *   If no minimum width is set on the control, it will only be as wide as the text cursor.
    *   Controls with [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
         attributes will be rendered large enough to display the placeholder text.
    *   The [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
         attribute modifies the default preferred size of such `<input>` elements. As a result, `size` has no effect on `<input>` elements with `field-sizing: content` set.
*   [`file`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
     inputs. Direct text input is not possible; however, the displayed filename changes as the user selects a new file to upload. When `field-sizing: content` is set, the control will change size to shrinkwrap the filename.
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     controls. It is worth noting that `<textarea>` elements with `field-sizing: content` set behave much like single-line text controls, with the following additions:
    *   If `<textarea>` elements are unable to grow due to a width constraint, they will start to grow in height to display additional rows of content. When a height constraint is then reached, they will then start to show a scrollbar to allow all the content to be viewed.
    *   [`rows`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#rows)
         and [`cols`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea#cols)
         attributes modify the default preferred size of a `<textarea>`. As a result, `rows`/`cols` have no effect on `<textarea>` elements with `field-sizing: content` set.
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     controls. These behave a bit differently to what you might expect with `field-sizing: content` set. The effect depends on the type of `<select>` control you are creating:
    *   Regular drop-down boxes will change their width to always fit the displayed option value as new values are selected. (By default, the drop-down's size is set to be large enough to display the longest option value.)
    *   List boxes (`<select>` elements with the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#multiple)
         or [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#size)
         attribute) will be large enough to display all the options without needing to scroll. (By default, the drop-down box will require scrolling to view all the option values.)
    *   The [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#size)
         attribute has very little effect on `<select>` elements that have `field-sizing: content` set. In such cases, the browser checks if the `size` is equal to `1` to determine whether the `<select>` control should appear as a drop-down or a listbox. However, it will always display all the options of a listbox, even if `size` is smaller than the number of options.

### [`field-sizing` interaction with other size settings](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#field-sizing_interaction_with_other_size_settings)

The sizing flexibility provided to form controls by `field-sizing: content` can be overridden if you use other CSS sizing properties. Avoid setting a fixed [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 when using `field-sizing: content` because they will reimpose a fixed size on the control. However, using properties like [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
 and [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 alongside `field-sizing: content` is quite effective because they allow the control to grow and shrink with the entered text and also prevent the control from becoming too large or too small.

The [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 attribute causes the control to stop growing in size when the maximum character limit is reached.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `fixed` |
| Applies to | Elements with default preferred size |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#formal_syntax)

------------------------------------------------------------------------------------------------------------------

field-sizing =   
  fixed    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  content    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#examples)

--------------------------------------------------------------------------------------------------------

### [Growing and shrinking text fields](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#growing_and_shrinking_text_fields)

This example illustrates the effect of `field-sizing: content` on single- and multi-line text fields. The fields adjust their size as text is added or removed, effectively shrinkwrapping the contents, until a lower or upper size limit is reached.

#### HTML

The HTML in this example contains four form fields, each with an associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
: three `<input>` elements of types [`text`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, [`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
, and [`tel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
, and a [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element.

html

    <div>
      <label for="name">Enter name:</label>
      <input type="text" id="name" />
    </div>
    <div>
      <label for="email">Enter email:</label>
      <input type="email" id="email" placeholder="e.g. a@b.com" />
    </div>
    <div>
      <label for="tel">Enter telephone:</label>
      <input type="tel" id="tel" maxlength="15" />
    </div>
    <div>
      <label for="comment">Enter comment:</label>
      <textarea id="comment">This is a comment.</textarea>
    </div>
    

Note the following points about the HTML:

*   The first two fields have no length restrictions set.
*   The third field (of type `tel`) has a [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
     attribute set, which stops the size of the field from increasing when the character limit is reached.
*   The `<textarea>` will grow in the inline direction until the edge of the [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
     constraint (set in the CSS code below) is reached, then start to add new lines in the block direction to contain subsequent characters.
*   The `email` input has a placeholder set. This causes the field to render big enough to show the entire placeholder. Once the field is focused and the user starts typing, the field changes size to the `min-width` value. The `text` field, which doesn't have a placeholder, renders initially at `min-width`.

#### CSS

In the CSS, we set `field-sizing: content` on the three form fields, along with a [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
 and [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 to constrain the input size. It is worth reiterating that, if no minimum width was set on the fields, they would be rendered only as wide as the text cursor.

We also give the `<label>`s some rudimentary styling so that they sit neatly next to the fields.

    body {
      box-sizing: border-box;
      padding: 20px;
    }
    
    div {
      margin-bottom: 20px;
      display: flex;
    }
    

css

    input,
    textarea {
      field-sizing: content;
      min-width: 50px;
      max-width: 350px;
    }
    
    label {
      width: 150px;
      margin-right: 20px;
      text-align: right;
    }
    

#### Result

Try entering and removing text in the fields below to explore the effects of `field-sizing: content` alongside other sizing properties.

### [Controlling `<select>` element display](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#controlling_select_element_display)

This example illustrates the effect of `field-sizing: content` on [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements, both drop-down menu types and multiline listbox types.

#### HTML

The HTML contains two sets of `<select>` elements: one with `field-sizing: content` applied, and one without, allowing you to see the difference (though the effect may be less obvious than on text fields). Each set includes one drop-down menu type and one multiline listbox type (with the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#multiple)
 attribute set).

html

    <div class="field-sizing">
      <h2>With <code>field-sizing: content</code></h2>
      <select>
        <option>Bananas</option>
        <option>Strawberries</option>
        <option selected>Apples</option>
        <option>Raspberries</option>
        <option>Pomegranate</option>
      </select>
      <select multiple>
        <option>Bananas</option>
        <option>Strawberries</option>
        <option>Apples</option>
        <option>Raspberries</option>
        <option>Pomegranate</option>
      </select>
    </div>
    <div>
      <h2>Without <code>field-sizing: content</code></h2>
      <select>
        <option>Bananas</option>
        <option>Strawberries</option>
        <option selected>Apples</option>
        <option>Raspberries</option>
        <option>Pomegranate</option>
      </select>
      <select multiple>
        <option>Bananas</option>
        <option>Strawberries</option>
        <option>Apples</option>
        <option>Raspberries</option>
        <option>Pomegranate</option>
      </select>
    </div>
    

**Note:** Best practice is to include a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element for each form control, to associate a meaningful text description with each field for accessibility purposes (see [Use meaningful text labels](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML#use_meaningful_text_labels)
 for more information). We haven't done so in this example, as it focuses purely on aspects of the form controls' visual rendering, but you should make sure you include form labels in production code.

#### CSS

In the CSS, `field-sizing: content` is set only on the first set of `<select>` elements.

    body {
      box-sizing: border-box;
      display: flex;
      gap: 20px;
      font-family: sans-serif;
    }
    
    h2 {
      margin-top: 0;
      font-size: 1rem;
      text-align: center;
      flex: 1 0 100%;
    }
    
    div {
      margin-bottom: 20px;
      flex: 1;
      display: flex;
      align-items: flex-start;
      justify-content: space-around;
      flex-flow: row wrap;
    }
    

css

    .field-sizing select {
      field-sizing: content;
    }
    

#### Result

Note the following effects of `field-sizing: content`:

*   The drop-down menu always fits the size of the displayed option, changing size as different options are selected. Without `field-sizing: content`, the size is fixed as wide as the longest option.
*   The multi-select list box displays all of the options at once. Without `field-sizing: content`, the user has to scroll the box to view all the options.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Form Control Styling Level 1  <br>\# propdef-field-sizing](https://drafts.csswg.org/css-forms-1/#propdef-field-sizing) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing#see_also)

--------------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/field-sizing/index.md?plain=1 "Folder: en-us/web/css/reference/properties/field-sizing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffield-sizing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffield-sizing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffield-sizing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffield-sizing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")