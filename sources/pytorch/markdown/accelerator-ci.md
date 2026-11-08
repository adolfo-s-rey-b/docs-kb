Opens in a new window Opens an external website Opens an external website in a new window

Close this dialog

This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. To learn more, view the following link: [Privacy Policy](https://lfprojects.org/policies/privacy-policy/)

Manage Preferences

Close Cookie Preferences

[Skip to main content](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#main-content)

Back to top  

 Ctrl+K

v2.15.0 (stable)

[v2.16.0 (unstable)](https://docs.pytorch.org/docs/main/accelerator/ci.html)
[v2.15.0 (stable)](https://docs.pytorch.org/docs/2.15/accelerator/ci.html)
[v2.14.0](https://docs.pytorch.org/docs/2.14/accelerator/ci.html)
[v2.13.0](https://docs.pytorch.org/docs/2.13/accelerator/ci.html)
[v2.12.0](https://docs.pytorch.org/docs/2.12/accelerator/ci.html)
[v2.11.0](https://docs.pytorch.org/docs/2.11/accelerator/ci.html)
[v2.10.0](https://docs.pytorch.org/docs/2.10/accelerator/ci.html)
[v2.9.1](https://docs.pytorch.org/docs/2.9/accelerator/ci.html)
[v2.8.0](https://docs.pytorch.org/docs/2.8/accelerator/ci.html)
[v2.7.0](https://docs.pytorch.org/docs/2.7/accelerator/ci.html)
[v2.6.0](https://docs.pytorch.org/docs/2.6/accelerator/ci.html)
[v2.5.0](https://docs.pytorch.org/docs/2.5/accelerator/ci.html)
[v2.4.0](https://docs.pytorch.org/docs/2.4/accelerator/ci.html)
[v2.3.0](https://docs.pytorch.org/docs/2.3/accelerator/ci.html)
[v2.2.0](https://docs.pytorch.org/docs/2.2/accelerator/ci.html)
[v2.1.0](https://docs.pytorch.org/docs/2.1/accelerator/ci.html)
[v2.0.0](https://docs.pytorch.org/docs/2.0/accelerator/ci.html)
[v1.13](https://docs.pytorch.org/docs/1.13/accelerator/ci.html)
[v1.12](https://docs.pytorch.org/docs/1.12/accelerator/ci.html)
[v1.11](https://docs.pytorch.org/docs/1.11/accelerator/ci.html)
[v1.10](https://docs.pytorch.org/docs/1.10/accelerator/ci.html)
[v1.9.1](https://docs.pytorch.org/docs/1.9.1/accelerator/ci.html)
[v1.9.0](https://docs.pytorch.org/docs/1.9.0/accelerator/ci.html)
[v1.8.1](https://docs.pytorch.org/docs/1.8.1/accelerator/ci.html)
[v1.8.0](https://docs.pytorch.org/docs/1.8.0/accelerator/ci.html)
[v1.7.1](https://docs.pytorch.org/docs/1.7.1/accelerator/ci.html)
[v1.7.0](https://docs.pytorch.org/docs/1.7.0/accelerator/ci.html)
[v1.6.0](https://docs.pytorch.org/docs/1.6.0/accelerator/ci.html)
[v1.5.1](https://docs.pytorch.org/docs/1.5.1/accelerator/ci.html)
[v1.5.0](https://docs.pytorch.org/docs/1.5.0/accelerator/ci.html)
[v1.4.0](https://docs.pytorch.org/docs/1.4.0/accelerator/ci.html)
[v1.3.1](https://docs.pytorch.org/docs/1.3.1/accelerator/ci.html)
[v1.3.0](https://docs.pytorch.org/docs/1.3.0/accelerator/ci.html)
[v1.2.0](https://docs.pytorch.org/docs/1.2.0/accelerator/ci.html)
[v1.1.0](https://docs.pytorch.org/docs/1.1.0/accelerator/ci.html)
[v1.0.1](https://docs.pytorch.org/docs/1.0.1/accelerator/ci.html)
[v1.0.0](https://docs.pytorch.org/docs/1.0.0/accelerator/ci.html)
[v0.4.1](https://docs.pytorch.org/docs/0.4.1/accelerator/ci.html)
[v0.4.0](https://docs.pytorch.org/docs/0.4.0/accelerator/ci.html)
[v0.3.1](https://docs.pytorch.org/docs/0.3.1/accelerator/ci.html)
[v0.3.0](https://docs.pytorch.org/docs/0.3.0/accelerator/ci.html)
[v0.2.0](https://docs.pytorch.org/docs/0.2.0/accelerator/ci.html)
[v0.1.12](https://docs.pytorch.org/docs/0.1.12/accelerator/ci.html)

[Go to pytorch.org](https://pytorch.org/)

 Ctrl+K

|     |     |
| --- | --- |
|     | [×](javascript:void(0) "Clear search box") |

search

Custom Search

|     |     |
| --- | --- |
|     | Sort by<br><br>Relevance<br><br>Date |

*   [X](https://x.com/PyTorch)
    
*   [GitHub](https://github.com/pytorch/pytorch)
    
*   [PyTorch Forum](https://discuss.pytorch.org/)
    
*   [PyPi](https://pypi.org/project/torch/)
    

Rate this Page

★ ★ ★ ★ ★

CI Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#ci-integration "Link to this heading")

================================================================================================================

Created On: Apr 22, 2026 | Last Updated On: May 21, 2026

Background[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#background "Link to this heading")

--------------------------------------------------------------------------------------------------------

Out-of-tree (OOT) accelerator backends need to maintain compatibility with PyTorch’s evolving codebase. As PyTorch continues to develop rapidly, changes in the upstream repository can potentially break downstream accelerator integrations. To address this challenge, PyTorch provides a Cross-Repository CI Relay (CRCR) mechanism that enables automatic CI coordination between the PyTorch repository and downstream accelerator repositories.

This chapter guides third-party accelerator vendors through the process of integrating their repositories with PyTorch’s CI ecosystem, ensuring continuous compatibility validation.

Why CI Integration Matters[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#why-ci-integration-matters "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Integrating with PyTorch’s CI ecosystem provides several key benefits:

*   **Early Detection**: Catch compatibility issues before they reach production, reducing debugging effort and user impact.
    
*   **Automated Validation**: Automatically test your accelerator against PyTorch PRs without manual intervention.
    
*   **Reduced Maintenance Burden**: Proactive testing reduces the need for reactive fixes when compatibility breaks.
    

How It Works[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#how-it-works "Link to this heading")

------------------------------------------------------------------------------------------------------------

The CRCR system consists of four components: a **GitHub App** that bridges authentication and events, the **PyTorch repository** as the upstream event source, a **Relay Server** that dispatches events to eligible downstream repos, and **downstream repositories** that receive events and optionally report results back.

When a PR is opened or updated in PyTorch, GitHub notifies the Relay Server via the GitHub App. The Relay Server verifies the event, reads the allowlist, and dispatches a `repository_dispatch` event to each registered downstream repository. Downstream repos can optionally report CI results back to the Relay Server, which surfaces them in the PyTorch HUD or as PR check runs.

Participation is governed by a four-tier allowlist:

*   **L1**: Events are forwarded to the downstream repo; no results are reported upstream.
    
*   **L2**: Results are displayed on dedicated HUD pages for the downstream repo.
    
*   **L3**: Non-blocking check runs appear on PyTorch PRs, triggered by maintainer labels.
    
*   **L4**: Blocking check runs run on all PyTorch PRs (reserved for critical accelerators).
    

Downstream repos advance through levels by meeting documented requirements around hardware verification, CI reliability, and success rates.

For a deeper dive into the architecture and design decisions, see the [RFC-0050: Cross-Repository CI Relay for PyTorch Out-of-Tree Backends](https://github.com/fffrog/rfcs/blob/5e138470e962b0f9c5092e564f35bd7fb13b0b2f/RFC-0050-Cross-Repository-CI-Relay-for-PyTorch-Out-of-Tree-Backends.md)
.

Note

The CRCR currently supports **L1 (Silent)** integration only.

Integration Steps[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#integration-steps "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

### Step 1: Install the GitHub App[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#step-1-install-the-github-app "Link to this heading")

Install the [PyTorch Cross-Repo CI Relay](https://github.com/apps/pytorch-fdn-cross-repo-ci-relay)
 GitHub App on your repository by clicking the **Configure** button and selecting your repository.

### Step 2: Add Your Repository to the Allowlist[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#step-2-add-your-repository-to-the-allowlist "Link to this heading")

Submit a pull request to `pytorch/pytorch` adding your repository to `.github/allowlist.yml` under the `L1` key:

L1:
  \- your-org/your-accelerator

Copy to clipboard

See [#180352](https://github.com/pytorch/pytorch/pull/180352)
 for a reference example. The PyTorch team will review and merge the PR to complete the onboarding.

### Step 3: Create the Workflow File[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#step-3-create-the-workflow-file "Link to this heading")

Create a GitHub Actions workflow in your repository to receive `repository_dispatch` events:

.github/workflows/pytorch\_ci.yml[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#id1 "Link to this code")

name: PyTorch CI

run-name: \>-
  PyTorch CI -
  ${{
    github.event.client\_payload.event\_type == 'pull\_request' &&
    format('PR #{0} ({1})',
      github.event.client\_payload.payload.pull\_request.number,
      github.event.client\_payload.payload.action) ||
    format('Push {0}', github.event.client\_payload.payload.after)
  }}

on:
  repository\_dispatch:
    types: \[pull\_request, push\]

concurrency:
  group: \>-
    pytorch-ci-${{ github.event.client\_payload.payload.repository.full\_name }}-${{
    github.event.client\_payload.payload.pull\_request.number || github.run\_id }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  cancel-workflow:
    if: ${{ github.event.client\_payload.payload.action == 'closed' }}
    runs-on: ubuntu-latest
    steps:
      \- run: echo "PR closed, canceling in-progress runs"

  ci:
    if: ${{ github.event.client\_payload.payload.action != 'closed' }}
    runs-on: ubuntu-latest
    steps:
      \- name: Checkout downstream repo
        uses: actions/checkout@v4

      \- name: Checkout PyTorch at triggered commit
        uses: actions/checkout@v4
        with:
          repository: pytorch/pytorch
          ref: \>-
            ${{ github.event.client\_payload.event\_type == 'pull\_request' &&
            github.event.client\_payload.payload.pull\_request.head.sha ||
            github.event.client\_payload.payload.after }}
          path: pytorch

      \- name: Build and test
        run: |
          \# Your build and test commands
          echo "Running tests against PyTorch..."

Copy to clipboard

### Step 4: Test the Integration[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#step-4-test-the-integration "Link to this heading")

Verify your integration works correctly:

1.  Create a test PR in PyTorch (or ask maintainers to trigger a test dispatch)
    
2.  Confirm your workflow triggers correctly
    

Event Payload[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#event-payload "Link to this heading")

--------------------------------------------------------------------------------------------------------------

The CRCR relay is a stateless pass-through: it forwards the complete GitHub webhook payload as `client_payload` in the `repository_dispatch` event. There is no simplified intermediary schema.

The `client_payload` has two top-level fields:

*   `event_type`: either `pull_request` or `push`
    
*   `payload`: the raw GitHub webhook payload for that event type
    

Commonly used fields:

github.event.client\_payload.event\_type                       \# "pull\_request" or "push"
github.event.client\_payload.payload.action                   \# "opened", "synchronize", "reopened" or "closed" only
github.event.client\_payload.payload.pull\_request.number      \# PR number (pull\_request events only)
github.event.client\_payload.payload.pull\_request.head.sha    \# Head commit SHA to checkout
github.event.client\_payload.payload.after                    \# Commit SHA (push events only)

Copy to clipboard

Supported `action` values for `pull_request` events:

| Action | Description |
| --- | --- |
| `opened` | New PR created |
| `synchronized` | New commits pushed to an existing PR |
| `reopened` | Previously closed PR reopened |
| `closed` | PR closed or merged; triggers the `cancel-workflow` job to stop in-progress runs |

Troubleshooting[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#troubleshooting "Link to this heading")

------------------------------------------------------------------------------------------------------------------

### Workflow Not Triggering[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#workflow-not-triggering "Link to this heading")

1.  Confirm your onboarding with the PyTorch team is complete
    
2.  Check that your workflow file is on the default branch
    
3.  Ensure the `repository_dispatch` event type in your workflow matches what the relay sends
    

Resources[#](https://docs.pytorch.org/docs/2.15/accelerator/ci.html#resources "Link to this heading")

------------------------------------------------------------------------------------------------------

*   [RFC-0050: Cross-Repository CI Relay for PyTorch Out-of-Tree Backends](https://github.com/pytorch/rfcs/blob/master/RFC-0050-Cross-Repository-CI-Relay-for-PyTorch-Out-of-Tree-Backends.md)
    

On this page

[Edit on GitHub](https://github.com/pytorch/pytorch/edit/main/docs/source/accelerator/ci.md)

[Show Source](https://docs.pytorch.org/docs/2.15/_sources/accelerator/ci.md.txt)

PyTorch Libraries

*   [ExecuTorch](https://docs.pytorch.org/executorch)
    
*   [Helion](https://docs.pytorch.org/helion)
    
*   [torchao](https://docs.pytorch.org/ao)
    
*   [kineto](https://github.com/pytorch/kineto)
    
*   [torchtitan](https://github.com/pytorch/torchtitan)
    
*   [TorchRL](https://docs.pytorch.org/rl)
    
*   [torchvision](https://docs.pytorch.org/vision)
    
*   [torchaudio](https://docs.pytorch.org/audio)
    
*   [tensordict](https://docs.pytorch.org/tensordict)
    
*   [PyTorch on XLA Devices](https://docs.pytorch.org/xla)
    

Docs
----

Access comprehensive developer documentation for PyTorch

[View Docs](https://docs.pytorch.org/docs/stable/index.html)

Tutorials
---------

Get in-depth tutorials for beginners and advanced developers

[View Tutorials](https://docs.pytorch.org/tutorials)

Resources
---------

Find development resources and get your questions answered

[View Resources](https://pytorch.org/resources)

To analyze traffic and optimize your experience, we serve cookies on this site. By clicking or navigating, you agree to allow our usage of cookies. As the current maintainers of this site, Facebook’s Cookies Policy applies. Learn more, including about available controls: [Cookies Policy](https://opensource.fb.com/legal/cookie-policy)
.

|     |     |
| --- | --- |
|     |     |

|     |     |
| --- | --- |
|     |     |