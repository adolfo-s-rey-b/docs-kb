*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#mdn-search)
    

`interpolate-size` CSS property
===============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/253)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#browser_compatibility)
 carefully before using this in production.

The **`interpolate-size`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows you to enable [animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 and [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
 between a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 value and an [intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size)
, [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
, or [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
.

This property is typically used to animate the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and/or [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 of a container between a `<length-percentage>` and the full size of its content (i.e., between "closed" and "open" or "hide" and "reveal" states) when animating a non-box-model CSS property, such as [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
, is not a viable solution.

**Note:** The behavior opted-into by `interpolate-size` cannot be enabled by default across the web because many sites in the wild use stylesheets that assume intrinsic size values cannot be animated. Enabling it by default would cause several backwards-compatibility issues (see relevant [CSS WG discussion](https://github.com/w3c/csswg-drafts/issues/626#issuecomment-2071016522 "External link (opens in new tab)")
).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    interpolate-size: allow-keywords;
    interpolate-size: numeric-only;
    
    /* Global values */
    interpolate-size: inherit;
    interpolate-size: initial;
    interpolate-size: revert;
    interpolate-size: revert-layer;
    interpolate-size: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#values)

This property is specified as one of the following keyword values:

[`allow-keywords`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#allow-keywords)

Enables [interpolation](https://developer.mozilla.org/en-US/docs/Glossary/Interpolation)
 between a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 value and an intrinsic size value, to allow animation between the two.

[`numeric-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#numeric-only)

The default behavior — intrinsic size values cannot be interpolated.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#description)

------------------------------------------------------------------------------------------------------------------

Setting `interpolate-size: allow-keywords` enables interpolation between a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 value and an intrinsic size value. Note that it does not enable animating between two intrinsic size values. One end of the animation must be a `<length-percentage>`.

The `interpolate-size` value is inherited, so animating to (or from) an intrinsic size value can be enabled for an entire document by setting it on the document root:

css

    :root {
      interpolate-size: allow-keywords;
    }
    

If you want to limit the scope, you can set it on the relevant container element. The following enables interpolating intrinsic sizes only for [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 and its descendants:

css

    main {
      interpolate-size: allow-keywords;
    }
    

**Note:** The [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 function's return values can also be interpolated. In effect, including `calc-size()` in a property value automatically applies `interpolate-size: allow-keywords` to the selection. However, because `interpolate-size` is inherited as explained above, it is the preferred solution for enabling intrinsic size animations in most cases. You should only use `calc-size()` to enable intrinsic size animations if they also require calculations.

### [Values that can be interpolated](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#values_that_can_be_interpolated)

The following intrinsic values can currently be opted-in to animations:

*   `auto`
*   [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
    
*   [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    
*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    
*   `content` (for containers sized using [`flex-basis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    ).

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `numeric-only` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

interpolate-size =   
  numeric-only    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  allow-keywords    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#examples)

------------------------------------------------------------------------------------------------------------

### [Basic `interpolate-size` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#basic_interpolate-size_usage)

This example demonstrates how to set `interpolate-size: allow-keywords` on a document to enable animations involving an intrinsic size. The demo features a character badge/"name tag", which can be hovered or focused to reveal information about the character. The reveal is handled by a [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 transition between a set length and `max-content`.

#### HTML

The HTML contains a single [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element with [`tabindex="0"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
 set on it so it can receive keyboard focus. The `<section>` contains [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
 and [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 elements, each with their own child content.

html

    <section tabindex="0">
      <header>
        <h2>Tanuki</h2>
      </header>
      <main>
        <p>Tanuki is the silent phantom of MDN.</p>
        <ul>
          <li><strong>Height</strong>: 3.03m</li>
          <li><strong>Weight</strong>: 160kg</li>
          <li><strong>Tech Fu</strong>: 7</li>
          <li><strong>Bad Jokes</strong>: 9</li>
        </ul>
      </main>
    </section>
    

#### CSS

    * {
      box-sizing: border-box;
    }
    
    section {
      font-family: "Helvetica", "Arial", sans-serif;
      width: 175px;
      border-radius: 5px;
      background: #eeeeee;
      box-shadow:
        inset 1px 1px 4px rgb(255 255 255 / 0.5),
        inset -1px -1px 4px rgb(0 0 0 / 0.5);
    }
    
    header {
      padding: 0.7rem;
      border-bottom: 2px solid #cccccc;
    }
    
    main {
      padding: 10px;
    }
    
    h2 {
      margin: 0;
      font-weight: normal;
      font-size: 1.1rem;
      text-align: center;
      letter-spacing: 1px;
    }
    
    p,
    li {
      font-size: 0.8rem;
      line-height: 1.5;
    }
    
    p {
      margin-top: 0;
    }
    

In the CSS, we first set `interpolate-size: allow-keywords` on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
, to enable it for the whole document.

css

    :root {
      interpolate-size: allow-keywords;
    }
    

We then set the `<section>`'s [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 to `2.5rem` and [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
 to `hidden` so only the `<header>` is shown by default, then specify a `transition` that animates the `<section>` `height` over 1 second during state change. Finally, we set the `<section>` `height` on [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 and [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 to `max-content`.

css

    section {
      height: 2.5rem;
      overflow: hidden;
      transition: height ease 1s;
    }
    
    section:hover,
    section:focus {
      height: max-content;
    }
    

The rest of the CSS has been hidden for brevity.

#### Result

Try hovering over the `<section>` or focusing it via the keyboard — it will animate to its full height, revealing all the content.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 4  <br>\# propdef-interpolate-size](https://drafts.csswg.org/css-sizing-4/#propdef-interpolate-size) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size#see_also)

------------------------------------------------------------------------------------------------------------

*   [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
    
*   [Animate to height: auto; (and other intrinsic sizing keywords) in CSS](https://developer.chrome.com/docs/css-ui/animate-to-height-auto "External link (opens in new tab)")
     on developer.chrome.com (2024)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/interpolate-size/index.md?plain=1 "Folder: en-us/web/css/reference/properties/interpolate-size (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterpolate-size&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterpolate-size%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterpolate-size%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterpolate-size%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")