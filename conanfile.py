from conans import ConanFile, tools
import os

class IceShardConanRecipe(ConanFile):
    name = "<name>"
    license = "..."
    description = "..."
    url = "..."

    # Settings and options
    settings = "os", "compiler", "arch", "build_type"

    options = { }
    default_options = { }

    source_dir = "{name}-{version}"

    # Iceshard conan tools
    python_requires = "conan-iceshard-tools/0.8.0@iceshard/stable"
    python_requires_extend = "conan-iceshard-tools.IceTools"

    # Initialize the package
    def init(self):
        self.ice_init("none")

    def ice_build(self):
      pass

    def ice_package(self):
      pass

    def package_info(self):
      pass
