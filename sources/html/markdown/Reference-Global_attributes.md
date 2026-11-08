*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#mdn-search)
    

Global attributes
=================

**Global attributes** are attributes common to all HTML elements; they can be used on all elements, though they may have no effect on some elements.

Global attributes may be specified on all [HTML elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)
, _even those not specified in the standard_. That means that any non-standard elements must still permit these attributes, even though using those elements means that the document is no longer HTML5-compliant. For example, HTML5-compliant browsers hide content marked as `<foo hidden>…</foo>`, even though `<foo>` is not a valid HTML element.

In addition to the basic HTML global attributes, the following global attributes also exist:

*   `xml:lang` and `xml:base` — these are inherited from the XHTML specifications and deprecated, but kept for compatibility purposes.
*   The ARIA [`role`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles)
     attribute and the multiple [`aria-*`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes)
     states and properties, used for ensuring accessibility.
*   The [event handler attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#list_of_global_event_handler_attributes)
     listed below.

[List of global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#list_of_global_attributes)

-------------------------------------------------------------------------------------------------------------------------------------

[`accesskey`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/accesskey)

Provides a hint for generating a keyboard shortcut for the current element. This attribute consists of a space-separated list of characters. The browser should use the first one that exists on the computer keyboard layout.

[`anchor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor)

Associates a positioned element with an anchor element. The attribute's value is the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 value of the element you want to anchor the positioned element to. The element can then be positioned [using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
.

[`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize)

Controls whether inputted text is automatically capitalized and, if so, in what manner.

[`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)

Controls whether input text is automatically corrected for spelling errors. This can be applied to elements that have editable text except for [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements with the attribute: [`type="password"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
, [`type="email"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
, or [`type="url"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
.

[`autofocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autofocus)

Indicates that an element is to be focused on page load, or as soon as the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 it is part of is displayed. This attribute is a boolean, initially false.

[`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)

A space-separated list of the classes of the element. Classes allow CSS and JavaScript to select and access specific elements via the [class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors)
 or functions like the method [`Document.getElementsByClassName()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementsByClassName)
.

[`containertiming`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertiming)

A string that marks the element as a container root for observation by [`PerformanceObserver`](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver)
 objects using the `"container"` type; its value identifies the container.

[`containertimingignore`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/containertimingignore)

A boolean attribute that excludes the element and its descendants from contributing to the timing of any ancestor element marked with `containertiming`.

[`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)

An [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicating if the element should be editable by the user. If so, the browser modifies its widget to allow editing. The attribute must take one of the following values:

*   `true` or the _empty string_, which indicates that the element must be editable;
*   `false`, which indicates that the element must not be editable.
*   `plaintext-only`, which indicates the element's raw text is editable, but rich text formatting is disabled.

[`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)

Forms a class of attributes, called custom data attributes, that allow proprietary information to be exchanged between the [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 and its [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
 representation that may be used by scripts. All such custom data are available via the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface of the element the attribute is set on. The [`HTMLElement.dataset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dataset)
 property gives access to them.

[`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)

An enumerated attribute indicating the directionality of the element's text. It can have the following values:

*   `ltr`, which means _left to right_ and is to be used for languages that are written from the left to the right (like English);
*   `rtl`, which means _right to left_ and is to be used for languages that are written from the right to the left (like Arabic);
*   `auto`, which lets the user agent decide. It uses a basic algorithm as it parses the characters inside the element until it finds a character with a strong directionality, then it applies that directionality to the whole element.

[`draggable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/draggable)

An enumerated attribute indicating whether the element can be dragged, using the [Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
. It can have the following values:

*   `true`, which indicates that the element may be dragged
*   `false`, which indicates that the element may not be dragged.

[`enterkeyhint`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint)

Hints what action label (or icon) to present for the enter key on virtual keyboards.

[`exportparts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts)

Used to transitively export shadow parts from a nested shadow tree into a containing light tree.

[`headingoffset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset)

Increases the computed heading level of the [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 inside the element, without changing the elements used to write them.

[`headingreset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset)

A boolean attribute that stops the `headingoffset` values of ancestor elements from applying to the headings inside the element.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden)

An enumerated attribute indicating that the element is not yet, or is no longer, _relevant_. For example, it can be used to hide elements of the page that can't be used until the login process has been completed. The browser won't render such elements. This attribute must not be used to hide content that could legitimately be shown.

[`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)

Defines a unique identifier (ID) which must be unique in the whole document. Its purpose is to identify the element when linking (using a fragment identifier), scripting, or styling (with CSS).

[`inert`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inert)

A boolean value that makes the browser disregard user input events for the element. Useful when click events are present.

[`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode)

Provides a hint to browsers about the type of virtual keyboard configuration to use when editing this element or its contents. Used primarily on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, but is usable on any element while in [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 mode.

[`is`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/is)

Allows you to specify that a standard HTML element should behave like a registered customized built-in element (see [Using custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
 for more details).

**Note:** The `item*` attributes are part of the [WHATWG HTML Microdata feature](https://html.spec.whatwg.org/multipage/microdata.html#microdata "External link (opens in new tab)")
.

[`itemid`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemid)

The unique, global identifier of an item.

[`itemprop`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemprop)

Used to add properties to an item. Every HTML element may have an `itemprop` attribute specified, where an `itemprop` consists of a name and value pair.

[`itemref`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemref)

Properties that are not descendants of an element with the `itemscope` attribute can be associated with the item using an `itemref`. It provides a list of element ids (not `itemid`s) with additional properties elsewhere in the document.

[`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)

`itemscope` (usually) works along with [`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)
 to specify that the HTML contained in a block is about a particular item. `itemscope` creates the Item and defines the scope of the `itemtype` associated with it. `itemtype` is a valid URL of a vocabulary (such as [schema.org](https://schema.org/ "External link (opens in new tab)")
) that describes the item and its properties context.

[`itemtype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemtype)

Specifies the URL of the vocabulary that will be used to define `itemprop`s (item properties) in the data structure. [`itemscope`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/itemscope)
 is used to set the scope of where in the data structure the vocabulary set by `itemtype` will be active.

[`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)

Helps define the language of an element: the language that non-editable elements are in, or the language that editable elements should be written in by the user. The attribute should contain a valid [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
. `xml:lang` has priority over it.

[`nonce`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce)

A cryptographic [nonce](https://developer.mozilla.org/en-US/docs/Glossary/Nonce)
 ("number used once") which can be used by [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 to determine whether or not a given fetch will be allowed to proceed.

[`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)

A space-separated list of the part names of the element. Part names allows CSS to select and style specific elements in a shadow tree via the [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element.

[`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)

Used to designate an element as a popover element (see [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
). Popover elements are hidden via `display: none` until opened via an invoking/control element (i.e., a `<button>` or `<input type="button">` with a [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button#popovertarget)
 attribute) or a [`HTMLElement.showPopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover)
 call.

[`role`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles)

Roles define the semantic meaning of content, allowing screen readers and other tools to present and support interaction with an object in a way that is consistent with user expectations of that type of object. `roles` are added to HTML elements using `role="role_type"`, where `role_type` is the name of a role in the ARIA specification.

[`slot`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/slot)

Assigns a slot in a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 shadow tree to an element: An element with a `slot` attribute is assigned to the slot created by the [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
 element whose [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot#name)
 attribute's value matches that `slot` attribute's value.

[`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)

An enumerated attribute defines whether the element may be checked for spelling errors. It may have the following values:

*   empty string or `true`, which indicates that the element should be, if possible, checked for spelling errors;
*   `false`, which indicates that the element should not be checked for spelling errors.

[`style`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style)

Contains [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 styling declarations to be applied to the element. Note that it is recommended for styles to be defined in a separate file or files. This attribute and the [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 element have mainly the purpose of allowing for quick styling, for example for testing purposes.

[`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)

An integer attribute indicating if the element can take input focus (is _focusable_), if it should participate to sequential keyboard navigation, and if so, at what position. It can take several values:

*   a _negative value_ means that the element should be focusable, but should not be reachable via sequential keyboard navigation;
*   `0` means that the element should be focusable and reachable via sequential keyboard navigation, but its relative order is defined by the platform convention;
*   a _positive value_ means that the element should be focusable and reachable via sequential keyboard navigation; the order in which the elements are focused is the increasing value of the [`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/tabindex)
    . If several elements share the same tabindex, their relative order follows their relative positions in the document.

[`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)

Contains a text representing advisory information related to the element it belongs to. Such information can typically, but not necessarily, be presented to the user as a tooltip.

[`translate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/translate)

An enumerated attribute that is used to specify whether an element's attribute values and the values of its [`Text`](https://developer.mozilla.org/en-US/docs/Web/API/Text)
 node children are to be translated when the page is localized, or whether to leave them unchanged. It can have the following values:

*   empty string or `yes`, which indicates that the element will be translated.
*   `no`, which indicates that the element will not be translated.

[`virtualkeyboardpolicy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/virtualkeyboardpolicy)

An [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute used to control the on-screen virtual keyboard behavior on devices such as tablets, mobile phones, or other devices where a hardware keyboard may not be available for elements that its content is editable (for example, it is an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element, or an element with the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 attribute set).

*   `auto` or an _empty string_, which automatically shows the virtual keyboard when the element is focused or tapped.
*   `manual`, which decouples focus and tap on the element from the virtual keyboard's state.

[`writingsuggestions`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions)

An [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicating if browser-provided writing suggestions should be enabled under the scope of the element or not.

*   `false`, which disables the browser's writing suggestions.
*   `true` or an _empty string_, which enables writing suggestions.

[List of global event handler attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#list_of_global_event_handler_attributes)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

HTML event handler attributes are discouraged; see [HTML attribute reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes#event_handler_attributes)
 for how they work.

While the attributes listed below apply to all elements, they are not useful on all elements. For example, `onvolumechange` HTML attribute is accepted by all elements and attaches an event listener for `volumechange`, but only media elements will ever receive a `volumechange` event fired by the browser. For other elements, you can only use [`EventTarget.dispatchEvent()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/dispatchEvent)
 to manually dispatch one. [Some attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#event_attributes)
 can be specified on [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
, but they would instead listen to events on `window`.

*   [`onabort`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/abort_event)
    
*   [`onanimationcancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationcancel_event)
    
*   [`onanimationend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event)
    
*   [`onanimationiteration`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationiteration_event)
    
*   [`onanimationstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event)
    
*   [`onauxclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/auxclick_event)
    
*   [`onbeforeinput`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforeinput_event)
    
*   [`onbeforematch`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforematch_event)
    
*   [`onbeforetoggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/beforetoggle_event)
    
*   [`onblur`](https://developer.mozilla.org/en-US/docs/Web/API/Element/blur_event)
    
*   [`oncancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/cancel_event)
    
*   [`oncanplay`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplay_event)
    
*   [`oncanplaythrough`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/canplaythrough_event)
    
*   [`onchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
    
*   [`onclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event)
    
*   [`onclose`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event)
    
*   [`oncommand`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/command_event)
    
*   [`oncontentvisibilityautostatechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contentvisibilityautostatechange_event)
    
*   [`oncontextlost`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/contextlost_event)
    
*   [`oncontextmenu`](https://developer.mozilla.org/en-US/docs/Web/API/Element/contextmenu_event)
    
*   [`oncontextrestored`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/contextrestored_event)
    
*   [`oncopy`](https://developer.mozilla.org/en-US/docs/Web/API/Element/copy_event)
    
*   [`oncuechange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTrackElement/cuechange_event)
    
*   [`oncut`](https://developer.mozilla.org/en-US/docs/Web/API/Element/cut_event)
    
*   [`ondblclick`](https://developer.mozilla.org/en-US/docs/Web/API/Element/dblclick_event)
    
*   [`ondrag`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drag_event)
    
*   [`ondragend`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragend_event)
    
*   [`ondragenter`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragenter_event)
    
*   [`ondragleave`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragleave_event)
    
*   [`ondragover`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragover_event)
    
*   [`ondragstart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/dragstart_event)
    
*   [`ondrop`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/drop_event)
    
*   [`ondurationchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/durationchange_event)
    
*   [`onemptied`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/emptied_event)
    
*   [`onended`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ended_event)
    
*   [`onerror`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/error_event)
    
*   [`onfocus`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focus_event)
    
*   [`onfocusin`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusin_event)
    
*   [`onfocusout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/focusout_event)
    
*   [`onformdata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/formdata_event)
    
*   [`onfullscreenchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/fullscreenchange_event)
    
*   [`onfullscreenerror`](https://developer.mozilla.org/en-US/docs/Web/API/Element/fullscreenerror_event)
    
*   [`ongesturechange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gesturechange_event)
    
*   [`ongestureend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gestureend_event)
    
*   [`ongesturestart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gesturestart_event)
    
*   [`ongotpointercapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/gotpointercapture_event)
    
*   [`oninput`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event)
    
*   [`oninvalid`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event)
    
*   [`onkeydown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event)
    
*   [`onkeypress`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keypress_event)
    
*   [`onkeyup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/keyup_event)
    
*   [`onload`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/load_event)
    
*   [`onloadeddata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadeddata_event)
    
*   [`onloadedmetadata`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadedmetadata_event)
    
*   [`onloadstart`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/loadstart_event)
    
*   [`onlostpointercapture`](https://developer.mozilla.org/en-US/docs/Web/API/Element/lostpointercapture_event)
    
*   [`onmousedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event)
    
*   [`onmouseenter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseenter_event)
    
*   [`onmouseleave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseleave_event)
    
*   [`onmousemove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousemove_event)
    
*   [`onmouseout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseout_event)
    
*   [`onmouseover`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event)
    
*   [`onmouseup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event)
    
*   [`onmousewheel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousewheel_event)
    
*   [`onpaste`](https://developer.mozilla.org/en-US/docs/Web/API/Element/paste_event)
    
*   [`onpause`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/pause_event)
    
*   [`onplay`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/play_event)
    
*   [`onplaying`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/playing_event)
    
*   [`onpointercancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointercancel_event)
    
*   [`onpointerdown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerdown_event)
    
*   [`onpointerenter`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerenter_event)
    
*   [`onpointerleave`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerleave_event)
    
*   [`onpointermove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointermove_event)
    
*   [`onpointerout`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerout_event)
    
*   [`onpointerover`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerover_event)
    
*   [`onpointerrawupdate`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerrawupdate_event)
    
*   [`onpointerup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/pointerup_event)
    
*   [`onprogress`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/progress_event)
    
*   [`onratechange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/ratechange_event)
    
*   [`onreset`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/reset_event)
    
*   [`onresize`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLVideoElement/resize_event)
    
*   [`onscroll`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scroll_event)
    
*   [`onscrollend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollend_event)
    
*   [`onscrollsnapchange`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchange_event)
    
*   [`onscrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event)
    
*   [`onsecuritypolicyviolation`](https://developer.mozilla.org/en-US/docs/Web/API/Element/securitypolicyviolation_event)
    
*   [`onseeked`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeked_event)
    
*   [`onseeking`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/seeking_event)
    
*   [`onselect`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select_event)
    
*   [`onselectionchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/selectionchange_event)
    
*   [`onselectstart`](https://developer.mozilla.org/en-US/docs/Web/API/Node/selectstart_event)
    
*   [`onslotchange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement/slotchange_event)
    
*   [`onstalled`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/stalled_event)
    
*   [`onsubmit`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/submit_event)
    
*   [`onsuspend`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/suspend_event)
    
*   [`ontimeupdate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/timeupdate_event)
    
*   [`ontoggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/toggle_event)
    
*   [`ontouchcancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchcancel_event)
    
*   [`ontouchend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchend_event)
    
*   [`ontouchmove`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchmove_event)
    
*   [`ontouchstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/touchstart_event)
    
*   [`ontransitioncancel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitioncancel_event)
    
*   [`ontransitionend`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionend_event)
    
*   [`ontransitionrun`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionrun_event)
    
*   [`ontransitionstart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/transitionstart_event)
    
*   [`onvolumechange`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/volumechange_event)
    
*   [`onwaiting`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/waiting_event)
    
*   [`onwebkitmouseforcechanged`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcechanged_event)
    
*   [`onwebkitmouseforcedown`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcedown_event)
    
*   [`onwebkitmouseforceup`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforceup_event)
    
*   [`onwebkitmouseforcewillbegin`](https://developer.mozilla.org/en-US/docs/Web/API/Element/webkitmouseforcewillbegin_event)
    
*   [`onwheel`](https://developer.mozilla.org/en-US/docs/Web/API/Element/wheel_event)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-title-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-title-attribute) |
| [HTML  <br>\# the-draggable-attribute](https://html.spec.whatwg.org/multipage/dnd.html#the-draggable-attribute) |
| [HTML  <br>\# the-hidden-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute) |
| [HTML  <br>\# classes](https://html.spec.whatwg.org/multipage/dom.html#classes) |
| [HTML  <br>\# the-id-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-id-attribute) |
| [HTML  <br>\# the-dir-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-dir-attribute) |
| [HTML  <br>\# attr-autocapitalize](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocapitalize) |
| [HTML  <br>\# inert-subtrees](https://html.spec.whatwg.org/multipage/interaction.html#inert-subtrees) |
| [HTML  <br>\# attr-slot](https://html.spec.whatwg.org/multipage/dom.html#attr-slot) |
| [HTML  <br>\# the-accesskey-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-accesskey-attribute) |
| [HTML  <br>\# attr-tabindex](https://html.spec.whatwg.org/multipage/interaction.html#attr-tabindex) |
| [HTML  <br>\# heading-levels-&-offsets](https://html.spec.whatwg.org/multipage/sections.html#heading-levels-&-offsets) |
| [HTML  <br>\# attr-spellcheck](https://html.spec.whatwg.org/multipage/interaction.html#attr-spellcheck) |
| [HTML  <br>\# attr-is](https://html.spec.whatwg.org/multipage/custom-elements.html#attr-is) |
| [HTML  <br>\# attr-data-\*](https://html.spec.whatwg.org/multipage/dom.html#attr-data-*) |
| [HTML  <br>\# attr-contenteditable](https://html.spec.whatwg.org/multipage/interaction.html#attr-contenteditable) |
| [HTML  <br>\# the-autofocus-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-autofocus-attribute) |
| [HTML  <br>\# attr-enterkeyhint](https://html.spec.whatwg.org/multipage/interaction.html#attr-enterkeyhint) |
| [HTML  <br>\# the-style-attribute](https://html.spec.whatwg.org/multipage/dom.html#the-style-attribute) |
| [HTML  <br>\# attr-inputmode](https://html.spec.whatwg.org/multipage/interaction.html#attr-inputmode) |
| [HTML  <br>\# the-inert-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-inert-attribute) |
| [HTML  <br>\# attr-translate](https://html.spec.whatwg.org/multipage/dom.html#attr-translate) |
| [HTML  <br>\# attr-autocorrect](https://html.spec.whatwg.org/multipage/interaction.html#attr-autocorrect) |
| [HTML  <br>\# attr-popover-hint](https://html.spec.whatwg.org/multipage/popover.html#attr-popover-hint) |
| [HTML  <br>\# attr-nonce](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-nonce) |
| [HTML  <br>\# attr-lang](https://html.spec.whatwg.org/multipage/dom.html#attr-lang) |
| [HTML  <br>\# writing-suggestions](https://html.spec.whatwg.org/multipage/interaction.html#writing-suggestions) |
| [HTML  <br>\# the-popover-attribute](https://html.spec.whatwg.org/multipage/popover.html#the-popover-attribute) |
| [HTML  <br>\# attr-contenteditable-plaintextonly](https://html.spec.whatwg.org/multipage/interaction.html#attr-contenteditable-plaintextonly) |
| [Container Timing API  <br>\# dom-htmlelement-containertiming](https://w3c.github.io/container-timing/#dom-htmlelement-containertiming) |
| [Container Timing API  <br>\# dom-htmlelement-containertimingignore](https://w3c.github.io/container-timing/#dom-htmlelement-containertimingignore) |
| [Element Timing API  <br>\# dom-element-elementtiming](https://w3c.github.io/element-timing/#dom-element-elementtiming) |
| [DOM  <br>\# ref-for-dom-element-slot①](https://dom.spec.whatwg.org/#ref-for-dom-element-slot%E2%91%A0) |
| [CSS Shadow Module Level 1  <br>\# element-attrdef-html-global-exportparts](https://drafts.csswg.org/css-shadow/#element-attrdef-html-global-exportparts) |
| [CSS Shadow Module Level 1  <br>\# part-attr](https://drafts.csswg.org/css-shadow/#part-attr) |
| [VirtualKeyboard API  <br>\# dom-elementcontenteditable-virtualkeyboardpolicy](https://w3c.github.io/virtual-keyboard/#dom-elementcontenteditable-virtualkeyboardpolicy) |
| [CSS Style Attributes  <br>\# style-attribute](https://drafts.csswg.org/css-style-attr/#style-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes#see_also)

---------------------------------------------------------------------------------------------------

*   [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
     interface that allows querying most global attributes.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4d218f9fdff30e8e01a26402b9f9615c9527ccf6%0A*+Document+last+modified%3A+2026-10-26T03%3A15%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")