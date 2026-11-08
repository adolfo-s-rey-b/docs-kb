For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer.md)
.

The binary data buffer contains all the binary file data processed by a workflow. You need to access it if you want to perform operations on the binary data, such as:

*   Manipulating the data: for example, adding column headers to a CSV file.
    
*   Using the data in calculations: for example, calculating a hash value based on it.
    
*   Complex HTTP requests: for example, combining file upload with sending other data formats.
    

**Not available in Python**

`getBinaryDataBuffer()` isn't supported when using Python.

You can access the buffer using n8n's \`getBinaryDataBuffer()\` function:

Copy

    /* 
    * itemIndex: number. The index of the item in the input data.
    * binaryPropertyName: string. The name of the binary property. 
    * The default in the Read/Write File From Disk node is 'data'. 
    */
    let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(itemIndex, binaryPropertyName);

For example:

Copy

    let binaryDataBufferItem = await this.helpers.getBinaryDataBuffer(0, 'data');
    // Returns the data in the binary buffer for the first input item

You should always use the `getBinaryDataBuffer()` function, and avoid using older methods of directly accessing the buffer, such as targeting it with expressions like `items[0].binary.data.data`.

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer#related-resources)

---------------------------------------------------------------------------------------------------------------------------

*   [Code node cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
    
*   [Get number of items returned by last node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node)
    
*   [Output to the browser console](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console)
    

[PreviousGet number of items returned by last node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node)
[NextOutput to the browser console](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console)

Last updated 10 days ago

Was this helpful?