*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#mdn-search)
    

`<fieldset>` HTML field set element
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<fieldset>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to group several controls as well as labels ([`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
) within a web form.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#try_it)

-----------------------------------------------------------------------------------------------

    <form>
      <fieldset>
        <legend>Choose your favorite monster</legend>
    
        <input type="radio" id="kraken" name="monster" value="K" />
        <label for="kraken">Kraken</label><br />
    
        <input type="radio" id="sasquatch" name="monster" value="S" />
        <label for="sasquatch">Sasquatch</label><br />
    
        <input type="radio" id="mothman" name="monster" value="M" />
        <label for="mothman">Mothman</label>
      </fieldset>
    </form>
    

    legend {
      background-color: black;
      color: white;
      padding: 3px 6px;
    }
    
    input {
      margin: 0.4rem;
    }
    

As the example above shows, the `<fieldset>` element provides a grouping for a part of an HTML form, with a nested [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 element providing a caption for the `<fieldset>`. It takes few attributes, the most notable of which are `form`, which can contain the `id` of a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 on the same page, allowing you to make the `<fieldset>` part of that `<form>` even if it is not nested inside it, and `disabled`, which allows you to disable the `<fieldset>` and all its contents in one go.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

If this Boolean attribute is set, all form controls that are descendants of the `<fieldset>`, are disabled, meaning they are not editable and won't be submitted along with the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
. They won't receive any browsing events, like mouse clicks or focus-related events. By default browsers display such controls grayed out. Note that form elements inside the [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 element won't be disabled.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

This attribute takes the value of the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute of a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element you want the `<fieldset>` to be part of, even if it is not inside the form. Please note that usage of this is confusing — if you want the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements inside the `<fieldset>` to be associated with the form, you need to use the `form` attribute directly on those elements. You can check which elements are associated with a form via JavaScript, using [`HTMLFormElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#name)

The name associated with the group.

**Note:** The caption for the fieldset is given by the first [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 element nested inside it.

[Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#styling_with_css)

-------------------------------------------------------------------------------------------------------------------

There are several special styling considerations for `<fieldset>`.

Its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value is `block` by default, and it establishes a [block formatting context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Block_formatting_context)
. If the `<fieldset>` is styled with an inline-level `display` value, it will behave as `inline-block`, otherwise it will behave as `block`. By default there is a `2px` `groove` border surrounding the contents, and a small amount of default padding. The element has [`min-inline-size: min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-inline-size)
 by default.

If a [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
 is present, it is placed over the `block-start` border. The `<legend>` shrink-wraps, and also establishes a formatting context. The `display` value is blockified. (For example, `display: inline` behaves as `block`.)

There will be an anonymous box holding the contents of the `<fieldset>`, which inherits certain properties from the `<fieldset>`. If the `<fieldset>` is styled with `display: grid` or `display: inline-grid`, then the anonymous box will be a grid formatting context. If the `<fieldset>` is styled with `display: flex` or `display: inline-flex`, then the anonymous box will be a flex formatting context. Otherwise, it establishes a block formatting context.

You can feel free to style the `<fieldset>` and `<legend>` in any way you want to suit your page design.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#examples)

---------------------------------------------------------------------------------------------------

### [Basic fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#basic_fieldset)

This example includes a `<fieldset>` with a `<legend>`, with a single control inside it.

html

    <form action="#">
      <fieldset>
        <legend>Do you agree?</legend>
        <input type="checkbox" id="chbx" name="agree" value="Yes!" />
        <label for="chbx">I agree</label>
      </fieldset>
    </form>
    

#### Result

### [Disabled fieldset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#disabled_fieldset)

This example shows a disabled `<fieldset>` with two controls inside it. Note how both the controls are disabled due to being inside a disabled `<fieldset>`.

html

    <form action="#">
      <fieldset disabled>
        <legend>Disabled login fieldset</legend>
        <div>
          <label for="name">Name: </label>
          <input type="text" id="name" value="Chris" />
        </div>
        <div>
          <label for="pwd">Archetype: </label>
          <input type="password" id="pwd" value="Wookie" />
        </div>
      </fieldset>
    </form>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, sectioning root, [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [form-associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br> element, palpable content. |
| Permitted content | An optional [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)<br> element, followed by flow content. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role) |
| Permitted ARIA roles | [`radiogroup`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radiogroup_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br>, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role) |
| DOM interface | [`HTMLFieldSetElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFieldSetElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-fieldset-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-fieldset-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset#see_also)

---------------------------------------------------------------------------------------------------

*   The [`<legend>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/legend)
     element
*   The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element
*   The [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
     element
*   The [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
     element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/fieldset/index.md?plain=1 "Folder: en-us/web/html/reference/elements/fieldset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffieldset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffieldset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffieldset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffieldset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")