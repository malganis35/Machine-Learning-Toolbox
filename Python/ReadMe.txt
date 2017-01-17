Machine Learning Toolbox for R and Python
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Author:
Cao Tri DO - caotri.do88@gmail.com
Stefen CHAN - 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Summary
1. HOW TO INSTALL PYTHON
2. HOW TO USE PYTHON
3. INSTALL SOME USEFUL TOOLBOX FOR PYTHON



--------------------------------------------------------------------------------------------------
1. HOW TO INSTALL PYTHON
--------------------------------------------------------------------------------------------------
* Installing Python 3.6.0 (for windows): https://www.python.org/downloads/ -> Python 3.6.0 (32-64-bit)
* Make sure to check "Add to environment variables".
-- If not, in Windows, locate the path installation of Python
-- in general : C:\Python36;
-- or : C:\Users\xxx\AppData\Local\Programs\Python\Python36;
-- Go in Explorer, right click then --> Properties --> Environement variables --> Add to the variable "Path"
* If it's installed correctly you shouuld be able to open a command prompt and type "python".
* IDE : Liclipse : http://www.liclipse.com/download.html
* tutorial : https://www.youtube.com/watch?v=fAa80SpQJHo
* Anaconda : https://ipython.org/

--------------------------------------------------------------------------------------------------
2. HOW TO USE PYTHON
--------------------------------------------------------------------------------------------------
* General website 								: https://www.python.org/
* Introduction to Python (French) 				: https://openclassrooms.com/courses/apprenez-a-programmer-en-python
* Function and commands from Matlab to Python 	: http://mathesaurus.sourceforge.net/matlab-numpy.html



--------------------------------------------------------------------------------------------------
3. INSTALL SOME USEFUL TOOLBOX FOR PYTHON
--------------------------------------------------------------------------------------------------
* OPENCV
** Installing Opencv:
		To install Opencv with Python 3, we will use wheel files.
		Download here: http://www.lfd.uci.edu/~gohlke/pythonlibs/ the numpy and opencv ".whl".
** For example: numpy‑1.12.0rc2+mkl‑cp36‑cp36m‑win32.whl
		The number after cp corresponds to the version of Python. Here, cp36 means Python 3.6.
		win32 refers to the Python version, not Windows.
** Open a command prompt at the location of the downloaded files and type:
		pip install "numpy‑1.12.0rc2+mkl‑cp36‑cp36m‑win32.whl"
** pip install "opencv_python..."


