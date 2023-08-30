---
comments: True
layout: post
title: Student GitHub Pages
description: A key to development in this class is the association VSCode to a GitHub pages project.  This is where students update assignments and present work.
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1}, 'csa': {'week': 0}}
categories: ['C4.1']
---

## Create your own GitHub Pages Project
> Make you own project from GitHub Pages Student Repo.

## Fork a GitHub Pages Repository
> Goto GitHub [student](https://github.com/nighthawkcoders/student) and run Fork.

- Reference: [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

## Start the GitHub Pages Student Project
> Run the following commands using terminal on you machine.  Be sure Repo has been forked.

- Clone and Open project in VSCode
- Change "forkme" text with your "ghid" or selected location


```bash
(base) id:~$ mkdir -p vscode # make a vscode directory
(base) id:~$ cd vscode # change to the directory
(base) id:~$ git clone https://github.com/forkme/student.git # change to your repo
(base) id:~$ cd  student  # change to the project directory
(base) id:~$ code . # open VSCode in project directory
```

### VSCode for Python Extensions
- VSCode [Language extensions](https://code.visualstudio.com/docs/languages/overview)
    - Install Python, Python Environment Manager, Python Extension Pack, Pylance
    - Install Jupyter, Jupyter Keymap
    - Install IntelliCode, IntelliCode API Usage Examples
    - Windows machines install WSL Remote Development


```python
%%HTML

<!-- Here is a little preview of HTML to Describe VSCode Marketplace -->

<div>
    <div style="float: left; margin: 0px 10px 10px 0px;">
        <a href="https://marketplace.visualstudio.com/vscode">
            <img alt="Extensions" src="{{site.baseurl}}/images/extensions.png" title="VS Code Marketplace" width="250">
        </a>
    </div>
    <div>
        <hr>
        <p>
        Visual Studio Code claims to provide just the tools a developer needs for a quick code-build-debug and version control cycle.  It provides a Market Place for enhancements and more complex workflows.  <mark>Before adding extensions, clone projects</mark> and see what is requested or added.  Here are some extension that were added through that process or that I have added...
        </p>
        <ul>
            <li>
                <mark>In marketplace</mark> there are several extensions for Python, Python Intellisense, Python Extension Pack
            </li>
            <li>
                <mark>Jupyter</mark>: This supports build jupyter ipynb files from within VS Code
            </li>
            <li>
                <mark>Code Spell Checker</mark>: Got to have it when building documents, particularly if you spell and typo like the Teacher
            </li>
            <li>
                <mark>IntelliCode</mark>: Got to have it when creating a code file, it will sense type of code by extension.  Also, it help with syntax as you are coding.
            </li>
        </ul>
        <p>
        <mark>Review Details in Marketplace for better explanation of purpose of the things explained above</mark>. There is a lot more!  As you need Git help look at things like <mark>Git History and GitLens</mark>.  Or, perhaps you enjoy Vim and want Vim emulation for editing, their is an extension for that.  Later, there may be interest in AWS Toolkit or Deploy extensions.  We will learn more about Marketplace Extensions as we do more.
        </p>
        <hr>
    </div>
</div>
```



<!-- Here is a little preview of HTML to Describe VSCode Marketplace -->

<div>
    <div style="float: left; margin: 0px 10px 10px 0px;">
        <a href="https://marketplace.visualstudio.com/vscode">
            <img alt="Extensions" src="{{site.baseurl}}/images/extensions.png" title="VS Code Marketplace" width="250">
        </a>
    </div>
    <div>
        <hr>
        <p>
        Visual Studio Code claims to provide just the tools a developer needs for a quick code-build-debug and version control cycle.  It provides a Market Place for enhancements and more complex workflows.  <mark>Before adding extensions, clone projects</mark> and see what is requested or added.  Here are some extension that were added through that process or that I have added...
        </p>
        <ul>
            <li>
                <mark>In marketplace</mark> there are several extensions for Python, Python Intellisense, Python Extension Pack
            </li>
            <li>
                <mark>Jupyter</mark>: This supports build jupyter ipynb files from within VS Code
            </li>
            <li>
                <mark>Code Spell Checker</mark>: Got to have it when building documents, particularly if you spell and typo like the Teacher
            </li>
            <li>
                <mark>IntelliCode</mark>: Got to have it when creating a code file, it will sense type of code by extension.  Also, it help with syntax as you are coding.
            </li>
        </ul>
        <p>
        <mark>Review Details in Marketplace for better explanation of purpose of the things explained above</mark>. There is a lot more!  As you need Git help look at things like <mark>Git History and GitLens</mark>.  Or, perhaps you enjoy Vim and want Vim emulation for editing, their is an extension for that.  Later, there may be interest in AWS Toolkit or Deploy extensions.  We will learn more about Marketplace Extensions as we do more.
        </p>
        <hr>
    </div>
</div>



## Hacks
> Setup Tools and test GitHub connection. Tool and Equipment setup is like attendance, without Tools and Equipment you are effectually absent.
- Change index.md to show it is REALLY YOURS.  Refer to [Markdown Cheet Sheet](https://www.markdownguide.org/cheat-sheet/).
    - Push a minor "index.md" change and Verify on GitHub [https://code.visualstudio.com/docs/editor/versioncontrol#_git-support](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support)
    - Verify "index.md" change on deployed GitHub Pages


