For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure.md)
.

Understanding how n8n structures and passes data between nodes is fundamental to building workflows. This guide covers both the data structure format and how data flows through your workflow.

Data structure[](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#data-structure)

---------------------------------------------------------------------------------------------------------

In n8n, all data passed between nodes is an array of objects. It has the following structure:

Copy

    [\
    	{\
    		// For most data:\
    		// Wrap each item in another object, with the key 'json'\
    		"json": {\
    			// Example data\
    			"apple": "beets",\
    			"carrot": {\
    				"dill": 1\
    			}\
    		},\
    		// For binary data:\
    		// Wrap each item in another object, with the key 'binary'\
    		"binary": {\
    			// Example data\
    			"apple-picture": {\
    				"data": "....", // Base64 encoded binary data (required)\
    				"mimeType": "image/png", // Best practice to set if possible (optional)\
    				"fileExtension": "png", // Best practice to set if possible (optional)\
    				"fileName": "example.png", // Best practice to set if possible (optional)\
    			}\
    		}\
    	},\
    ]

**Skipping the** `**json**` **key and array syntax**

From 0.166.0 on, when using the Function node or Code node, n8n automatically adds the `json` key if it's missing. It also automatically wraps your items in an array (`[]`) if needed. This is only the case when using the Function or Code nodes. When building your own nodes, you must still make sure the node returns data with the `json` key.

How data flows within nodes[](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#how-data-flows-within-nodes)

-----------------------------------------------------------------------------------------------------------------------------------

When you connect nodes in a workflow, data automatically passes from one node to the next.

Nodes process multiple items automatically. When a node receives an array of data items, it processes each item individually and performs the configured operation for each one.

For example, if you set the Trello node to `Create-Card`, and create an expression that sets `Name` using a property called `name-input-value` from the incoming data, the node creates a card for each item, always choosing the `name-input-value` of the current item.

For example, this input will create two cards. One named `test1` the other one named `test2`:

Copy

    [\
    	{\
    		"name-input-value": "test1"\
    	},\
    	{\
    		"name-input-value": "test2"\
    	}\
    ]

Understand what you're mapping with drag and drop[](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#understand-what-youre-mapping-with-drag-and-drop)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Data mapping maps the field path, and loads the field's value. For example, given the following data:

Copy

    [\
    	{\
    		"fruit": "apples",\
    		"color": "green"\
    	}\
    ]

You can map `fruit` by dragging and dropping **fruit** from the **INPUT** into the field where you want to use its value. This creates an expression, `{{ $json.fruit }}`. When the node iterates over input items, the value of the field becomes the value of `fruit` for each item.

Understand nested data[](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#understand-nested-data)

-------------------------------------------------------------------------------------------------------------------------

Given the following data:

Copy

    [\
      {\
        "name": "First item",\
        "nested": {\
          "example-number-field": 1,\
          "example-string-field": "apples"\
        }\
      },\
      {\
        "name": "Second item",\
        "nested": {\
          "example-number-field": 2,\
          "example-string-field": "oranges"\
        }\
      }\
    ]

n8n displays it in table form like this, showing the `nested` field in bold to show that it contains nested data:

![](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F3488703508-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FrPN1zU5jaYNvwH7RzxqA%252Fuploads%252Fgit-blob-9a1523a8d56bec14ea59915ddf7ec21c70e3d805%252Fnested-data.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=33159353d26a2263b99b4495816547ca&sv=3)

Table view of the example data, with the nested field shown in bold

Related resources[](https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure#related-resources)

---------------------------------------------------------------------------------------------------------------

*   [Work with data](https://docs.n8n.io/build/work-with-data)
    
*   [Expressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    
*   [Reference data](https://docs.n8n.io/build/work-with-data/reference-data)
    
*   [Transform data](https://docs.n8n.io/build/work-with-data/transform-data)
    
*   [Filter out unwanted data](https://docs.n8n.io/build/work-with-data/filter-out-unwanted-data)
    
*   [Pin and mock data](https://docs.n8n.io/build/work-with-data/pin-and-mock-data)
    
*   [Handle special data types](https://docs.n8n.io/build/work-with-data/handle-special-data-types)
    
*   [Data tables](https://docs.n8n.io/build/work-with-data/data-tables)
    

[PreviousWork with data](https://docs.n8n.io/build/work-with-data)
[NextExpressions versus data nodes](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)

Last updated 10 days ago

Was this helpful?