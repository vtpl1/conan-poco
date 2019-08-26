#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    upload_remote = "https://api.bintray.com/conan/bincrafters/public-conan"
    builder = ConanMultiPackager(remotes=upload_remote)
    builder.add_common_builds(shared_option_name="Poco:shared", pure_c=False)
    builder.run()
