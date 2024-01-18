.. _cellml_opencor_pmr_tutorial__installation:

==========================
Install and launch OpenCOR
==========================

Download OpenCOR from `https://opencor.ws <https://opencor.ws>`_.
Versions are available for Windows, OS X and Linux [#]_.
At time of revising this tutorial the current version of OpenCOR is 0.7.1 and we assume this version or newer.
Upon first launching the OpenCOR application a window will appear that looks like :numref:`Fig. %s(a)<ocr_tut_main_win>`.

.. Figure:: _static/images/opencor_01.png
   :name: ocr_tut_main_win
   :alt: OpenCOR application
   :align: center
   
   OpenCOR application (a) Default positioning of dockable windows. (b) An
   alternative configuration achieved by dragging and dropping the dockable
   windows.

The OpenCOR website `https://opencor.ws <https://opencor.ws>`_ contains information explaining how to use all features of the application.
Of particular relevance is the `user help <https://opencor.ws/user/index.html>`_.
Here we introduce specific features and functionality, please see the website for more comprehensive coverage of OpenCOR capabilities.

Dockable Windows
================

The central area is used to interact with files. By default, no files
are open, hence the OpenCOR logo is shown instead. To the sides, there
are dockable windows, which provide additional features. Those windows
can be dragged and dropped to the top or bottom of the central area as
shown in :numref:`Fig. %s(b)<ocr_tut_main_win>` or they can be individually undocked or closed. All
closed panels can be re-displayed by enabling them in the *View* menu,
or by using the *Tools* menu *Reset All* option. The key combination 
:kbd:`Control-spacebar` removes (for less clutter) or restores these 
two side panels [#]_.

Any of the subpanels (*Physiome Model Repository*, *File Browser*, and
*File Organiser*) can be closed with the top right delete button, and
then restored from the *View* .. *Windows* .. menu. Files can be dragged
and dropped into the File Organiser to create a local directory
structure for your files.

Plugins
=======

OpenCOR has a plugin architecture and can be used with or
without a range of modules. These can be viewed under the *Tools* menu.
By default they are all included, as shown in :numref:`ocor_tut_inla_def_plug`. Information
about developing plugins for OpenCOR is also `available <https://www.opencor.ws/developer/develop/plugins/index.html>`_.

.. Figure:: _static/images/opencor_02.png
   :name: ocor_tut_inla_def_plug
   :alt: OpenCOR plugin menu
   :align: center
   :width: 100%
   :figwidth: 66%
   
   OpenCOR tools menu showing the plugins that are selectable.  Untick 
   the box on the bottom left to show all plugins.

Python
======

OpenCOR version 0.7 introduced support for Python scripting, both within the application itself (see the Python console in :numref:`Fig. %s<ocr_tut_main_win>`) and from Python scripts outside the application.
Comprehensive description of this capability is provided on the OpenCOR `Python support page <https://opencor.ws/user/pythonSupport.html#pythonsupport>`_) and in :ref:`cellml_opencor_pmr_tutorial__opencor_python` we provide some brief guidance.

---------------------------

.. rubric:: Footnotes

.. [#] http://opencor.ws/user/supportedPlatforms.html

.. [#] |cmd| :kbd:`-spacebar` being the equivalent on MacOS.

.. |cmd| unicode:: U+2318

