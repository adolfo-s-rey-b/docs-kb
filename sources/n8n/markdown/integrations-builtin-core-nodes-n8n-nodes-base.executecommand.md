For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand.md)
.

The Execute Command node runs shell commands on the host machine that runs n8n.

**Security considerations**

The Execute Command node can introduce significant security risks in environments that operate with untrusted users. Because of this, the node is [disabled](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes#exclude-nodes)
 by default from n8n 2.0.

**Which shell runs the command?**

This node executes the command in the default shell of the host machine. For example, `cmd` on Windows and `zsh` on macOS.

If you run n8n with Docker, your command will run in the n8n container and not the Docker host.

If you're using [queue mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode)
, the command runs on the worker that's executing the task in production mode. When running manual executions, it runs on the main instance, unless you set `OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS` to `true`.

**Feature availability**

The Execute Command node is available on:

*   **Self-hosted:** All editions
    

It isn't available on n8n Cloud.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#node-parameters)

---------------------------------------------------------------------------------------------------------------------

Configure the node using the following parameters.

### Execute Once[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#execute-once)

Choose whether you want the node to execute only once (turned on) or once for every item it receives as input (turned off).

### Command[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#command)

Enter the command to execute on the host machine. Refer to sections below for examples of running [multiple commands](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#run-multiple-commands)
 and [cURL commands](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#run-curl-command)
.

#### Run multiple commands[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#run-multiple-commands)

Use one of two methods to run multiple commands in one Execute Command node:

*   Enter each command on one line separated by `&&`. For example, you can combine the change directory (cd) command with the list (ls) command using `&&`.
    
    Copy
    
        cd bin && ls
    
*   Enter each command on a separate line. For example, you can write the list (ls) command on a new line after the change directory (cd) command.
    
    Copy
    
        cd bin
        ls
    

#### Run cURL command[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#run-curl-command)

You can also use the [HTTP Request](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest)
 node to make a cURL request.

If you want to run the curl command in the Execute Command node, you will have to build a Docker image based on the existing n8n image. The default n8n Docker image uses Alpine Linux.

`**apk**` **isn't included in the n8n image**

The `apk` package manager was removed from the official n8n Docker image. To install a package like `curl`, you need to restore `apk` from a fresh Alpine base image first, as shown below.

1.  Create a file named `Dockerfile`.
    
2.  Add the below code snippet to the Dockerfile.
    

Copy

       FROM n8nio/n8n
       USER root
    
       # Restore the apk package manager (removed from the base image)
       COPY --from=alpine:3.22 /sbin/apk /sbin/apk
       COPY --from=alpine:3.22 /lib/apk /lib/apk
       COPY --from=alpine:3.22 /usr/lib/libapk* /usr/lib/
    
       RUN apk add --no-cache curl
       USER node

1.  In the same folder, execute the command below to build the Docker image.
    

Copy

       docker build -t n8n-curl .

1.  Replace the Docker image you used before. For example, replace `n8nio/n8n` with `n8n-curl`.
    
2.  Run the newly created Docker image. You'll now be able to execute curl using the Execute Command Node.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#templates-and-examples)

-----------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.executecommand integration templates](https://n8n.io/integrations/execute-command)
 or [search all templates](https://n8n.io/workflows/)

Common issues[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand#common-issues)

-----------------------------------------------------------------------------------------------------------------

For common questions or issues and suggested solutions, refer to [Common Issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues)
.

[PreviousEvaluation Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.evaluationtrigger)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues)

Last updated 10 days ago

Was this helpful?