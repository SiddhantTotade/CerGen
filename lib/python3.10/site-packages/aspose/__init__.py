import sys
import sysconfig
import os
import importlib.machinery as im
from importlib._bootstrap import _load
from importlib import util
from importlib.machinery import SourceFileLoader
import inspect
import re

if sys.platform == "darwin":
    _platform_suffixes = [re.sub(r"\.so", ".dylib", str) for str in im.EXTENSION_SUFFIXES[:-1]]
else:
    _platform_suffixes = im.EXTENSION_SUFFIXES[:-1];

def foreach_file(folder, suffixes, action):
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            for ext in suffixes:
                if file.endswith(ext):
                    file_name = str.split(file, '.', 1)[0]
                    if file_name.endswith("_d") == ext.startswith("_d"):
                        name = file[:-len(ext)]
                        action(name, full_path)


class AsposeModuleLoader:
    aspose_native_lib_dir = os.path.dirname(__file__)
    aspose_py_modules = os.path.join(aspose_native_lib_dir, "lib")

    def load_module(self, fullname):
        try:
            return sys.modules[fullname]
        except KeyError:
            pass

        parts = fullname.split('.')
        parts_len = len(parts)
        if parts_len < 2:
            return None

        native_name = parts[1]
        package_name = ".".join(parts[:-1])

        if parts_len == 2:
            # root Aspose native library
            native_module = self._load_native_module(native_name)
            if native_module == None:
                return None

            self._register_additional_classes(native_module, native_name)

            return self._prepare_as_package(native_module, fullname, package_name)

        else:
            # submodule
            parent_mod = self.load_module(package_name)
            mod = getattr(parent_mod, parts[-1])
            if mod == None:
                return None

            self._register_additional_classes(mod, os.path.join(*parts[1:]))

            return self._prepare_as_package(mod, fullname, package_name)

    def _prepare_as_package(self, module, fullname, package):
        module.__package__ = package
        module.__path__ = []
        sys.modules.setdefault(fullname, module)
        return module

    def _load_native_module(self, native_name):
        for ext in _platform_suffixes:
            lib_file = os.path.join(
                self.aspose_native_lib_dir, native_name + ext)
            if os.path.isfile(lib_file):
                loader = im.ExtensionFileLoader(native_name, lib_file)
                spec = im.ModuleSpec(native_name, loader, origin=lib_file)
                return _load(spec)

        return None

    @staticmethod
    def _import_file(module, name, path):
        try:
            private_name = module.__name__ + "._" + name
            src_module = SourceFileLoader(private_name, path).load_module()
            for element_name in dir(src_module):
                element = getattr(src_module, element_name)
                if hasattr(element, "__module__") and element.__module__ == private_name:
                    element.__module__ = module.__name__
                    element.__name__ = module.__name__ + "." + name
                    setattr(module, element_name, element)

        except Exception as e:
            print(e)

    def _register_additional_classes(self, module, sub_lib):
        folder = os.path.join(AsposeModuleLoader.aspose_py_modules, sub_lib)
        if os.path.isdir(folder):
            foreach_file(folder, im.SOURCE_SUFFIXES, lambda name, path,
                         module=module: AsposeModuleLoader._import_file(module, name, path))

        return


class AsposeModuleFinder:
    def find_module(self, fullname, path=None):
        if fullname.startswith(__package__):
            return AsposeModuleLoader()
        return None


__path__ = []

os.environ["NETCORE_WRAPPER_NETCORE_DIR_aspose"] = os.path.join(
    AsposeModuleLoader.aspose_native_lib_dir, "netcore")
os.environ["NETCORE_WRAPPER_ASSEMBLY_DIR_aspose"] = os.path.join(
    AsposeModuleLoader.aspose_native_lib_dir, "assemblies")


os.environ["WRAPPER_MODULE_DIR_aspose"] = AsposeModuleLoader.aspose_native_lib_dir

os.environ["WRAPPER_MODULE_DIR_aspose"] = AsposeModuleLoader.aspose_native_lib_dir

# see https://www.python.org/dev/peps/pep-0382/
# see https://www.python.org/dev/peps/pep-0420/

# to support 'from Aspose import *' syntax
__all__ = []
foreach_file(AsposeModuleLoader.aspose_native_lib_dir,
             _platform_suffixes, lambda name, path: __all__.append(name))

sys.meta_path.append(AsposeModuleFinder())

