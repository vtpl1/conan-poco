#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    if platform.system() == "Windows":
        builder.add(settings={"arch": "x86", "build_type": "Debug", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MTd"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Debug", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MTd"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MT"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 15, "compiler.runtime": "MT"},
                    options={}, env_vars={}, build_requires={})
    else:
        builder.add(settings={"arch": "x86", "build_type": "Debug"},
                    options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Debug"},
                    options={}, env_vars={}, build_requires={})
    #builder.add_common_builds(shared_option_name="Poco:shared", pure_c=False)
    builder.run()
