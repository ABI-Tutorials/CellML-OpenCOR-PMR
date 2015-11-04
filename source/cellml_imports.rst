
.. _ocr_tut_intro_cellml_imports:

=================================================================
A model of the nerve action potential: Introducing CellML imports
=================================================================

Here we describe the first (and most famous) model of nerve fibre
electrophysiology based on the membrane ion channels that we have
discussed in the last two sections. This is the work by Alan Hodgkin and
Andrew Huxley in 1952 [10] that won them (together with John Eccles) the
1963 Noble prize in Physiology or Medicine for *"their discoveries
concerning the ionic mechanisms involved in excitation and inhibition in
the peripheral and central portions of the nerve cell membrane"*.

***Cable equation***

The *cable equation* was developed in 1890 [35]_ to predict the
degradation of an electrical signal passing along the transatlantic
cable. It is derived as follows:

If the voltage is raised at the left hand end of the cable (shown by the
deep red in Figure 24), a current :math:`i_{a}` (A) will flow that
depends on the voltage gradient, given by
:math:`\frac{\partial V}{\partial x}` (V.m:sup:`-1`) and the resistance
:math:`r_{a}` (Ω.m:sup:`-1`), Ohm’s law gives
:math:`- \frac{\partial V}{\partial x} = r_{a}i_{a}` . But if the cable
leaks current :math:`i_{m}` (A.m:sup:`-1`) per unit length of cable,
conservation of current gives
:math:`\frac{\partial i_{a}}{\partial x} = i_{m}` and therefore,
substituting for :math:`i_{a}` ,
:math:`\frac{\partial}{\partial x}\left( - \frac{1}{r_{a}}\frac{\partial V}{\partial x} \right) = i_{m}`
. There are two sources of membrane current :math:`i_{m}` , one
associated with the capacitance :math:`C_{m}`
(:math:`\approx 1\mu F/\text{cm}^{2}`) of the membrane,
:math:`C_{m}\frac{\partial V}{\partial t}`, and one associated with
holes or channels in the membrane, :math:`i_{\text{leak}}`. Inserting
these into the RHS gives

:math:`\frac{\partial}{\partial x}\left( - \frac{1}{r_{a}}\frac{\partial V}{\partial x} \right) = i_{m} = C_{m}\frac{\partial V}{\partial t} + i_{\text{leak}}`

Rearranging gives the *cable equation* (for constant :math:`r_{a}`):

:math:`C_{m}\frac{\partial V}{\partial t} = - \frac{1}{r_{a}}\frac{\partial^{2}V}{\partial x^{2}} - i_{\text{leak}}`

where all terms represent *current density* (current per membrane area)
and have units of :math:`\mu A/\text{cm}^{2}`.

***Action potentials***

The cable equation can be used to model the propagation of an action
potential along a neuron or any other excitable cell. The ‘leak’ current
is associated primarily with the inward movement of sodium ions through
the membrane ‘sodium channel’, giving the **inward** membrane current
:math:`i_{\text{Na}}`, and the outward movement of potassium ions
through a membrane ‘potassium channel’, giving the **outward** current
:math:`i_{K}` (see Figure 25). A further small leak current
:math:`i_{L} = g_{L}\left( V - E_{L} \right)` associated with chloride
and other ions is also included.

When the membrane potential :math:`V` rises due to axial current flow,
the Na channels open and the K channels close, such that the membrane
potential moves towards the Nernst potential for sodium. The subsequent
decline of the Na channel conductance and the increasing K channel
conductance as the voltage drops rapidly repolarises the membrane to its
resting potential of -85mV (see Figure 26).

We can neglect [36]_ the term
(:math:`- \frac{1}{r_{a}}\frac{\partial^{2}V}{\partial x^{2}}`) (the
rate of change of axial current along the cable) for the present models
since we assume the whole cell is clamped with an axially uniform
potential. We can therefore obtain the membrane potential :math:`V` by
integrating the first order ODE

|image18|\ :math:`\frac{\text{dV}}{\text{dt}} = - \left( i_{\text{Na}} + \ i_{K} + i_{L} \right)/C_{m}`.

**Figure 27**. A schematic cell diagram describing the current flows
across the cell bilipid membrane that are captured in the Hodgkin-Huxley
model. The membrane ion channels are a sodium (Na:sup:`+`) channel, a
potassium (K:sup:`+`) channel, and a leakage (L) channel (for chloride
and other ions) through which the currents I\ :sub:`Na`, I\ :sub:`K` and
I\ :sub:`L` flow, respectively.

We use this example to demonstrate the importing feature of CellML.
CellML *imports* are used to bring a previously defined CellML model of
a component into the new model (in this case the Na and K channel
components defined in the previous two sections, together with a leakage
ion channel model specified below). Note that importing a component
brings the children components with it along with their connections and
units, but it does not bring the siblings of that component with it.

To establish a CellML model of the HH equations we first lay out the
model components with their public and private interfaces (Figure 28).

**Figure 28**. Overall structure of the HH CellML model showing the
encapsulation hierarchy (**purple**), the CellML model imports
(**blue**) and the other key parts (**units**, **components** &
**mappings**) of the top level CellML model.

The HH model is the top level model. The *CellML Text* code for the HH
model, together with the leakage\_channel model, is given on the next
page. The imported potassium\_ion\_channel model and
sodium\_ion\_channel model are unchanged from the previous sections

***HH.cellml***

**def model HH as**

**def** **import** using "sodium\_ion\_channel.cellml" for

comp Na\_channel using comp sodium\_channel;

**enddef**;

**def** **import** using "potassium\_ion\_channel.cellml" for

comp K\_channel using comp potassium\_channel;

**enddef**;

**def** **import** using "leakage\_ion\_channel.cellml" for

comp L\_channel using comp leakage\_channel;

**enddef**;

**def** **unit millisec** as

unit second {pref: milli};

**enddef**;

**def** **unit millivolt** as

unit volt {pref: milli};

**enddef**;

**def** **unit microA\_per\_cm2** as

unit ampere {pref: micro};

unit metre {pref: centi, expo: -2};

| **enddef**;
|  **def** **unit microF\_per\_cm2** as

unit farad {pref: micro};

unit metre {pref: centi, expo: -2};

**enddef**;

**def** **group as encapsulation** for

**comp membrane** incl

**comp Na\_channel**;

**comp K\_channel**;

**comp L\_channel**;

endcomp;

**enddef**;

**def** **comp environment** as

var V: millivolt {init: -85, pub: out};

var t: millisec {pub: out};

**enddef**;

**def** **map** between **environment** and **membrane** for

vars V and V;

vars t and t;

**enddef**;

**def** **map** between **membrane** and **Na\_channel** for

vars V and V;

vars t and t;

vars i\_Na and i\_Na;

**enddef**;

**def** **map** between **membrane** and **K\_channel** for

vars V and V;

vars t and t;

vars i\_K and i\_K;

**enddef**;

**def** **map** between **membrane** and **L\_channel** for

vars V and V;

vars i\_L and i\_L;

**enddef**;

**def** **comp membrane** as

var V: millivolt {pub: in, priv: out};

var t: millisec {pub: in, priv: out};

var i\_Na: microA\_per\_cm2 {pub: out, priv: in};

var i\_K: microA\_per\_cm2 {pub: out, priv: in};

var i\_L: microA\_per\_cm2 {pub: out, priv: in};

var Cm: microF\_per\_cm2 {init: 1};

var i\_Stim: microA\_per\_cm2;

var i\_Tot: microA\_per\_cm2;

i\_Stim = sel

case (t >= 1{millisec}) and (t <= 1.2{millisec}):

100{microA\_per\_cm2};

otherwise:

0{microA\_per\_cm2};

endsel;

i\_Tot = i\_Stim + i\_Na + i\_K + i\_L;

ode(V,t) = -i\_Tot/Cm;

**enddef**;

**enddef**;

**def model leakage\_ion\_channel as**

**def** **unit millisec** as

unit second {pref: milli};

**enddef**;

**def** **unit millivolt** as

unit volt {pref: milli};

**enddef**;

**def** **unit per\_millivolt** as

unit millivolt {expo: -1};

**enddef**;

**def** **unit microA\_per\_cm2** as

unit ampere {pref: micro};

unit metre {pref: centi, expo: -2};

**enddef**;

**def** **unit milliS\_per\_cm2** as

unit siemens {pref: milli};

unit metre {pref: centi, expo: -2};

**enddef**;

**def** **comp environment** as

var V: millivolt {init: 0, pub: out};

var t: millisec {pub: out};

**enddef**;

**def** **map** between **leakage\_channel** and **environment** for

vars V and V;

**enddef**;

**def** **comp leakage\_channel** as

var V: millivolt {pub: in};

var i\_L: microA\_per\_cm2 {pub: out};

var g\_L: milliS\_per\_cm2 {init: 0.3};

var E\_L: millivolt {init: -54.4};

i\_L = g\_L\*(V-E\_L);

**enddef**;

**enddef**;

Note that the CellML Text code for the potassium channel is on page 17
and for the sodium channel is on page 21.

Note that the only units that need to be defined for this top level HH
model are the ones explicitly required for the membrane component. All
the other units, required for the various imported sub-models, are
imported along with the imported components.

The results generated by the HH model are shown in Figure 29.

**Figure 29**. Results from OpenCOR for the Hodgkin Huxley (HH) CellML
model. The top panel shows the generated action potential. Note that the
stimulus current is not really needed as the background outward leakage
current is enough to drive the membrane potential up to the threshold
for sodium channel opening.

**Important note**

It is often convenient to have the sub-models – in this case the
sodium\_ion\_channel.cellml model, the potassium\_ion\_channel.cellml
model and the leakage\_ion\_channel.cellml model - loaded into OpenCOR
at the same time as the high level model (HH.cellml), as shown in Figure
30. If you make changes to a model in the *CellML Text* view, you must
save the file (*CTRL-S*) before running a new simulation since the
simulator works with the saved model. Furthermore, a change to a
sub-model will only affect the high level model which imports it if you
also save the high level model (or use the *Reload* option under the
File menu). An asterisk appears next to the name of a file when a change
has been made and the file has not been saved. The asterisk disappears
when the file is saved.

|image19|

**Figure 30.** The HH.cellml model and its three sub-models are
available under separate tabs in OpenCOR.

