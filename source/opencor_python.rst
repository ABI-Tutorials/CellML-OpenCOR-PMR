.. include:: resources/roles.txt

.. _cellml_opencor_pmr_tutorial__opencor_python:

================================
Using OpenCOR with Python (beta)
================================

CellML provides a good technology to create, describe, and share definitions of mathematical models. :ref:`SED-ML <cellml_opencor_pmr_tutorial__sedml_web_lab>` similarly provides a good technology to share reproducible descriptions of simulation experiments. Whenever possible, it is best to make use of these standard formats to ensure the models and simulations are Findable, Accessible, Interoperable, and Reusable.

Often in research projects, however, it is not always possible to describe the model and/or simulation that you need to perform in these declarative formats. It also doesn't make sense to try and standardise extensions or modifications in such standards for potentially short-lived, one-off, research studies. Thus having access to a flexible scripting environment that works in concert with a standards-based tool like OpenCOR allows users to make use of standards when possible but with the flexibility to adapt as needed. OpenCOR supports this through the integration of a Python interpreter within the OpenCOR application.

Python-enabled versions of OpenCOR are now relatively mature, but still undergoing extensive user testing and implementation review. As such, this functionality is only available in special snapshot releases of OpenCOR available from: https://github.com/dbrnz/opencor/releases. In this part of the tutorial we are going to be using the *20 September 2019* snapshot of the Python-enabled OpenCOR.

Installation and setup
======================

Python-enabled OpenCOR release can be installed as per the standard :ref:`installation instructions <cellml_opencor_pmr_tutorial__installation>`. As this is an early release of the new functionality, it is best to use one of the compressed archive releases which you can extract locally rather than overwriting the stable system install. Once you have a Python-enabled release of OpenCOR your main OpenCOR window should look similar to that shown in :numref:`Fig. %s<ocr_tut_python_main_window>`.

.. Figure:: _static/images/python-opencor-01.png
   :name: ocr_tut_python_main_window
   :alt: OpenCOR+Python application
   :align: center
   :width: 100%
   :figwidth: 66%

   OpenCOR application with default positioning of dockable windows including the Python console (right-side, middle). As described in :ref:`cellml_opencor_pmr_tutorial__installation` the dockable windows can be rearranged as desired to suit your preferred layout.

Command line usage
------------------

In Python-enabled versions of OpenCOR the Python interpreter is embedded within the OpenCOR application. Which means that in order to access the OpenCOR functionality you must use that Python within the OpenCOR application rather than, for example, importing OpenCOR into your system Python. The Python console available in the OpenCOR graphical user interface handles this for you allowing a seamless user experience. However, often with Python-scripted simulation workflows it is nice to have the ability to run in a headless or batch mode. As such, Python-enabled versions of OpenCOR come with some command line scripts to help provide the user avoid the issues of making sure their Python scripts run using the correct Python interpreter.

In the top-level folder of your Python-enabled OpenCOR installation there is a script named ``run_python`` which will depend on your operating system - on Windows for example, it is called ``run_python.bat``. Running this script without providing a Python script to execute will give you a standard Python console using the Python embedded inside the OpenCOR application:

.. code-block::

    C:\Users\andre\OpenCOR-2019-09-20-Windows> run_python.bat
    Python 3.7.4 (default, Sep 20 2019, 18:29:34) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Providing a Python script will result in that script being interpreted by the interpreter embedded in the OpenCOR application:

.. code-block::

    C:\Users\andre\OpenCOR-2019-09-20-Windows> run_python.bat hello_world.py
    Hello World!

Command line arguments can be provided as usual following the script to be executed.

.. warning::

    Due to the use of a Python interpreter embedded in a graphical user interface, there can be some weirdness when trying to use UI toolkits from the command line, for example using ``matplotlib``. This works within the OpenCOR graphical user interface, but will fail when running from the command line. Hence, it is best to currently use the command line version when working in a truly headless manner without the need for a graphical user interface.

Jupyter notebooks
-----------------

There is another mode to make use of the Python-enabled versions of OpenCOR and that is to access this functionality via Jupyter notebooks. This is enabled via the ``run_jupyter`` helper script.

.. todo::

    Write this section on Jupyter notebooks and OpenCOR.