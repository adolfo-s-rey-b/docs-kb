*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#mdn-search)
    

Intl.NumberFormat.prototype.resolvedOptions()
=============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`resolvedOptions()`** method of [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)
 instances returns a new object with properties reflecting the options computed during initialization of this `NumberFormat` object.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#try_it)

------------------------------------------------------------------------------------------------------------------------------------

    const numberFormat = new Intl.NumberFormat("de-DE");
    const options = numberFormat.resolvedOptions();
    
    console.log(options.locale);
    // Expected output: "de-DE"
    
    console.log(options.numberingSystem);
    // Expected output: "latn"
    
    console.log(options.style);
    // Expected output: "decimal"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#syntax)

------------------------------------------------------------------------------------------------------------------------------------

js

    resolvedOptions()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#parameters)

None.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#return_value)

A new object with properties reflecting the options computed during the initialization of this `NumberFormat` object. The object has the following properties, in the order they are listed:

[`locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#locale)

The [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
 for the locale actually used, determined by the [locale negotiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locale_identification_and_negotiation)
 process. Only the `nu` Unicode extension key, if requested, may be included in the output.

[`numberingSystem`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#numberingsystem)

The value provided for this property in the `options` argument, or using the Unicode extension key `"nu"`, with default filled in as needed. It is a supported [numbering system](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_numbering_system_types)
 for this locale. The default is locale dependent.

[`style`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#style)

The value provided for this property in the `options` argument, with default filled in as needed. It is either `"decimal"`, `"percent"`, `"currency"`, or `"unit"`. The default is `"decimal"`.

[`currency` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#currency)

The value provided for this property in the `options` argument. It is only present if `style` is `"currency"`. It is an ISO 4217 currency code; see [`Intl.supportedValuesOf()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/supportedValuesOf#supported_currency_identifiers)
. It is required if `style` is `"currency"` so there is no default.

[`currencyDisplay` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#currencydisplay)

The value provided for this property in the `options` argument, with default filled in as needed. It is only present if `style` is `"currency"`. It is either `"code"`, `"symbol"`, `"narrowSymbol"`, or `"name"`. The default is `"symbol"`.

[`currencySign` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#currencysign)

The value provided for this property in the `options` argument, with default filled in as needed. It is only present if `style` is `"currency"`. It is either `"standard"` or `"accounting"`. The default is `"standard"`.

[`unit` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#unit)

The value provided for this property in the `options` argument. It is only present if `style` is `"unit"`. It is a [sanctioned unit identifier](https://tc39.es/ecma402/#table-sanctioned-single-unit-identifiers "External link (opens in new tab)")
 from the [full CLDR list](https://github.com/unicode-org/cldr/blob/main/common/validity/unit.xml "External link (opens in new tab)")
. It is required if `style` is `"unit"` so there is no default.

[`unitDisplay` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#unitdisplay)

The value provided for this property in the `options` argument, with default filled in as needed. It is only present if `style` is `"unit"`. It is either `"short"`, `"narrow"`, or `"long"`. The default is `"short"`.

[`minimumIntegerDigits`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#minimumintegerdigits)

The value provided for this property in the `options` argument, with default filled in as needed. It is an integer between `1` and `21`. The default is `1`.

[`minimumFractionDigits`, `maximumFractionDigits` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#minimumfractiondigits)

The value provided for these properties in the `options` argument, with defaults filled in as needed. They are only present if necessary; see [digit options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#digit_options)
. It is an integer between `0` and `100`.

[`minimumSignificantDigits`, `maximumSignificantDigits` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#minimumsignificantdigits)

The value provided for these properties in the `options` argument, with defaults filled in as needed. They are only present if necessary; see [digit options](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#digit_options)
. It is an integer between `1` and `21`.

[`useGrouping`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#usegrouping)

The value provided for this property in the `options` argument, with default filled in as needed, and with some values normalized. It is either `"always"`, `"auto"`, `"min2"`, or the boolean `false`. The default is `"min2"` if `notation` is `"compact"`, and `"auto"` otherwise.

[`notation`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#notation)

The value provided for this property in the `options` argument, with default filled in as needed. It is either `"standard"`, `"scientific"`, `"engineering"`, or `"compact"`. The default is `"standard"`.

[`compactDisplay` Optional](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#compactdisplay)

The value provided for this property in the `options` argument, with default filled in as needed. It is only present if `notation` is `"compact"`. It is either `"short"` or `"long"`. The default is `"short"`.

[`signDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#signdisplay)

The value provided for this property in the `options` argument, with default filled in as needed. It is either `"auto"`, `"always"`, `"exceptZero"`, `"negative"`, or `"never"`. The default is `"auto"`.

[`roundingIncrement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#roundingincrement)

The value provided for this property in the `options` argument, with default filled in as needed. It is one of `1`, `2`, `5`, `10`, `20`, `25`, `50`, `100`, `200`, `250`, `500`, `1000`, `2000`, `2500`, and `5000`. The default is `1`.

[`roundingMode`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#roundingmode)

The value provided for this property in the `options` argument, with default filled in as needed. It is one of `"ceil"`, `"floor"`, `"expand"`, `"trunc"`, `"halfCeil"`, `"halfFloor"`, `"halfExpand"`, `"halfTrunc"`, and `"halfEven"`. The default is `"halfExpand"`.

[`roundingPriority`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#roundingpriority)

The value provided for this property in the `options` argument, with default filled in as needed. It is either `"auto"`, `"morePrecision"`, or `"lessPrecision"`. The default is `"auto"`.

[`trailingZeroDisplay`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#trailingzerodisplay)

The value provided for this property in the `options` argument, with default filled in as needed. It is either `"auto"` or `"stripIfInteger"`. The default is `"auto"`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#examples)

----------------------------------------------------------------------------------------------------------------------------------------

### [Using the `resolvedOptions` method](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#using_the_resolvedoptions_method)

js

    // Create a NumberFormat
    const de = new Intl.NumberFormat("de-DE", {
      style: "currency",
      currency: "USD",
      maximumFractionDigits: 2,
      roundingIncrement: 5,
      roundingMode: "halfCeil",
    });
    
    // Resolve the options
    const usedOptions = de.resolvedOptions();
    console.log(usedOptions.locale); // "de-DE"
    console.log(usedOptions.numberingSystem); // "latn"
    console.log(usedOptions.compactDisplay); // undefined ("notation" not set to "compact")
    console.log(usedOptions.currency); // "USD"
    console.log(usedOptions.currencyDisplay); // "symbol"
    console.log(usedOptions.currencySign); // "standard"
    console.log(usedOptions.minimumIntegerDigits); // 1
    console.log(usedOptions.minimumFractionDigits); // 2
    console.log(usedOptions.maximumFractionDigits); // 2
    console.log(usedOptions.minimumSignificantDigits); // undefined (maximumFractionDigits is set)
    console.log(usedOptions.maximumSignificantDigits); // undefined (maximumFractionDigits is set)
    console.log(usedOptions.notation); // "standard"
    console.log(usedOptions.roundingIncrement); // 5
    console.log(usedOptions.roundingMode); // halfCeil
    console.log(usedOptions.roundingPriority); // auto
    console.log(usedOptions.signDisplay); // "auto"
    console.log(usedOptions.style); // "currency"
    console.log(usedOptions.trailingZeroDisplay); // auto
    console.log(usedOptions.useGrouping); // auto
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#specifications)

----------------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Internationalization API Specification  <br>\# sec-intl.numberformat.prototype.resolvedoptions](https://tc39.es/ecma402/#sec-intl.numberformat.prototype.resolvedoptions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions#see_also)

----------------------------------------------------------------------------------------------------------------------------------------

*   [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 24, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/resolvedOptions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/intl/numberformat/resolvedoptions/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/intl/numberformat/resolvedoptions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FNumberFormat%2FresolvedOptions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fnumberformat%2Fresolvedoptions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FIntl%2FNumberFormat%2FresolvedOptions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fintl%2Fnumberformat%2Fresolvedoptions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7bc0ed5466f5834641d75d416fa81886cf6b37e%0A*+Document+last+modified%3A+2025-09-24T12%3A28%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")