.. _cellml_opencor_pmr_tutorial__sedml_web_lab:

=======================================
SED-ML, functional curation and Web Lab
=======================================

In the same way that CellML models can be defined unambiguously, and shared easily, in a machine- readable format, there is a need to do the same thing with 'protocols' - i.e. to define what you have to do to replicate/simulate an experiment, and to analyse the results. An XML standard for this called SED-ML\ [#]_ is being developed by the CellML/SBML community and preliminary support for SED-ML has been implemented in OpenCOR in order to allow precise and reproducible control over the OpenCOR simulation and graphical output (e.g., see :numref:`ocr_tut_out_moble62_ocr`).

The current snapshot release (2016-02-27) of OpenCOR supports exporting the *Simulation view* configuration to a SED-ML file, which can then be read back into OpenCOR to reproduce a given simulation experiment, illustrated in :numref:`ocr_tut_sedml_export_fig`.

.. figure:: _static/images/sedml_export.png
   :name: ocr_tut_sedml_export_fig
   :alt: Export SED-ML
   :align: center

   Once you are happy with the configuration of the *Simulation view* in OpenCOR, clicking the SED-ML button (highlighted) will prompt for a file to save the SED-ML document to. This document can be loaded back into OpenCOR to reproduce the simulation, or shared with collaborators so they can reproduce the simulation.

Support for SED-ML will also facilitate the curation of models according to their functional behaviour under a range of experimental scenarios.
The key idea behind functional curation is that, when mathematical and computational models are being developed, a primary goal should be the continuous comparison of those models against experimental data. When computational models are being re-used in new studies, it is similarly important to check that they behave appropriately in the new situation to which you're applying them. To achieve this goal, a pre-requisite is to be able to replicate in-silico precisely the same protocols used in an experiment of interest. A language for describing rich 'virtual experiment' protocols and software for running these on compatible models is being developed in the Computational Biology Group at Oxford University\ [#]_.
An online system called Web Lab\ [#]_ is also being developed that supports definition of experimental protocols for cardiac electrophysiology, and allows any CellML model to be tested under these protocols :cite:`16`. This enables comparison of the behaviours of cellular models under different experimental protocols: both to characterise a model's behaviour, and comparing hypotheses by seeing how different models react under the same protocol (:numref:`ocr_tut_web_lab_fc_sch` adapted from :cite:`16`).

.. figure:: _static/images/fc_schematic.png
   :name: ocr_tut_web_lab_fc_sch
   :alt: Functional curation schematic
   :align: center

   A schematic of the way we organise model and protocol descriptions. Web Lab provides an interface to a Model/Protocol Simulator, storing and displaying the results for cardiac electrophysiology models.

The Web Lab website provides tools for comparing how two different cardiac electrophysiology models behave under the same experimental protocols. Note that Web Lab demonstration for CellML models of cardiac electrophysiology is a prototype for a more general approach to defining simulation protocols for all CellML models.

---------------------------

.. rubric:: Footnotes

.. [#] The 'Simulation Experiment Description Markup Language': `sed-ml.org <http://sed-ml.org>`_

.. [#] `travis.cs.ox.ac.uk/FunctionalCuration/about.html <http://travis.cs.ox.ac.uk/FunctionalCuration/about.html>`_ This initiative is led by Jonathan Cooper and Gary Mirams.

.. [#] `travis.cs.ox.ac.uk/FunctionalCuration <http://travis.cs.ox.ac.uk/FunctionalCuration>`_.
