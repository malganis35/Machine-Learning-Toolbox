# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:23:59 2017

@author: CaoTri
"""

#%% Clear the console
import os
os.system('cls')
print("Cleaning the console")


#%% Here is a code for automatic import or installation of the missing packages

def install_and_import(package):
    """
        General function to load and/or install a package.
        input:
            package: name of a package (String)
    """ 
    import importlib
    try:
        # Try to import the package if it is install on the computer
        print("- Importing the package ", package)
        importlib.import_module(package)
        print("- The package ", package, " is successfully loaded")
    except ImportError:
        # If the package connot be loaded, install the package (need for internet connection)
        print("- The package ", package, " cannot be loaded. Starting installation ... ")
        import pip
        pip.main(['install', package])
        print("- The package ", package, " is installed ")
    finally:
        globals()[package] = importlib.import_module(package)

def importPackages(list_package):
    """
        Recursively add packages. \n
        input:
            list_package: a list of n x 1 packages (array of Strings)
    """
    print("Import/Install of multiples packages:")
    print(list_package)
    nb_packages = len(list_package);
    for i in range(nb_packages):
        package_i = list_package[i]
        install_and_import(package_i)
  
list_package = ['plotly', 'numpy', 'matplotlib']      
importPackages(list_package)
