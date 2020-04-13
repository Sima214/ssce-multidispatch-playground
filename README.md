# Multi-Dispatch Playground

Finding the best(in terms of execution speed) method to implement multi-dispatch for each platform.

## Status

|               |          Linux         |  Windows  |  MacOS  |
|--------------:|:----------------------:|:---------:|:-------:|
| gcc i386      |                        |           |   N/S   |
| clang i386    |                        |           |   N/S   |
| gcc amd64     |[![Gitlab CI Status]][2]|           |   N/S   |
| clang amd64   |[![Gitlab CI Status]][2]|[![Windows Clang amd64 build status]][3]|[![MacOS Clang amd64 build status]][1]|
| gcc AArch64   |                        |           |   N/S   |
| clang AArch64 |                        |           |         |

\* N/S: Not Supported

[1]: https://travis-ci.org/Sima214/ssce_multidispatch_playground
[2]: https://gitlab.com/Sima214/ssce_multidispatch_playground/-/commits/master
[3]: https://ci.appveyor.com/project/Sima214/ssce-multidispatch-playground

[MacOS Clang amd64 build status]: https://travis-ci.org/Sima214/ssce_multidispatch_playground.svg?branch=master
[Gitlab CI Status]: https://gitlab.com/Sima214/ssce_multidispatch_playground/badges/master/pipeline.svg
[Windows Clang amd64 build status]: https://ci.appveyor.com/api/projects/status/

## Building

### Linux

First you need to install using your distribution's package manager:

1. A compiler (gcc or clang)
1. git python3 ninja meson

Then to first setup the build, inside a terminal you should run the following commands:

- `cd \<Root of project\>`
- `mkdir build`
- `meson setup build`

To compile run the following from the terminal while inside the root folder of the project:

- `ninja -C build`

And to also run the tests:

- `ninja -C build test`

### Windows

The Windows build depends on a number of things to be installed and accessible on the system:

1. Visual Studio 2019 (only the MSVC command line build system is required).
1. Python3, ninja, llvm, meson and optionally git.

Visual Studio 2017 should also be supported, but the [llvm toolset extension for visual studio](https://marketplace.visualstudio.com/items?itemName=LLVMExtensions.llvm-toolchain) is needed.

**Important notes**:

1. The clang/llvm compiler provided by the Visual Studio installation (clang/c2) is not supported.
1. The Visual Studio Compiler is NOT supported.

If you have [chocolatey](https://chocolatey.org) installed, then you can install the required components on an administrative command line with:

- `choco install visualstudio2019buildtools python3 ninja git`
- `python -m pip install meson`

Now open the Visual Studio **x64** command line from the start menu. This sets the environment variables to the correct paths for using MSBuild and Windows SDK.

Next you should check if you have everything installed correctly and the path variable updated by:

- `python --version`
- `ninja --version`
- `meson --version`
- `clang --version`

To actually configure the build, you must first be inside the root folder of the project in the Visual Studio Command Line and then run:

- `set CC=clang-cl`
- `set CXX=clang-cl`
- `mkdir build`
- `meson setup build`

Compile with:

- `ninja -C build`

Run tests with:

- `ninja -C build test`

### MacOS

I don't own an Apple computer, but from what I can gather the steps should be as follows:

1. Install xcode.
1. Install homebrew.
1. Install python3 and ninja using homebrew.
1. Install meson using pip.
1. Follow the [linux](#Linux) steps.
