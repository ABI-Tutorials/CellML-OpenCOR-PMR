.. include:: resources/roles.txt

.. _cellml_opencor_pmr_tutorial__opencor_python:

================================
Using OpenCOR with Python (beta)
================================

CellML provides a good technology to create, describe, and share definitions of mathematical models. :ref:`SED-ML <cellml_opencor_pmr_tutorial__sedml_web_lab>` similarly provides a good technology to share reproducible descriptions of simulation experiments. Whenever possible, it is best to make use of these standard formats to ensure the models and simulations are Findable, Accessible, Interoperable, and Reusable.

Often in research projects, however, it is not always possible to describe the model and/or simulation that you need to perform in these declarative formats. It also doesn't make sense to try and standardise extensions or modifications in such standards for potentially short-lived, one-off, research studies. Thus having access to a flexible scripting environment that works in concert with a standards-based tool like OpenCOR allows users to make use of standards when possible but with the flexibility to adapt as needed. OpenCOR supports this through the integration of a Python interpreter within the OpenCOR application.

Python-enabled versions of OpenCOR are now relatively mature, but still undergoing extensive user testing and implementation review. As such, this functionality is only available in special snapshot releases of OpenCOR available from: https://github.com/dbrnz/opencor/releases. In this part of the tutorial we are going to be using the *20 September 2019* snapshot of the Python-enabled OpenCOR. This particular release is distributed with the following Python packages and their dependencies: ``numpy``, ``scipy``, and ``matplotlib``.

.. contents::

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

Installing packages
-------------------

As described above, the Python interpreter lives inside the OpenCOR application -- making it difficult to access in order to install packages or modules that are not distributed with the Python-enabled versions of OpenCOR. To install packages using ``pip`` combined with the interactive Python console in the OpenCOR graphical user interface is the way to go here, as shown below.

.. code-block::

    Jupyter QtConsole 4.5.5
    Python 3.7.4 (default, Sep 20 2019, 18:29:34) [MSC v.1916 64 bit (AMD64)]
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: !pip install [options] package

Basic usage
===========

The scope and capabilities of the Python interface to OpenCOR is still being refined, but here we focus on use of the capabilities relevant to performing simulation experiments. Here we walk through the basic usage of using Python to interact with OpenCOR in performing a simulation experiment.

As with any Python script, we must first import the OpenCOR module to expose the functionality that we desire.

.. code-block:: python

    import OpenCOR as oc

The main object that we are interested in dealing with is OpenCOR's representation of a simulation. OpenCOR is able to generate a default simulation for a CellML model or to load a SED-ML document which defines the simulation experiment in detail. As the exposed simulation features are not yet complete, it is best to load a SED-ML document giving full control over the simulation settings. The output plots defined in the SED-ML will also be used when running the Python code via the interactive Python console in OpenCOR, but will be disregarded when running via the command line mode.

.. code-block:: python

    # for a local file
    simulation = oc.openSimulation('path/to/cellml/or/sedml')

    # OR for loading a remote file, e.g., from the model repository:
    simulation = oc.openRemoteSimulation('URL/of/cellml/or/sedml')

    # OR if using the OpenCOR GUI and models are already loaded
    simulation = oc.simulation()   # The model in the currently active tab

For a given simulation, the ``data`` object houses all the relevant information and pointers to the OpenCOR internal data representations.

.. code-block:: python

    data = simulation.data()

And the data object allows us to define the interval of interest for this simulation experiment.

.. code-block:: python

    data.setStartingPoint(start)
    data.setEndingPoint(end)
    data.setPointInterval(pointInterval)

As in the OpenCOR graphical user interface, constant parameters and initial values for the state variables can also be set via the Python interface OpenCOR provides. When address specific variables in a model, they are mapped to Python dictionaries using key's comprising of ``component_name/variable_name``. This provides a method to uniquely identify all variables in a model.

.. code-block:: python

    # Set constant parameter values
    data.constants()['key'] = value

    # Set initial value for state variables
    data.states()['key'] = value

Once you have the simulation defined that you would like to perform, it can be executed with the following.

.. code-block:: python

    simulation.run()

If you are using the OpenCOR graphical user interface and have define plots for the current simulation experiment, then these will be displayed as usual during the execution of the simulation. The simulation results can also be used directly in the Python script as shown below.

.. code-block:: python

    # Access simulation results
    results = simulation.results()

    # grab a specific state variable results
    r1 = results.states()['key'].values()  # Numpy array

    # grab a specific algebraic variable results
    r2 = results.algebraic()['key'].values()  # Numpy array

    # access the full datastore representation of the simulation results
    ds = results.dataStore()
    # the dictionary or all result variables in the simulation
    variables = ds.voiAndVariables()

    # grab a the results for a given variable
    r3 = variables['key'].values()   # Python list of values

When continuing a simulation from an existing state, the default behaviour is to continue from the current state. The system can be reset to the initial state as shown below. As with using the OpenCOR graphical user interface, this includes resetting any parameters or initial values that you may have set via the GUI or the Python interface.

.. code-block:: python

    # Reset things if needed when re-running
    simulation.resetParameters()
    # clear any existing results
    simulation.clearResults()

Interactive example
-------------------

In this example, we use the :ref:`simple ODE model <ocr_tut_out_first_ode>` introduced earlier in the tutorial. We will be using the Python console in the OpenCOR graphical user interface, working with the SED-ML loaded directly from the Physiome Model Repository. As we are using the OpenCOR application, you should see the user interface updating in response the to various Python commands. The following commands should be copy-pasted one at a time into the Python console to observe the behaviour.

.. code-block:: python

    import OpenCOR as oc

    simulation = oc.openRemoteSimulation('https://models.physiomeproject.org/workspace/25d/rawfile/60ac9389285471a704f2f4be6e1a8ba5cbf45d1a/Firstorder.sedml')
    data = simulation.data()
    data.setStartingPoint(0)
    data.setEndingPoint(10)
    data.setPointInterval(0.1)
    simulation.run()

    # reset
    simulation.resetParameters()
    simulation.clearResults()

    # change parameter values
    data.constants()['main/b'] = 5
    data.states()['main/y'] = 2
    simulation.run()

    # look at the simulation results
    results = simulation.results()
    y = results.states()['main/y'].values()  # Numpy array
    print(y)

    ds = results.dataStore()
    variables = ds.voiAndVariables()
    y = variables['main/y'].values()   # Python list of values
    print(y)

    a = variables['main/a'].values()
    print(a)

In working through this example, you should be able to reproduce the results as seen in :numref:`Fig. %s<ocr_tut_out_first_ord>`.

OpenCOR, CellML, and TensorFlow
===============================

`TensorFlow <https://www.tensorflow.org/>`_ is a popular end-to-end open source machine learning platform in Python. Together with the Python-enabled OpenCOR capabilities and CellML itself, this opens up a new world of application of machine learning in computational physiology. This is a very new application that we are still actively developing, but here we give a brief demonstration that might help show what could be achieved.

Getting prepared
----------------

The first step is to ensure that you have TensorFlow installed. As described above, Python packages need to be installed in the Python embedded inside OpenCOR. We are using here TensorFlow version 1.15, which can be installed using the OpenCOR Python console with the following command. (TensorFlow 2.0 will not work with this demonstration.)

.. code-block::

    In [1]: !pip install tensorflow==1.15

We have prepared a couple of Python scripts that you can use for this demonstration. The first is :download:`MPL.py <resources/python-demonstration-01/MLP.py>`, which is a TensorFlow-based script to construct a simple MLP (fully-connected feed-forward network or MultiLayer Perceptron) and trains it with a given dataset. The second is :download:`train-tf-model.py <resources/python-demonstration-01/train-tf-model.py>`, which will first generate a set of training data using the `O'Hara & Rudy <https://www.ncbi.nlm.nih.gov/pubmed/21637795>`_ cardiac electrophysiology model, which has been encoded in the CellML format as an extension of this `model <https://models.physiomeproject.org/e/4eb>`_ in the Physiome Model Repository. Both files should be downloaded into the same folder on your local machine.

Finally, in the OpenCOR Python console we need to make sure the plotting happens in-place rather than trying to bring windows. This is done by exectuing the following command in the OpenCOR Python console.

.. code-block::

    In [1]: %matplotlib inline

Training a machine learning model
---------------------------------

The :download:`train-tf-model.py <resources/python-demonstration-01/train-tf-model.py>` script is the one that contains the definition of the workflow we are demonstrating here. It is easiest to open this file in your preferred Python editor and follow through the script, with the comments attempting to explain what is happening.

This script can be run in the OpenCOR Python console by first making sure the console is looking at the correct folder,

.. code-block::

    In [1]: %cd path/to/folder/with/downloaded/scripts

and then running the training script as follows.

.. code-block::

    In [1]: %run train-tf-model.py

All going well, this should result in something similar to :numref:`Fig. %s<ocr_tut_python_training_ML_model>`.

.. Figure:: _static/images/python-opencor-02.png
   :name: ocr_tut_python_training_ML_model
   :alt: Training a TensorFlow machine learning model using a CellML model in OpenCOR.
   :align: center
   :width: 100%
   :figwidth: 66%

   The result of training a TensorFlow machine learning model using data from a simulation of a CellML model in OpenCOR and then comparing the ML-model predictions to the actual simulation results.

You should now be able to play around with the training script to see what happens as you change, for example, the stimulation period or simulation duration.
