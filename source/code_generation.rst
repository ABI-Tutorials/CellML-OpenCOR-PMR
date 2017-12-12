.. include:: resources/roles.txt

.. _opencor_tutorial_code_generation:

===============
Code generation
===============

It is sometimes required to export CellML models to various procedural formats to make use of a given model with existing tools. OpenCOR currently uses the CellML Language Export Definition Service provided by the CellML API to achieve this (see `this article <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2858041/>`_ for details). This service takes an XML file containing a conversion definition and uses that to export a CellML model to the defined format.

The OpenCOR distribution packages include definition files for `C <https://raw.githubusercontent.com/opencor/opencor/master/formats/C.xml>`_, `Fortran 77 <https://raw.githubusercontent.com/opencor/opencor/master/formats/F77.xml>`_, `Python <https://raw.githubusercontent.com/opencor/opencor/master/formats/Python.xml>`_, and `Matlab <https://raw.githubusercontent.com/opencor/opencor/master/formats/MATLAB.xml>`_. These definition files are available in the :file:`formats` folder of your OpenCOR installation or can be downloaded and used directly using the previous links.

The C and Fortran code generated using these definition files contain functions suitable for inclusion in DAE/ODE simulation codes. Whereas the Python and Matlab code generated are complete scripts that use standard Python or Matlab methods to actually perform an *default* simulation. The default simulation is probably not what is needed, so the generated code can be modified or reused to meet the specific usage requirements.

Exporting CellML to code
------------------------

The steps to generate code from OpenCOR are given below.

1. Load the desired CellML model into OpenCOR (both CellML 1.0 and 1.1 models can be used)
2. From the OpenCOR menu, choose :menuselection:`Tools --> CellML File Export To --> User-Defined Format`.
3. The first file selection dialog is to provide the conversion definition file (as above).
4. The second file selection dialog is to provide the file to save the generated code to.

This conversion can also be performed using OpenCOR as a command line client. In this case the command is::

   $ ./OpenCOR -c CellMLTools::export myfile.cellml myformat.xml
   
or for a remote model::

   $ ./OpenCOR -c CellMLTools::export http://mydomain.com/myfile.cellml myformat.xml
   
where :file:`myformat.xml` can be one of the standard definition files described above.

Generated code in PMR
---------------------

The Physiome Model Repository uses the same code generation service from the CellML API to generate code in the above formats for all exposures containing CellML models. These are available from the :guilabel:`Generated Code` view for CellML models. See `here <https://models.physiomeproject.org/e/430/sodium_ion_channel.cellml/cellml_codegen>`_ for an example.
