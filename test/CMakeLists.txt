PROJECT(MyHello)
cmake_minimum_required(VERSION 3.0)

include(conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(echo EchoServer.cpp)
TARGET_LINK_LIBRARIES(echo ${CONAN_LIBS})

ADD_EXECUTABLE(md5 md5.cpp)
TARGET_LINK_LIBRARIES(md5 ${CONAN_LIBS})

ADD_EXECUTABLE(sample SampleApp.cpp)
TARGET_LINK_LIBRARIES(sample ${CONAN_LIBS})
