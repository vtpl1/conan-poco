[![Build Status](https://travis-ci.org/pocoproject/conan-poco.svg?branch=master)](https://travis-ci.org/pocoproject/conan-poco)

# conan-poco

[Conan.io](https://conan.io) package for [POCO](http://pocoproject.org/) library

The packages generated with this **conanfile** can be found on [bintray](https://bintray.com/pocoproject/conan/Poco%3Apocoproject).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.

## Upload packages to server

    $ conan upload Poco/1.7.9@lasote/stable --all

## Reuse the packages

### Basic setup

    $ conan install Poco/1.7.9@lasote/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Poco/1.7.9@lasote/stable

    [options]
    Poco:shared=True # False

    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

