
import mypackage.mymodule1 as mod1
import mypackage.mymodule2 as mod2

# PYTHON PATH Example-
import sys
# Add the directory containing lib_module.py to the module search path
sys.path.append('my_library')  # Speaking to python compiler
import lib_module
# import my_library.lib_module as lib1    # instead of this we can use PYTHON PATH


def main():
    name = "Lokendra Arya"
    print(mod1.greet(name))
    print(mod2.good_bye(name))

    lib_module.lib_function()
    # lib1.lib_function()


if __name__ == "__main__":
    main()
    