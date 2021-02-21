[![GCC Conan](https://github.com/sintef-ocean/conan-coinbrew/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-coinbrew/actions?query=workflow%3A"GCC+Conan")
[![Download](https://api.bintray.com/packages/sintef-ocean/conan/coinbrew%3Asintef/images/download.svg)](https://bintray.com/sintef-ocean/conan/coinbrew%3Asintef/_latestVersion)


[Conan.io](https://conan.io) recipe for [coinbrew](http://github.com/coin-or/coinbrew).

The recipe installs `coinbrew` and makes it available on path. It can be found at [Bintray](https://bintray.com/sintef-ocean/conan/coinbrew%3Asintef).
The package is usually consumed using the `conan install` command or a *conanfile.txt*.
For details on installing necessary system requirements for `coinbrew`, please consult [coinbrew documentation](https://coin-or.github.io/coinbrew).

## How to use this package

1. Add remote to conan's package [remotes](https://docs.conan.io/en/latest/reference/commands/misc/remote.html?highlight=remotes):

   ```bash
   $ conan remote add sintef https://api.bintray.com/conan/sintef-ocean/conan
   ```

2. Using *conanfile.txt* in your project with *cmake*

   Add a [*conanfile.txt*](http://docs.conan.io/en/latest/reference/conanfile_txt.html) to your project. This file describes dependencies and your configuration of choice, e.g.:

   ```
   [requires]
   coinbrew/[>=2021.01]@sintef/stable

   [options]


   [imports]
   licenses, * -> ./licenses @ folder=True

   [generators]
   virtualenv
   ```

   Then, do
   ```bash
   $ . activate.sh
   $ coinbrew --help
   ```

   Typically, `coinbrew` is used as a build requirement in a conan recipe to help build
   libraries supported by the `coinbrew` package manager.

## Known recipe issues

   This recipe does not install the necessary requirements in order for coinbrew to run successfully.
