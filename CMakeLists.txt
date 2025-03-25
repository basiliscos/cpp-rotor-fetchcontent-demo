cmake_minimum_required(VERSION 3.11)

project(rotor_fetchcontent_demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

set(FETCHCONTENT_QUIET OFF)

FetchContent_Declare(rotor
    URL https://github.com/basiliscos/cpp-rotor/archive/refs/tags/v0.34.tar.gz
    URL_HASH SHA256=8c59a36b3b2917c91650fb91e57f8e116e0dd7f88b70d95e2e92bde4f9395202
    LOG_DOWNLOAD FALSE
    LOG_CONFIGURE TRUE
    LOG_BUILD TRUE
    LOG_INSTALL TRUE
)
set(BUILD_THREAD  ON CACHE INTERNAL "")
set(BUILD_TESTING OFF CACHE INTERNAL "")

FetchContent_MakeAvailable(rotor)

add_executable(ping-pong-thread src/ping-pong-thread.cpp)
target_link_libraries(ping-pong-thread rotor::thread)
