import os
import shutil
import platform
import hashlib


def test(arguments):
    command = "/usr/bin/conan test %s" % arguments
    retcode = os.system(command)
    if retcode != 0:
        exit("Error while executing:\n\t %s" % command)

if __name__ == "__main__":
    os.system('conan export lasote/stable')

    if platform.system() == "Windows":
        # x86_64, static
        compiler = '-s compiler="Visual Studio" -s compiler.version=12 '
        test(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MDd -o Poco:poco_static=True')
        test(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MTd -o Poco:poco_static=True')

        test(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MD -o Poco:poco_static=True')
        test(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MT -o Poco:poco_static=True')

        # x86_64, shared
        test(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MDd -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 
        
        test(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MD -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

        # x86, static
        test(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MDd -o Poco:poco_static=True')
        test(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MTd -o Poco:poco_static=True')

        test(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MD -o Poco:poco_static=True')
        test(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MT -o Poco:poco_static=True')

        # x86, shared
        test(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MDd -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

        test(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MD -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

    else:  # Compiler and version not specified, please set it in your home/.conan/conan.conf (Valid for Macos and Linux)
        # x86_64 debug
        test('-s build_type=Debug -s arch=x86_64 -o Poco:poco_static=True')
        test('-s build_type=Debug -s arch=x86_64 -o Poco:poco_static=False')

        # x86_64 release
        test('-s build_type=Release -s arch=x86_64 -o Poco:poco_static=True')
        test('-s build_type=Release -s arch=x86_64 -o Poco:poco_static=False')

        # x86 debug
        test('-s build_type=Debug -s arch=x86 -o Poco:poco_static=True')
        test('-s build_type=Debug -s arch=x86 -o Poco:poco_static=False')

        # x86 release
        test('-s build_type=Release -s arch=x86 -o Poco:poco_static=True')
        test('-s build_type=Release -s arch=x86 -o Poco:poco_static=False')
