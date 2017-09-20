from conans import ConanFile
from conans import CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "conan"
default_channel = "testing"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    requires = "Poco/1.7.9@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.dylib", dst="bin", src="lib")

    def test(self):
        self.run("cd bin && .%ssample" % os.sep)
        self.run("cd bin && .%ssocket" % os.sep)
        assert os.path.exists(os.path.join(self.deps_cpp_info["Poco"].rootpath, "LICENSE"))
