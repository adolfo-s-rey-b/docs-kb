*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#mdn-search)
    

`autocomplete` HTML attribute
=============================

The HTML `autocomplete` attribute lets web developers specify what if any permission the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 has to provide automated assistance in filling out form field values, as well as guidance to the browser as to the type of information expected in the field.

It is available on [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements that take a text or numeric value as input, [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements, and [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#try_it)

-----------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#description)

---------------------------------------------------------------------------------------------------------------

The `autocomplete` attribute provides a hint to the user agent specifying how to, or indeed whether to, prefill a form control. The attribute value is either the keyword `off` or `on`, or an ordered list of space-separated tokens.

If an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element has no `autocomplete` attribute, the browser will use the [`autocomplete` attribute of the element's **owning form**](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#autocomplete)
. The owning form is either the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 matching the `id` specified by the [`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)
 attribute of the element (if present) or, more commonly, the `<form>` the element is nested in.

**Note:** In order to provide autocompletion, user-agents might require `<input>`/`<select>`/`<textarea>` elements to:

1.  Have a `name` and/or `id` attribute
2.  Be descendants of a `<form>` element
3.  Be owned by a form with a [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
     button

If the same list of tokens is used in more than one form control, the user-agent will autocomplete all occurrences of the same `autocomplete` value with the same data value.

Some tokens may be used more than once with potentially different expected values, such as the `postal-code` token in a form that contains both shipping and billing addresses. Including multiple different tokens in a space-separated list causes the associated form controls to be given unique autocomplete values: in this case, `autocomplete="shipping postal-code"` and `autocomplete="billing postal-code"`.

Some autocomplete values may need to be re-used multiple times. For example, a form may contain multiple shipping addresses and therefore multiple occurrences of `"shipping postal-code"` while still expecting different values. To make the autocomplete value unique in these cases, the first token in the space-separated list of tokens can be a `section-*` token, where the token's first eight characters are always the string "section-", followed by an alphanumeric string. All form fields given the `section-*` token with the same alphanumeric string belong to the same **named group**.

If including the `autocomplete` attribute on [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
 input elements (`<input type="hidden">`), its value must be an ordered list of space-separated tokens; the `on` and `off` keywords are not allowed.

The source of the suggested values is generally up to the browser; typically values come from past values entered by the user, but they may also come from pre-configured values. For instance, a browser might let the user save their name, address, phone number, and email addresses for autocomplete purposes. The browser may also offer the ability to save encrypted credit card information, for autocompletion following an authentication procedure.

**Note:** The `autocomplete` attribute also controls whether Firefox will — unlike other browsers — [persist the dynamic disabled state and (if applicable) dynamic checkedness](https://stackoverflow.com/questions/5985839/bug-with-firefox-disabled-attribute-of-input-not-resetting-when-refreshing "External link (opens in new tab)")
 of an `<input>` element, `<textarea>` element, or entire `<form>` across page loads. The persistence feature is enabled by default. Setting the value of the `autocomplete` attribute to `off` disables this feature. This works even when the `autocomplete` attribute would normally not apply by virtue of its `type`. See [Firefox bug 654072](https://bugzil.la/654072 "External link (opens in new tab)")
.

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#value)

---------------------------------------------------------------------------------------------------

The attribute value is either the keyword `off` or `on`, or a space-separated `<token-list>` that describes the meaning of the autocompletion value.

[`off`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#off)

The browser is not permitted to automatically enter or select a value for this field. It is possible that the document or application provides its own autocomplete feature, or that security concerns require that the field's value not be automatically entered.

**Note:** In most modern browsers, setting `autocomplete` to `"off"` will not prevent a password manager from asking the user if they would like to save username and password information, or from automatically filling in those values in a site's login form. See [Managing autofill for login fields](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/Turning_off_form_autocompletion#managing_autofill_for_login_fields)
.

[`on`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#on)

The browser is allowed to automatically complete the input. No guidance is provided as to the type of data expected in the field, so the browser may use its own judgment.

[`<token-list>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#token-list)

An ordered set of [space-separated tokens](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#token_list_tokens)
 consisting of autofill detail tokens preceded by optional sectioning and either billing or shipping grouping tokens. Phone numbers, email addresses, and messaging protocol tokens are preceded by a token identifying the type of recipient.

See the [WHATWG Standard](https://html.spec.whatwg.org/multipage/forms.html#autofill "External link (opens in new tab)")
 for more detailed information.

### [Token list tokens](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#token_list_tokens)

The `<token-list>` options include, in order:

1.  [Group naming token](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#named_groups)
    
2.  [Grouping identifier](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#grouping_identifier)
    
3.  [Detail tokens](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#detail_tokens)
    
4.  [Web authorization](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#web_authorization_token)
    

#### Named groups

To create a named group of form fields, the optional `section-*` token can be used. If present, this token must be the first token in the space-separated list of tokens.

[`section-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#section-)

Defines the name for a group of form controls. A token whose first eight characters are the string "section-", case-insensitive, followed by additional characters. All form controls that start with the same token belong to the named group.

#### Grouping identifier

An optional `shipping` or `billing` grouping identifier

[`shipping`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#shipping)

The field identified by subsequent tokens is part of the shipping address or contact information

[`billing`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#billing)

The field identified by subsequent tokens is part of the billing address or contact information

#### Detail tokens

Each space-separated detail token list includes either a recipient type with digital contact information, in that order, or a space-separated token list of other tokens.

##### Recipient type

The tokens that identify the type of recipient include:

[`home`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#home)

The contact type identified by subsequent tokens is for contacting the recipient at their residence.

[`work`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#work)

The contact type identified by subsequent tokens is for contacting the recipient at their work.

[`mobile`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#mobile)

The contact type identified by subsequent tokens is for contacting the recipient regardless of location.

[`fax`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#fax)

The recipient identified by subsequent tokens is for a fax machine.

[`pager`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#pager)

The recipient identified by subsequent tokens is for a pager or beeper.

##### Digital contact tokens

The token or group of tokens for telephone numbers or a number's component parts, phone extensions, email addresses, or instant messaging protocols.

[`tel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel)

A full telephone number, including the country code. If you need to break the phone number up into its components, you can use these values for those fields:

[`tel-country-code`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel-country-code)

The country code, such as "1" for the United States, Canada, and other areas in North America and parts of the Caribbean.

[`tel-national`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel-national)

The entire phone number without the country code component, including a country-internal prefix. For the phone number "1-855-555-6502", this field's value would be "855-555-6502".

[`tel-area-code`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel-area-code)

The area code, with any country-internal prefix applied if appropriate.

[`tel-local`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel-local)

The phone number without the country or area code. This can be split further into two parts, for phone numbers which have an exchange number and then a number within the exchange. For the phone number "555-6502", use `tel-local-prefix` for "555" and `tel-local-suffix` for "6502".

[`tel-extension`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#tel-extension)

A telephone extension code within the phone number, such as a room or suite number in a hotel or an office extension in a company.

[`email`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#email)

An email address.

[`impp`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#impp)

A URL for an instant messaging protocol endpoint, such as `xmpp:username@example.net`.

##### Other tokens

When the form field is not a phone number, email address, or instant messaging protocol, the space-separated list of tokens is not preceded by a contact type:

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#name)

The field expects the value to be a person's full name. Using `name` rather than breaking the name down into its components is generally preferred because it avoids dealing with the wide diversity of human names and how they are structured; however, you can use the following `autocomplete` values if you do need to break the name down into its components:

[`honorific-prefix`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#honorific-prefix)

The prefix or title, such as "Mrs.", "Mr.", "Miss", "Ms.", "Dr.", or "Mlle.".

[`given-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#given-name)

The given (or "first") name.

[`additional-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#additional-name)

The middle name.

[`family-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#family-name)

The family (or "last") name.

[`honorific-suffix`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#honorific-suffix)

The suffix, such as "Jr.", "B.Sc.", "PhD.", "MBASW", or "IV".

[`nickname`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#nickname)

A nickname or handle.

[`username`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#username)

A username or account name.

[`new-password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#new-password)

A new password. When creating a new account or changing passwords, this should be used for an "Enter your new password" or "Confirm new password" field, as opposed to a general "Enter your current password" field that might be present. This may be used by the browser both to avoid accidentally filling in an existing password and to offer assistance in creating a secure password.

[`current-password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#current-password)

The user's current password.

[`one-time-code`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#one-time-code)

A one-time password (OTP) for verifying user identity that is used as an additional factor in a sign-in flow. Most commonly this is a code received via some out-of-channel mechanism, such as SMS, email, or authenticator application.

[`organization-title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#organization-title)

A job title, or the title a person has within an organization, such as "Senior Technical Writer", "President", or "Assistant Troop Leader".

[`organization`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#organization)

A company or organization name, such as "Acme Widget Company" or "Girl Scouts of America".

[`street-address`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#street-address)

A street address. This can be multiple lines of text, and should fully identify the location of the address within its second administrative level (typically a city or town), but should not include the city name, ZIP or postal code, or country name.

[`address-line1`, `address-line2`, `address-line3`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#address-line1)

Each individual line of the street address. These should only be present if the `street-address` is not present.

[`address-level4`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#address-level4)

The finest-grained [administrative level](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#administrative_levels_in_addresses)
, in addresses which have four levels.

[`address-level3`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#address-level3)

The third [administrative level](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#administrative_levels_in_addresses)
, in addresses with at least three administrative levels.

[`address-level2`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#address-level2)

The second [administrative level](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#administrative_levels_in_addresses)
, in addresses with at least two of them. In countries with two administrative levels, this would typically be the city, town, village, or other locality in which the address is located.

[`address-level1`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#address-level1)

The first [administrative level](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#administrative_levels_in_addresses)
 in the address. This is typically the province in which the address is located. In the United States, this would be the state. In Switzerland, the canton. In the United Kingdom, the county.

[`country`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#country)

A country or territory code.

[`country-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#country-name)

A country or territory name.

[`postal-code`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#postal-code)

A postal code (in the United States, this is the ZIP code).

[`cc-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-name)

The full name as printed on or associated with a payment instrument such as a credit card. Using a full name field is preferred, typically, over breaking the name into pieces.

[`cc-given-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-given-name)

A given (first) name as given on a payment instrument like a credit card.

[`cc-additional-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-additional-name)

A middle name as given on a payment instrument or credit card.

[`cc-family-name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-family-name)

A family name, as given on a credit card.

[`cc-number`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-number)

A credit card number or other number identifying a payment method, such as an account number.

[`cc-exp`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-exp)

A payment method expiration date, typically in the form "MM/YY" or "MM/YYYY".

[`cc-exp-month`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-exp-month)

The month in which the payment method expires.

[`cc-exp-year`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-exp-year)

The year in which the payment method expires.

[`cc-csc`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-csc)

The security code for the payment instrument; on credit cards, this is the 3-digit verification number on the back of the card.

[`cc-type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#cc-type)

The type of payment instrument (such as "Visa" or "Master Card").

[`transaction-currency`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#transaction-currency)

The currency in which the transaction is to take place.

[`transaction-amount`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#transaction-amount)

The amount, given in the currency specified by `transaction-currency`, of the transaction, for a payment form.

[`language`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#language)

A preferred language, given as a valid [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
.

[`bday`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#bday)

A birth date, as a full date.

[`bday-day`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#bday-day)

The day of the month of a birth date.

[`bday-month`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#bday-month)

The month of the year of a birth date.

[`bday-year`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#bday-year)

The year of a birth date.

[`sex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#sex)

A gender identity (such as "Female", "Fa'afafine", "Hijra", "Male", "Nonbinary"), as freeform text without newlines.

[`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#url)

A URL, such as a home page or company website address as appropriate given the context of the other fields in the form.

[`photo`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#photo)

The URL of an image representing the person, company, or contact information given in the other fields in the form.

#### Web authorization token

With [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
, the `webauthn` token can be included last to indicate the user agent should show public key credentials when the user is interacting with the control.

[`webauthn`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#webauthn)

Passkeys generated by the [Web Authentication API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API)
, as requested by a conditional [`navigator.credentials.get()`](https://developer.mozilla.org/en-US/docs/Web/API/CredentialsContainer/get "navigator.credentials.get()")
 call (i.e., one that includes `mediation: 'conditional'`). If included, this is the last token in the space-separated token list. See [Sign in with a passkey through form autofill](https://web.dev/articles/passkey-form-autofill "External link (opens in new tab)")
 for more details.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#accessibility)

-------------------------------------------------------------------------------------------------------------------

Using appropriate `autocomplete` values helps users with cognitive disabilities, motor impairments, and other conditions fill out forms more quickly and accurately by reducing the need to type and remember information. When the browser can identify the purpose of a form field through its `autocomplete` value, it can offer stored data such as names, addresses, and payment details, which benefits all users but is especially important for those who find manual data entry difficult.

Providing valid autocomplete tokens also satisfies [WCAG 2.2 Success Criterion 1.3.5: Identify Input Purpose](https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose "External link (opens in new tab)")
 (Level AA), which requires that the purpose of input fields collecting user information can be programmatically determined. This enables user agents and assistive technologies to apply personalized presentations, such as displaying familiar icons next to fields, to help users understand and complete forms.

### [Avoid disabling autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#avoid_disabling_autocomplete)

Setting `autocomplete="off"` prevents the browser from offering stored data for a field. While developers sometimes use this to prevent autofill for security reasons (such as one-time codes), it removes a feature that many users depend on. Users with cognitive disabilities may rely on autocomplete to recall personal information, and users with motor impairments benefit from reduced typing. Browsers may also ignore `autocomplete="off"` on login fields to support password managers.

### [Avoid invalid autocomplete values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#avoid_invalid_autocomplete_values)

Using invalid or non-standard values (such as made-up strings to circumvent autofill) has a similar effect: the browser cannot match the field to any known purpose, so it cannot offer relevant suggestions. This also fails the WCAG requirement above, since the input purpose is no longer programmatically determinable. If you need to disable autofill for a specific field, consider using `autocomplete="off"` only where genuinely necessary (such as for CAPTCHA or one-time token fields) rather than applying it broadly across a form.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#examples)

---------------------------------------------------------------------------------------------------------

### [Administrative levels in addresses](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#administrative_levels_in_addresses)

The four administrative level fields (`address-level1` through `address-level4`) describe the address in terms of increasing levels of precision within the country in which the address is located. Each country has its own system of administrative levels, and may arrange the levels in different orders when addresses are written.

`address-level1` always represents the broadest administrative division; it is the least-specific portion of the address short of the country name.

### [Form layout flexibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#form_layout_flexibility)

Given that different countries write their address in different ways, with each field in different places within the address, and even different sets and numbers of fields entirely, it can be helpful if, when possible, your site is able to switch to the layout expected by your users when presenting an address entry form, given the country the address is located within.

### [Variations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#variations)

The way each administrative level is used will vary from country to country. Below are some examples; this is not meant to be an exhaustive list.

#### United States

A typical home address within the United States looks like this:

432 Anywhere St Exampleville CA 95555

In the United States, the least-specific portion of the address is the state, in this case "CA" (the official US Postal Service shorthand for "California"). Thus `address-level1` is the state, or "CA" in this case.

The second-least specific portion of the address is the city or town name, so `address-level2` is "Exampleville" in this example address.

United States addresses do not use levels 3 and up.

#### United Kingdom

Address input forms in the UK should contain one or two address levels and one, two or three address lines, depending on the address. A complete address would look like so:

103 Frogmarch Street Upper-Wapping Winchelsea Whereshire TN99 8ZZ

The address levels are:

*   `address-level1`: The county — "Whereshire" in this case.
*   `address-level2`: The post town — "Winchelsea" in this case.
*   `address-line2`: The locality — "Upper-Wapping" in this case.
*   `address-line1`: The house/street particulars — "103 Frogmarch Street".

The postcode is separate. Note that you can actually use just the postcode and `address-line1` to successfully deliver mail in the UK, so they should be the only mandatory items, but usually people tend to provide more details.

#### China

China can use as many as three administrative levels: the province, the city, and the district.

The 6 digit postal code is not always needed but when supplied it is placed separately with a label for clarity. For example:

北京市东城区建国门北大街 8 号华润大厦 17 层 1708 单元 邮编：100005

#### Japan

An address in Japan is typically **written in one line**, in an order from the least-specific to more-specific portions (in **reverse order to the United States**). There are two or three administrative levels in an address. Additional line can be used to show building names and room numbers. The postal code is separate. For example:

〒 381-0000 長野県長野市某町 123

"〒" and following seven digits shows the postal code.

`address-level1` is used for prefectures or the Tokyo Metropolis; "長野県" (Nagano Prefecture) is in this case. `address-level2` is typically used for cities, counties, towns and villages; "長野市" (Nagano City) in this case. "某町 123" is `address-line1` which consists of an area name and a lot number.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-form-autocomplete](https://html.spec.whatwg.org/multipage/forms.html#attr-form-autocomplete) |
| [HTML  <br>\# attr-fe-autocomplete](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-autocomplete) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

### [html.elements.form.autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#html.elements.form.autocomplete)

### [html.elements.input.autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#html.elements.input.autocomplete)

### [html.elements.select.autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#html.elements.select.autocomplete)

### [html.elements.textarea.autocomplete](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#html.elements.textarea.autocomplete)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#see_also)

---------------------------------------------------------------------------------------------------------

*   The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element
*   The [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     element
*   The [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     element
*   The [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
     element
*   [HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/autocomplete/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/autocomplete (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fautocomplete&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fautocomplete%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fautocomplete%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fautocomplete%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F87adaa5384b1015690f3435ce0ba64ac097764eb%0A*+Document+last+modified%3A+2026-08-27T09%3A50%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")