
.. figure:: _static/images/banner_introduction.png
   :align: center
   :width: 100%
   :alt: logo banner

===========================================================
Tutorial on CellML, OpenCOR & the Physiome Model Repository
===========================================================

.. warning::
   This version of the tutorial is undergoing translation from the original source to reStructuredText. Many aspects of formatting and presentation are currently lacking, although being worked on. The original tutorial is available here: :download:`OpenCOR-Tutorial-v17.pdf <resources/OpenCOR-Tutorial-v17.pdf>`.


This tutorial shows you how to install and run the OpenCOR [#]_ software
:cite:`1`, to author and edit CellML models [#]_ :cite:`2` and to use the Physiome
Model Repository (PMR) [#]_ :cite:`3`. We start by giving a brief background
on the VPH-Physiome project. We then create a simple model, save it as a
CellML file and run model simulations. We next try opening existing
CellML models, both from a local directory and from the Physiome Model
Repository. The various features of CellML [#]_ and OpenCOR are then
explained in the context of increasingly complex biological models. A
simple linear first order ODE model and a nonlinear third order model
are introduced. Ion channel gating models are used to introduce the way
that CellML handles units, components, encapsulation groups and
connections. More complex potassium and sodium ion channel models are
then developed and subsequently imported into the Hodgkin-Huxley 1952
squid axon neural model using the CellML model import facility. The
Noble 1962 model of a cardiac cell action potential is used to
illustrate importing of units and parameters. The tutorial finishes with
sections on model annotation and the facilities available on the CellML
website and the Physiome Model Repository to support model development,
including the links to bioinformatic databases. There is a strong
emphasis in the tutorial on establishing ‘best practice’ in the creation
of CellML models and using the PMR resources, particularly in relation
to modular approaches (model hierarchies) and model annotation.

.. note::

   This tutorial relies on readers having some background in
   algebra and calculus, but tries to explain all mathematical concepts
   beyond this, along with the physical principles, as they are needed for
   the development of CellML models. [#]_

.. toctree::
   :maxdepth: 1

   background
   install
   create_and_first_run
   open_existing
   simple_ode
   lorenz
   cellml_units
   cellml_comp_and_conn
   cellml_encaps_and_inter
   cellml_imports
   cellml_import_unit_params
   annotation
   pmr
   sedml_func_cur_web_lab
   speed_comp
   future
   zreferences

.. todo::

   * Colour background of *CellML Text*
   * Annotate screen shots with svg for same look and feel
   * *CellML Text* code is not highlighted for all display situations, currently only in environments that are using an adapted version of pygments 
   * Tidy up citations and BiBTeX source (possibly use Zotero to manage?)
   * Make horizontal line for footnotes only visible in html output
   * Check external references markup
   * Consider a more suitable theme (may require changes to an existing one to get a good result)
   * Must check over output (and models) from screenshots to make sure that it matches the current release of OpenCOR, especially against running experiments for the first time.
   
---------------------------

.. rubric:: Footnotes

.. [#] OpenCOR is an open source, freely available, C++ desktop application written by Alan Garny at INRIA with funding support from the Auckland Bioengineering Institute (http://www.abi.auckland.ac.nz) and the NIH-funded Virtual Physiological Rat (VPR) project led by Dan Beard at the University of Michigan (http://virtualrat.org).

.. [#] For an overview and the background of CellML see http://www.cellml.org. This project is led by Poul Nielsen and David (Andre) Nickerson at the Auckland (University) Bioengineering Institute (`ABI <http://www.abi.auckland.ac.nz>`_).

.. [#] https://models.physiomeproject.org. The PMR project is led by Tommy Yu at the ABI.

.. [#] For details on the specifications of CellML1.0 see http://www.cellml.org/specifications/cellml_1.0.

.. [#] Please send any errors discovered or suggested improvements to p.hunter@auckland.ac.nz.

