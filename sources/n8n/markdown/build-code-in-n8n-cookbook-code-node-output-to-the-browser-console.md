For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console.md)
.

You can use `console.log()` or `print()` in the Code node to help when writing and debugging your code.

For help opening your browser console, refer to [this guide by Balsamiq](https://balsamiq.com/support/faqs/browserconsole/)
.

console.log (JavaScript)[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console#consolelog-javascript)

-----------------------------------------------------------------------------------------------------------------------------------------

For technical information on `console.log()`, refer to the [MDN developer docs](https://developer.mozilla.org/en-US/docs/Web/API/Console/log)
.

For example, copy the following code into a Code node, then open your console and run the node:

Copy

    let a = "apple";
    console.log(a);

print (Python)[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console#print-python)

----------------------------------------------------------------------------------------------------------------------

For technical information on `print()`, refer to the [Real Python's guide](https://realpython.com/python-print/)
.

For example, set your Code node **Language** to **Python**, copy the following code into the node, then open your console and run the node:

Copy

    a = "apple"
    print(a)

### Printing node data[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console#printing-node-data)

`_items` and `_item` are standard Python objects, so you can print them directly:

Copy

    print(_items)

`**type()**` **isn't available**

The Python Code node denies some built-in functions by default, including `type()`. Refer to [task runners environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners)
 for the full list and how to change it when self-hosting.

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console#related-resources)

------------------------------------------------------------------------------------------------------------------------------

*   [Code node cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
    
*   [Get number of items returned by last node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node)
    
*   [Get the binary data buffer](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer)
    

[PreviousGet the binary data buffer](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer)
[NextHTTP Request node](https://docs.n8n.io/build/code-in-n8n/cookbook/http-request-node)

Last updated 10 days ago

Was this helpful?