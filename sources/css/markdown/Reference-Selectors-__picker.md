*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#mdn-search)
    

`::picker()` CSS pseudo-element
===============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/278)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::picker()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 targets the picker part of an element, for example the drop-down picker of a [customizable select element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#syntax)

-----------------------------------------------------------------------------------------------

css

    ::picker(<ident>) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#parameters)

[`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)

A string representing the element whose picker you want to target. The following values are available:

[`select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#select)

The drop-down picker of customizable select elements.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#description)

---------------------------------------------------------------------------------------------------------

The `::picker()` pseudo-element targets the picker part of a form control, that is, the pop-up part that appears to allow you to make a selection when you press the control button. It is only available to target when the originating element has a picker and has base appearance set on it via the [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 property `base-select` value.

The `::picker(select)` selector targets all descendants of customizable `<select>` element except for the first `<button>` child; these descendants are grouped together by the browser and rendered as the picker. The first `<button>` child represents the control button that opens the picker when pressed.

This allows you to target all of the picker contents as a single entity, for example if you want to customize its border, animate it when it appears and disappears, or position it somewhere different to the default position. Our [customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 guide shows many examples of `::picker(select)` usage.

### [Picker popover behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#picker_popover_behavior)

The `<select>` element and the picker have an implicit invoker/popover relationship assigned to them automatically, as specified by the [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
. See [Using the Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using)
 for more details of popover behavior, and see [Animating the picker drop-down using popover states](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select#animating_the_picker_using_popover_states)
 for a typical use case allowed by the implicit popover association.

### [Picker anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#picker_anchor_positioning)

A further side-effect of the implicit invoker/popover relationship mentioned above is that the `<select>` element and the picker also have an implicit anchor reference, meaning that the picker is automatically associated with the select via [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
. This has several advantages, most notably:

*   The browser default styles position the picker relative to the button (the anchor) and you can customize this position as explained in [Positioning elements relative to their anchor](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#positioning_elements_relative_to_their_anchor)
    . For reference, the related default styles are as follows:
    
    css
    
        inset: auto;
        margin: 0;
        min-inline-size: anchor-size(self-inline);
        min-block-size: 1lh;
        /* Go to the edge of the viewport, and add scrollbars if needed. */
        max-block-size: stretch;
        overflow: auto;
        /* Below and span-right, by default. */
        position-area: block-end span-inline-end;
        
    
*   The browser default styles also define some position-try fallbacks that reposition the picker if it is in danger of overflowing the viewport. Position-try fallbacks are explained in the [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     guide. For reference, the related default fallback styles are as follows:
    
    css
    
        position-try-order: most-block-size;
        position-try-fallbacks:
          /* First try above and span-right, */
          /* then below but span-left, */
          /* then above and span-left. */
          block-start span-inline-end,
          block-end span-inline-start,
          block-start span-inline-start;
        
    

**Note:** If you want to remove the implicit anchor reference to stop the picker from being anchored to the `<select>` element, you can do so by setting the `position-anchor` property of the picker to an anchor name that doesn't exist in the current document, such as `--not-an-anchor-name`. See also [removing an anchor association](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#removing_an_anchor_association)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#examples)

---------------------------------------------------------------------------------------------------

### [Basic custom select usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#basic_custom_select_usage)

To opt-in to the custom select functionality and minimal browser base styles (and remove the OS-provided styling), the `<select>` element and its picker both need to have an [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 value of `base-select` set on them:

css

    select,
    ::picker(select) {
      appearance: base-select;
    }
    

You could then, for example, remove the picker's default black [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
:

css

    ::picker(select) {
      border: none;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Form Control Styling Level 1  <br>\# picker-pseudo](https://drafts.csswg.org/css-forms-1/#picker-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker#see_also)

---------------------------------------------------------------------------------------------------

*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
    , [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
    , [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
    , [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<selectedcontent>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent)
    
*   [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
    
*   [`::picker-icon`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker-icon)
    , [`::checkmark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::checkmark)
    
*   [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
    , [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
    
*   [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_picker/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_picker (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Apicker&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_picker%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Apicker%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_picker%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")