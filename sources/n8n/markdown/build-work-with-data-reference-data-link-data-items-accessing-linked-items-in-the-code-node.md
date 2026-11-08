For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node.md)
.

Every item in a node's input data links back to the items used in previous nodes to generate it. This is useful if you need to retrieve linked items from further back than the immediate previous node.

To access the linked items from earlier in the workflow, use `("<node-name>").itemMatching(currentNodeinputIndex)`.

For example, consider a workflow that does the following:

1.  The Customer Datastore node generates example data:
    
    Copy
    
        [\
        	{\
        		"id": "23423532",\
        		"name": "Jay Gatsby",\
        		"email": "gatsby@west-egg.com",\
        		"notes": "Keeps asking about a green light??",\
        		"country": "US",\
        		"created": "1925-04-10"\
        	},\
        	{\
        		"id": "23423533",\
        		"name": "José Arcadio Buendía",\
        		"email": "jab@macondo.co",\
        		"notes": "Lots of people named after him. Very confusing",\
        		"country": "CO",\
        		"created": "1967-05-05"\
        	},\
        	...\
        ]
    
2.  The Edit Fields node simplifies this data:
    
    Copy
    
        [\
        	{\
        		"name": "Jay Gatsby"\
        	},\
        	{\
        		"name": "José Arcadio Buendía"\
        	},\
            ...\
        ]
    
3.  The Code node restores the email address to the correct person:
    
    Copy
    
        [\
        	{\
        		"name": "Jay Gatsby",\
        		"restoreEmail": "gatsby@west-egg.com"\
        	},\
        	{\
        		"name": "José Arcadio Buendía",\
        		"restoreEmail": "jab@macondo.co"\
        	},\
        	...\
        ]
    

The Code node does this using the following code:

JavaScript

Python

Copy

    for(let i=0; i<$input.all().length; i++) {
    	$input.all()[i].json.restoreEmail = $('Customer Datastore (n8n training)').itemMatching(i).json.email;
    }
    return $input.all();

Copy

    for i,item in enumerate(_input.all()):
    	_input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email
    
    return _input.all();

You can view and download the example workflow from [n8n website | itemMatching usage example](https://n8n.io/workflows/1966-itemmatching-usage-example/)
.

Related resources[](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node#related-resources)

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Link data items](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items)
    
*   [How items link through workflows](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
    
*   [Preserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)
    
*   [Item linking errors](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors)
    
*   [Item linking for node creators](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-for-node-creators)
    

[PreviousHow items link through workflows](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
[NextPreserving linking in the Code node](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/preserving-linking-in-the-code-node)

Last updated 10 days ago

Was this helpful?