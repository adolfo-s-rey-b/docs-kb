For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking.md)
.

**Programmatic-style nodes only**

This guidance applies to programmatic-style nodes. If you're using declarative style, n8n handles paired items for you automatically.

Use n8n's item linking to access data from items that precede the current item. n8n needs to know which input item a given output item comes from. If this information is missing, expressions in other nodes may break. As a node developer, you must ensure any items returned by your node support this.

This applies to programmatic nodes (including trigger nodes). You don't need to consider item linking when building a declarative-style node. Refer to [Choose your node building approach](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style)
 for more information on node styles.

Start by reading [Item linking concepts](https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows)
, which provides a conceptual overview of item linking, and details of the scenarios where n8n can handle the linking automatically.

If you need to handle item linking manually, do this by setting `pairedItem` on each item your node returns:

Copy

    // Use the pairedItem information of the incoming item
    newItem = {
    	"json": { . . . },
    	"pairedItem": {
    		"item": item.pairedItem,
    		// Optional: choose the input to use
    		// Set this if your node combines multiple inputs
    		"input": 0
    };
    
    // Or set the index manually
    newItem = {
    		"json": { . . . }
    		"pairedItem": {
    			"item": i,
    			// Optional: choose the input to use
    			// Set this if your node combines multiple inputs
    			"input": 0
    		},
    };

Related resources[](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/item-linking#related-resources)

-----------------------------------------------------------------------------------------------------------------------

*   [Node building reference](https://docs.n8n.io/connect/create-nodes/build-your-node/reference)
    

[PreviousHTTP request helpers](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/http-request-helpers)
[NextUX guidelines](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/ux-guidelines)

Last updated 10 days ago

Was this helpful?