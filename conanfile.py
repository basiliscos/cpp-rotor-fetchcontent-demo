from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout

class IoSentinelRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    default_options = {
        "*/*:shared": True,
        "boost/*:magic_autolink": False,
        "boost/*:visibility": "hidden",
        "boost/*:header_only": False,
        "boost/*:without_serialization": True,
        "boost/*:without_graph": True,
        "boost/*:without_fiber": True,
        "boost/*:without_log": True,
        "boost/*:without_math": True,
        "boost/*:without_process": True,
        "boost/*:without_stacktrace": True,
        "boost/*:without_test": True,
        "boost/*:without_wave": True,
        "rotor/*:enable_thread": True,
        "rotor/*:enable_asio": False,
        "rotor/*:enable_thread": True,
        "rotor/*:enable_fltk": False,
    }

    def requirements(self):
        self.requires("boost/1.86.0", headers=True, libs=True, transitive_libs=True, force=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        tc = CMakeDeps(self)
        tc.generate()
