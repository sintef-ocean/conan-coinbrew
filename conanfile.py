from conans import ConanFile, tools
import os


class CoinbrewConan(ConanFile):
    name = "coinbrew"
    version = "2021.01"
    license = "Undefined"
    author = "SINTEF Ocean"
    url = "https://github.com/sintef-ocean/conan-coinbrew"
    homepage = "https://github.com/coin-or/coinbrew"
    description = "Package manager: fetch, build, and install COIN-OR projects"
    topics = ("COIN-OR", "coinbrew")
    no_copy_source = True

    def source(self):

        _git = tools.Git()
        _git.clone("https://github.com/coin-or/coinbrew",
                   branch="e3dbb3fe3d27f8dff3d734c91b28ddc17e07625c",
                   shallow=True)

        os.chmod(os.path.join(self.source_folder, "coinbrew"), 0o755)

    def build(self):
        pass

    def package(self):
        self.copy('*coinbrew', dst="bin")

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        self.info.header_only()

    def system_requirements(self):
        pass

        # These are the tools
        #tools.which("make")
        #tools.which("git")
        #tools.which("tar")
        #tools.which("patch")
        #tools.which("dos2unix")
        #tools.which("pkg-config")

        # Turn into requires!
