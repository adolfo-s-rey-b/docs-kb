*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#mdn-search)
    

`will-change` CSS property
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`will-change`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables optimizing animations by providing a rendering hint to a browser about how an element is expected to change.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#values)

The value is either `auto` or one or more comma separated `<animatable-feature>` values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#auto)

Indicates that the browser applies whatever heuristics and optimizations it normally does. This is the default value.

[`<animatable-feature>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#animatable-feature)

Represents one of the following:

[`scroll-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#scroll-position)

Specifies that the scroll position of the element is expected to change in the near future, indicating the browser can optimize the rendering of overflowing content.

[`contents`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#contents)

Specifies that the element's contents, including all the elements in its subtree, are expected to change in the near future, indicating the browser can cache the element less aggressively.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

Specifies the name of a CSS property, as an [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
, whose value is animated or otherwise expected to change in the near future. If the specified `<ident>` represents a property shorthand, all of its longhand components are applied. The value cannot be `will-change`, `none`, `all`, `auto`, `scroll-position`, or `contents`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#description)

-------------------------------------------------------------------------------------------------------------

The `will-change` property provides a rendering hint to the browser indicating which properties are expected to be animated or otherwise changed. This enables browsers to create the necessary rendering optimizations to enable smoother changes and avoid [jank](https://developer.mozilla.org/en-US/docs/Glossary/Jank)
.

The `will-change` property is aimed at improving rendering performance. This property can improve performance for elements with frequent repaints and reflows or for those that use properties such as [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 and [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 to create complex visual effects.

Applying the property to an element applies the value to the element's entire subtree, indicating that any of the descendants can change. For this reason, applying a non-`auto` value on a large section, such as the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
, can actually be bad for a page's performance. Instead, limit the use of this property to deeply nested elements, containing as little of the document as possible.

**Warning:** Use the `will-change` property as a last resort to try to deal with existing performance problems. Don't use it to anticipate performance problems.

Proper usage of this property can be a bit tricky. Keep the following guidelines in mind:

*   **Don't apply `will-change` to too many elements**: The browser already tries as hard as it can to optimize everything. Some of the stronger optimizations that are likely to be tied to `will-change` end up using a lot of a machine's resources. Overusing the property can cause the page to slow down instead of improving its performance.
*   **Use sparingly**: The browser's normal behavior for optimizations is to remove the optimizations as soon as it can and revert to normal state. But adding `will-change` directly to a stylesheet implies that the targeted elements are always a few moments away from changing and the browser will keep the optimizations for a much longer time than it would have otherwise. So it is a good practice to switch `will-change` on and off using script code before and after the change occurs.
*   **Don't apply will-change to elements to perform premature optimization**: If your page is performing well, don't add the `will-change` property to elements just to wring out a little more speed. `will-change` is intended to be used as a last resort to try to deal with existing performance problems. It should not be used to anticipate performance problems. Excessive use of `will-change` will result in excessive memory use and will cause more complex rendering to occur as the browser attempts to prepare for the possible change. This will lead to worse performance.
*   **Give it sufficient time to work**: This property enables you to signal to the browser about properties that are likely to change, so the browser can choose to apply any ahead-of-time optimizations before the property change occurs. For this reason, you should give the browser some time to do the optimizations. Predict slightly ahead of time that something will change, and then set `will-change`.
*   **Be aware that `will-change` may influence the visual appearance of elements**: When used with property values that create a [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
     (e.g., `will-change: opacity`), the stacking context is created up front.

### [Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#animations)

If applying `will-change` to improve animations, add the property before the animation starts, not within the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animation definitions. Animated properties are treated as if they're already included in a `will-change`, so there's no reason to add them there.

### [Via stylesheet](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#via_stylesheet)

It may be appropriate to include `will-change` in your style sheet for an application that does page flips on key presses like an album or a slide deck presentation where the pages are large and complex. This will let browser prepare the transition ahead of time and allow for snappy transitions between the pages as soon as the key is pressed. But use caution with the `will-change` property directly in stylesheets. It may cause the browser to keep the optimization in memory for much longer than it is needed.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

will-change =   
  auto                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <animateable-feature>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<animateable-feature> =   
  scroll-position  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  contents         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#basic_usage)

This example demonstrates the basic CSS application of the `will-change` property.

#### CSS

We use CSS to apply the `will-change` property to the `#element`, providing a hint to the browser that the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 and [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 property values will be animated or otherwise change in the near future.

### [Via script](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#via_script)

This example shows how to apply the `will-change` property when needed and remove optimizations when done using JavaScript, which is generally how `will-change` should be applied.

#### JavaScript

We use JavaScript to add the `will-change` property to `#element` when the element is hovered over by using the [`mouseenter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event "mouseenter")
 event. Setting `will-change` to `transform, opacity` tells the browser to optimize for changes to the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 and [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 properties. When the [`animationend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event "animationend")
 event occurs, our script sets the value to `auto`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Will Change Module Level 1  <br>\# will-change](https://drafts.csswg.org/css-will-change/#will-change) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change#see_also)

-------------------------------------------------------------------------------------------------------

*   [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   Individual transform properties: [`translate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    , [`scale`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
    , [`rotate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    
*   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    
*   [CSS will change](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Will_change)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/will-change/index.md?plain=1 "Folder: en-us/web/css/reference/properties/will-change (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwill-change&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwill-change%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fwill-change%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fwill-change%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")