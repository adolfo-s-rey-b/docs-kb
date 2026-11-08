For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully.md)
.

When designing your [flow logic](https://docs.n8n.io/build/flow-logic)
, it's a good practice to consider potential errors, and set up methods to handle them gracefully. With an error workflow, you can control how n8n responds to a workflow execution failure.

**Investigating errors**

To investigate failed executions, you can:

*   Review your [Executions](https://docs.n8n.io/build/understand-workflows/understand-executions)
    , for a [single workflow](https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow)
     or [all workflows you have access to](https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions)
    . You can [load data from previous execution](https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions)
     into your current workflow.
    
*   Enable [Log streaming](https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems)
    .
    

How do I set up an error workflow?[](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully#create-and-set-an-error-workflow)

-------------------------------------------------------------------------------------------------------------------------------------

For each workflow, you can set an error workflow in **Workflow Settings**. It runs if an execution fails. This means you can, for example, send email or Slack alerts when a workflow execution errors. The error workflow must start with the [Error Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger)
.

You can use the same error workflow for multiple workflows.

1.  Create a new workflow, with the Error Trigger as the first node.
    
2.  Give the workflow a name, for example `Error Handler`.
    
3.  Select **Save**.
    
4.  In the workflow where you want to use this error workflow:
    
    1.  Select **Options** ![Options menu icon](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F2738857267-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FGixZThfitWP21x2gQFpD%252Fuploads%252Fgit-blob-f19a4d097d364587b73864eaed77b12bfd8f516b%252Fthree-dot-options-menu.png%3Falt%3Dmedia&width=19&dpr=3&quality=100&sign=2ffc9760cc11f87330c24b8445804ba2&sv=3) > **Settings**.
        
    2.  In **Error workflow**, select the workflow you just created. For example, if you used the name Error Handler, select **Error handler**.
        
    3.  Select **Save**. Now, when this workflow errors, the related error workflow runs.
        
    

What data does an error workflow receive?[](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully#error-data)

----------------------------------------------------------------------------------------------------------------------

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

How do I make a workflow fail on purpose with the Stop and Error node?[](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully#cause-a-workflow-execution-failure-using-stop-and-error)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When you create and set an error workflow, n8n runs it when an execution fails. Usually, this is due to things like errors in node settings, or the workflow running out of memory.

You can add the [Stop And Error](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror)
 node to your workflow to force executions to fail under your chosen circumstances, and trigger the error workflow.

Related resources[](https://docs.n8n.io/build/flow-logic/handle-errors-gracefully#related-resources)

-----------------------------------------------------------------------------------------------------

*   [Flow logic](https://docs.n8n.io/build/flow-logic)
    
*   [Split with conditionals](https://docs.n8n.io/build/flow-logic/split-with-conditionals)
    
*   [Merge data](https://docs.n8n.io/build/flow-logic/merge-data)
    
*   [Loop](https://docs.n8n.io/build/flow-logic/loop)
    
*   [Wait](https://docs.n8n.io/build/flow-logic/wait)
    
*   [Understand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)
    
*   [Break workflows into smaller parts](https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts)
    
*   [Convert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
    

[PreviousConvert to sub-workflows](https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows)
[NextUnderstand execution order](https://docs.n8n.io/build/flow-logic/understand-execution-order)

Last updated 10 days ago

Was this helpful?