
=============================
Speed comparisons with MATLAB
=============================

Solution speed is important for complex computational models and here we
compare the performance of OpenCOR with MATLAB\ [#]_. Nine
representative CellML models were chosen from the PMR model repository.
For the MATLAB tests we used the MATLAB code, generated automatically
from CellML, that is available on the PMR site. These comparisons are
based on using the default solvers (listed below) available in the two
packages.

-------------------
Testing environment
-------------------

 -  MacBook Pro (Retina, Mid 2012).
 -  Processor: 2.6 GHz Intel Core i7.
 -  Memory: 16 GB 1600 MHz DDR3.
 -  Operating system: OS X Yosemite 10.10.3.

-----------------------------------
`OpenCOR <http://www.opencor.ws/>`_
-----------------------------------

 -  Version: 0.4.1.
 -  Solver: CVODE with its default settings, except for its Maximum step
    parameter, which is set to the model's stimulation duration, if
    needed.

-----------------------------------------------------
`MATLAB <http://www.mathworks.com/products/matlab/>`_
-----------------------------------------------------

 -  Version: R2013a.
 -  Solver: ode15s (i.e. a solver suitable for stiff problems and which
    has low to medium order of accuracy) with both its RelTol and
    AbsTol parameters set to 1e-7 and its MaxStep parameter set to
    the stimulation duration, if needed.

----------------
Testing protocol
----------------

 -  Run a model for a given simulation duration.
 -  Generate simulation data every milliseconds.
 -  Only keep track of all the simulation data (i.e. no graphical
    output).
 -  Run a model 7 times, discard the 2 slowest runs (to account for
    unpredictable slowdowns of the testing machine) and average the
    resulting computational times.
 -  Computational times are obtained directly from OpenCOR and MATLAB
    (through a couple of calls to cputime in the case of MATLAB).

-------
Results
-------

+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| **CellML model**  (from PMR on 18/6/2015)                                                               | **Duration** (s) | **OpenCOR time** (s) | **MATLAB time** (s) | **Time ratio**       |
|                                                                                                         |                  |                      |                     | (MATLAB/OpenCOR)     |
+=========================================================================================================+==================+======================+=====================+======================+
| `Bondarenko et al. 2004 <http://models.cellml.org/e/41>`__                                              | 10               | 1.16                 | 140.14              | 121                  |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Courtemanche et al. 1998 <http://models.cellml.org/exposure/0e03bbe01606be5811691f9d5de10b65>`__       | 100              | 0.998                | 45.720              | 46                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Faber & Rudy 2000 <http://models.cellml.org/exposure/55643f2114a2a463ada007deb9fc3913>`__              | 50               | 0.717                | 29.010              | 40                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Garny et al. 2003 <http://models.cellml.org/exposure/d71105df45dd7030b3c99b2b1e95b8c0>`__              | 100              | 0.996                | 48.180              | 48                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Luo & Rudy 1991 <http://models.cellml.org/exposure/2d2ce7737b42a4f72d6bf8b67f6eb5a2>`__                | 200              | 0.666                | 70.070              | 105                  |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Noble 1962 <http://models.cellml.org/exposure/812eeafbc8ebe97bef435340c80cfcce>`__                     | 1000             | 1.42                 | 310.02              | 218                  |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Noble et al. 1998 <http://models.cellml.org/exposure/a40c4434423c0436e2789a2d457b7ab2>`__              | 100              | 0.834                | 42.010              | 50                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `Nygren et al. 1998 <http://models.cellml.org/exposure/ad761ce160f3b4077bbae7a004c229e3>`__             | 100              | 0.824                | 31.370              | 38                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+
| `ten Tusscher & Panfilov 2006 <http://models.cellml.org/exposure/a7179d94365ff0c9c0e6eb7c6a787d3d>`__   | 100              | 0.969                | 59.080              | 61                   |
+---------------------------------------------------------------------------------------------------------+------------------+----------------------+---------------------+----------------------+

:sup:`\*`\ The value of membrane.stim_end was increased so as to get
action potentials for the duration of the simulation

-----------
Conclusions
-----------

For this range of tests, OpenCOR is between 38 and 218 times faster than MATLAB.
A more extensive evaluation of these results is available on GitHub\ [#]_.

---------------------------

.. rubric:: Footnotes

.. [#] `www.mathworks.com/products/matlab <http://www.mathworks.com/products/matlab>`_

.. [#] `https://github.com/opencor/speedcomparison <https://github.com/opencor/speedcomparison>`_. These tests were carried out by Alan Garny.
