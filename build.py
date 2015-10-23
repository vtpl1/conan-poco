import os
import shutil
import platform
import hashlib


def system(command):
    retcode = os.system(command)
    if retcode != 0:
        raise Exception("Error while executing:\n\t %s" % command)


def build_run_example(settings):
    current_dir = os.getcwd()
    sha = hashlib.sha1(settings).hexdigest()
    build_folder = os.path.join(current_dir, "conan_tmp", sha)
    shutil.copytree("test", build_folder)
    try:
        os.chdir(build_folder)
        system('conan install %s' % (settings))
        system('conan build')
        system("cd bin && .%ssample" % (os.sep))
    finally:
        os.chdir(current_dir)


if __name__ == "__main__":
    system('conan export lasote/stable')

    shutil.rmtree("conan_tmp", ignore_errors=True)
    if platform.system() == "Windows":
        # x86_64, static
        compiler = '-s compiler="Visual Studio" -s compiler.version=12 '
        build_run_example(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MDd -o Poco:poco_static=True')
        build_run_example(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MTd -o Poco:poco_static=True')

        build_run_example(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MD -o Poco:poco_static=True')
        build_run_example(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MT -o Poco:poco_static=True')

        # x86_64, shared
        build_run_example(compiler + '-s build_type=Debug -s arch=x86_64 -s compiler.runtime=MDd -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 
        
        build_run_example(compiler + '-s build_type=Release -s arch=x86_64 -s compiler.runtime=MD -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

        # x86, static
        build_run_example(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MDd -o Poco:poco_static=True')
        build_run_example(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MTd -o Poco:poco_static=True')

        build_run_example(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MD -o Poco:poco_static=True')
        build_run_example(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MT -o Poco:poco_static=True')

        # x86, shared
        build_run_example(compiler + '-s build_type=Debug -s arch=x86 -s compiler.runtime=MDd -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

        build_run_example(compiler + '-s build_type=Release -s arch=x86 -s compiler.runtime=MD -o Poco:poco_static=False')
        # MT with shared doesn't work and has no much sense 

    else:  # Compiler and version not specified, please set it in your home/.conan/conan.conf (Valid for Macos and Linux)
        # x86_64 debug
        build_run_example('-s build_type=Debug -s arch=x86_64 -o Poco:poco_static=True')
        build_run_example('-s build_type=Debug -s arch=x86_64 -o Poco:poco_static=False')

        # x86_64 release
        build_run_example('-s build_type=Release -s arch=x86_64 -o Poco:poco_static=True')
        build_run_example('-s build_type=Release -s arch=x86_64 -o Poco:poco_static=False')

        # x86 debug
        build_run_example('-s build_type=Debug -s arch=x86 -o Poco:poco_static=True')
        build_run_example('-s build_type=Debug -s arch=x86 -o Poco:poco_static=False')

        # x86 release
        build_run_example('-s build_type=Release -s arch=x86 -o Poco:poco_static=True')
        build_run_example('-s build_type=Release -s arch=x86 -o Poco:poco_static=False')
