*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#mdn-search)
    

Firefox (-moz-) vendor-prefixed CSS extensions
==============================================

A [vendor prefix](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
 is used to indicate that a feature is specific to a certain browser. Firefox supports several extensions to [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
, which are prefixed with `-moz-`.

[\-moz-prefixed properties without standard equivalents](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#-moz-prefixed_properties_without_standard_equivalents)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Note:** These extensions are mostly experimental or deprecated but kept for backward compatibility. You should avoid using them on production websites.

*   [`-moz-float-edge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-float-edge)
    
*   [`-moz-force-broken-image-icon`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-force-broken-image-icon)
     : Use `alt` text instead.
*   [`-moz-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-orient)
    
*   `-moz-osx-font-smoothing`: A similar [`font-smooth`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-smooth)
     equivalent exists.
*   [`-moz-user-focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus)
    
*   [`-moz-user-input`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input)
    
*   `-moz-user-modify`: A non-prefixed [`user-modify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify)
     equivalent exists, but the HTML [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute is recommended instead.

[\-moz-prefixed properties with standard equivalents](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#-moz-prefixed_properties_with_standard_equivalents)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following properties were implemented first using the `-moz-` vendor prefix, but are now supported in Firefox using the standard (non-prefixed) syntax. Support for the prefixed version is typically dropped eventually, so use the standard property instead.

### [A](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#a)

*   [`-moz-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
     : Prefixed version still supported.
*   [`-moz-animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
     : Prefixed version still supported.
*   [`-moz-animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
     : Prefixed version still supported.
*   [`-moz-animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
     : Prefixed version still supported.
*   [`-moz-animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
     : Prefixed version still supported.
*   [`-moz-animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
     : Prefixed version still supported.
*   [`-moz-animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
     : Prefixed version still supported.
*   [`-moz-animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
     : Prefixed version still supported.
*   [`-moz-animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
     : Prefixed version still supported.
*   `-moz-appearance`: The prefixed version of [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
     is still supported.

### [B](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#b)

*   [`-moz-backface-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backface-visibility)
     : Prefixed version still supported.
*   `-moz-background-clip` : Not supported; use [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    .
*   `-moz-background-origin` : Not supported; use [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    .
*   `-moz-box-align` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
    .
*   `-moz-background-inline-policy` : Not supported; use [`box-decoration-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-decoration-break)
    .
*   `-moz-box-direction` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    .
*   `-moz-box-flex` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`flex-grow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-grow)
    .
*   `-moz-box-ordinal-group` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`order`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/order)
    .
*   `-moz-box-orient` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    .
*   `-moz-box-pack` : Use [CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
     with [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
    .
*   `-moz-background-size` : Not supported; use [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    .
*   `-moz-border-end` : Not supported; use [`border-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
    .
*   `-moz-border-end-color` : Not supported; use [`border-inline-end-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-color)
    .
*   `-moz-border-end-style` : Not supported; use [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
    .
*   `-moz-border-end-width` : Not supported; use [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
    .
*   `-moz-border-image` : Not supported; use [`border-inline-end-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-width)
    .
*   `-moz-border-start` : Not supported; use [`border-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
    .
*   `-moz-border-start-color` : Not supported; use [`border-inline-start-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-color)
    .
*   `-moz-border-start-style` : Not supported; use [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
    .
*   `-moz-border-start-width` : Not supported; use [`border-inline-start-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-width)
    .
*   [`-moz-box-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-sizing)
     : Prefixed version still supported.

### [C](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#c)

*   `-moz-column-count` : Not supported; use [`column-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-count)
    .
*   `-moz-column-fill` : Not supported; use [`column-fill`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-fill)
    .
*   `-moz-column-gap` : Not supported; use [`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-gap)
    .
*   `-moz-column-width` : Not supported; use [`column-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-width)
    .
*   `-moz-column-rule` : Not supported; use [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    .
*   `-moz-column-rule-width` : Not supported; use [`column-rule-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-width)
    .
*   `-moz-column-rule-style` : Not supported; use [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    .
*   `-moz-column-rule-color` : Not supported; use [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    .

### [F–M](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#f%E2%80%93m)

*   [`-moz-font-feature-settings`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-feature-settings)
     : Prefixed version still supported.
*   [`-moz-font-language-override`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-language-override)
     : Prefixed version still supported.
*   [`-moz-hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
     : Prefixed version still supported.
*   `-moz-margin-end` : Not supported; use [`margin-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-end)
    .
*   `-moz-margin-start` : Not supported; use [`margin-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline-start)
    .

### [O-P](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#o-p)

*   `-moz-opacity` : Not supported; use [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
    .
*   `-moz-outline` : Not supported; use [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    .
*   `-moz-outline-color` : Not supported; use [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    .
*   `-moz-outline-offset` : Not supported; use [`outline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
    .
*   `-moz-outline-style` : Not supported; use [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
    .
*   `-moz-outline-width` : Not supported; use [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
    .
*   `-moz-padding-end` : Not supported; use [`padding-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-end)
    .
*   `-moz-padding-start` : Not supported; use [`padding-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-inline-start)
    .
*   [`-moz-perspective`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective)
     : Prefixed version still supported.
*   [`-moz-perspective-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective-origin)
     : Prefixed version still supported.

### [T–Z](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#t%E2%80%93z)

*   `-moz-tab-size`: Use [`tab-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/tab-size)
    
*   `-moz-text-align-last` : Not supported; use [`text-align-last`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align-last)
    .
*   `-moz-text-decoration-color` : Not supported; use [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    .
*   `-moz-text-decoration-line` : Not supported; use [`text-decoration-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-line)
    .
*   `-moz-text-decoration-style` : Not supported; use [`text-decoration-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-style)
    .
*   `-moz-text-size-adjust`: See [`text-size-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-size-adjust)
     .
*   [`-moz-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
     : Prefixed version still supported.
*   [`-moz-transform-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-origin)
     : Prefixed version still supported.
*   [`-moz-transform-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform-style)
     : Prefixed version still supported.
*   `-moz-transition` : Not supported; use [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    .
*   `-moz-transition-delay` : Not supported; use [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    .
*   `-moz-transition-duration` : Not supported; use [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    .
*   `-moz-transition-property` : Not supported; use [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    .
*   `-moz-transition-timing-function` : Not supported; use [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    .
*   `-moz-user-select`: Use [`user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    .

[\-moz-prefixed property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#-moz-prefixed_property_values)

----------------------------------------------------------------------------------------------------------------------------------------------

### [Global values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#global_values)

*   `-moz-initial`: See [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    .

### [background-image](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#background-image)

**Property:** [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)

*   `-moz-linear-gradient` : Use [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
    .
*   `-moz-radial-gradient` : Use [`radial-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/radial-gradient)
    .
*   `-moz-element` : Use [`element()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/element)
    .
*   [`-moz-image-rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect)
    

### [border-style and outline-style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#border-style_and_outline-style)

**Properties:** [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 and [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
.

*   `-moz-bg-inset`
*   `-moz-bg-outset`
*   `-moz-bg-solid`

### [<color> keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#color_keywords)

**Type:** [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)

*   `-moz-activehyperlinktext`
*   `-moz-hyperlinktext`
*   `-moz-visitedhyperlinktext`
*   `-moz-buttonhoverface`
*   `-moz-buttonhovertext`
*   `-moz-default-background-color`
*   `-moz-default-color`
*   `-moz-cellhighlight`
*   `-moz-cellhighlighttext`
*   `-moz-field`
*   `-moz-fieldtext`
*   `-moz-dialog`
*   `-moz-dialogtext`
*   `-moz-menuhover`
*   `-moz-menuhovertext`

### [empty-cells](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#empty-cells)

**Property:** [`empty-cells`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/empty-cells)

*   `-moz-show-background` (default value in quirks mode)

### [font-family](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#font-family)

**Property:** [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)

*   `-moz-fixed`

### [image-rendering](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#image-rendering)

**Property:** [`image-rendering`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering)

*   `-moz-crisp-edges` : Use [`crisp-edges`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/image-rendering#crisp-edges)
    .

### [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#length)

**Type:** [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

*   `-moz-calc`: Use [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    .

### [list-style-type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#list-style-type)

**Property:** [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)

Several vendor-prefixed values for `list-style-type` are now supported as standard values without a `-moz-` prefix, except for those in the following list. See [Browser Compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type#browser_compatibility)
 for details.

*   `-moz-ethiopic-halehame`
*   `-moz-ethiopic-halehame-am`
*   `-moz-ethiopic-halehame-ti-er`
*   `-moz-ethiopic-halehame-ti-et`
*   `-moz-hangul`
*   `-moz-hangul-consonant`
*   `-moz-urdu`

### [text-align](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#text-align)

**Property:** [`text-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)

*   `-moz-center` : Use [`text-align: center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    .
*   `-moz-left` : Use [`text-align: left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    .
*   `-moz-right` : Use [`text-align: right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-align)
    .

### [width, min-width, and max-width](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#width_min-width_and_max-width)

**Properties:** [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, and [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)

*   `-moz-min-content`: See [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
    .
*   `-moz-fit-content`: See [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    .
*   `-moz-max-content`: See [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    .
*   `-moz-available`: See [`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#stretch)
    .

[Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#pseudo-classes)

---------------------------------------------------------------------------------------------------------------

*   `:-moz-any` : Use [`:is`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
    .
*   `:-moz-any-link` : Use [`:any-link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:any-link)
    .
*   [`:-moz-broken`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-broken)
    
*   [`:-moz-drag-over`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-drag-over)
    
*   [`:-moz-first-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-first-node)
    
*   `:-moz-full-screen` : Not supported; use [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    .
*   `:-moz-full-screen-ancestor` : Not supported; use [`:fullscreen`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:fullscreen)
    .
*   [`:-moz-handler-blocked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-blocked)
    
*   [`:-moz-handler-crashed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-crashed)
    
*   [`:-moz-handler-disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-handler-disabled)
    
*   [`:-moz-last-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-last-node)
    
*   [`:-moz-loading`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-loading)
    
*   [`:-moz-locale-dir(ltr)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_ltr)
    
*   [`:-moz-locale-dir(rtl)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-locale-dir_rtl)
    
*   `:-moz-native-anonymous`
*   `:-moz-placeholder` : Use [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
    .
*   [`:-moz-only-whitespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-only-whitespace)
    
*   `:-moz-read-only` : Use [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only)
    .
*   `:-moz-read-write` : Use [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write)
    .
*   [`:-moz-submit-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-submit-invalid)
    : See [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
    .
*   [`:-moz-suppressed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-suppressed)
    
*   `:-moz-ui-invalid` : Use [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid)
    .
*   `:-moz-ui-valid` : Use [`:user-valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-valid)
    .
*   [`:-moz-user-disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-user-disabled)
    
*   [`:-moz-window-inactive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-window-inactive)
    

[Pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#pseudo-elements)

-----------------------------------------------------------------------------------------------------------------

*   `::-moz-canvas`
*   `::-moz-cell-content`
*   [`::-moz-color-swatch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-color-swatch)
    
*   [`::-moz-focus-inner`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-focus-inner)
    
*   `::-moz-focus-outer`
*   `::-moz-inline-table`
*   [`::-moz-list-bullet`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-bullet)
    
*   [`::-moz-list-number`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-list-number)
    
*   [`::-moz-meter-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-meter-bar)
    
*   `::-moz-pagebreak`
*   `::-moz-pagecontent`
*   `::-moz-placeholder` : Use [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
    .
*   [`::-moz-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-progress-bar)
    
*   [`::-moz-range-progress`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-progress)
    
*   [`::-moz-range-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-thumb)
    
*   [`::-moz-range-track`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-track)
    
*   `::-moz-scrolled-canvas`
*   `::-moz-scrolled-content`
*   `::-moz-selection` : Use [`::selection`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::selection)
    .
*   `::-moz-svg-foreign-content`
*   `::-moz-table`
*   `::-moz-table-cell`
*   `::-moz-table-column`
*   `::-moz-table-column-group`
*   `::-moz-table-outer`
*   `::-moz-table-row`
*   `::-moz-table-row-group`
*   `::-moz-viewport`
*   `::-moz-viewport-scroll`

[At-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#at-rules)

---------------------------------------------------------------------------------------------------

*   [`@-moz-document`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document)
    

[Media features](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#media_features)

---------------------------------------------------------------------------------------------------------------

*   [`-moz-device-pixel-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-moz-device-pixel-ratio)
    
*   `-moz-platform`
*   `-moz-windows-glass`

[Other](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#other)

---------------------------------------------------------------------------------------------

*   `-moz-alt-content`: See [Firefox bug 11011](https://bugzil.la/11011 "External link (opens in new tab)")
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions#see_also)

---------------------------------------------------------------------------------------------------

*   [WebKit (-webkit-) vendor-prefixed CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
    
*   [Vendor Prefix](https://developer.mozilla.org/en-US/docs/Glossary/Vendor_Prefix)
     glossary entry

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/mozilla_extensions/index.md?plain=1 "Folder: en-us/web/css/reference/mozilla_extensions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FMozilla_extensions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fmozilla_extensions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FMozilla_extensions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fmozilla_extensions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa9fd2746e238ae3948572a94036bb505de19b81b%0A*+Document+last+modified%3A+2026-04-02T07%3A54%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")