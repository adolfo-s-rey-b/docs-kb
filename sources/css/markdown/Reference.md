*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#mdn-search)
    

CSS reference
=============

Use this **CSS reference** to browse an [alphabetical index](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#index)
 of all of the standard [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties)
, [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
, [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
, [data types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
, [functional notations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 and [at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
. You can also browse [key CSS concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#concepts)
 and a list of [selectors organized by type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#selectors)
. Also included is a brief [DOM-CSS / CSSOM reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#dom-css_cssom)
.

[Basic rule syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#basic_rule_syntax)

--------------------------------------------------------------------------------------------------

### [Style rule syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#style_rule_syntax)

style-rule ::=
    selectors-list {
      properties-list
    }

Where:

selectors-list ::=
    selector\[:pseudo-class\] \[::pseudo-element\]
    \[, selectors-list\]

properties-list ::=
    \[property : value\] \[; properties-list\]

See the index of [_selectors_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#selectors)
, [_pseudo-classes_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#pseudo)
, and _[pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#pseudo)
_ below. The syntax for each specified _value_ depends on the data type defined for each specified _property_.

#### Style rule examples

For a beginner-level introduction to the syntax of selectors, see our [guide on CSS Selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
. Be aware that any [syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
 error in a rule definition invalidates the entire rule. Invalid rules are ignored by the browser. Note that CSS rule definitions are entirely (Unicode) [text-based](https://drafts.csswg.org/css-syntax/#intro "External link (opens in new tab)")
, whereas DOM-CSS / CSSOM (the rule management system) is [object-based](https://drafts.csswg.org/cssom/#introduction "External link (opens in new tab)")
.

### [At-rule syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#at-rule_syntax)

As the structure of at-rules varies widely, please see [At-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
 to find the syntax of the specific one you want.

[Index](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#index)

--------------------------------------------------------------------------

**Note:** This index does not include SVG-exclusive presentation attributes, which can be used as CSS properties on [SVG](https://developer.mozilla.org/en-US/docs/Web/SVG)
 elements.

**Note:** The property names in this index do **not** include the JavaScript names which do differ from the CSS standard names.

### \-

*   [`:-moz-broken` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-broken)
    
*   [`::-moz-color-swatch` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch)
    
*   [`:-moz-drag-over` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over)
    
*   [`:-moz-first-node` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-first-node)
    
*   [`::-moz-focus-inner` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner)
    
*   [`:-moz-handler-blocked` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-blocked)
    
*   [`:-moz-handler-crashed` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-crashed)
    
*   [`:-moz-handler-disabled` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-disabled)
    
*   [`:-moz-last-node` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node)
    
*   [`::-moz-list-bullet` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-bullet)
    
*   [`::-moz-list-number` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-number)
    
*   [`:-moz-loading` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading)
    
*   [`:-moz-locale-dir(ltr)` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_ltr)
    
*   [`:-moz-locale-dir(rtl)` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl)
    
*   [`::-moz-meter-bar` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-meter-bar)
    
*   [`:-moz-only-whitespace` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace)
    
*   [`::-moz-progress-bar` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-progress-bar)
    
*   [`::-moz-range-progress` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-progress)
    
*   [`::-moz-range-thumb` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-thumb)
    
*   [`::-moz-range-track` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-track)
    
*   [`:-moz-submit-invalid` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-submit-invalid)
    
*   [`:-moz-suppressed` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-suppressed)
    
*   [`:-moz-user-disabled` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-user-disabled)
    
*   [`:-moz-window-inactive` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-window-inactive)
    
*   [`::-webkit-inner-spin-button` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-inner-spin-button)
    
*   [`::-webkit-meter-bar` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-bar)
    
*   [`::-webkit-meter-even-less-good-value` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-even-less-good-value)
    
*   [`::-webkit-meter-inner-element` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-inner-element)
    
*   [`::-webkit-meter-optimum-value` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-optimum-value)
    
*   [`::-webkit-meter-suboptimum-value` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-suboptimum-value)
    
*   [`::-webkit-progress-bar` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-bar)
    
*   [`::-webkit-progress-inner-element` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element)
    
*   [`::-webkit-progress-value` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-value)
    
*   [`::-webkit-scrollbar` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar)
    
*   [`::-webkit-search-cancel-button` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-search-cancel-button)
    
*   [`::-webkit-search-results-button` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-search-results-button)
    
*   [`::-webkit-slider-runnable-track` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-runnable-track)
    
*   [`::-webkit-slider-thumb` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-thumb)
    

### A

*   [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
    
*   [`abs()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
    
*   [`<absolute-size>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/absolute-size)
    
*   [`accent-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
    
*   [`acos()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`:active` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
    
*   [`:active-view-transition` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition)
    
*   [`:active-view-transition-type()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active-view-transition-type)
    
*   [`additive-symbols` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
    
*   [`::after` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
    
*   [`align-content` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-content)
    
*   [`align-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    
*   [`align-self` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
    
*   [`alignment-baseline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/alignment-baseline)
    
*   [`all` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    
*   [`alpha()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/alpha)
    
*   [`<alpha-value>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/alpha-value)
    
*   [`anchor()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
    
*   [`anchor-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`anchor-scope` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope)
    
*   [`anchor-size()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
    
*   [`<angle-percentage>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle-percentage)
    
*   [`<angle>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    
*   [`animation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    
*   [<animation-action>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
    
*   [`animation-composition` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    
*   [`animation-delay` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    
*   [`animation-direction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    
*   [`animation-duration` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    
*   [`animation-fill-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    
*   [`animation-iteration-count` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    
*   [`animation-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    
*   [`animation-play-state` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    
*   [`animation-range` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [`animation-range-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    
*   [`animation-range-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   [`animation-timeline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`animation-timing-function` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    
*   [animation-trigger CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`:any-link` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
    
*   [`appearance` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
    
*   [`ascent-override` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/ascent-override)
    
*   [`asin()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`aspect-ratio` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
    
*   [`atan()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [`atan2()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    
*   [`attr()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
    
*   [`:autofill` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:autofill)
    
*   [`<axis>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
    

### B

*   [`::backdrop` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::backdrop)
    
*   [`backdrop-filter` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
    
*   [`backface-visibility` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility)
    
*   [`background` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    
*   [`background-attachment` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    
*   [`background-blend-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-blend-mode)
    
*   [`background-clip` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    
*   [`background-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`background-image` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`background-origin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    
*   [`background-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`background-position-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
    
*   [`background-position-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    
*   [`background-repeat` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
    
*   [`background-repeat-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x)
    
*   [`background-repeat-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y)
    
*   [`background-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`base-palette` CSS at-rule descriptor (`@font-palette-values`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/base-palette)
    
*   [`<baseline-position>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/baseline-position)
    
*   [`baseline-shift` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-shift)
    
*   [`baseline-source` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/baseline-source)
    
*   [`<basic-shape>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
    
*   [`::before` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
    
*   [`:blank` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank)
    
*   [`<blend-mode>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/blend-mode)
    
*   [`block-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
    
*   [`blur()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/blur)
    
*   [`border` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`-webkit-border-before` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-border-before)
    
*   [`border-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
    
*   [`border-block-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-color)
    
*   [`border-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
    
*   [`border-block-end-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-color)
    
*   [`border-block-end-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style)
    
*   [`border-block-end-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-width)
    
*   [`border-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    
*   [`border-block-start-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-color)
    
*   [`border-block-start-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)
    
*   [`border-block-start-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-width)
    
*   [`border-block-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-style)
    
*   [`border-block-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-width)
    
*   [`border-bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    
*   [`border-bottom-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-color)
    
*   [`border-bottom-left-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-left-radius)
    
*   [`border-bottom-right-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-right-radius)
    
*   [`border-bottom-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    
*   [`border-bottom-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-width)
    
*   [`border-collapse` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
    
*   [`border-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    
*   [`border-end-end-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-end-radius)
    
*   [`border-end-start-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-start-radius)
    
*   [`border-image` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image)
    
*   [`border-image-outset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-outset)
    
*   [`border-image-repeat` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-repeat)
    
*   [`border-image-slice` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-slice)
    
*   [`border-image-source` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-source)
    
*   [`border-image-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-image-width)
    
*   [`border-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline)
    
*   [`border-inline-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-color)
    
*   [`border-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
    
*   [`border-inline-end-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)
    
*   [`border-inline-end-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
    
*   [`border-inline-end-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
    
*   [`border-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
    
*   [`border-inline-start-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)
    
*   [`border-inline-start-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
    
*   [`border-inline-start-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)
    
*   [`border-inline-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)
    
*   [`border-inline-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-width)
    
*   [`border-left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    
*   [`border-left-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-color)
    
*   [`border-left-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    
*   [`border-left-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-width)
    
*   [`border-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    
*   [`border-right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    
*   [`border-right-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-color)
    
*   [`border-right-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    
*   [`border-right-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-width)
    
*   [`border-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    
*   [`border-spacing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-spacing)
    
*   [`border-start-end-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-end-radius)
    
*   [`border-start-start-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius)
    
*   [`border-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   [`border-top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    
*   [`border-top-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-color)
    
*   [`border-top-left-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-left-radius)
    
*   [`border-top-right-radius` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius)
    
*   [`border-top-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    
*   [`border-top-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-width)
    
*   [`border-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-width)
    
*   [`bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    
*   [`box-align` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align)
    
*   [`box-decoration-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
    
*   [`box-direction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction)
    
*   [`<box-edge>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge)
    
*   [`box-flex` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex)
    
*   [`box-flex-group` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-flex-group)
    
*   [`box-lines` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-lines)
    
*   [`box-ordinal-group` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-ordinal-group)
    
*   [`box-orient` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient)
    
*   [`box-pack` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
    
*   [`-webkit-box-reflect` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-box-reflect)
    
*   [`box-shadow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`box-sizing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
    
*   [`break-after` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-after)
    
*   [`break-before` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-before)
    
*   [`break-inside` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside)
    
*   [`brightness()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/brightness)
    
*   [`:buffering` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:buffering)
    

### C

*   [Class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
    
*   [Custom properties (--\*): CSS variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    
*   [`calc()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [`<calc-keyword>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-keyword)
    
*   [`calc-size()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
    
*   [`<calc-sum>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-sum)
    
*   [`caption-side` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caption-side)
    
*   [`caret` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
    
*   [`caret-animation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    
*   [`caret-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    
*   [`caret-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    
*   [`@charset` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset)
    
*   [`:checked` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
    
*   [`::checkmark` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::checkmark)
    
*   [`circle()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/circle)
    
*   [`clamp()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)
    
*   [`clear` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clear)
    
*   [`clip` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip)
    
*   [`clip-path` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
    
*   [`clip-rule` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-rule)
    
*   [`color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`color()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
    
*   [`color-interpolation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation)
    
*   [`color-interpolation-filters` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-interpolation-filters)
    
*   [`<color-interpolation-method>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color-interpolation-method)
    
*   [`color-mix()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color-mix)
    
*   [`@color-profile` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile)
    
*   [`color-scheme` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme)
    
*   [`<color>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
    
*   [`::column` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::column)
    
*   [`column-count` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    
*   [`column-fill` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill)
    
*   [`column-gap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    
*   [`column-height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-height)
    
*   [`column-rule` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    
*   [`column-rule-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-break)
    
*   [`column-rule-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`column-rule-inset-cap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap)
    
*   [`column-rule-inset-cap-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-end)
    
*   [`column-rule-inset-cap-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-cap-start)
    
*   [`column-rule-inset-junction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction)
    
*   [`column-rule-inset-junction-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-end)
    
*   [`column-rule-inset-junction-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-inset-junction-start)
    
*   [`column-rule-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`column-rule-visibility-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-visibility-items)
    
*   [`column-rule-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    
*   [`column-span` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-span)
    
*   [`column-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    
*   [`column-wrap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-wrap)
    
*   [`columns` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/columns)
    
*   [`conic-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/conic-gradient)
    
*   [`contain` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`contain-intrinsic-block-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-block-size)
    
*   [`contain-intrinsic-height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-height)
    
*   [`contain-intrinsic-inline-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-inline-size)
    
*   [`contain-intrinsic-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-size)
    
*   [`contain-intrinsic-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain-intrinsic-width)
    
*   [`@container` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
    
*   [`container` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
    
*   [`container-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
    
*   [`container-type` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
    
*   [`content` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
    
*   [`<content-distribution>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-distribution)
    
*   [`<content-position>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/content-position)
    
*   [`content-visibility` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
    
*   [`contrast()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/contrast)
    
*   [`contrast-color()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/contrast-color)
    
*   [`corner-block-end-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-end-shape)
    
*   [`corner-block-start-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-start-shape)
    
*   [`corner-bottom-left-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)
    
*   [`corner-bottom-right-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)
    
*   [`corner-bottom-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-shape)
    
*   [`corner-end-end-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-end-shape)
    
*   [`corner-end-start-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-start-shape)
    
*   [`corner-inline-end-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-end-shape)
    
*   [`corner-inline-start-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape)
    
*   [`corner-left-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-left-shape)
    
*   [`corner-right-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-right-shape)
    
*   [`corner-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
    
*   [`<corner-shape-value>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
    
*   [`corner-start-end-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)
    
*   [`corner-start-start-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)
    
*   [`corner-top-left-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
    
*   [`corner-top-right-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)
    
*   [`corner-top-shape` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-shape)
    
*   [`cos()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`counter()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
    
*   [`counter-increment` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-increment)
    
*   [`counter-reset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-reset)
    
*   [`counter-set` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/counter-set)
    
*   [`@counter-style` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
    
*   [`counters()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counters)
    
*   [`cross-fade()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cross-fade)
    
*   [`cubic-bezier()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
    
*   [`::cue` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::cue)
    
*   [`:current` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:current)
    
*   [`cursor` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
    
*   [`<custom-ident>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
*   [`@custom-media` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media)
    
*   [`cx` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cx)
    
*   [`cy` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cy)
    

### D

*   [`d` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/d)
    
*   [`<dashed-function>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
    
*   [`<dashed-ident>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    
*   [`:default` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default)
    
*   [`:defined` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined)
    
*   [`descent-override` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/descent-override)
    
*   [`::details-content` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::details-content)
    
*   [`device-cmyk()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/device-cmyk)
    
*   [`<dimension>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dimension)
    
*   [`:dir()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir)
    
*   [`direction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    
*   [`:disabled` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled)
    
*   [`display` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
    
*   [`<display-box>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-box)
    
*   [`<display-inside>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-inside)
    
*   [`<display-internal>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-internal)
    
*   [`<display-legacy>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-legacy)
    
*   [`<display-listitem>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-listitem)
    
*   [`<display-outside>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/display-outside)
    
*   [`@document` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document)
    
*   [`dominant-baseline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dominant-baseline)
    
*   [`drop-shadow()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/drop-shadow)
    
*   [`dynamic-range-limit` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/dynamic-range-limit)
    
*   [`dynamic-range-limit-mix()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dynamic-range-limit-mix)
    

### E

*   [`<easing-function>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
    
*   [`element()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    
*   [`ellipse()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/ellipse)
    
*   [`:empty` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:empty)
    
*   [`empty-cells` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells)
    
*   [`:enabled` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled)
    
*   [`env()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
    
*   [`exp()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    

### F

*   [`fallback` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
    
*   [`field-sizing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)
    
*   [`::file-selector-button` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::file-selector-button)
    
*   [`fill` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill)
    
*   [`fill-opacity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-opacity)
    
*   [`fill-rule` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
    
*   [`filter` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/filter)
    
*   [`<filter-function>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function)
    
*   [`:first` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first)
    
*   [`:first-child` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child)
    
*   [`::first-letter` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)
    
*   [`::first-line` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
    
*   [`:first-of-type` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    
*   [`fit-content` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    
*   [`fit-content()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
    
*   [`flex` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex)
    
*   [`flex-basis` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-basis)
    
*   [`flex-direction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    
*   [`flex-flow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-flow)
    
*   [`flex-grow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    
*   [`flex-line-count` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-line-count)
    
*   [`flex-shrink` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink)
    
*   [`flex-wrap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap)
    
*   [`<flex>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/flex_value)
    
*   [`float` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
    
*   [`-moz-float-edge` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-float-edge)
    
*   [`flood-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-color)
    
*   [`flood-opacity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flood-opacity)
    
*   [`:focus` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
    
*   [`:focus-visible` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
    
*   [`:focus-within` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
    
*   [`font` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
    
*   [`font-display` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-display)
    
*   [`font-display` CSS at-rule descriptor (`@font-feature-values`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values/font-display)
    
*   [`@font-face` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
    
*   [`font-family` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-family)
    
*   [`font-family` CSS at-rule descriptor (`@font-palette-values`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/font-family)
    
*   [`font-family` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
    
*   [`font-feature-settings` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-feature-settings)
    
*   [`font-feature-settings` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
    
*   [`@font-feature-values` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
    
*   [`font-kerning` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-kerning)
    
*   [`font-language-override` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
    
*   [`font-optical-sizing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-optical-sizing)
    
*   [`font-palette` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
    
*   [`@font-palette-values` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
    
*   [`font-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    
*   [`font-size-adjust` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size-adjust)
    
*   [`font-smooth` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth)
    
*   [`font-stretch` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-stretch)
    
*   [`font-stretch` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-stretch)
    
*   [`font-style` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-style)
    
*   [`font-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-synthesis` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis)
    
*   [`font-synthesis-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-position)
    
*   [`font-synthesis-small-caps` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-small-caps)
    
*   [`font-synthesis-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-style)
    
*   [`font-synthesis-weight` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-synthesis-weight)
    
*   [`font-variant` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [`font-variant-alternates` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [`font-variant-caps` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [`font-variant-east-asian` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [`font-variant-emoji` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   [`font-variant-ligatures` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [`font-variant-numeric` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [`font-variant-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-position)
    
*   [`font-variation-settings` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-variation-settings)
    
*   [`font-variation-settings` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variation-settings)
    
*   [`font-weight` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-weight)
    
*   [`font-weight` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`font-width` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/font-width)
    
*   [`font-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-width)
    
*   [`-moz-force-broken-image-icon` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon)
    
*   [`forced-color-adjust` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/forced-color-adjust)
    
*   [`frame-sizing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/frame-sizing)
    
*   [`<frequency-percentage>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency-percentage)
    
*   [`<frequency>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    
*   [`:fullscreen` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    
*   [`@function` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
    
*   [`:future` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:future)
    

### G

*   [`gap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/gap)
    
*   [`<generic-family>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/generic-family)
    
*   [`<gradient>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient)
    
*   [`::grammar-error` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::grammar-error)
    
*   [`grayscale()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/grayscale)
    
*   [`grid` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid)
    
*   [`grid-area` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-area)
    
*   [`grid-auto-columns` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-columns)
    
*   [`grid-auto-flow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-flow)
    
*   [`grid-auto-rows` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
    
*   [`grid-column` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column)
    
*   [`grid-column-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-end)
    
*   [`grid-column-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-column-start)
    
*   [`grid-row` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row)
    
*   [`grid-row-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-end)
    
*   [`grid-row-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-row-start)
    
*   [`grid-template` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template)
    
*   [`grid-template-areas` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
    
*   [`grid-template-columns` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
    
*   [`grid-template-rows` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-rows)
    

### H

*   [`hanging-punctuation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hanging-punctuation)
    
*   [`:has()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
    
*   [`:has-slotted` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
    
*   [`:heading` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading)
    
*   [`:heading()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function)
    
*   [`height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    
*   [`<hex-color>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
    
*   [`::highlight()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::highlight)
    
*   [`:host` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    
*   [`:host()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
    
*   [`:host-context()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
    
*   [`:hover` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
    
*   [`hsl()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
    
*   [`<hue-interpolation-method>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue-interpolation-method)
    
*   [`hue-rotate()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/hue-rotate)
    
*   [`<hue>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
    
*   [`hwb()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
    
*   [`hyphenate-character` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character)
    
*   [`hyphenate-limit-chars` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars)
    
*   [`hyphens` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [`hypot()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hypot)
    

### I

*   [ID selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)
    
*   [`<ident>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
*   [`if()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
    
*   [`image()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image)
    
*   [`image-orientation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-orientation)
    
*   [`-moz-image-rect()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect)
    
*   [`image-rendering` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)
    
*   [`image-resolution` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-resolution)
    
*   [`image-set()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/image-set)
    
*   [`<image>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
    
*   [`@import` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
    
*   [`!important` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
    
*   [`:in-range` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range)
    
*   [`:indeterminate` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
    
*   [`inherit` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    
*   [`inherits` CSS at-rule descriptor (`@property`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
    
*   [`initial` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    
*   [`initial-letter` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/initial-letter)
    
*   [`initial-value` CSS at-rule descriptor (`@property`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
    
*   [`inline-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
    
*   [`inset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset)
    
*   [`inset()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
    
*   [`inset-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block)
    
*   [`inset-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-end)
    
*   [`inset-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-block-start)
    
*   [`inset-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline)
    
*   [`inset-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-end)
    
*   [`inset-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inset-inline-start)
    
*   [`<integer>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
    
*   [`interactivity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interactivity)
    
*   [`interest-delay` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
    
*   [`interest-delay-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
    
*   [`interest-delay-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
    
*   [`:interest-source` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
    
*   [`:interest-target` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-target)
    
*   [`interpolate-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
    
*   [`:invalid` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    
*   [`invert()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/invert)
    
*   [`:is()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
    
*   [`isolation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/isolation)
    

### J

*   [`justify-content` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    
*   [`justify-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-items)
    
*   [`justify-self` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
    

### K

*   [Keyframe selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
    
*   [`@keyframes` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
    

### L

*   [`lab()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lab)
    
*   [`:lang()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
    
*   [`:last-child` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    
*   [`:last-of-type` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
    
*   [`@layer` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
    
*   [`layer()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import/layer_function)
    
*   [`lch()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/lch)
    
*   [`left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    
*   [`:left` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:left)
    
*   [`<length-percentage>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
    
*   [`<length>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    
*   [`letter-spacing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/letter-spacing)
    
*   [`light-dark()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
    
*   [`lighting-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/lighting-color)
    
*   [`line-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-break)
    
*   [`line-clamp` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-clamp)
    
*   [`line-gap-override` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/line-gap-override)
    
*   [`line-height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
    
*   [`line-height-step` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height-step)
    
*   [`<line-style>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
    
*   [`<line-width>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
    
*   [`linear()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
    
*   [`linear-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    
*   [`:link` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
    
*   [`link-parameters` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/link-parameters)
    
*   [`list-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    
*   [`list-style-image` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    
*   [`list-style-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`list-style-type` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
    
*   [`:local-link` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:local-link)
    
*   [`log()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    

### M

*   [`margin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
    
*   [`margin-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
    
*   [`margin-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-end)
    
*   [`margin-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block-start)
    
*   [`margin-bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    
*   [`margin-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
    
*   [`margin-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    
*   [`margin-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    
*   [`margin-left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    
*   [`margin-right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    
*   [`margin-top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    
*   [`margin-trim` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-trim)
    
*   [`marker` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker)
    
*   [`::marker` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
    
*   [`marker-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-end)
    
*   [`marker-mid` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-mid)
    
*   [`marker-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/marker-start)
    
*   [`mask` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask)
    
*   [`mask-border` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border)
    
*   [`mask-border-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-mode)
    
*   [`mask-border-outset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-outset)
    
*   [`mask-border-repeat` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-repeat)
    
*   [`mask-border-slice` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-slice)
    
*   [`mask-border-source` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-source)
    
*   [`mask-border-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-border-width)
    
*   [`-webkit-mask-box-image` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-box-image)
    
*   [`mask-clip` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-clip)
    
*   [`-webkit-mask-composite` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-composite)
    
*   [`mask-composite` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-composite)
    
*   [`mask-image` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-image)
    
*   [`mask-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-mode)
    
*   [`mask-origin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-origin)
    
*   [`mask-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-position)
    
*   [`-webkit-mask-position-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-position-x)
    
*   [`-webkit-mask-position-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-position-y)
    
*   [`mask-repeat` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-repeat)
    
*   [`-webkit-mask-repeat-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-x)
    
*   [`-webkit-mask-repeat-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-mask-repeat-y)
    
*   [`mask-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-size)
    
*   [`mask-type` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mask-type)
    
*   [`math-depth` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-depth)
    
*   [`math-shift` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-shift)
    
*   [`math-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/math-style)
    
*   [`matrix()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix)
    
*   [`matrix3d()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/matrix3d)
    
*   [`max()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    
*   [`max-block-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-block-size)
    
*   [`max-content` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    
*   [`max-height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
    
*   [`max-inline-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-inline-size)
    
*   [`max-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
    
*   [`@media` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [`min()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
    
*   [`min-block-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-block-size)
    
*   [`min-content` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
    
*   [`min-height` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    
*   [`min-inline-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
    
*   [`min-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    
*   [`minmax()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)
    
*   [`mix-blend-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/mix-blend-mode)
    
*   [`mod()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)
    
*   [`:modal` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
    
*   [`:muted` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:muted)
    

### N

*   [Namespace separator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator)
    
*   [`<named-color>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
    
*   [`@namespace` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
    
*   [`negative` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
    
*   [& nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
    
*   [`:not()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:not)
    
*   [`:nth-child()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    
*   [`:nth-last-child()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-child)
    
*   [`:nth-last-of-type()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-last-of-type)
    
*   [`:nth-of-type()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-of-type)
    
*   [`<number>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

### O

*   [`object-fit` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    
*   [`object-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    
*   [`object-view-box` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box)
    
*   [`offset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset)
    
*   [`offset-anchor` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-anchor)
    
*   [`offset-distance` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-distance)
    
*   [`offset-path` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
    
*   [`offset-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-position)
    
*   [`offset-rotate` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-rotate)
    
*   [`oklab()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklab)
    
*   [`oklch()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/oklch)
    
*   [`:only-child` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-child)
    
*   [`:only-of-type` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:only-of-type)
    
*   [`opacity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    
*   [`opacity()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/opacity)
    
*   [`:open` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
    
*   [`:optional` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional)
    
*   [`order` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order)
    
*   [`-moz-orient` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-orient)
    
*   [`orphans` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/orphans)
    
*   [`:out-of-range` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
    
*   [`outline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`outline-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
*   [`outline-offset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
    
*   [`outline-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    
*   [`outline-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    
*   [`overflow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`overflow-anchor` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-anchor)
    
*   [`overflow-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-block)
    
*   [`overflow-clip-margin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-clip-margin)
    
*   [`overflow-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-inline)
    
*   [`<overflow-position>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow-position)
    
*   [`overflow-wrap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    
*   [`overflow-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
    
*   [`overflow-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-y)
    
*   [`<overflow>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/overflow_value)
    
*   [`overlay` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overlay)
    
*   [`override-colors` CSS at-rule descriptor (`@font-palette-values`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values/override-colors)
    
*   [`overscroll-behavior` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior)
    
*   [`overscroll-behavior-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-block)
    
*   [`overscroll-behavior-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-inline)
    
*   [`overscroll-behavior-x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-x)
    
*   [`overscroll-behavior-y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overscroll-behavior-y)
    

### P

*   [`pad` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
    
*   [`padding` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    
*   [`padding-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block)
    
*   [`padding-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-end)
    
*   [`padding-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-block-start)
    
*   [`padding-bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    
*   [`padding-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline)
    
*   [`padding-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
    
*   [`padding-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
    
*   [`padding-left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    
*   [`padding-right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    
*   [`padding-top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    
*   [`@page` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
    
*   [`page` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page)
    
*   [`page-break-after` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-after)
    
*   [`page-break-before` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-before)
    
*   [`page-break-inside` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/page-break-inside)
    
*   [`page-orientation` CSS at-rule descriptor (`@page`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/page-orientation)
    
*   [`paint()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image/paint)
    
*   [`paint-order` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/paint-order)
    
*   [`palette-mix()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette/palette-mix)
    
*   [`param()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param)
    
*   [`::part()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
    
*   [`:past` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:past)
    
*   [`path()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path)
    
*   [`path-length` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/path-length)
    
*   [`:paused` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:paused)
    
*   [`<percentage>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
*   [`perspective` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
    
*   [`perspective()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/perspective)
    
*   [`perspective-origin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective-origin)
    
*   [`::picker()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
    
*   [`::picker-icon` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker-icon)
    
*   [`:picture-in-picture` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:picture-in-picture)
    
*   [`place-content` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
    
*   [`place-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
    
*   [`place-self` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
    
*   [`::placeholder` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
    
*   [`:placeholder-shown` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
    
*   [`:playing` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:playing)
    
*   [`pointer-events` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
    
*   [`polygon()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/polygon)
    
*   [`:popover-open` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
    
*   [`position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [`position-anchor` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`position-area` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [`<position-area>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position-area_value)
    
*   [`@position-try` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
    
*   [`position-try` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
    
*   [`position-try-fallbacks` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
    
*   [`position-try-order` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-order)
    
*   [`position-visibility` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility)
    
*   [`<position>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/position_value)
    
*   [`pow()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`prefix` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
    
*   [`print-color-adjust` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
    
*   [`progress()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/progress)
    
*   [`@property` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
    

### Q

*   [`quotes` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/quotes)
    

### R

*   [`r` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/r)
    
*   [`radial-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    
*   [`random()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/random)
    
*   [`range` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
    
*   [`<ratio>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
    
*   [`ray()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ray)
    
*   [`:read-only` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
    
*   [`:read-write` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    
*   [`reading-flow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
    
*   [`reading-order` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-order)
    
*   [`rect()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
    
*   [`<relative-size>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/relative-size)
    
*   [`rem()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
    
*   [`repeat()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/repeat)
    
*   [`repeating-conic-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-conic-gradient)
    
*   [`repeating-linear-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-linear-gradient)
    
*   [`repeating-radial-gradient()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/repeating-radial-gradient)
    
*   [`:required` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required)
    
*   [`resize` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize)
    
*   [`<resolution>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    
*   [`revert` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    
*   [`revert-layer` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    
*   [`revert-rule` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
    
*   [`rgb()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
    
*   [`right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    
*   [`:right` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:right)
    
*   [`:root` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
    
*   [`rotate` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rotate)
    
*   [`rotate()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate)
    
*   [`rotate3d()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotate3d)
    
*   [`rotateX()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateX)
    
*   [`rotateY()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateY)
    
*   [`rotateZ()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/rotateZ)
    
*   [`round()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    
*   [`row-gap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-gap)
    
*   [`row-rule` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
    
*   [`row-rule-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-break)
    
*   [`row-rule-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-color)
    
*   [`row-rule-inset-cap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap)
    
*   [`row-rule-inset-cap-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-end)
    
*   [`row-rule-inset-cap-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-cap-start)
    
*   [`row-rule-inset-junction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction)
    
*   [`row-rule-inset-junction-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-end)
    
*   [`row-rule-inset-junction-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-inset-junction-start)
    
*   [`row-rule-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    
*   [`row-rule-visibility-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-visibility-items)
    
*   [`row-rule-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-width)
    
*   [`ruby-align` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align)
    
*   [`ruby-overhang` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang)
    
*   [`ruby-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-position)
    
*   [`rule` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule)
    
*   [`rule-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-break)
    
*   [`rule-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-color)
    
*   [`rule-inset-cap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-cap)
    
*   [`rule-inset-junction` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-inset-junction)
    
*   [`<rule-list>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
    
*   [`rule-overlap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-overlap)
    
*   [`rule-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-style)
    
*   [`rule-visibility-items` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-visibility-items)
    
*   [`rule-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rule-width)
    
*   [`rx` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/rx)
    
*   [`ry` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ry)
    

### S

*   [Selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
    
*   [`saturate()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/saturate)
    
*   [`scale` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scale)
    
*   [`scale()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale)
    
*   [`scale3d()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scale3d)
    
*   [`scaleX()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleX)
    
*   [`scaleY()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleY)
    
*   [`scaleZ()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/scaleZ)
    
*   [`@scope` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
    
*   [`:scope` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
    
*   [`scroll()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
    
*   [`scroll-behavior` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-behavior)
    
*   [`::scroll-button()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-button)
    
*   [`scroll-initial-target` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-initial-target)
    
*   [`scroll-margin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin)
    
*   [`scroll-margin-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block)
    
*   [`scroll-margin-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-end)
    
*   [`scroll-margin-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-block-start)
    
*   [`scroll-margin-bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-bottom)
    
*   [`scroll-margin-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline)
    
*   [`scroll-margin-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-end)
    
*   [`scroll-margin-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-inline-start)
    
*   [`scroll-margin-left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-left)
    
*   [`scroll-margin-right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-right)
    
*   [`scroll-margin-top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-margin-top)
    
*   [`::scroll-marker` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker)
    
*   [`scroll-marker-group` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-marker-group)
    
*   [`::scroll-marker-group` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker-group)
    
*   [`scroll-padding` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding)
    
*   [`scroll-padding-block` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block)
    
*   [`scroll-padding-block-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-end)
    
*   [`scroll-padding-block-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-block-start)
    
*   [`scroll-padding-bottom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-bottom)
    
*   [`scroll-padding-inline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline)
    
*   [`scroll-padding-inline-end` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-end)
    
*   [`scroll-padding-inline-start` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-inline-start)
    
*   [`scroll-padding-left` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-left)
    
*   [`scroll-padding-right` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-right)
    
*   [`scroll-padding-top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-padding-top)
    
*   [`scroll-snap-align` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-align)
    
*   [`scroll-snap-stop` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-stop)
    
*   [`scroll-snap-type` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
    
*   [`scroll-target-group` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-target-group)
    
*   [`scroll-timeline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    
*   [`scroll-timeline-axis` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
    
*   [`scroll-timeline-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
    
*   [`scrollbar-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color)
    
*   [`scrollbar-gutter` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
    
*   [`scrollbar-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
    
*   [`::search-text` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::search-text)
    
*   [`:seeking` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:seeking)
    
*   [`::selection` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
    
*   [`<self-position>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/self-position)
    
*   [`sepia()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/filter-function/sepia)
    
*   [`shape()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
    
*   [`shape-image-threshold` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-image-threshold)
    
*   [`shape-margin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-margin)
    
*   [`shape-outside` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [`shape-rendering` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-rendering)
    
*   [`<shape>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape)
    
*   [`sibling-count()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count)
    
*   [`sibling-index()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)
    
*   [`sign()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sign)
    
*   [`sin()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`size` CSS at-rule descriptor (`@page`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size)
    
*   [`size-adjust` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/size-adjust)
    
*   [`skew()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skew)
    
*   [`skewX()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewX)
    
*   [`skewY()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/skewY)
    
*   [`::slotted()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
    
*   [`speak-as` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
    
*   [`speak-as` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/speak-as)
    
*   [`::spelling-error` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::spelling-error)
    
*   [`sqrt()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`src` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/src)
    
*   [`:stalled` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:stalled)
    
*   [`@starting-style` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    
*   [`:state()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
    
*   [`steps()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
    
*   [`stop-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-color)
    
*   [`stop-opacity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stop-opacity)
    
*   [`<string>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    
*   [`stroke` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke)
    
*   [`stroke-dasharray` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dasharray)
    
*   [`stroke-dashoffset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-dashoffset)
    
*   [`stroke-linecap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linecap)
    
*   [`stroke-linejoin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-linejoin)
    
*   [`stroke-miterlimit` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-miterlimit)
    
*   [`stroke-opacity` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-opacity)
    
*   [`stroke-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/stroke-width)
    
*   [`suffix` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
    
*   [`superellipse()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
    
*   [`@supports` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
    
*   [`symbols` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
    
*   [`symbols()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    
*   [`syntax` CSS at-rule descriptor (`@property`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
    
*   [`system` CSS at-rule descriptor (`@counter-style`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
    
*   [`<system-color>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
    

### T

*   [Type selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
    
*   [`tab-size` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size)
    
*   [`table-layout` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/table-layout)
    
*   [`tan()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    
*   [`-webkit-tap-highlight-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-tap-highlight-color)
    
*   [`:target` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
    
*   [`:target-after` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-after)
    
*   [`:target-before` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-before)
    
*   [`:target-current` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target-current)
    
*   [`::target-text` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
    
*   [`text-align` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    
*   [`text-align-last` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last)
    
*   [`text-anchor` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-anchor)
    
*   [`text-autospace` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-autospace)
    
*   [`text-box` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box)
    
*   [`text-box-edge` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-edge)
    
*   [`text-box-trim` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-box-trim)
    
*   [`text-combine-upright` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-combine-upright)
    
*   [`text-decoration` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
    
*   [`text-decoration-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-decoration-inset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-inset)
    
*   [`text-decoration-line` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    
*   [`text-decoration-skip` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip)
    
*   [`text-decoration-skip-ink` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-skip-ink)
    
*   [`text-decoration-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    
*   [`text-decoration-thickness` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-thickness)
    
*   [`<text-edge>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/text-edge)
    
*   [`text-emphasis` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis)
    
*   [`text-emphasis-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    
*   [`text-emphasis-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-position)
    
*   [`text-emphasis-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-style)
    
*   [`-webkit-text-fill-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-fill-color)
    
*   [`text-fit` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-fit)
    
*   [`text-indent` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent)
    
*   [`text-justify` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-justify)
    
*   [`text-orientation` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    
*   [`text-overflow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-overflow)
    
*   [`text-rendering` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-rendering)
    
*   [`-webkit-text-security` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security)
    
*   [`text-shadow` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    
*   [`text-size-adjust` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust)
    
*   [`text-spacing-trim` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-spacing-trim)
    
*   [`-webkit-text-stroke` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke)
    
*   [`-webkit-text-stroke-color` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-color)
    
*   [`-webkit-text-stroke-width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-stroke-width)
    
*   [`text-transform` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    
*   [`text-underline-offset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-offset)
    
*   [`text-underline-position` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-underline-position)
    
*   [`text-wrap` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap)
    
*   [`text-wrap-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
    
*   [`text-wrap-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-style)
    
*   [`<time-percentage>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time-percentage)
    
*   [`<time>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    
*   [`<timeline-range-name>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
    
*   [`timeline-scope` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
    
*   [timeline-trigger CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
    
*   [timeline-trigger-activation-range CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    
*   [timeline-trigger-activation-range-end CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
    
*   [timeline-trigger-activation-range-start CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
    
*   [timeline-trigger-active-range CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [timeline-trigger-active-range-end CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
    
*   [timeline-trigger-active-range-start CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
    
*   [timeline-trigger-name CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    
*   [timeline-trigger-source CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    
*   [`top` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    
*   [`touch-action` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action)
    
*   [`-webkit-touch-callout` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-touch-callout)
    
*   [`transform` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
    
*   [`transform-box` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-box)
    
*   [`<transform-function>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
    
*   [`transform-origin` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
    
*   [`transform-style` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style)
    
*   [`transition` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`transition-behavior` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [`transition-delay` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`transition-duration` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    
*   [`transition-property` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-timing-function` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    
*   [`translate` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/translate)
    
*   [`translate()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate)
    
*   [`translate3d()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translate3d)
    
*   [`translateX()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateX)
    
*   [`translateY()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateY)
    
*   [`translateZ()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function/translateZ)
    
*   [trigger-scope CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    
*   [`type()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
    

### U

*   [Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
    
*   [`unicode-bidi` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/unicode-bidi)
    
*   [`unicode-range` CSS at-rule descriptor (`@font-face`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face/unicode-range)
    
*   [`unset` CSS keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [`url()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_function)
    
*   [`<url>` CSS type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
    
*   [`-moz-user-focus` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus)
    
*   [`-moz-user-input` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input)
    
*   [`:user-invalid` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    
*   [`user-modify` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify)
    
*   [`user-select` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    
*   [`:user-valid` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)
    

### V

*   [`:valid` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
    
*   [`var()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    
*   [`vector-effect` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vector-effect)
    
*   [`vertical-align` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
    
*   [`view()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    
*   [`view-timeline` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    
*   [`view-timeline-axis` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    
*   [`view-timeline-inset` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`view-timeline-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    
*   [`@view-transition` CSS at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)
    
*   [`::view-transition` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition)
    
*   [`view-transition-class` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-class)
    
*   [`::view-transition-group()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-group)
    
*   [`::view-transition-image-pair()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-image-pair)
    
*   [`view-transition-name` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-name)
    
*   [`::view-transition-new()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-new)
    
*   [`::view-transition-old()` CSS pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::view-transition-old)
    
*   [`view-transition-scope` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-transition-scope)
    
*   [`visibility` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
    
*   [`:visited` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
    
*   [`:volume-locked` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:volume-locked)
    

### W

*   [`:where()` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
    
*   [`white-space` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space)
    
*   [`white-space-collapse` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space-collapse)
    
*   [`widows` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/widows)
    
*   [`width` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
*   [`will-change` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
    
*   [`word-break` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [`word-spacing` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-spacing)
    
*   [`writing-mode` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    

### X

*   [`x` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/x)
    
*   [`:xr-overlay` CSS pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:xr-overlay)
    
*   [`xywh()` CSS function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
    

### Y

*   [`y` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/y)
    

### Z

*   [`z-index` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/z-index)
    
*   [`zoom` CSS property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/zoom)
    

[Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#selectors)

----------------------------------------------------------------------------------

The following are the various [selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors)
, which allow styles to be conditional based on various features of elements within the DOM.

### [Basic selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#basic_selectors)

**Basic selectors** are fundamental selectors; these are the most basic selectors that are frequently combined to create other, more complex selectors.

*   [Universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
     `*`
*   [Type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
     `elementname`
*   [Class selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
     `.classname`
*   [ID selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/ID_selectors)
     `#idname`
*   [Attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
     `[attr=value]`

### [Grouping selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#grouping_selectors)

[Selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list)
 `A, B`

Specifies that both `A` and `B` elements are selected. This is a grouping method to select several matching elements.

### [Combinators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#combinators)

Combinators are selectors that establish a relationship between two or more simple selectors, such as "`A` is a child of `B`" or "`A` is adjacent to `B`", creating a complex selector.

[Next-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Next-sibling_combinator)
 `A + B`

Specifies that the elements selected by both `A` and `B` have the same parent and that the element selected by `B` immediately follows the element selected by `A` horizontally.

[Subsequent-sibling combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Subsequent-sibling_combinator)
 `A ~ B`

Specifies that the elements selected by both `A` and `B` share the same parent and that the element selected by `A` comes before—but not necessarily immediately before—the element selected by `B`.

[Child combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Child_combinator)
 `A > B`

Specifies that the element selected by `B` is the direct child of the element selected by `A`.

[Descendant combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Descendant_combinator)
 `A B`

Specifies that the element selected by `B` is a descendant of the element selected by `A`, but is not necessarily a direct child.

[Column combinator](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Column_combinator)
 `A || B`

Specifies that the element selected by `B` is located within the table column specified by `A`. Elements which span multiple columns are considered to be a member of all of those columns.

### [Pseudo](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#pseudo)

[Pseudo classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 `:`

Specifies a special state of the selected element(s).

[Pseudo elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 `::`

Represents entities that are not included in HTML.

See also [selectors in the Selectors specification](https://drafts.csswg.org/selectors/ "External link (opens in new tab)")
 and the [pseudo-element specification](https://drafts.csswg.org/css-pseudo/ "External link (opens in new tab)")
.

[Concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#concepts)

--------------------------------------------------------------------------------

### [Syntax and semantics](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#syntax_and_semantics)

*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
    
*   [At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
    
*   [Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Comments](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Comments)
    
*   [Descriptor](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Descriptor)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    
*   [Shorthand properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
    
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values)
    
*   [Value definition syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax)
    
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
    
*   [CSS functional notations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#values)

*   [Actual value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
    
*   [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
    
*   [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    
*   [Resolved value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#resolved_value)
    
*   [Specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
    
*   [Used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    

### [Layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#layout)

*   [Block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
    
*   [Box model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Introduction)
    
*   [Containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
    
*   [Layout mode](https://developer.mozilla.org/en-US/docs/Glossary/Layout_mode)
    
*   [Margin collapsing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_model/Margin_collapsing)
    
*   [Replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
    
*   [Stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Positioned_layout/Stacking_context)
    
*   [Visual formatting model](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Visual_formatting_model)
    

[DOM-CSS / CSSOM](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#dom-css_cssom)

--------------------------------------------------------------------------------------------

### [Major object types](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#major_object_types)

*   [`Document.styleSheets`](https://developer.mozilla.org/en-US/docs/Web/API/Document/styleSheets)
    
*   [`HTMLElement.style`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style)
    
*   [`Element.className`](https://developer.mozilla.org/en-US/docs/Web/API/Element/className)
    
*   [`Element.classList`](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)
    
*   [`StyleSheetList`](https://developer.mozilla.org/en-US/docs/Web/API/StyleSheetList)
    
*   [`CSSRuleList`](https://developer.mozilla.org/en-US/docs/Web/API/CSSRuleList)
    
*   [`CSSRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule)
    
*   [`CSSStyleRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleRule)
    
*   [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration)
    

### [Important methods](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#important_methods)

*   [`CSSStyleSheet.insertRule()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet/insertRule)
    
*   [`CSSStyleSheet.deleteRule()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleSheet/deleteRule)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#see_also)

--------------------------------------------------------------------------------

*   [Mozilla CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
     (prefixed with `-moz-`)
*   [WebKit CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
     (mostly prefixed with `-webkit-`)

[External Links](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#external_links)

--------------------------------------------------------------------------------------------

*   [CSS Indices (w3.org)](https://www.w3.org/TR/css/#indices "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 13, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/index.md?plain=1 "Folder: en-us/web/css/reference (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F93b85a5bc2b4589d93185263fd2c14381c36f821%0A*+Document+last+modified%3A+2025-11-13T17%3A22%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")