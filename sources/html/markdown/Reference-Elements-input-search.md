*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#mdn-search)
    

`<input type="search">` HTML attribute value
============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`search`** are text fields designed for the user to enter search queries into. These are functionally identical to [`text`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
 inputs, but may be styled differently by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#try_it)

---------------------------------------------------------------------------------------------------

    <label for="site-search">Search the site:</label>
    <input type="search" id="site-search" name="q" />
    
    <button>Search</button>
    

    label {
      display: block;
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    input,
    label {
      margin: 0.4rem 0;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#value)

-------------------------------------------------------------------------------------------------

The [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string representing the value contained in the search field. You can retrieve this using the [`HTMLInputElement.value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value)
 property in JavaScript.

js

    searchTerms = mySearch.value;
    

If no validation constraints are in place for the input (see [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#validation)
 for more details), the value can be any text string or an empty string (`""`).

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#additional_attributes)

---------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and the attributes that operate on all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements regardless of their type, search field inputs support the following attributes.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [maxlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#maxlength)

The maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the search field. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the search field has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [minlength](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#minlength)

The minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the search field. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the search input has no minimum length.

The search field will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. Constraint validation is only applied when the value is changed by the user.

### [pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#pattern)

The `pattern` attribute, when specified, is a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
; the `'u'` flag is specified when compiling the regular expression so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
. No forward slashes should be specified around the pattern text.

If the specified pattern is not specified or is invalid, no regular expression is applied and this attribute is ignored completely.

**Note:** Use the [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to specify text that most browsers will display as a tooltip to explain what the requirements are to match the pattern. You should also include other explanatory text nearby.

See the section [Specifying a pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#specifying_a_pattern)
 for details and an example.

### [placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#placeholder)

The `placeholder` attribute is a string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message. The text _must not_ include carriage returns or line feeds.

If the control's content has one directionality ([LTR](https://developer.mozilla.org/en-US/docs/Glossary/LTR)
 or [RTL](https://developer.mozilla.org/en-US/docs/Glossary/RTL)
) but needs to present the placeholder in the opposite directionality, you can use Unicode bidirectional algorithm formatting characters to override directionality within the placeholder; see [How to use Unicode controls for bidi text](https://www.w3.org/International/questions/qa-bidi-unicode-controls "External link (opens in new tab)")
 for more information.

**Note:** Avoid using the `placeholder` attribute if you can. It is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [`<input>` labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#size)

The `size` attribute is a numeric value indicating how many characters wide the input field should be. The value must be a number greater than zero, and the default value is 20. Since character widths vary, this may or may not be exact and should not be relied upon to be so; the resulting input may be narrower or wider than the specified number of characters, depending on the characters and the font ([`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 settings in use).

This does _not_ set a limit on how many characters the user can enter into the field. It only specifies approximately how many can be seen at a time. To set an upper limit on the length of the input data, use the [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#maxlength)
 attribute.

### [spellcheck](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#spellcheck)

[`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)
 is a global attribute that is used to indicate whether to enable spell-checking for an element. It can be used on any editable content, but here we consider specifics related to the use of `spellcheck` on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements. The permitted values for `spellcheck` are:

[`false`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#false)

Disable spell-checking for this element.

[`true`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#true)

Enable spell-checking for this element.

["" (empty string) or no value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#empty_string_or_no_value)

Follow the element's default behavior for spell-checking. This may be based upon a parent's `spellcheck` setting or other factors.

An input field can have spell-checking enabled if it doesn't have the [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#readonly)
 attribute set and is not disabled.

The value returned by reading `spellcheck` may not reflect the actual state of spell-checking within a control, if the [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 preferences override the setting.

[Non-standard attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#non-standard_attributes)

-------------------------------------------------------------------------------------------------------------------------------------

The following non-standard attributes are available to search input fields. Avoid using them where possible.

### [incremental](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#incremental)

The Boolean attribute `incremental` is a WebKit and Blink extension (so supported by Safari, Opera, Chrome, etc.) which, if present, tells the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 to process the input as a live search. As the user edits the value of the field, the user agent sends [`search`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/search_event "search")
 events to the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 object representing the search box. This allows your code to update the search results in real time as the user edits the search.

If `incremental` is not specified, the [`search`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/search_event "search")
 event is only sent when the user explicitly initiates a search (such as by pressing the Enter or Return key while editing the field).

The `search` event is rate-limited so that it is not sent more frequently than an implementation-defined interval.

### [results](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#results)

The `results` attribute—supported only by Safari—is a numeric value that lets you override the maximum number of entries to be displayed in the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element's natively-provided drop-down menu of previous search queries.

The value must be a non-negative decimal number. If not provided, or an invalid value is given, the browser's default maximum number of entries is used.

[Using search inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#using_search_inputs)

-----------------------------------------------------------------------------------------------------------------------------

`<input>` elements of type `search` are very similar to those of type `text`, except that they are specifically intended for handling search terms. They are basically equivalent in behavior, but user agents may choose to style them differently by default (and, of course, sites may use stylesheets to apply custom styles to them).

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#basic_example)

html

    <input type="search" id="mySearch" name="q" />
    

This renders like so:

`q` is the most common `name` given to search inputs, although it's not mandatory. If this input is included in a form and submitted, the data name/value pair sent to the server will be `q=searchTerm`.

**Note:** You must remember to set a [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
 for your input, otherwise nothing will be submitted.

### [Differences between search and text types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#differences_between_search_and_text_types)

The main basic differences come in the way browsers handle them. The first thing to note is that some browsers show a cross icon that can be clicked on to remove the search term instantly if desired, in Chrome this action is also triggered when pressing escape. The following screenshot comes from Chrome:

![Focused search input, with focus ring, with the text 'cats'. There is an x icon in the input abutting the right side.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search/chrome-cross-icon.png)

In addition, modern browsers also tend to automatically store search terms previously entered across domains, which then come up as autocomplete options when subsequent searches are performed in search inputs on that domain. This helps users who tend to do searches on the same or similar search queries over time. This screenshot is from Firefox:

![An input in error state with a red focus ring. The user has entered the letter 'h'. A pop-up selection list is open directly under the input box with two options: hello and hermansje.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search/firefox-auto-complete.png)

At this point, let's look at some useful techniques you can apply to your search forms.

### [Setting placeholders](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#setting_placeholders)

You can provide a useful placeholder inside your search input that could give a hint on what to do using the [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 attribute. Look at the following example:

html

    <input type="search" id="mySearch" name="q" placeholder="Search the site…" />
    

You can see how the placeholder is rendered below:

### [Search form labels and accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#search_form_labels_and_accessibility)

One problem with search forms is their accessibility; a common design practice is not to provide a label for the search field (although there might be a magnifying glass icon or similar), as the purpose of a search form is normally fairly obvious for sighted users due to placement ([this example shows a typical visual pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#accessible_search_form)
).

This could, however, cause confusion for screen reader users, as they will not receive any verbal indication of what the search input is. One way around this that won't impact your visual design is to use [landmark elements](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/landmark_role)
.

*   Wrap the whole search functionality in a [`<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search)
     element, which creates a landmark region that assistive technologies can announce and quickly navigate to. If your `<input>` is already in a `<form>`, you can alternatively add [`role="search"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role)
     to the `<form>` element, which also makes the `<form>` a search landmark. The `<search>` element uses native HTML semantics, while `role="search"` has more support and may be terser to type if you already have a `<form>` wrapper.
*   If that isn't enough, you can use an [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
     attribute on the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     itself. This should be a descriptive text label that will be read out by the screen reader; it's used as a non-visual equivalent to `<label>`.

Let's have a look at a minimal example:

html

    <search>
      <input
        type="search"
        id="mySearch"
        name="q"
        placeholder="Search the site…"
        aria-label="Search through site content" />
    </search>
    

You can see how this is rendered below:

There is no visual difference from the previous example, but screen reader users have way more information available to them.

**Note:** See [Signposts/Landmarks](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics#signpostslandmarks)
 for more information about such accessibility features.

### [Physical input element size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#physical_input_element_size)

The physical size of the input box can be controlled using the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
 attribute. With it, you can specify the number of characters the input box can display at a time. In this example, for instance, the search box is 30 characters wide:

html

    <input
      type="search"
      id="mySearch"
      name="q"
      placeholder="Search the site…"
      size="30" />
    

The result is this wider input box:

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#validation)

-----------------------------------------------------------------------------------------------------------

`<input>` elements of type `search` have the same validation features available to them as regular `text` inputs. It is less likely that you'd want to use validation features in general for search boxes. In many cases, users should just be allowed to search for anything, but there are a few cases to consider, such as searches against data of a known format.

**Note:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data (or data which is too large, is of the wrong type, and so forth) is entered into your database.

### [A note on styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#a_note_on_styling)

There are useful pseudo-classes available for styling valid/invalid form elements: [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
. In this section, we'll use the following CSS, which will place a check (tick) next to inputs containing valid values, and a cross next to inputs containing invalid values.

css

    input:invalid ~ span::after {
      content: "✖";
      padding-left: 5px;
      position: absolute;
    }
    
    input:valid ~ span::after {
      content: "✓";
      padding-left: 5px;
      position: absolute;
    }
    

The technique also requires a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element to be placed after the form element, which acts as a holder for the icons. This was necessary because some input types on some browsers don't display icons placed directly after them very well.

### [Making input required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#making_input_required)

You can use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute as an easy way of making entering a value required before form submission is allowed:

html

    <form>
      <div>
        <input
          type="search"
          id="mySearch"
          name="q"
          placeholder="Search the site…"
          required />
        <button>Search</button>
        <span class="validity"></span>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    input {
      margin-right: 10px;
    }
    
    input:invalid ~ span::after {
      content: "✖";
      padding-left: 5px;
      position: absolute;
    }
    
    input:valid ~ span::after {
      content: "✓";
      padding-left: 5px;
      position: absolute;
    }
    

This renders like so:

In addition, if you try to submit the form with no search term entered into it, the browser will show a message. The following example is from Firefox:

![form field with attached message that says Please fill out this field](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search/firefox-required-message.png)

Different messages will be shown when you try to submit the form with different types of invalid data contained inside the inputs; see the below examples.

### [Input value length](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#input_value_length)

You can specify a minimum length, in characters, for the entered value using the [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)
 attribute; similarly, use [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)
 to set the maximum length of the entered value.

The example below requires that the entered value be 4–8 characters in length.

html

    <form>
      <div>
        <label for="mySearch">Search for user</label>
        <input
          type="search"
          id="mySearch"
          name="q"
          placeholder="User IDs are 4–8 characters in length"
          required
          size="30"
          minlength="4"
          maxlength="8" />
        <button>Search</button>
        <span class="validity"></span>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    input {
      margin-right: 10px;
    }
    
    input:invalid ~ span::after {
      content: "✖";
      padding-left: 5px;
      position: absolute;
    }
    
    input:valid ~ span::after {
      content: "✓";
      padding-left: 5px;
      position: absolute;
    }
    

This renders like so:

If you try to submit the form with less than 4 characters, you'll be given an appropriate error message (which differs between browsers). If you try to go beyond 8 characters in length, the browser won't let you.

### [Specifying a pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#specifying_a_pattern)

You can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute to specify a regular expression that the inputted value must follow to be considered valid (see [Validating against a regular expression](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#validating_against_a_regular_expression)
 for a crash course).

Let's look at an example. Say we wanted to provide a product ID search form, and the IDs were all codes of two letters followed by four numbers. The following example covers it:

html

    <form>
      <div>
        <label for="mySearch">Search for product by ID:</label>
        <input
          type="search"
          id="mySearch"
          name="q"
          placeholder="two letters followed by four numbers"
          required
          size="30"
          pattern="[A-z]{2}[0-9]{4}" />
        <button>Search</button>
        <span class="validity"></span>
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

    input {
      margin-right: 10px;
    }
    
    input:invalid ~ span::after {
      content: "✖";
      padding-left: 5px;
      position: absolute;
    }
    
    input:valid ~ span::after {
      content: "✓";
      padding-left: 5px;
      position: absolute;
    }
    

This renders like so:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#examples)

-------------------------------------------------------------------------------------------------------

### [Accessible search form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#accessible_search_form)

This example shows a typical [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
 menu that includes a search form. [WAI-ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)
 features are used to make the form more accessible to assistive technology (AT) users.

#### HTML

The main nav items are comprised of a list of links. The search [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 is given a [`role="search"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/search_role)
 attribute, which makes the `<form>` a search landmark, announcing it to AT. We also give the `<input type="search">` element an [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 to give it a clear label that is read out by screen readers.

html

    <nav>
      <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <form role="search">
        <input
          type="search"
          name="q"
          placeholder="Search query"
          aria-label="Search through site content" />
        <button>Search!</button>
      </form>
    </nav>
    

    html {
      font-family: sans-serif;
      font-size: 10px;
    }
    
    nav {
      display: flex;
      align-items: center;
      gap: 1em;
      padding: 10px;
    }
    
    nav ul {
      padding: 0;
      list-style-type: none;
      flex: 2;
      display: flex;
    }
    
    nav li {
      text-align: center;
      flex: 1;
    }
    
    nav a {
      font-size: 2rem;
      text-transform: uppercase;
      text-decoration: none;
      color: black;
      display: block;
      width: 100%;
      height: 100%;
      line-height: 1.2;
    }
    
    nav form {
      flex: 1;
      display: flex;
      align-items: center;
      height: 100%;
    }
    
    input {
      font-size: 1.6rem;
    }
    
    input[type="search"] {
      flex: 3;
      height: 30px;
    }
    
    button {
      flex: 1;
      height: 30px;
      padding: 0 1em;
      background: #333333;
      border: 0;
      color: white;
    }
    

We have hidden the example's CSS and JavaScript for brevity, as they are not relevant to understanding the HTML. You can check them out by pressing the "Play" button in the live example below.

    const form = document.querySelector("form");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
    });
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#technical_summary)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#value)<br>** | A string representing the value contained in the search field. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported Common Attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength)<br>, [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br>, [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)<br>. |
| **IDL attributes** | `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | with no `list` attribute: `[searchbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/searchbox_role) `  <br>with `list` attribute: `[combobox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# text-(type=text)-state-and-search-state-(type=search)](https://html.spec.whatwg.org/multipage/input.html#text-(type=text)-state-and-search-state-(type=search)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search#see_also)

-------------------------------------------------------------------------------------------------------

*   [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface it's based upon
*   [`<input type="text">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/search/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/search (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fsearch&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fsearch%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fsearch%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fsearch%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")