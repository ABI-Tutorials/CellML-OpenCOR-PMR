
==============================================================================
A model of the sodium channel: Introducing CellML encapsulation and interfaces
==============================================================================

The HH sodium channel has two types of gate, an :math:`m` gate (of which
there are 3) that is initially closed (:math:`m = 0`) before activating
and inactivating back to the closed state, and an :math:`h` gate that is
initially open (:math:`h = 1`) before activating and inactivating back
to the open state. The short period when both types of gate are open
allows a brief window current to pass through the channel. Therefore,

:math:`i_{\text{Na}} = {\overset{\overline{}}{i}}_{\text{Na}}m^{3}h = m^{3}\text{h.}{\overset{\overline{}}{g}}_{\text{Na}}\left( V - E_{\text{Na}} \right)`

where :math:`{\overset{\overline{}}{g}}_{\text{Na}} = \ `\ 120
mS.cm\ :sup:`-2`, and with
:math:`\left\lbrack \text{Na}^{+} \right\rbrack_{i}`\ = 30mM and
:math:`\left\lbrack \text{Na}^{+} \right\rbrack_{o}`\ = 140mM, the
Nernst potential for the sodium channel (z=1) is

:math:`E_{\text{Na}} = \frac{\text{RT}}{\text{zF}}\ln\frac{\left\lbrack \text{Na}^{+} \right\rbrack_{o}}{\left\lbrack \text{Na}^{+} \right\rbrack_{i}} = 25\ \ln\frac{140}{30} = 35\text{mV}`.

The gating kinetics are described by

:math:`\frac{\text{dm}}{\text{dt}} = \alpha_{m}\left( 1 - m \right) - \beta_{m}\text{.m}`;
:math:`\frac{\text{dh}}{\text{dt}} = \alpha_{h}\left( 1 - h \right) - \beta_{h}\text{.h}`

where the voltage dependence of these four rate constants is determined
experimentally to be [34]_

:math:`\alpha_{m} = \frac{- 0.1\left( V + 50 \right)}{e^{\frac{- \left( V + 50 \right)}{10}} - 1}`;
:math:`\beta_{m} = 4e^{\frac{- \left( V + 75 \right)}{18}}`;
:math:`\alpha_{h} = 0.07e^{\frac{- \left( V + 75 \right)}{20}}`;
:math:`\beta_{h} = \frac{1}{e^{\frac{- \left( V + 45 \right)}{10}} + 1}`.

Before we construct a CellML model of the sodium channel, we first
introduce some further CellML concepts that help deal with the
complexity of biological models: first the use of *encapsulation groups*
and *public* and *private* *interfaces* to control the visibility of
information in modular CellML components. To understand encapsulation,
it is useful to use the terms ‘parent’, ‘child’ and ‘sibling’.

We define the CellML components **sodium\_channel\_m\_gate** and
**sodium\_channel\_h\_gate** below. Each of these components has its own
equations (voltage-dependent gates and first order gate kinetics) but
they are both parts of one protein – the sodium channel – and it is
useful to group them into one **sodium\_channel** component as shown on
the right:

We can then talk about the sodium channel as the parent of two children:
the m gate and the h gate, which are therefore siblings. A *private
interface* allows a parent to talk to its children and a *public
interface* allows siblings to talk among themselves and to their parents
(see Figure 22).

**Figure 22**. Children talk to each other as siblings, and to their
parents, via **public** interfaces. But the outside world can only talk
to children through their parents via a **private** interface. Note that
the siblings **m\_gate** and **h\_gate** could talk via a **public**
interface but only if a mapping is established between them (not needed
here).

The OpenCOR *CellML Text* for the HH sodium ion channel is given below.

***Sodium\_ion\_channel.cellml***

**def model sodium\_ion\_channel as**

**def unit** **millisec** as

unit second *{pref: milli}*;

**enddef**;

**def unit per\_millisec** as

unit second *{pref: milli, expo: -1}*;

**enddef**;

**def unit millivolt** as

unit volt *{pref: milli}*;

**enddef**;

**def** **unit per\_millivolt** as

unit millivolt {expo: -1};

**enddef**;

**def** **unit per\_millivolt\_millisec** as

unit per\_millivolt;

unit per\_millisec;

**enddef**;

**def unit microA\_per\_cm2** as

unit ampere *{pref: micro}*;

unit metre *{pref: centi, expo: -2}*;

**enddef**;

**def unit milliS\_per\_cm2** as

unit siemens *{pref: milli}*;

unit metre *{pref: centi, expo: -2}*;

**enddef**;

def **unit mM** as

unit mole *{pref: milli}*;

**enddef**;

**def comp environment** as

var V: millivolt *{pub: out}*;

var t: millisec *{pub: out}*;

V = sel

case (t > 5 *{millisec}*) and (t < 15 *{millisec}*):

-20.0 *{millivolt}*;

otherwise:

-85.0 *{millivolt}*; 

endsel;

**enddef**;

**def** **group as encapsulation** for

**comp** **sodium\_channel** incl

**comp** **sodium\_channel\_m\_gate**;

**comp** **sodium\_channel\_h\_gate**;

endcomp;

**enddef**;

**def comp sodium\_channel** as

var V: millivolt *{pub: in, priv: out}*;

var t: millisec *{pub: in, priv: out }*;

var m: dimensionless *{priv: in}*;

var h: dimensionless *{priv: in}*;

var g\_Na: milliS\_per\_cm2 *{init: 120}*;

var E\_Na: millivolt *{init: 35}*;

var i\_Na: microA\_per\_cm2 *{pub: out}*;

var Nao: mM *{init: 140}*;

var Nai: mM *{init: 30}*;

var RTF: millivolt *{init: 25}*;

var E\_Na: millivolt;

var Na\_conductance: milliS\_per\_cm2 *{pub: out}*;

E\_Na=RTF\*ln(Nao/Nai);

Na\_conductance = g\_Na\*pow(m, 3{dimensionless})\*h);

i\_Na= Na\_conductance\*(V-E\_Na);

**enddef**;

**def comp sodium\_channel\_m\_gate** a s

var V: millivolt *{pub: in}*;

var t: millisec *{pub: in}*;

var alpha\_m: per\_millisec;

var beta\_m: per\_millisec;

var m: dimensionless *{init: 0.05, pub: out}*;

| alpha\_m = 0.1{per\_millivolt\_millisec}\*(V+25{millivolt})
|  /(exp((V+25{millivolt})/10{millivolt})-1{dimensionless});

beta\_m = 4{per\_millisec}\*exp(V/18{millivolt});

ode(m, t) = alpha\_m\*(1{dimensionless}-m)-beta\_m\*m;

**enddef**;

**def comp sodium\_channel\_h\_gate** as

var V: millivolt *{pub: in}*;

var t: millisec *{pub: in}*;

var alpha\_h: per\_millisec;

var beta\_h: per\_millisec;

var h: dimensionless *{init: 0.6, pub: out}*;

alpha\_h = 0.07{per\_millisec}\*exp(V/20{millivolt});

beta\_h =
1{per\_millisec}/(exp((V+30{millivolt})/10{millivolt})+1{dimensionless});

ode(h, t) = alpha\_h\*(1{dimensionless}-h)-beta\_h\*h;

**enddef**;

**def** **map** between **environment** and **sodium\_channel** for

vars V and V;

vars t and t;

**enddef**;

**def** **map** between **sodium\_channel** and
**sodium\_channel\_m\_gate** for

vars V and V;

vars t and t;

vars m and m;

**enddef**;

**def** **map** between **sodium\_channel** and
**sodium\_channel\_h\_gate** for

vars V and V;

vars t and t;

vars h and h;

**enddef**;

**enddef**;

| The results of the OpenCOR computation, with *Ending point* 40 and
  *Point interval* 0.1, are shown in Figure 23 with plots of
  :math:`V\left( t \right)`, :math:`m\left( t \right)`,
  :math:`h\left( t \right)`, :math:`g_{\text{Na}}\left( t \right)` and
  :math:`i_{\text{Na}}(t)` for voltage steps from (a) -85mV to
| -20mV, (b) -85mV to 0mV and (c) -85mV to 20mV. There are several
  things to note:

i.   The kinetics of the m-gate are much faster than the h-gate.

ii.  The opening behaviour is faster as the voltage is stepped to higher
     values since :math:`\tau = \frac{1}{\alpha_{n} + \beta_{n}}`
     reduces with increasing V (see Figure 18).

iii. The sodium channel conductance rises (*activates*) and then falls
     (*inactivates*) under a positive voltage step from rest since the
     three m-gates turn on but the h-gate turns off and the conductance
     is a product of these. Compare this with the potassium channel
     conductance shown in Figure 21 which is only reduced back to zero
     by stepping the voltage back to its resting value – i.e.
     *deactivating* it.

iv.  The only time current :math:`i_{\text{Na}}` flows through the
     sodium channel is during the brief period when the m-gate is
     rapidly opening and the much slower h-gate is beginning to close. A
     small current flows during the reverse voltage step but this is at
     a time when the h-gate is now firmly off so the magnitude is very
     small.

v.   The large sodium current :math:`i_{\text{Na}}` is an inward current
     and hence negative.

Note that the bottom trace does not quite line up at t=0 because the
values shown on the axes are computed automatically and hence can take
more or less space depending on their magnitude.

**Figure 23.** Kinetics of the sodium channel gates for voltage steps to
(a) -20mV, (b) 0mV, and (c) 20mV.

