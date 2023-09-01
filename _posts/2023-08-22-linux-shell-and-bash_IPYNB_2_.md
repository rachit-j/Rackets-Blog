---
comments: True
layout: post
title: Linux Shell and Bash
description: The complete Hack of the section Linux Shell and Bash. This page is also saved in a jupyter notebook.
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1}, 'csa': {'week': 0}, 'labnotebook': {'week': 1}}
categories: ['C4.1']
---

### Hack #1: Tool Script
This is the script I have created that will check if all the prerequisites from the [Tools and Equipment Overview](https://nighthawkcoders.github.io/teacher//c4.3/c5.0/2023/08/16/Tools_Equipment.html) have been fullfilled for a MacOS System.


```bash
%%bash
echo "Starting the Tools and Equipment Overview Confirmation Script..."

echo "Checking Homebrew..."
if which brew | grep -q "not found"; then
    echo "Homebrew not installed! Install Homebrew to complete the script!"
    exit 1
else
    echo "Homebrew installed!"
fi

echo "Checking GitHub..."
if ls /usr/bin | grep -q git; then
    echo "Git installed on Host"
else
    echo "Git not installed on Host!"
fi

echo "Checking VSCode..."
if ls /Applications/ | grep -q "Visual Studio Code"; then
    echo "Visual Studio Code installed on Host"
else
    echo Visual Studio Code not installed on Host!
fi

echo "Checking Jupyter Notebook..."
if brew list | grep -q "jupyterlab"; then
    echo "Jupyter Notebook installed on Host"
else
    echo "Jupyter Notebook not installed on Host!"
fi

echo "Checking Slack..."
if ls /Applications/ | grep -q "Slack"; then
    echo "Slack installed on Host"
else
    echo Slack not installed on Host!
fi

echo "Checking Docker..."
if ls /Applications/ | grep -q "Docker"; then
    echo "Docker installed on Host"
else
    echo Docker not installed on Host!
fi

echo "Checks complete!"
exit 0
```

    Starting the Tools and Equipment Overview Confirmation Script...
    Checking Homebrew...
    Homebrew installed!
    Checking GitHub...
    Git installed on Host
    Checking VSCode...
    Visual Studio Code installed on Host
    Checking Jupyter Notebook...
    Jupyter Notebook not installed on Host!
    Checking Slack...
    Slack installed on Host
    Checking Docker...
    Docker installed on Host
    Checks complete!


### Linux Commands
Here is my blog of [Common Linux Commands](https://rachit-j.github.io/Rackets-Blog/c1.4/2023/08/21/Terminal_Commands.html)

### How do we confirm packages

If we are doing a package manager install, ususally you can write list commands for all types of systems. For example, on Ubuntu, you can write


```bash
%%bash
dpkg -l | less
```

    bash: line 1: dpkg: command not found


And on Mac with Homebrew, you can write


```bash
%%bash
brew list | less
```

    autoconf
    automake
    bison
    black
    brotli
    c-ares
    ca-certificates
    cairo
    cffi
    chruby
    fontconfig
    freetype
    gdbm
    gettext
    giflib
    git
    glib
    gradle
    graphite2
    harfbuzz
    icu4c
    ipython
    jpeg-turbo
    libffi
    libidn2
    libnghttp2
    libpng
    libsodium
    libtiff
    libunistring
    libuv
    libx11
    libxau
    libxcb
    libxdmcp
    libxext
    libxrender
    libyaml
    little-cms2
    lz4
    lzo
    m4
    md5sha1sum
    mpdecimal
    mypy
    node
    openjdk
    openssl@1.1
    openssl@3
    pandoc
    pcre2
    pixman
    pkg-config
    pycodestyle
    pycparser
    pydocstyle
    pygments
    python-certifi
    python-lsp-server
    python@3.11
    pyyaml
    readline
    ruby-install
    six
    sqlite
    wget
    xorgproto
    xz
    zeromq
    zstd


Usually, with most packages, you can do the following to get the version.

```bash
[package name/command] -v
[package name/command] --version
```

If you want more information, a lot of packages have the following features.

```bash
[package name/command] -h # Package manual
[package name/command] --help # Package manual
man [command] # Linux manual for the command of the package
```

If you are installing packages from an outside source, make sure the package comes from the official company website and scan the installer with an antivirus.

If you are concerned that the download is corrupted while it was transferred, then you can get a checksum from the website and calculate the checksum on your computer. For example, if you have an md5 checksum of a .gif file, you can run the following command:

```bash
rachitjaiswal@Rachits-MBP# md5sum Desktop/yomp.gif
bc75b5ce8a75c1f4c7ed1e51b113353b  Desktop/yomp.gif
rachitjaiswal@Rachits-MBP#
```

This can be verified if you download the gif and check for yourself. Even if the .gif is on a completely different architecture, the file will still have the same md5 sum, and if it is tampered with or malformed, the sum will change. Using something like this on an .exe or a .pkg file ensures that the package is valid and that it comes from the source, without being tampered or malformed.

### Updating a Repository with the command line
To update a git repository with your command line, you must follow the steps below.

```bash
# 1. Open a terminal and navigate to the directory of your github repository on your localhost
# 2. Use the following command to add a repository.

git add .

# 3. To verify the status of the repository, run the following command

git status

# 4. To commit after making a change, type in the following command

git commit -m 'your message here'

# 5. To push, type in the following command

git push
```
