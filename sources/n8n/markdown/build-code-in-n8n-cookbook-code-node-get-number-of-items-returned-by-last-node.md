For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node.md)
.

To get the number of items returned by the previous node:

JavaScript

Python

Copy

    if (Object.keys(items[0].json).length === 0) {
    return [\
    	{\
    		json: {\
    			results: 0,\
    		}\
    	}\
    ]
    }
    return [\
    	{\
    		json: {\
    			results: items.length,\
    		}\
    	}\
    ];

The output will be similar to the following.

Copy

    [\
    	{\
    		"results": 8\
    	}\
    ]

Copy

    if len(items[0].json) == 0:
    	return [\
    		{\
    			"json": {\
    				"results": 0,\
    			}\
    		}\
    	]
    else:
    	return [\
    		{\
    			"json": {\
    				"results": len(items),\
    			}\
    		}\
    	]

The output will be similar to the following.

Copy

    [\
    	{\
    		"results": 8\
    	}\
    ]

Related resources[](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node#related-resources)

------------------------------------------------------------------------------------------------------------------------------------------

*   [Code node cookbook](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
    
*   [Get the binary data buffer](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer)
    
*   [Output to the browser console](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/output-to-the-browser-console)
    

[PreviousCode node](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node)
[NextGet the binary data buffer](https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-the-binary-data-buffer)

Last updated 10 days ago

Was this helpful?