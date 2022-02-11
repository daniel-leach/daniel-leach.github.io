cmake_policy( SET CMP0048 NEW )
set(CMAKE_CXX_COMPILER clang++)

project( dleach-path VERSION 0.0.0 LANGUAGES CXX )
cmake_minimum_required( VERSION 3.0 )

# add compile flags here

add_subdirectory( src )