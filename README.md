[![Build Status](https://travis-ci.org/lasote/conan-poco.svg?branch=master)](https://travis-ci.org/lasote/conan-poco)

# conan-poco

[Conan.io](https://conan.io) package for [POCO](http://pocoproject.org/) library

The packages generated with this **conanfile** can be found in [conan.io](https://conan.io/source/Poco/1.6.1/lasote/stable).

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

If your are in Windows you should run it from a VisualStudio console in order to get "mc.exe" in path.
    
## Upload packages to server

    $ conan upload Poco/1.6.1@lasote/stable --all
    
## Reuse the packages

### Basic setup

    $ conan install Poco/1.6.1@lasote/stable
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    Poco/1.6.1@lasote/stable

    [options]
    Poco:poco_static=True # False
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install . 

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

