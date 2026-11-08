For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md)
.

You can use the Error Trigger node to create error workflows. When another linked workflow fails, this node gets details about the failed workflow and the errors, and runs the error workflow.

Usage[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger#usage)

-----------------------------------------------------------------------------------------------

1.  Create a new workflow, with the Error Trigger as the first node.
    
2.  Give the workflow a name, for example `Error Handler`.
    
3.  Select **Save**.
    
4.  In the workflow where you want to use this error workflow:
    
    1.  Select **Options** ![Options menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=2ffc9760cc11f87330c24b8445804ba2&sv=3) > **Settings**.
        
    2.  In **Error workflow**, select the workflow you just created. For example, if you used the name Error Handler, select **Error handler**.
        
    3.  Select **Save**. Now, when this workflow errors, the related error workflow runs.
        
    

Note the following:

*   If a workflow uses the Error Trigger node, you don't have to publish the workflow.
    
*   If a workflow contains the Error Trigger node, by default, the workflow uses itself as the error workflow.
    
*   You can't test error workflows when running workflows manually. The Error Trigger only runs when an automatic workflow errors.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------------

[Browse Error Trigger node documentation integration templates](https://n8n.io/integrations/error-trigger)
 or [search all templates](https://n8n.io/workflows/)

Related resources[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger#related-resources)

-----------------------------------------------------------------------------------------------------------------------

You can use the [Stop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror)
 node to send custom messages to the Error Trigger.

Read more about [Error workflows](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully)
 in n8n workflows.

Error data[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger#error-data)

---------------------------------------------------------------------------------------------------------

The default error data received by the Error Trigger is:

Copy

    [\
    	{\
    		"execution": {\
    			"id": "231",\
    			"url": "https://n8n.example.com/execution/231",\
    			"retryOf": "34",\
    			"error": {\
    				"message": "Example Error Message",\
    				"stack": "Stacktrace"\
    			},\
    			"lastNodeExecuted": "Node With Error",\
    			"mode": "manual"\
    		},\
    		"workflow": {\
    			"id": "1",\
    			"name": "Example Workflow"\
    		}\
    	}\
    ]
    

All information is always present, except:

*   `execution.id`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
    
*   `execution.url`: requires the execution to be saved in the database. Not present if the error is in the trigger node of the main workflow, as the workflow doesn't execute.
    
*   `execution.retryOf`: only present when the execution is a retry of a failed execution.
    

If the error is caused by the trigger node of the main workflow, rather than a later stage, the data sent to the error workflow is different. There's less information in `execution{}` and more in `trigger{}`:

Copy

    {
      "trigger": {
        "error": {
          "context": {},
          "name": "WorkflowActivationError",
          "cause": {
            "message": "",
            "stack": ""
          },
          "timestamp": 1654609328787,
          "message": "",
          "node": {
            . . . 
          }
        },
        "mode": "trigger"
      },
      "workflow": {
        "id": "",
        "name": ""
      }
    }

[PreviousEmail Trigger (IMAP)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap)
[NextEvaluation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluation)

Last updated 10 days ago

Was this helpful?