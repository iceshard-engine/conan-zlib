cmake_minimum_required(VERSION 2.8)
project(conanzlib)

message(STATUS "Conan CMake Wrapper")
include(conanbuildinfo.cmake)
conan_basic_setup()

include_directories(${CMAKE_SOURCE_DIR}/zlib-1.2.11)
add_subdirectory("zlib-1.2.11")
