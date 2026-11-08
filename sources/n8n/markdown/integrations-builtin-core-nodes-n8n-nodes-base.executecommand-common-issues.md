For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md)
.

Here are some common errors and issues with the [Execute Command node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand)
 and steps to resolve or troubleshoot them.

Command failed: <command> /bin/sh: <command>: not found[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues#command-failed-andltcommandandgt-binsh-andltcommandandgt-not-found)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This error occurs when the shell environment can't find one of the commands in the **Command** parameter.

To fix this error, review the following:

*   Check that the command and its arguments don't have typos in the **Command** parameter.
    
*   Check that the command is in the `PATH` of the user running n8n.
    
*   If you are running n8n with Docker, check if the command is available within the container by trying to run it manually. If your command isn't included in the container, you might have to extend the official n8n image with a [custom image](https://docs.docker.com/build/building/base-images/)
     that includes your command.
    
    *   If n8n is already running:
        
        Copy
        
            # Find n8n's container ID, it will be the first column
            docker ps | grep n8n
            # Try to execute the command within the running container
            docker container exec <container_ID> <command_to_run>
        
    *   If n8n isn't running:
        
        Copy
        
            # Start up a new container that runs the command instead of n8n
            # Use the same image and tag that you use to run n8n normally
            docker run -it --rm --entrypoint /bin/sh n8nio/n8n -c <command_to_run>
        
    

Error: stdout maxBuffer length exceeded[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues#error-stdout-maxbuffer-length-exceeded)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This error happens when your command returns more output than the Execute Command node is able to process at one time.

To avoid this error, reduce output your command produces. Check your command's manual page or documentation to see if there are flags to limit or filter output. If not, you may need to pipe the output to another command to remove unneeded info.

PowerShell commands get truncated at line breaks[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues#powershell-commands-get-truncated-at-line-breaks)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

On Windows, the Execute Command node passes the **Command** parameter to the system shell as a single string. If your command contains line breaks, the shell only executes the first line and ignores the rest.

This is a Windows shell limitation. The underlying `cmd.exe` process treats each line break as the end of the command.

To fix this, write your PowerShell command on a single line. If the command is complex, join statements with semicolons:

Copy

    powershell -Command "Get-ChildItem C:\Data; Write-Output 'Done'"

For longer scripts, save the script to a file and run it with the `-File` flag instead:

Copy

    powershell -File C:\Scripts\my-script.ps1

[PreviousExecute Command](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executecommand)
[NextExecute Sub-workflow](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow)

Last updated 10 days ago

Was this helpful?