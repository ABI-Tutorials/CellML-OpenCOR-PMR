.. include:: resources/roles.txt

.. _cellml_opencor_pmr_tutorial__pmr_intro:

============================================================
The Physiome Model Repository and the link to bioinformatics
============================================================

The Physiome Model Repository (PMR) :cite:`13` is the main online repository
for the IUPS Physiome Project, providing version and access controlled
repositories, called *workspaces*, for users to store their data.
Currently there are over 700 public workspaces and many
private workspaces in the repository. PMR also provides a mechanism to
create persistent access to specific revisions of a workspace, termed
*exposures*. Exposure plugins are available for specific types of data
(e.g. CellML or FieldML documents) which enable customizable views of
the data when browsing the repository via a web browser, or an
application accessing the repository’s content via web services.

More complete documentation describing how to use PMR is available in the PMR documentation: https://models.physiomeproject.org/docs.

The CellML models on  `models.physiomeproject.org <https://models.physiomeproject.org>`_  are listed under 20 categories, shown below:
(numbers of exposures in each category are given besides the bar graph, correct as at early 2016)

**Browse by category**

.. tabularcolumns:: |l|c|

====================================  ==========================================
 Calcium Dynamics                     |image_variable_node_140| 140
 Cardiovascular Circulation           |image_variable_node_60| 60
 Cell Cycle                           |image_variable_node_38| 38
 Cell Migration                       |image_variable_node_2| 2
 Circadian Rhythms                    |image_variable_node_22| 22
 Electrophysiology                    |image_variable_node_230| 230
 Endocrine                            |image_variable_node_60| 60
 Excitation-Contraction Coupling      |image_variable_node_22| 22
 Gene Regulation                      |image_variable_node_12| 12
 Hepatology                           |image_variable_node_29| 29
 Immunology                           |image_variable_node_55| 55
 Ion transport                        |image_variable_node_13| 13
 Mechanical Constitutive Laws         |image_variable_node_19| 19
 Metabolism                           |image_variable_node_86| 86
 Myofilament Mechanics                |image_variable_node_22| 22
 Neurobiology                         |image_variable_node_33| 33
 pH regulation                        |image_variable_node_2| 2
 PKPD                                 |image_variable_node_11| 11
 Signal Transduction                  |image_variable_node_120| 120
 Synthetic Biology                    |image_variable_node_6| 6
====================================  ==========================================

Note that searching of models can be done anywhere on the site using the
search box on the upper right hand corner. An important benefit of
ensuring that the models on the PMR are annotated is that models can
then be retrieved by a web-search using any of the annotated terms in
the models.

To illustrate the features of PMR, click on the Hund, Rudy 2004 (Basic)
model in the alphabetic listing of models under the *Electrophysiology* category.

.. figure:: _static/images/pmr_website_exp_hund_rudy.png
   :name: ocr_tut_pmr_exp_hr
   :alt: PMR exposure page for the Hund-Rudy 2004 model
   :align: center
   :figwidth: 95%

   The Physiome Model Repository exposure page for the basic `Hund-Rudy 2004 model <https://models.physiomeproject.org/exposure/f4b7120aa512c7f5e7a0664abcee3e8b/hund_rudy_2004_a.cellml/view>`_.

The section labelled ‘Model Structure’ contains the journal paper
abstract and often a diagram of the model\ [#]_. This is shown for the
Hund-Rudy 2004 model in :numref:`ocr_tut_hund_2004`. This model, with over 22 separate
protein model components, is also a good example of why it is important
to build models from modular components :cite:`14`, and in particular the
individual ion channels for electrophysiology models.

.. figure:: _static/images/hund_2004.png
   :name: ocr_tut_hund_2004
   :alt: Hund 2004 shematic diagram
   :align: center
   :figwidth: 95%

   A diagrammatic representation of the Hund-Rudy 2004 model.

There is a list of ‘Views Available’ for the CellML model on the
right hand side of the exposure page. The function of each of these
views is as follows:

**Views Available**

**Documentation** - Takes you to the main exposure page.

**Model Metadata** - Lists metadata including authors, title, journal,
Pubmed ID and model annotations.

**Model Curation** - Provides the curation status of the model. Note:
this is soon to be updated.

**Mathematics** - Displays all the mathematical equations contained in
the model.

**Generated Code** - Various codes (C, C-IDA, F77, MATLAB or Python) generated from
the model.

**Cite this model** - Provides details on how to cite use of the CellML
model.

**Source view** - Gives a full listing of the XML code for the model.

**Launch with OpenCOR** - Opens the model (or simulation experiment) in OpenCOR.

Note that CellML models are available under a Creative Commons
Attribution 3.0 Unported License\ [#]_. This means that you are free to:

 -  Share — copy and redistribute the material in any medium or format

 -  Adapt — remix, transform, and build upon the material

for any purpose, including commercial use.

The next stage of content development for PMR is to provide a list of
the modular components of these models each with their own exposure. For
example, models for each of the individual ion channels used in the
publication-based electrophysiological models will be available as
standalone models that can then be imported as appropriate into a new
composite model. Similarly for enzymes in metabolic pathways and
signalling complexes in signalling pathways, etc. Some examples of these
protein modules are:

*Sodium/hydrogen exchanger 3* https://models.physiomeproject.org/e/236/

*Thiazide-sensitive Na-Cl cotransporter*
https://models.physiomeproject.org/e/231/

*Sodium/glucose cotransporter 1*
https://models.physiomeproject.org/e/232/

*Sodium/glucose cotransporter 2*
https://models.physiomeproject.org/e/233/

Note that in each case, as well as the CellML-encoded mathematical
model, links are provided (see :numref:`ocr_tut_pmr_wsp_thiazide`) to the UniProt Knowledgebase
for that protein, and to the Foundational Model of Anatomy (FMA)
ontology (via the EMBLE-EBI Ontology Lookup Service) for information
about tissue regions relevant to the expression of that protein (e.g.
*Proximal convoluted tubule*, *Apical plasma membrane*; *Epithelial cell
of proximal tubule*; *Proximal straight tubule*). Similar facilities are
available for SMBL-encoded biochemical reaction models through the
Biomodels database :cite:`15`.

.. figure:: _static/images/pmr_wsp_thiazide.png
   :name: ocr_tut_pmr_wsp_thiazide
   :alt: Thiazide-sensitive Na-Cl cotransporter workspace
   :align: center
   :figwidth: 95%

   The PMR workspace for the Thiazide-sensitive Na-Cl
   cotransporter. Bioinformatic data for this model is accessed via the
   links under the headings highlight by the :red:`arrows` and include
   **Protein** (labelled :red:`A`) and the model **Location** (labelled
   :red:`B`). Other information is as already described for the Hund-Rudy 2004
   model.

---------------------------

.. rubric:: Footnotes

.. [#] These are currently hand drawn SVG diagrams but the plan is to automatically generate them from the model annotation and also (at some stage!) to animate them as the model is executed.

.. [#] `https://creativecommons.org/licenses/by/3.0/ <https://creativecommons.org/licenses/by/3.0/>`_

.. |image_variable_node_230| image:: _static/images/bar.png
   :height: 10pt
   :width: 230pt

.. |image_variable_node_2| image:: _static/images/bar.png
   :height: 10pt
   :width: 2pt

.. |image_variable_node_60| image:: _static/images/bar.png
   :height: 10pt
   :width: 60pt

.. |image_variable_node_22| image:: _static/images/bar.png
   :height: 10pt
   :width: 22pt

.. |image_variable_node_12| image:: _static/images/bar.png
   :height: 10pt
   :width: 12pt

.. |image_variable_node_33| image:: _static/images/bar.png
   :height: 10pt
   :width: 33pt

.. |image_variable_node_55| image:: _static/images/bar.png
   :height: 10pt
   :width: 55pt

.. |image_variable_node_120| image:: _static/images/bar.png
   :height: 10pt
   :width: 120pt

.. |image_variable_node_19| image:: _static/images/bar.png
   :height: 10pt
   :width: 19pt

.. |image_variable_node_140| image:: _static/images/bar.png
   :height: 10pt
   :width: 140pt

.. |image_variable_node_38| image:: _static/images/bar.png
   :height: 10pt
   :width: 38pt

.. |image_variable_node_29| image:: _static/images/bar.png
   :height: 10pt
   :width: 29pt

.. |image_variable_node_13| image:: _static/images/bar.png
   :height: 10pt
   :width: 13pt

.. |image_variable_node_86| image:: _static/images/bar.png
   :height: 10pt
   :width: 86pt

.. |image_variable_node_11| image:: _static/images/bar.png
   :height: 10pt
   :width: 11pt

.. |image_variable_node_6| image:: _static/images/bar.png
   :height: 10pt
   :width: 6pt
