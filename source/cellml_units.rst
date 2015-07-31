
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

Entropy :math:`S` (J.K:sup:`-1`) is a measure of the number of
microstates available to a system, as defined by Boltzmann’s equation
:math:`S = k_{B}\text{lnW}`, where :math:`W` is the number of ways of
arranging a given distribution of microstates of a system and
:math:`k_{B}` is Boltzmann’s constant [25]_. The driving force for ion
movement is the dispersal of energy into a more probable distribution
(see Figure 12; cf the second law of thermodynamics [26]_).

The energy change :math:`\Delta q` associated with this change of
entropy :math:`\Delta S` at temperature :math:`T` is
:math:`\Delta q = T\Delta S` (J).

For a given volume of fluid the number of microstates :math:`W`
available to a solute (and hence the entropy of the solute) at a high
concentration is less than that for a low concentration [27]_. The
energy difference driving ion movement from a high ion concentration
:math:`\left\lbrack Y^{+} \right\rbrack_{i}` (lower entropy) to a lower
ion concentration :math:`\left\lbrack Y^{+} \right\rbrack_{o}` (higher
entropy) is therefore

:math:`\Delta q = T\Delta S = k_{B}T\left( \ln{\left\lbrack Y^{+} \right\rbrack_{o} - \ln\left\lbrack Y^{+} \right\rbrack_{i}} \right) = k_{B}T\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(J.ion:sup:`-1`) or

:math:`\Delta Q = RT\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(J.mol:sup:`-1`).

| :math:`R = k_{B}N_{A}` ≈ 1.34x10\ :sup:`-23` (J.K:sup:`-1`) x
  6.02x10\ :sup:`23` (mol:sup:`-1`) ≈ 8.4 (J.mol:sup:`-1`\ K\ :sup:`-1`)
  is the ‘universal gas constant’ [28]_.
| At 25°C (298K), :math:`\text{RT}` ≈ 2.5 kJ.mol\ :sup:`-1`.

| Every positively charged ion that crosses the membrane raises the
  potential difference and produces an electrostatic driving force that
  opposes the entropic force (see Figure 13). To move an electron of
  charge *e* (≈1.6x10:sup:`-19`\ C) through a voltage change of
| :math:`\Delta\phi` (V) requires energy :math:`e\Delta\phi` (J) and
  therefore the energy needed to move an ion :math:`Y^{+}` of valence
  *z=1* (the number of charges per ion) through a voltage change of
  :math:`\Delta\phi` is :math:`\text{ze}\Delta\phi`
  *(*\ J.ion\ :sup:`-1`) or
| :math:`\text{ze}N_{A}\Delta\phi` (J.mol:sup:`-1`). Using Faraday’s
  constant :math:`F = eN_{A}`, where
| :math:`F` ≈0.96x10\ :sup:`5` C.mol\ :sup:`-1`, the change in energy
  density at the macroscopic scale is :math:`\text{zF}\Delta\phi`
  (J.mol:sup:`-1`).

No further movement of ions takes place when the force for entropy
driven ion movement exactly equals the opposing electrostatic driving
force associated with charge movement:

:math:`\text{zF}\Delta\phi = \text{RT}\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(J.mol:sup:`-1`) or
:math:`\Delta\phi = E_{Y} = \frac{\text{RT}}{\text{zF}}\ln\frac{\left\lbrack Y^{+} \right\rbrack_{o}}{\left\lbrack Y^{+} \right\rbrack_{i}}`
(J.C:sup:`-1` or V)

where :math:`E_{Y}` is the ‘equilibrium’ or ‘Nernst’ potential for
:math:`Y^{+}`. At 25°C (298K),
:math:`\frac{\text{RT}}{F} = \frac{2.5x10^{3}\ }{0.96x10^{5}}`
(J.C:sup:`-1`) ≈ 25mV.

For an open channel the electrochemical current flow is driven by the
open channel conductance :math:`{\overset{\overline{}}{g}}_{Y}` times
the difference between the transmembrane voltage :math:`V` and the
Nernst potential for that ion:

:math:`{\overset{\overline{}}{i}}_{Y}\mathbf{=}{\overset{\overline{}}{g}}_{Y}\left( V - E_{Y} \right)`.

This defines a linear current-voltage relation (‘Ohms law’) as shown in
Figure 14. The gates to be discussed below modify this open channel
conductance.

To describe the time dependent transition between the closed and open
states of the channel, Hodgkin and Huxley introduced the idea of channel
gates that control the passage of ions through a membrane ion channel.
If the fraction of gates that are open is *y*, the fraction of gates
that are closed is *1-y*, and a first order ODE can be used to describe
the transition between the two states (see Fig.15):

:math:`\frac{\text{dy}}{\text{dt}} = \alpha_{y}\left( 1 - y \right) - \beta_{y}\text{.y}`

where :math:`\alpha_{y}`\ is the opening rate and :math:`\beta_{y}` is
the closing rate.

The solution to this ODE is

:math:`y = \frac{\alpha_{y}}{\alpha_{y} + \beta_{y}} + Ae^{- \left( \alpha_{y} + \beta_{y} \right)t}`

The constant :math:`A` can be interpreted as
:math:`A = y\left( 0 \right) - \frac{\alpha_{y}}{\alpha_{y} + \beta_{y}}`
as in the previous example and, with :math:`y\left( 0 \right) = 0` (i.e.
all gates initially shut), the solution looks like Figure 16(a).

The experimental data obtained by Hodgkin and Huxley for the squid axon,
however, indicated that the initial current flow began more slowly
(Figure 16b) and they modelled this by assuming that the ion channel had
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
physical consistency of all terms in each equation. [29]_

| There are seven base physical quantities defined by the *Système
  International d’Unités* (SI) [30]_.
| These are (with their SI units):

-  **length** (meter or m)

-  **time** (second or s)

-  **amount of substance** (mole)

-  **temperature** (K)

-  **mass** (kilogram or kg)

-  **current** (amp or A)

-  **luminous intensity** (candela).

All other units are derived from these seven. Additional derived units
that CellML defines intrinsically (with their dependence on previously
defined units) are: **Hz** (s:sup:`−1`); **Newton**, N
(kg⋅m⋅s:sup:`−2`); **Joule**, J (N.m); **Pascal**, Pa (N.m:sup:`-2`);
**Watt**, W (J.s:sup:`−1`); **Volt**, V (W.A:sup:`−1`); **Siemen**, S
(A.V:sup:`−1`); **Ohm**, :math:`\Omega` (V.A:sup:`−1`); **Coulomb**, C
(s.A); **Farad**, F (C.V:sup:`−1`); **Weber**, Wb (V.s); and **Henry**,
H (Wb.A:sup:`−1`). Multiples and fractions of these are defined as
follows:

+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+
| Multiples | Prefix |              | deca          | hecto         | kilo          | mega          | giga          | tera           | peta           | exa            | zetta          | yotta          |
+===========+========+==============+===============+===============+===============+===============+===============+================+================+================+================+================+
|           | Symbol |              | da            | h             | k             | M             | G             | T              | P              | E              | Z              | Y              |
+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+
|           | Factor | 10\ :sup:`0` | 10\ :sup:`1`  | 10\ :sup:`2`  | 10\ :sup:`3`  | 10\ :sup:`6`  | 10\ :sup:`9`  | 10\ :sup:`12`  | 10\ :sup:`15`  | 10\ :sup:`18`  | 10\ :sup:`21`  | 10\ :sup:`24`  |
+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+
| Fractions | Prefix |              | deci          | centi         | milli         | micro         | nano          | pico           | femto          | atto           | zepto          | yocto          |
+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+
|           | Symbol |              | d             | c             | m             | μ             | n             | p              | f              | a              | z              | y              |
+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+
|           | Factor | 10\ :sup:`0` | 10\ :sup:`−1` | 10\ :sup:`−2` | 10\ :sup:`−3` | 10\ :sup:`−6` | 10\ :sup:`−9` | 10\ :sup:`−12` | 10\ :sup:`−15` | 10\ :sup:`−18` | 10\ :sup:`−21` | 10\ :sup:`−24` |
+-----------+--------+--------------+---------------+---------------+---------------+---------------+---------------+----------------+----------------+----------------+----------------+----------------+

Units for this model, with multiples and fractions, are illustrated in
the following *CellML Text* code:

**def model first\_order\_model** as

**def unit** **millisec** as

unit second *{pref: milli}*;

**enddef**;

**def unit per\_millisec** as

unit second *{pref: milli, expo: -1}*;

**enddef**;

**def unit millivolt** as

unit volt *{pref: milli}*;

**enddef**;

**def unit microA\_per\_cm2** as

unit ampere *{pref: micro}*;

unit metre *{pref: centi, expo: -2}*;

**enddef**;

**def unit milliS\_per\_cm2** as

unit siemens *{pref: milli}*;

unit metre *{pref: centi, expo: -2}*;

**enddef**;

**def comp ion\_channel** as

var V: millivolt *{init: 0}*;

var t: millisec *{init: 0}*;

var y: dimensionless *{init: 0}*;

var E\_y: millivolt *{init: -85}*;

var i\_y: microA\_per\_cm2;

var g\_y: milliS\_per\_cm2 *{init: 36}*;

var gamma: dimensionless *{init: 4}*;

var alpha\_y: per\_millisec *{init: 1}*;

var beta\_y: per\_millisec *{init: 2}*;

ode(y, t) = alpha\_y\*(1{dimensionless}-y)-beta\_y\*y;

i\_y = g\_y\*pow(y, gamma)\*(V-E\_y);

**enddef**;

**enddef**;

The solution of these equations for the parameters indicated above is
illustrated in Figure 17.

**Figure 17**. The behaviour of an ion channel with :math:`\gamma = 4`
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

