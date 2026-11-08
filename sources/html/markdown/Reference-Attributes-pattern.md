*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#mdn-search)
    

`pattern` HTML attribute
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`pattern`** attribute specifies a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
 the form control's value should match. If a non-`null` value doesn't conform to the constraints set by the `pattern` value, the [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
 object's read-only [`patternMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch "patternMismatch")
 property will be true.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#try_it)

------------------------------------------------------------------------------------------------

    <label for="username">Username: (3-16 characters)</label>
    <input
      id="username"
      name="username"
      type="text"
      value="Sasha"
      pattern="\w{3,16}"
      required />
    
    <label for="pin">PIN: (4 digits)</label>
    <input id="pin" name="pin" type="password" pattern="\d{4,4}" required />
    

    label {
      display: block;
      margin-top: 1em;
    }
    
    input:valid {
      background-color: palegreen;
    }
    
    input:invalid {
      background-color: lightpink;
    }
    

[Overview](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#overview)

----------------------------------------------------------------------------------------------------

The `pattern` attribute is an attribute of the [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, [tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel)
, [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
, [url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
, [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password)
, and [search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search)
 input types.

The `pattern` attribute, when specified, is a regular expression which the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
.

The pattern's regular expression is compiled with the [`'v'` flag](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions/Character_class#v-mode_character_class)
. This makes the regular expression [unicode-aware](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicode#unicode-aware_mode)
, and also changes how character classes are interpreted. This allows character class set intersection and subtraction operations, and in addition to `]` and `\`, the following characters must be escaped using a `\` backslash if they represent literal characters: `(`, `)`, `[`, `{`, `}`, `/`, `-`, `|`. Before mid-2023, the `'u'` flag was specified instead; if you're updating older code, read the [`unicodeSets`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/unicodeSets)\
 reference.\
\
The pattern's regular expression must match the entire input's `value`, rather than matching a substring - as if a `^(?:` were implied at the start of the pattern and `)$` at the end.\
\
No forward slashes should be specified around the pattern text. No regular expression is applied if the attribute value is absent, an empty string, or invalid.\
\
Some of the input types supporting the pattern attribute, notably the [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)\
 and [url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)\
 input types, have expected value syntaxes that must be matched. If the pattern attribute isn't present, and the value doesn't match the expected syntax for that value type, the [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)\
 object's read-only [`typeMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/typeMismatch "typeMismatch")\
 property will be true.\
\
### [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#constraint_validation)\
\
If the input's value is not the empty string and the value does not match the entire regular expression, there is a constraint violation reported by the [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)\
 object's [`patternMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch "patternMismatch")\
 property being `true`.\
\
**Note:** If the `pattern` attribute is specified with no value, its value is implicitly the empty string. Thus, **any non-empty** input `value` will result in constraint violation.\
\
### [Usability and accessibility considerations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#usability_and_accessibility_considerations)\
\
When including a `pattern`, provide a description of the pattern in visible text near the control. Additionally, include a [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)\
 attribute which gives a description of the pattern. User agents may use the title contents during constraint validation to tell the user that the pattern is not matched. Some browsers show a tooltip with title contents, improving usability for sighted users. Additionally, assistive technology may read the title aloud when the control gains focus, but this should not be relied upon for accessibility.\
\
Only relying on the `title` attribute for the visual display of text content is discouraged, as many user agents do not expose the attribute in an accessible manner. Although some browsers show a tooltip when an element with a title is hovered, that leaves out keyboard-only and touch-only users. This is one of the several reasons you must include information informing users how to fill out the control to match the requirements.\
\
While `title`s are used by some browsers to populate error messaging, because browsers sometimes also show the title as text on hover, it therefore shows in non-error situations, so be careful not to word titles as if an error has occurred.\
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#examples)\
\
----------------------------------------------------------------------------------------------------\
\
### [Matching a phone number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#matching_a_phone_number)\
\
Given the following:\
\
html\
\
    <p>\
      <label>\
        Enter your phone number in the format (123) - 456 - 7890 (<input\
          name="tel1"\
          type="tel"\
          pattern="[0-9]{3}"\
          placeholder="###"\
          aria-label="3-digit area code"\
          size="2" />) -\
        <input\
          name="tel2"\
          type="tel"\
          pattern="[0-9]{3}"\
          placeholder="###"\
          aria-label="3-digit prefix"\
          size="2" />\
        -\
        <input\
          name="tel3"\
          type="tel"\
          pattern="[0-9]{4}"\
          placeholder="####"\
          aria-label="4-digit number"\
          size="3" />\
      </label>\
    </p>\
    \
\
Here we have 3 sections for a north American phone number with an implicit label encompassing all three components of the phone number, expecting 3-digits, 3-digits and 4-digits respectively, as defined by the `pattern` attribute set on each.\
\
If the values are too long or too short, or contain characters that aren't digits, the `patternMismatch` will be true. When `true`, the element matches the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)\
 CSS pseudo-classes.\
\
css\
\
    input:invalid {\
      border: red solid 3px;\
    }\
    \
\
If we had used [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)\
 and [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)\
 attributes instead, we may have seen [`validityState.tooLong`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooLong)\
 or [`validityState.tooShort`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooShort)\
 being true.\
\
### [Specifying a pattern](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#specifying_a_pattern)\
\
You can use the [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)\
 attribute to specify a regular expression that the inputted value must match in order to be considered valid (see [Validating against a regular expression](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#validating_against_a_regular_expression)\
 for a crash course on using regular expressions to validate inputs).\
\
The example below restricts the value to 4-8 characters and requires that it contain only lower-case letters.\
\
html\
\
    <form>\
      <div>\
        <label for="uname">Choose a username: </label>\
        <input\
          type="text"\
          id="uname"\
          name="name"\
          required\
          size="45"\
          pattern="[a-z]{4,8}"\
          title="4 to 8 lowercase letters" />\
        <span class="validity"></span>\
        <p>Usernames must be lowercase and 4-8 characters in length.</p>\
      </div>\
      <div>\
        <button>Submit</button>\
      </div>\
    </form>\
    \
\
    document.querySelector("form").addEventListener("submit", (event) => {\
      event.preventDefault();\
    });\
    \
\
    div {\
      margin-bottom: 10px;\
      position: relative;\
    }\
    \
    p {\
      font-size: 80%;\
      color: #999999;\
    }\
    \
    input + span {\
      padding-right: 30px;\
    }\
    \
    input:invalid + span::after {\
      position: absolute;\
      content: "✖";\
      padding-left: 5px;\
    }\
    \
    input:valid + span::after {\
      position: absolute;\
      content: "✓";\
      padding-left: 5px;\
    }\
    \
\
This renders like so:\
\
[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#specifications)\
\
----------------------------------------------------------------------------------------------------------------\
\
| Specification |\
| --- |\
| [HTML  <br>\# attr-input-pattern](https://html.spec.whatwg.org/multipage/input.html#attr-input-pattern) |\
\
[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#browser_compatibility)\
\
------------------------------------------------------------------------------------------------------------------------------\
\
[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern#see_also)\
\
----------------------------------------------------------------------------------------------------\
\
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)\
    \
*   [Forms: Data form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)\
    \
*   [Regular Expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)\
    \
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/pattern/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/pattern (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fpattern&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fpattern%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fpattern%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fpattern%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")