For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners.md)
.

[Task runners](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners)
 are responsible for executing code from the [Code node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.code)
. While Code node executions are secure, you can follow these recommendations to further harden your task runners.

Run task runners as sidecars in external mode[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#run-task-runners-as-sidecars-in-external-mode)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To increase the isolation between the core n8n process and code in the Code node, run task runners in [external mode](https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners#setting-up-external-mode)
. External task runners launch as separate containers, providing a fully isolated environment to execute the JavaScript defined in the Code node.

Use the distroless image[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#use-the-distroless-image)

------------------------------------------------------------------------------------------------------------------------------------

For a reduced attack surface, use the distroless Docker image variant. Distroless images contain only the application and its runtime dependencies, excluding package managers, shells, and other utilities that aren't needed at runtime.

To use the distroless image, append the `-distroless` suffix to the Docker tag. For example: `2.4.6-distroless`.

Run as the nobody user[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#run-as-the-nobody-user)

--------------------------------------------------------------------------------------------------------------------------------

For improved security, configure task runners to run as the unprivileged `nobody` user with user and group ID 65532. This prevents the container process from running with root privileges and limits potential damage from security vulnerabilities.

Configure read-only root filesystem[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#configure-read-only-root-filesystem)

----------------------------------------------------------------------------------------------------------------------------------------------------------

Configure a [read-only root filesystem](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
 to prevent any modifications to the container's filesystem at runtime. This helps protect against malicious code that might attempt to modify system files.

Task runners still require some temporary storage for operation. To accommodate this, mount a minimal `emptyDir` volume to `/tmp`. If your workflows require more temporary space, increase the size of the volume accordingly.

Configure an AppArmor profile[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#configure-an-apparmor-profile)

----------------------------------------------------------------------------------------------------------------------------------------------

As a defence-in-depth measure, apply an [AppArmor](https://apparmor.net/)
 profile to prevent the task runner container from reading sensitive `/proc` files such as `environ` and `mounts`. These files can expose environment variables, including secrets and credentials, to code running inside the container. Refer to the [Kubernetes AppArmor documentation](https://kubernetes.io/docs/tutorials/security/apparmor/)
 for how to apply a profile to a pod.

Add the following rule to your AppArmor profile:

Copy

    audit deny @{PROC}/[0-9]*/{environ,mounts} rwl,

This denies and logs any attempt to read, write, or link to per-process `environ` and `mounts` files.

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/harden-task-runners#related-resources)

----------------------------------------------------------------------------------------------------------------------

*   [Security](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security)
    

[PreviousBlock specific nodes](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes)
[NextVerify user emails](https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails)

Last updated 10 days ago

Was this helpful?