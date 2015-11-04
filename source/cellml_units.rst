.. include:: resources/roles.txt

===================================================================
A model of ion channel gating and current: Introducing CellML units
===================================================================

A good example of a model based on a first order equation is the one
used by Hodgkin and Huxley [10] to describe the gating behaviour of an
ion channel (see also next three sections). Before we describe the
gating behaviour of an ion channel, however, we need to explain the
concepts of the ‘Nernst potential’ and channel conductance.

An ion channel is a protein or protein complex embedded in the bilipid
membrane surrounding a cell and containing a pore through which an ion
:math:`Y^{+}` (or :math:`Y^{-}`) can pass when the channel is open. If
the concentration of this ion is
:math:`\left\lbrack Y^{+} \right\rbrack_{o}` outside the cell and
:math:`\left\lbrack Y^{+} \right\rbrack_{i}` inside the cell, the force
driving an ion through the pore is calculated from the change in
*entropy*.

.. figure:: _static/images/distribution_microstates.png
   :name: ocr_tut_dist_ust
   :alt: Distribution of microstates
   :align: right
   :figwidth: 30%
   :width: 100%
   
   Distribution of microstates in a system [11]. The 16 particles in a confined region (left) have only one possible arrangement (W = 1) and    therefore zero entropy (:math:`k_{B}\text{lnW}=0`). When the barrier is removed and the number of possible locations for each particle increases 4x (right), the number of possible arrangements for the 16 particles increases by 416 and the increase in entropy is therefore :math:`ln(416)` or :math:`16ln4`. The thermal energy (temperature) of the previously confined particles on the left has been redistributed in space to achieve a more probable (higher entropy) state. If we now added more particles to the container on the right, the concentration would increase and the entropy would decrease. 
   
Entropy :math:`S` (:math:`J.K^{-1}`) is a measure of the number of
microstates available to a system, as defined by Boltzmann’s equation
:math:`S = k_{B}\text{lnW}`, where :math:`W` is the number of ways of
arranging a given distribution of microstates of a system and
:math:`k_{B}` is Boltzmann’s constant [*]_. The driving force for ion
movement is the dispersal of energy into a more probable distribution
(see :numref:`ocr_tut_dist_ust`; cf. the second law of thermodynamics [*]_).

The energy change :math:`\Delta q` associated with this change of
entropy :math:`\Delta S` at temperature :math:`T` is
:math:`\Delta q = T\Delta S` (J).

For a given volume of fluid the number of microstates :math:`W`
available to a solute (and hence the entropy of the solute) at a high
concentration is less than that for a low concentration [*]_. The
energy difference driving ion movement from a high ion concentration
:math:`\left\lbrack Y^{+} \right\rbrack_{i}` (lower entropy) to a lower
ion concentration :math:`\left\lbrack Y^{+} \right\rbrack_{o}` (higher
entropy) is therefore

:math:`\Delta q = T\Delta S = k_{B}T\left( \ln{\left\lbrack Y^{+} \right\rbrack_{o} - \ln\left\lbrack Y^{+} \right\rbrack_{i}} \right) = k_{B}T\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(:math:`J.ion^{-1}`)

or

:math:`\Delta Q = RT\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(:math:`J.mol^{-1}`).

:math:`R = k_{B}N_{A} ≈ 1.34x10^{-23} (J.K^{-1}) \text{x}
6.02x10^{23} (mol^{-1}) ≈ 8.4 (J.mol^{-1}K^{-1})`
is the ‘universal gas constant’ [*]_.
At 25°C (298K), :math:`\text{RT}` ≈ 2.5 :math:`kJ.mol^{-1}`.

.. figure:: _static/images/balance_forces.png
   :name: ocr_tut_bal_force
   :alt: Balance of entropic and electrostatic forces
   :align: right
   :figwidth: 30%
   :width: 100%
   
   The balance between :purple:`entropic` and :red:`electrostatic` forces determines the Nernst potential.
   
Every positively charged ion that crosses the membrane raises the
potential difference and produces an electrostatic driving force that
opposes the entropic force (see :numref:`ocr_tut_bal_force`). To move an electron of
charge *e* (:math:`≈1.6x10^{-19}` C) through a voltage change of
:math:`\Delta\phi` (V) requires energy :math:`e\Delta\phi` (J) and
therefore the energy needed to move an ion :math:`Y^{+}` of valence
*z=1* (the number of charges per ion) through a voltage change of
:math:`\Delta\phi` is :math:`\text{ze}\Delta\phi`
(:math:`J.ion^{-1}`) or
:math:`\text{ze}N_{A}\Delta\phi` (:math:`J.mol^{-1}`). Using Faraday’s
constant :math:`F = eN_{A}`, where
:math:`F ≈ 0.96x10^{5} C.mol^{-1}`, the change in energy
density at the macroscopic scale is :math:`\text{zF}\Delta\phi`
(:math:`J.mol^{-1}`).

No further movement of ions takes place when the force for entropy
driven ion movement exactly equals the opposing electrostatic driving
force associated with charge movement:

:math:`\text{zF}\Delta\phi = \text{RT}\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(:math:`J.mol^{-1}`) or
:math:`\Delta\phi = E_{Y} = \frac{\text{RT}}{\text{zF}}\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(:math:`J.C^{-1}` or V)

where :math:`E_{Y}` is the ‘equilibrium’ or ‘Nernst’ potential for
:math:`Y^{+}`. At 25°C (298K),
:math:`\frac{\text{RT}}{F} = \frac{2.5x10^{3}\ }{0.96x10^{5}}`
(:math:`J.C^{-1}`) ≈ 25mV.

.. figure:: _static/images/open_ch_linear_iv.png
   :name: ocr_tut_open_ch_iv
   :alt: Open channel linear IV
   :align: right
   :figwidth: 30%
   :width: 100%
   
   Open channel linear current-voltage relation
   
For an open channel the electrochemical current flow is driven by the
open channel conductance :math:`{\overset{\overline{}}{g}}_{Y}` times
the difference between the transmembrane voltage :math:`V` and the
Nernst potential for that ion:

:math:`{\overset{\overline{}}{i}}_{Y}\mathbf{=}{\overset{\overline{}}{g}}_{Y}\left( V - E_{Y} \right)`.

This defines a linear current-voltage relation (‘Ohms law’) as shown in
:numref:`ocr_tut_open_ch_iv`. The gates to be discussed below modify this open channel
conductance.

.. figure:: _static/images/ion_ch_gating.png
   :name: ocr_tut_ion_ch_gating
   :alt: Ion channel gating kinetics
   :align: right
   :figwidth: 30%
   :width: 100%
   
   Ion channel gating kinetics. y is the fraction of gates in the open state. α_y and β_y  are the rate constants for opening and closing, respectively.
   
.. figure:: _static/images/transient_beh_gates.png
   :name: ocr_tut_trans_gate_beh
   :alt: Transient gate behaviour
   :align: right
   :figwidth: 30%
   :width: 100%
   
   Transient behaviour for one gate (left) and γ gates in series (right). Note that the right hand graph has an initial S-shaped increase, reflecting the multiple gates in series.
   
To describe the time dependent transition between the closed and open
states of the channel, Hodgkin and Huxley introduced the idea of channel
gates that control the passage of ions through a membrane ion channel.
If the fraction of gates that are open is *y*, the fraction of gates
that are closed is :math:`1-y`, and a first order ODE can be used to describe
the transition between the two states (see :numref:`ocr_tut_ion_ch_gating`):

:math:`\frac{\text{dy}}{\text{dt}} = \alpha_{y}\left( 1 - y \right) - \beta_{y}\text{.y}`

where :math:`\alpha_{y}`\ is the opening rate and :math:`\beta_{y}` is
the closing rate.

The solution to this ODE is

:math:`y = \frac{\alpha_{y}}{\alpha_{y} + \beta_{y}} + Ae^{- \left( \alpha_{y} + \beta_{y} \right)t}`

The constant :math:`A` can be interpreted as
:math:`A = y\left( 0 \right) - \frac{\alpha_{y}}{\alpha_{y} + \beta_{y}}`
as in the previous example and, with :math:`y\left( 0 \right) = 0` (i.e.
all gates initially shut), the solution looks like :numref:`Fig. %s(a) <ocr_tut_trans_gate_beh>`.

The experimental data obtained by Hodgkin and Huxley for the squid axon,
however, indicated that the initial current flow began more slowly
(:numref:`Fig. %s(b) <ocr_tut_trans_gate_beh>`) and they modelled this by assuming that the ion channel had
:math:`\gamma` gates in series so that conduction would only occur when
all gates were at least partially open. Since :math:`y` is the
probability of a gate being open, :math:`y^{\gamma}` is the probability
of all :math:`\gamma` gates being open (since they are assumed to be
independent) and the current through the channel is

:math:`i_{Y} = {\overset{\overline{}}{i}}_{Y}y^{\gamma} = y^{\gamma}{\overset{\overline{}}{g}}_{Y}\left( V - E_{Y} \right)`

where
:math:`{\overset{\overline{}}{i}}_{Y}{= \overset{\overline{}}{g}}_{Y}\left( V - E_{Y} \right)`
is the steady state current through the open gate.

We can represent this in OpenCOR with a simple extension of the first
order ODE model, but in developing this model we will also demonstrate
the way in which CellML deals with units.

Note that the decision to deal with units in CellML, rather than just
ignoring them or insisting that all equations are represented in
dimensionless form, was made in order to be able to be able to check the
physical consistency of all terms in each equation. [*]_

There are seven base physical quantities defined by the *International d’Unités* (SI) [*]_.  These are (with their SI units):

-  **length** (meter or m)

-  **time** (second or s)

-  **amount of substance** (mole)

-  **temperature** (K)

-  **mass** (kilogram or kg)

-  **current** (amp or A)

-  **luminous intensity** (candela).

All other units are derived from these seven. Additional derived units
that CellML defines intrinsically (with their dependence on previously
defined units) are: **Hz** (:math:`s^{-1}`); **Newton**, N
(:math:`kg⋅m⋅s^{-1}`); **Joule**, J (:math:`N.m`); **Pascal**, Pa (:math:`N.m^{-2}`);
**Watt**, W (:math:`J.s^{-1}`); **Volt**, V (:math:`W.A^{-1}`); **Siemen**, S
(:math:`A.V^{-1}`); **Ohm**, :math:`\Omega` (:math:`V.A^{-1}`); **Coulomb**, C
(:math:`s.A`); **Farad**, F (:math:`C.V^{-1}`); **Weber**, Wb (:math:`V.s`); and **Henry**,
H (:math:`Wb.A^{-1}`). Multiples and fractions of these are defined as
follows:

+-----------+--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
|           | Prefix |                | deca            | hecto         | kilo            | mega            | giga            | tera             | peta              | exa              | zetta            | yotta            |
+           +--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
| Multiples | Symbol |                | da              | h             | k               | M               | G               | T                | P                 | E                | Z                | Y                |
+           +--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
|           | Factor | :math:`10^0`   | :math:`10^{1}`  | :math:`10^{2}`| :math:`10^{3}`  | :math:`10^{6}`  | :math:`10^{9}`  | :math:`10^{12}`  | :math:`10^{15}`   | :math:`10^{18}`  | :math:`10^{21}`  | :math:`10^{24}`  |
+-----------+--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
|           | Prefix |                | deci            | centi         | milli           | micro           | nano            | pico             | femto             | atto             | zepto            | yocto            |
+           +--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
| Fractions | Symbol |                | d               | c             | m               | μ               | n               | p                | f                 | a                | z                | y                |
+           +--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+
|           | Factor | :math:`10^{0}` | :math:`10^{−1}` |:math:`10^{-2}`| :math:`10^{−3}` | :math:`10^{−6}` | :math:`10^{−9}` | :math:`10^{−12}` | :math:`10^{−15}`  | :math:`10^{−18}` | :math:`10^{−21}` | :math:`10^{−24}` |
+-----------+--------+----------------+-----------------+---------------+-----------------+-----------------+-----------------+------------------+-------------------+------------------+------------------+------------------+

Units for this model, with multiples and fractions, are illustrated in
the following *CellML Text* code:

.. code-block:: cell
   :linenos:
   :emphasize-lines: 29,30

   def model first_order_model as
       def unit millisec as
           unit second {pref: milli};
       enddef;
       def unit per_millisec as
           unit second {pref: milli, expo: -1};
        enddef;
       def unit millivolt as
           unit volt {pref: milli};
       enddef;
       def unit microA_per_cm2 as
           unit ampere {pref: micro};
           unit metre {pref: centi, expo: -2};
       enddef;
       def unit milliS_per_cm2 as
           unit siemens {pref: milli};
           unit metre {pref: centi, expo: -2};
       enddef;
       def comp ion_channel as
           var V: millivolt {init: 0};
           var t: millisec {init: 0};
           var y: dimensionless {init: 0};
           var E_y: millivolt {init: -85};
           var i_y: microA_per_cm2;
           var g_y: milliS_per_cm2 {init: 36};
           var gamma: dimensionless {init: 4};
           var alpha_y: per_millisec {init: 1};
           var beta_y: per_millisec {init: 2};
           ode(y, t) = alpha_y*(1{dimensionless}-y)-beta_y*y;
           i_y = g_y*pow(y, gamma)*(V-E_y);
        enddef;
   enddef;

|  **Line 2:** Define units for time as millisecs
|  **Line 5:** Define per_millisec units
|  **Line 8:** Define units for voltage as millivolts
|  **Line 11:** Define units for current as microAmps per cm\ :sup:`2`
|  **Line 15:** Define units for conductance as milliSiemens per cm\ :sup:`2`
|  **Lines 20-28:** Define units and initial conditions for variables
|  **Line 29:** Define ODE for gating variable y
|  **Line 30:** Define channel current

The solution of these equations for the parameters indicated above is
illustrated in :numref:`ocr_tut_ocr_4_ion_ch`.

.. figure:: _static/images/opencor_four_gate_ion_channel.png
   :name: ocr_tut_ocr_4_ion_ch
   :alt: OpenCOR solution to 4 gate ion channel model
   :align: center
   
   The behaviour of an ion channel with :math:`\gamma = 4`
   gates transitioning from the closed to the open state at a membrane
   voltage :math:`V = 0`. The opening and closing rate constants are
   :math:`\alpha_{y} = 1` ms\ :sup:`-1` and :math:`\beta_{y} = 2`
   ms\ :sup:`-1`. The ion channel has an open conductance of
   :math:`{\overset{\overline{}}{g}}_{Y} = 36` mS.cm\ :sup:`-2` and an
   equilibrium potential of :math:`E_{Y} = - 85` mV. The upper transient is
   the response :math:`y\left( t \right)` for each gate and the lower trace
   is the current through the channel. Note the slow start to the current
   trace in comparison with the single gate transient
   :math:`y\left( t \right)`.

The model of a gated ion channel presented here is used in the next two
sections for the neural potassium and sodium channels and then in
Section 11 for cardiac ion channels. The gates make the channel
conductance time dependent and, as we will see in the next section, the
experimentally observed voltage dependence of the gating rate constants
:math:`\alpha_{y}` and :math:`\beta_{y}` means that the channel
conductance (including the open channel conductance) is voltage
dependent. For a partially open channel (:math:`y < 1`), the steady
state conductance is
:math:`\left( y_{\infty} \right)^{\gamma}{.\overset{\overline{}}{g}}_{Y}`,
where :math:`y_{\infty} = \frac{\alpha_{y}}{\alpha_{y} + \beta_{y}}`.
Moreover the gating time constants
:math:`\tau = \frac{1}{\alpha_{y} + \beta_{y}}` are therefore also
voltage dependent. Both of these voltage dependent factors of ion
channel gating are important in explaining channel properties, as we
show now for the neural potassium and sodium ion channels.

---------------------------

.. rubric:: Footnotes

.. [*]
   The Brownian motion of individual molecules has energy :math:`k_{B}T`
   (J), where the Boltzmann constant :math:`k_{B}` is approximately
   :math:`1.34x10^{-23}` (:math:`J.K^{-1}`). At 25°C, or 298K, :math:`k_{B}T`
   = :math:`4.10^{-21}` (J) is the minimum amount of energy to contain a
   ‘bit’ of information at that temperature.

.. [*]
   The *first law of thermodynamics* states that energy is conserved,
   and the *second law* (that natural processes are accompanied by an
   increase in entropy of the universe) deals with the distribution of
   energy in space.

.. [*]
   At infinitely high concentration the specified volume is jammed
   packed with solute and the entropy is zero.

.. [*]
   :math:`N_{A}` is Avogadro’s number (:math:`6.023x10^{23}`) and is the
   scaling factor between molecular and macroscopic processes.
   Boltzmann’s constant :math:`k_{B}` and electron charge *e* operate at
   the atomic/molecular scale. Their effect at the physiological scale
   is via the universal gas constant :math:`R = k_{B}N_{A}` and
   Faraday’s constant :math:`F = eN_{A}`.

.. [*]
   It is well accepted in engineering analysis that thinking about and
   dealing with units is a key aspect of modelling. Taking the ratio of
   dimensionally consistent terms provides non-dimensional numbers which
   can be used to decide when a term in an equation can be omitted in
   the interests of modelling simplicity. We investigate this idea
   further in a later section.

.. [*] http://en.wikipedia.org/wiki/International_System_of_Units


