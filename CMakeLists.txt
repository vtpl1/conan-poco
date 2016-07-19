PROJECT(conanpoco)
cmake_minimum_required(VERSION 2.8)
include(${CMAKE_CURRENT_SOURCE_DIR}/../conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

if(ACTIVATE_CXX14)
    MESSAGE("Activating CXX_STANDARD 14")
    set(CMAKE_CXX_STANDARD 14)
else()
    MESSAGE("Not activating CXX_STANDARD 14")
endif()


include("CMakeListsOriginal.cmake")
