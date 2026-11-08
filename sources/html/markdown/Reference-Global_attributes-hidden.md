*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#mdn-search)
    

`hidden` HTML global attribute
==============================

The **`hidden`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicating that the browser should not render the contents of the element. For example, it can be used to hide elements of the page that can't be used until the login process has been completed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#try_it)

------------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#description)

----------------------------------------------------------------------------------------------------------------

The `hidden` attribute indicates that the content of an element should not be presented to the user. The attribute takes any one of the following values:

*   the keyword `hidden`
*   the keyword `until-found`
*   an empty string or no value

Invalid `hidden` attribute values also place the element in the _hidden_ state. Therefore, all the following elements are in the [_hidden_](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#the_hidden_state)
 state:

The keyword `until-found` sets the element to the [_hidden until found_](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#the_hidden_until_found_state)
 state:

### [The hidden state](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#the_hidden_state)

The _hidden_ state indicates that the element is not currently relevant to the page, or that it is being used to declare content for reuse by other parts of the page and should not be directly presented to the user. The browser will not render elements that are in the _hidden_ state.

Web browsers may implement the _hidden_ state using `display: none`, in which case the element will not participate in page layout. Additionally, changing the value of the CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property on a hidden element will override the _hidden_ state. For instance, elements styled `display: block` will be displayed despite the `hidden` attribute's presence.

### [The hidden until found state](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#the_hidden_until_found_state)

In the _hidden until found_ state, the element is hidden but its content will be accessible to the browser's "Find in page" feature or to fragment navigation. When these features cause a scroll to an element in a _hidden until found_ subtree, the browser will:

1.  Fire a [`beforematch`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforematch_event)
     event on the hidden element
2.  Remove the `hidden` attribute from the element
3.  Scroll to the element

This lets you collapse a section of content while still allowing users to find it through search or navigation.

Browsers typically implement _hidden until found_ using [`content-visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
. This means that, unlike elements in the _hidden_ state, elements in the _hidden until-found_ state generate boxes, and:

*   they participate in page layout
*   their margin, borders, padding, and background are rendered

Also, the element needs to be affected by [layout containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
 in order to be revealed. If the element in the _hidden until found_ state has a `display` value of `none`, `contents`, or `inline`, then the element will not be revealed by "Find in page" or fragment navigation.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#usage_notes)

----------------------------------------------------------------------------------------------------------------

The `hidden` attribute must not be used to hide content just from one presentation. If something is marked hidden, it is hidden from all presentations, including, for instance, screen readers.

Hidden elements shouldn't be linked from visible elements unless using `hidden="until-found"`. For example, it would be incorrect to use the `href` attribute to link to a section with the `hidden` attribute. If the content is not applicable or relevant, it shouldn't be linked.

It is fine, however, to use the ARIA [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
 attribute to refer to hidden descriptions. While hiding the descriptions implies that they're not useful on their own, they can provide helpful context when referenced in this way.

Similarly, a canvas element with the `hidden` attribute could be used by a scripted graphics engine as an off-screen buffer, and a form control could refer to a hidden form element using its form attribute.

Finally, note that elements that are descendants of a hidden element are still active, which means that script elements can still execute, and form elements can still submit:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#examples)

----------------------------------------------------------------------------------------------------------

### [Using the hidden attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#using_the_hidden_attribute)

In this example, we have three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements. The first and the third are not hidden, while the second has a `hidden` attribute. Note that the hidden element has no generated box.

### [Using the until-found value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#using_the_until-found_value)

In this example, we have three [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements. The first and the third are visible, while the second has the `hidden="until-found"` and `id="until-found-box"` attributes. The element with a `until-found-box` id has a dotted red border and a gray background.

We also have a link that targets the `"until-found-box"` fragment and JavaScript that listens for the `beforematch` event firing on that hidden element. The event handler changes the text content of the box to illustrate an action that can occur when the _hidden until found_ state is about to be removed.

#### HTML

#### CSS

#### JavaScript

#### Result

Clicking the "Go to hidden content" link navigates to the _hidden until found_ element. The `beforematch` event fires, the text content is updated, and the element becomes visible. Note that although the content of the element is hidden, the element still has a generated box, occupying space in the layout and with background and borders rendered.

To run the example again, click "Reset".

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-hidden-attribute](https://html.spec.whatwg.org/multipage/interaction.html#the-hidden-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden#see_also)

----------------------------------------------------------------------------------------------------------

*   [`HTMLElement.hidden`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/hidden)
    
*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    
*   The [`aria-hidden`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden)
     attribute
*   The [`beforematch`](https://developer.mozilla.org/en-US/docs/Web/API/Element/beforematch_event)
     event

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/hidden/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/hidden/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/hidden (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fhidden&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fhidden%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fhidden%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fhidden%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")