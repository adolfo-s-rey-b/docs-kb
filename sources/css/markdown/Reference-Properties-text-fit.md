*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#mdn-search)
    

`text-fit` CSS property
=======================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/846)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#browser_compatibility)
 carefully before using this in production.

The **`text-fit`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to scale the rendered font size of text nodes (and other inline content) so that they fit exactly within the inline dimension of their containing boxes, optionally limited by a maximum or minimum **scaling factor**.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#syntax)

------------------------------------------------------------------------------------------------

css

    /* One keyword */
    text-fit: none;
    text-fit: grow;
    text-fit: shrink;
    
    /* Two keywords */
    text-fit: grow consistent;
    text-fit: shrink per-line-all;
    
    /* Keywords and <percentage> */
    text-fit: grow 300%;
    text-fit: shrink 80%;
    text-fit: grow per-line-all 300%;
    
    /* Global values */
    text-fit: inherit;
    text-fit: initial;
    text-fit: revert;
    text-fit: revert-layer;
    text-fit: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#values)

This property is specified as a space-separated list of one to three values from the following list:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#none)

The default value. No text scaling is applied.

[`grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#grow)

The text node's rendered font size is scaled up until it exactly fits inside its containing box's inline dimension.

[`shrink`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#shrink)

The text node's rendered font size is scaled down until it exactly fits inside its containing box's inline dimension.

[`consistent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#consistent)

All of the lines of the text node are scaled using the same scaling factor. This keyword has no effect if `none` is specified as the first keyword. If a second keyword is not specified, `consistent` is assumed.

[`per-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#per-line)

All of the lines of the text node are scaled with their own scaling factor. The last line of the text node, and any lines that end in a forced break (for example, due to a [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
 element) have no text scaling applied. This keyword has no effect if `none` is specified as the first keyword.

[`per-line-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#per-line-all)

All of the lines of the text node are scaled with their own scaling factor, including the last line and lines that end in a forced break. This keyword has no effect if `none` is specified as the first keyword.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

Specifies the maximum (when `grow` is specified) or minimum (when `shrink` is specified) scaling factor. This must be `100%` or greater if `grow` is specified, or between `0%` and `100%` inclusive if `shrink` is specified, otherwise the percentage has no effect.

The mandatory first value can be `none`, `grow`, or `shrink`. The optional second value can be `consistent`, `per-line`, or `per-line-all`. The optional [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value is declared last. The components must be specified in this order.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#description)

----------------------------------------------------------------------------------------------------------

A common web design challenge is getting headings and other text features to fit neatly within their containing boxes, regardless of layout or viewport size. The most typical use case is getting a horizontal text heading to fit the width of its containing box perfectly. Complex [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 calculations and JavaScript workarounds were historically used to achieve this.

The `text-fit` property provides a convenient CSS-only solution, adjusting the rendered font size of the text by a specific scaling factor to fit the space available, rather than justifying it like the [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
 property's `justify` value does.

The basic form of `text-fit` uses a single keyword:

*   You can specify `grow` to scale the font size up so that the text fits exactly inside its containing box. This works well for the use case described previously.
*   You can specify `shrink` to scale the font size down so that the text fits exactly inside its containing box. This works well in cases where you have a line of text that is longer than its containing box, maybe due to a really long word, and you want to shrink it to avoid overflow.

Specifically, the parts of a text node that are affected by this scaling (the **scalable parts**) are the text itself, excluding trailing whitespace, and spacing whose inline size is proportional to the text's `font-size`, such as percentage-based [`letter-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
 and [`word-spacing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
, and [`text-autospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace)
. Other parts, including inline [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
, [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
, and [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
, are not scaled.

The `text-fit` property does not affect a container's intrinsic size, which means that the text content cannot grow in cases where the container is sized by its content, for example using the [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
 keyword. Setting `text-fit` also doesn't change an element's computed `font-size`: the size adjustment is applied after the final rendering.

### [How is the scaling factor calculated?](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#how_is_the_scaling_factor_calculated)

The scaling factor is the ratio by which the scalable parts of a text line must be scaled in order for its inline content to fit exactly inside its containing box. The scaling factor for each line of a text node is calculated using a formula along these lines (the exact method for determining the scaling factor may differ between implementations):

(A + B) / A

where:

*   `A` is the total inline size of the text line's scalable parts.
*   `B` is the remaining space inside the text line, including any trailing whitespace, which may be negative if the text overflows.

The scaling factor for a text line with no scalable parts is `1`.

### [Specifying scaling factor limits](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#specifying_scaling_factor_limits)

To limit the amount by which the text can grow, you can specify a `<percentage>` value after the `grow` or `shrink` keyword.

If `grow` is specified, the percentage has to be `100%` or greater, and acts as a maximum scaling factor. For example:

css

    text-fit: grow 300%;
    

Any text this is applied to will grow to fit its containing box, but will not scale to a size greater than 300% of its original `font-size`.

If `shrink` is specified, the percentage has to be between `0%` and `100%` inclusive, and acts as a minimum scaling factor. For example:

css

    text-fit: shrink 50%;
    

Any text this is applied to will shrink to fit its containing box, but will not scale to a size less than 50% of its original `font-size`.

**Note:** In many situations, word breaking behavior results in `text-fit: shrink` having no effect — the words wrap onto new lines rather than shrinking. In these cases, you need to stop the breaking behavior using something like a [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 value of `nowrap` to see it working. See this in action in our [basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#basic_text-fit_usage)
.

### [Specifying how scaling factor is applied to multiple text lines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#specifying_how_scaling_factor_is_applied_to_multiple_text_lines)

By default, a text node with multiple lines scales all of the lines by the same scaling factor. Each line has its scaling factor calculated separately, and the smallest scaling factor is then applied to all of the lines. This is usually the behavior you'll want, to ensure that each line grows or shrinks by the same proportion.

If you want to adjust this behavior, you can specify a second value after the first keyword and before the percentage, if specified. This value can be specified as the default `consistent` keyword, which keeps the behavior described previously, but you can also specify `per-line` or `per-line-all`. Both of these cause the lines of the text node to be scaled with their own scaling factors. The difference is that, with `per-line`, the last line of the text node, and any lines that end in a forced break (for example, due to a `<br>` element) have no text scaling applied, whereas with `per-line-all` scaling is applied to these lines.

For example, this declaration will grow all lines of a text node by their own scaling factor to fit the containing box.

css

    text-fit: grow per-line-all;
    

This declaration on the other hand will shrink all lines of a text node by their own scaling factor to fit the containing box, but not the last line or lines with forced breaks, and not below `50%` of the original `font-size`.

css

    text-fit: shrink per-line 50%;
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#accessibility)

--------------------------------------------------------------------------------------------------------------

When using `text-fit`, designs must be tested carefully at different viewport sizes to make sure the rendered font size doesn't become too small (or too large). This can lead to content becoming illegible, especially for people with visual impairments or in low vision conditions.

In any case, text content should be resizable without loss of content or functionality; see [WCAG Success Criterion 1.4.4 Resize Text](https://w3c.github.io/wcag/guidelines/22/#resize-text "External link (opens in new tab)")
.

Related guidance:

*   [MDN Understanding WCAG, Guideline 1.4: Make it easier for users to see and hear content including separating foreground from background](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#formal_definition)

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | block container elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | specified keyword, or computed `<percentage>` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#formal_syntax)

--------------------------------------------------------------------------------------------------------------

text-fit =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 grow [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 shrink [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 consistent [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 per-line [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 per-line-all [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#examples)

----------------------------------------------------------------------------------------------------

### [Basic `text-fit` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#basic_text-fit_usage)

This example demonstrates basic usage of `text-fit` to grow and shrink text nodes to fit their containers.

#### HTML

We include two text elements, an [`<h1>` and an `<h2>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
, nested inside a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
.

    <input
      type="range"
      min="0.4"
      max="1"
      value="1"
      step="0.01"
      aria-label="adjust the width of the page" />
    

html

    <div>
      <h1>My heading</h1>
    
      <h2>My subtitle: a bit longer, may need shrinking</h2>
    </div>
    

    const divElem = document.querySelector("div");
    const slider = document.querySelector("input");
    let maxWidth;
    
    function setMaxWidth() {
      maxWidth = document.documentElement.clientWidth;
    }
    
    function setWidth() {
      divElem.style.width = `${maxWidth * slider.value}px`;
    }
    
    slider.addEventListener("input", setWidth);
    window.addEventListener("resize", () => {
      setMaxWidth();
      setWidth();
    });
    
    setMaxWidth();
    setWidth();
    

We also include an [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 element to enable adjusting the content width to emulate a changing viewport width. The range input, plus the JavaScript that powers it, have been hidden for brevity.

#### CSS

We give the container `<div>` a [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 value of `20px` to give the text some space.

    * {
      box-sizing: border-box;
    }
    
    html {
      font-family: sans-serif;
      background-color: white;
    }
    
    div {
      margin: 0 auto;
      background-color: coral;
    }
    
    input {
      width: 99%;
    }
    

css

    div {
      padding: 20px;
    }
    

We give the `<h1>` a `text-fit` value of `grow`, so that it will grow to fill its container's available inline space. We give the longer `<h2>` a [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 value of `nowrap` so that ordinarily, it would all stay on a single line and overflow its container rather than wrapping, if it reaches the container edge. We then set `text-fit: shrink` on it so that, instead of overflowing, it will shrink to fit inside its container's available inline space.

css

    h1 {
      text-fit: grow;
    }
    
    h2 {
      white-space: nowrap;
      text-fit: shrink;
    }
    

#### Result

Adjust the slider and note how the `<h1>` grows automatically so that it always fills the available space inside its parent `<div>`. Also note how the `<h2>` shrinks so that it always fills the available space inside the `<div>` at narrower widths; at wider widths where it fits inside the `<div>`, it maintains its natural width.

Without `text-fit`, the `<h1>` wouldn't fill the available space, and the `<h2>` would overflow it at narrower widths.

### [Setting scaling factor percentage limits](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#setting_scaling_factor_percentage_limits)

This example is very similar to the previous one, except that in this case we limit the amount that our headings can grow or shrink using `<percentage>` values.

The HTML and JavaScript are identical to the previous example.

#### CSS

We give the `<h1>` a `text-fit` value of `grow 300%`, so that it will grow to fill its container's available inline space, up to 300% of its natural `font-size`:

css

    h1 {
      text-fit: grow 300%;
    }
    

We give the `<h2>` a [`white-space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
 value of `nowrap` so that it will all stay on a single line and overflow its container rather than wrapping, when it touches the container edge. We then set `text-fit: shrink 80%` on it so that, instead of overflowing, it will shrink to fit inside its container's available inline space, down to `80%` of its natural `font-size`.

css

    h2 {
      white-space: nowrap;
      text-fit: shrink 80%;
    }
    

One issue that presents itself at this point is that, when the `<div>`'s `width` gets smaller than about `400px`, the `<h2>` will start to overflow its container. To avoid this, we want to set the text to wrap onto new lines normally at this point. To solve the problem, we first give the containing `<div>` a [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
 of `inline-size`, so that we can use [container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
 to selectively apply CSS depending on its width.

    div {
      padding: 20px;
    }
    

css

    div {
      container-type: inline-size;
    }
    

We then use a container query to change the `<h2>`'s `white-space` value to `wrap` when the `<div>`'s `width` gets smaller than `400px`:

css

    @container (width < 400px) {
      h2 {
        white-space: wrap;
      }
    }
    

#### Result

Adjust the slider. Note how the `<h1>` grows automatically so that it always fills the available space inside its parent `<div>`, but only up to a certain width. Note how the `<h2>` shrinks so that it always fills the available space inside the `<div>` at narrower widths. When the `<div>` gets narrower than `400px`, the container query kicks in and we set `white-space: wrap`, meaning that the `<h2>` starts to wrap onto multiple lines.

### [Demonstrating multi-line scaling behavior keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#demonstrating_multi-line_scaling_behavior_keywords)

This example demonstrates the difference in effect between setting the `consistent`, `per-line`, and `per-line-all` keywords in the `text-fit` property values of different paragraphs.

#### HTML

The HTML features three [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements containing the same filler text, each with different `id` values set on them:

html

    <div>
      <p id="consistent">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste vitae in id
        esse odit autem quisquam saepe repellendus.
      </p>
    
      <p id="per-line">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste vitae in id
        esse odit autem quisquam saepe repellendus.
      </p>
    
      <p id="per-line-all">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste vitae in id
        esse odit autem quisquam saepe repellendus.
      </p>
    </div>
    

The HTML and JavaScript for the width adjustment slider are also included in this example.

#### CSS

We give each paragraph a `text-fit` value with the first keyword set to `grow`; the second keyword in each case is set to a different value — `consistent`, `per-line`, and `per-line-all`, respectively.

css

    #consistent {
      text-fit: grow consistent;
    }
    
    #per-line {
      text-fit: grow per-line;
    }
    
    #per-line-all {
      text-fit: grow per-line-all;
    }
    

    * {
      box-sizing: border-box;
    }
    
    :root {
      overflow: hidden;
    }
    
    div {
      padding: 20px;
    }
    
    p {
      padding: 20px;
      background-color: rgb(0 0 0 / 0.2);
      position: relative;
      margin-bottom: 40px;
    }
    
    p::before {
      content: attr(id);
      background-color: black;
      color: white;
      padding: 5px 10px;
      position: absolute;
      top: -28px;
      left: 0px;
    }
    

#### Result

Adjust the slider up and down the scale, taking careful note of the behavior of each paragraph. You should note that:

*   The `consistent` paragraph's text lines always have the same `font-size` as one another throughout.
*   The `per-line` paragraph's text lines vary in `font-size` somewhat, which becomes more noticeable at narrower widths. The last line's `font-size` is not scaled.
*   The `per-line-all` paragraph's text lines vary in `font-size` somewhat, which includes the last line. This is very noticeable at widths that cause only one or two words to wrap onto the last line.

    @supports not (text-fit: grow) {
      body::before {
        content: "Your browser does not support text-fit.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 5  <br>\# text-fit-property](https://drafts.csswg.org/css-text-5/#text-fit-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit#see_also)

----------------------------------------------------------------------------------------------------

*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 29, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/text-fit/index.md?plain=1 "Folder: en-us/web/css/reference/properties/text-fit (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-fit&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-fit%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftext-fit%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftext-fit%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcc66520c973185b32319769333271680832a854e%0A*+Document+last+modified%3A+2026-09-29T16%3A16%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")