
=======================================================================
A model of the cardiac action potential: Importing units and parameters
=======================================================================

We now examine the Noble 1962 model [12] that applied the Hodgkin-Huxley
approach to cardiac cells and thereby initiated the development of a
long line of cardiac cell models that, in their human cell formulation,
are now used clinically and are the most sophisticated models of any
cell type. It was the incorporation of these models into whole heart
bioengineering models that initiated the Physiome Project. We also
illustrate the use of imported units and imported parameter sets.

Cardiac cells have similar gradients of potassium and sodium ions that
operate in a similar way to neurons (as do all electrically active
cells). There is one major difference, however, in the potassium channel
that holds the cells in their resting state at -85mV (HH neuron) or
-100mV (cardiac Purkinje cells). This difference is illustrated in
Figure 31a. When the membrane potential is raised above the equilibrium
potential for potassium, the cardiac channel conductance shown by the
dashed line drops to nearly zero – i.e. it is an *inward rectifier*
since it rectifies (‘cuts off’) the outward current that otherwise would
have flowed through the channel at that potential. This is an
evolutionary adaptation of the potassium channel to avoid loss of
potassium ions out of the cell during the long plateau phase of the
cardiac action potential (Figure 31b) needed to give the heart time to
contract. This evolutionary change saves the additional energy that
would otherwise be needed to pump potassium ions back into the cell, but
this Faustian “pact with the devil” is also the reason the heart is so
susceptible to conduction failure (more on this later). To explain his
data on Purkinje cells Noble [12] postulated the existence of two inward
rectifier potassium channels, one with a conductance :math:`g_{K1}` that
showed voltage dependence but no significant time dependence and another
with conductance :math:`g_{K2}` that showed less severe rectification
with time dependent gating similar to the HH four-gated potassium
channel.

(a) (b)

**Figure 31**. Current-voltage relations (a) around the equilibrium
potentials for the potassium and sodium channels in cardiac cells. The
sodium channel is similar to the one in neurons but the two potassium
channels have an inward rectifying property that stops leakage of
potassium ions out of the cell when the membrane potential (illustrated
in (b)) is high during the plateau phase of the cardiac action
potential.

To model the cardiac action potential in Purkinje fibres (a cardiac cell
specialised for rapid conduction from the atrio-ventricular node to the
apical ventricular myocardial tissue), Noble [12] proposed two potassium
channels (one of these being the inwardly rectifying potassium channel
described above and the other called the delayed potassium channel), one
sodium channel (very similar to the HH neuronal sodium channel) and one
leakage channel (also similar to the HH one).

The equations for these are as follows: (as for the HH model, time is in
ms, voltages are in mV, concentrations are in mM, conductances are in
mS, currents are in µA and capacitance is in µF).

***Inward rectifying*** :math:`\mathbf{i}_{\mathbf{K}\mathbf{1}}`
***potassium channel** (voltage dependent only)*

:math:`i_{K1} = g_{K1}\left( V - E_{K} \right)`, with
:math:`E_{K} = \frac{\text{RT}}{\text{zF}}\ln\frac{\left\lbrack K^{+} \right\rbrack_{o}}{\left\lbrack K^{+} \right\rbrack_{i}} = 25\ \ln\frac{2.5}{140} = - 100\text{mV}`.

:math:`g_{K1} = 1.2e^{\frac{- \left( V + 90 \right)}{50}} + 0.015e^{\frac{\left( V + 90 \right)}{60}}`

***Inward rectifying*** :math:`\mathbf{i}_{\mathbf{K}\mathbf{2}}`
***potassium channel** (voltage and time dependent)*\  [37]_

:math:`i_{K2} = g_{K2}\left( V - E_{K} \right)`.

:math:`g_{K2} = 1.2n^{4}`

:math:`\frac{\text{dn}}{\text{dt}} = \alpha_{n}\left( 1 - n \right) - \beta_{n}\text{.n}`,
where
:math:`\alpha_{n} = \frac{- 0.0001\left( V + 50 \right)}{e^{\frac{- \left( V + 50 \right)}{10}} - 1}`
and :math:`\beta_{n} = 0.002e^{\frac{- \left( V + 90 \right)}{80}}`.

Note that the rate constants here reflect a much slower onset of the
time dependent change in conductance than in the HH potassium channel.

***Sodium channel***

:math:`i_{\text{Na}} = \left( g_{\text{Na}} + 140 \right)\left( V - E_{\text{Na}} \right)`,
with
:math:`E_{\text{Na}} = \frac{\text{RT}}{\text{zF}}\ln\frac{\left\lbrack \text{Na}^{+} \right\rbrack_{o}}{\left\lbrack \text{Na}^{+} \right\rbrack_{i}} = 25\ \ln\frac{140}{30} = 35\text{mV}`.

:math:`g_{\text{Na}} = m^{3}\text{h.}g_{Na\_ max}` where
:math:`g_{Na\_ max} = 400\text{mS}.`

:math:`\frac{\text{dm}}{\text{dt}} = \alpha_{m}\left( 1 - m \right) - \beta_{m}\text{.m}`,
where
:math:`\alpha_{m} = \frac{- 0.1\left( V + 48 \right)}{e^{\frac{- \left( V + 48 \right)}{15}} - 1}`
and
:math:`\beta_{m} = \frac{0.12\left( V + 8 \right)}{e^{\frac{\left( V + 8 \right)}{5}} - 1}`

:math:`\frac{\text{dh}}{\text{dt}} = \alpha_{h}\left( 1 - h \right) - \beta_{h}\text{.h}`,
where :math:`\alpha_{h} = 0.17e^{\frac{- \left( V + 90 \right)}{20}}`
and
:math:`\beta_{h} = \frac{1}{1 + e^{\frac{- \left( V + 42 \right)}{10}}}`

***Leakage channel ***

:math:`i_{\text{leak}} = g_{L}\left( V - E_{L} \right)`, with
:math:`E_{L} = - 60mV` and :math:`g_{L} = 0.075\text{mS}`.

***Membrane equation ***

:math:`\frac{\text{dV}}{\text{dt}} = - \left( i_{\text{Na}} + i_{K1} + i_{K2} + i_{\text{leak}} \right)/C_{m}`
where :math:`C_{m} = 12\text{μF}`. [38]_

Figure 32 shows the structure of the model, including separate files for
units, parameters, and the three ion channels (the two potassium
channels are lumped together). We include the Nernst equations
dependence on potassium and sodium ion concentrations in order to
demonstrate the use of parameter values, defined in a separate
parameters file, that are read in at the top (whole cell model) level
and passed down to the individual ion channel models.

**Figure 32**. Overall structure of the Noble62 CellML model showing the
encapsulation hierarchy (**purple**), the CellML model imports
(**blue**) and the other key parts (**units**, **components** &
**mappings**) of the top level CellML model. Note that the overall
structure of the Noble62 model differs from that of the earlier HH model
in that all units are defined in a units file and imported where needed
(shown by the **red arrows**). Also the ion concentration parameters are
defined in a parameters file and imported into the top level file but
passed down to the modules that use them via the mappings.

The CellML Text code for all six files is shown on the following two
pages. The arrows indicate the imports (appropriately colour coded for
**units**, **components**, and **parameters**).

Graphical outputs from solution of the Noble 1962 model with OpenCOR for
5000ms are shown in Figure 33.

Interpretation of the model outputs is given in the Figure 33 legend.
The Noble62 model was developed further by Noble and others to include
additional sodium and potassium channels, calcium channels (needed for
excitation-contraction coupling), chloride channels and various ion
exchange mechanisms (Na/Ca, Na/H), co-transporters (Na/Cl, K/Cl) and
energy (ATP)-dependent pumps (Na/K, Ca) needed to model the observed
beat by beat changes in intracellular ion concentrations. These are
discussed further in Section 15.

***Noble\_1962.cellml***

**def model Noble\_1962** as

**def** **import** using "Noble62\_Na\_channel.xml" for

comp **Na\_channel** using comp sodium\_channel;

**enddef**;

**def** **import** using "Noble62\_K\_channel.xml" for

comp **K\_channel** using comp potassium\_channel;

**enddef**;

**def** **import** using "Noble62\_L\_channel.xml" for

comp **L\_channel** using comp leakage\_channel;

**enddef**;

**def** **import** using "Units\_for\_Noble62.xml" for

unit mV using unit mV;

unit ms using unit ms;

unit nanoF using unit nanoF;

unit nanoA using unit nanoA;

**enddef**;

**def** **import** using "Parameters\_for\_Noble62.xml" for

comp **parameters** using comp parameters;

**enddef**;

**def** **map** between **parameters** and **membrane** for

vars Ki and Ki;

vars Ko and Ko;

vars Nai and Nai;

vars Nao and Nao;

**enddef**;

**def** **comp** **environment** as

var t: ms {init: 0, pub: out};

**enddef**;

**def** **group** as encapsulation for

comp **membrane** incl

comp **Na\_channel**;

comp **K\_channel**;

comp **L\_channel**;

endcomp;

**enddef**;

def **comp** **membrane** as

var V: mV {init: -85, pub: out, priv: out};

var t: ms {pub: in, priv: out};

var Cm: nanoF {init: 12000};

var Ki: mM {pub: in, priv: out};

var Ko: mM {pub: in, priv: out};

var Nai: mM {pub: in, priv: out};

var Nao: mM {pub: in, priv: out};

var i\_Na: nanoA {pub: out, priv: in};

var i\_K: nanoA {pub: out, priv: in};

var i\_L: nanoA {pub: out, priv: in};

ode(V, t) = -(i\_Na+i\_K+i\_L)/Cm;

**enddef**;

**def** **map** between **environment** and **membrane** for

vars t and t;

enddef;

**def** **map** between **membrane** and **Na\_channel** for

vars V and V;

vars t and t;

vars Nai and Nai;

vars Nao and Nao;

vars i\_Na and i\_Na;

**enddef**;

**def** **map** between **membrane** and **K\_channel** for

vars V and V;

vars t and t;

vars Ki and Ki;

vars Ko and Ko;

vars i\_K and i\_K;

**enddef**;

**def** **map** between **membrane** and **L\_channel** for

vars V and V;

vars i\_L and i\_L;

**enddef**;

**enddef**;

***Units\_for\_Noble62.xml***

**def model units\_for\_Noble62** as

**def** **unit ms** as

unit second {pref: milli};

**enddef**;

**def** **unit per\_ms** as

unit second {pref: milli, expo: -1};

**enddef**;

**def** **unit mV** as

unit volt {pref: milli};

enddef;

**def** **unit mM** as

unit mole {pref: milli};

**enddef**;

**def** **unit per\_mV** as

unit volt {pref: milli, expo: -1};

**enddef**;

**def** **unit per\_mV\_ms** as

unit mV {expo: -1};

unit ms {expo: -1};

**enddef**;

**def** **unit microS** as

unit siemens {pref: micro};

**enddef**;

**def** **unit nanoF** as

unit farad {pref: nano};

**enddef**;

**def** **unit nanoA** as

unit ampere {pref: nano};

**enddef**;

**enddef**;

***Parameters\_for\_Noble62.xml ***

**def** **model parameters\_for\_Noble62** as

**def** **import** using "units\_for\_Noble62.xml" for

unit mM using unit mM;

**enddef**;

**def** **comp parameters** as

var Ki: mM {init: 140, pub: out};

var Ko: mM {init: 2.5, pub: out};

var Nai: mM {init: 30, pub: out};

var Nao: mM {init: 140, pub: out};

**enddef**;

**enddef**;

***Noble62\_L\_channel.xml***

**def model leakage\_ion\_channel** as

**def import** using "Units\_for\_Noble62.xml" for

unit mV using unit mV;

unit ms using unit ms;

unit microS using unit microS;

unit nanoA using unit nanoA;

**enddef**;

**def comp leakage\_channel** as

var V: mV {pub: in};

var g\_L: microS {init: 75};

var E\_L: mV {init: -60};

var i\_L: nanoA {pub: out};

i\_L = g\_L\*(V-E\_L);

**enddef**;

**enddef**;

***Noble62\_Na\_channel.xml***

**def model sodium\_ion\_channel** as

**def** **import** using "Units\_for\_Noble62.xml" for

unit mV using unit mV;

unit ms using unit ms;

unit mM using unit mM;

unit per\_ms using unit per\_ms;

unit per\_mV using unit per\_mV;

unit per\_mV\_ms using unit per\_mV\_ms;

unit microS using unit microS;

unit nanoA using unit nanoA;

**enddef**;

**def** **group** as encapsulation for

comp sodium\_channel incl

comp sodium\_channel\_m\_gate;

comp sodium\_channel\_h\_gate;

endcomp;

enddef;

**def comp** **sodium\_channel** as

var V: mV {pub: in, priv: out};

var t: ms {pub: in, priv: out};

var g\_Na\_max: microS {init: 400000};

var g\_Na: microS;

var E\_Na: mV;

var m: dimensionless {priv: in};

var h: dimensionless {priv: in};

var Nai: mM {pub: in};

var Nao: mM {pub: in};

var RTF: mV {init: 25};

var i\_Na: nanoA {pub: out};

E\_Na = RTF\*ln(Nao/Nai);

g\_Na = pow(m, 3{dimensionless})\*h\*g\_Na\_max;

i\_Na = (g\_Na+140{microS})\*(V-E\_Na);

**enddef**;

**def** **comp** **sodium\_channel\_m\_gate** as

var V: mV {pub: in};

var t: ms {pub: in};

var m: dimensionless {init: 0.01, pub: out};

var alpha\_m: per\_ms;

var beta\_m: per\_ms;

| alpha\_m = -0.10{per\_mV\_ms}\*(V+48{mV})
|  /(exp(-(V+48{mV})/15{mV})-1{dimensionless});

| beta\_m = 0.12{per\_mV\_ms}\*(V+8{mV})
|  /(exp((V+8{mV})/5{mV})-1{dimensionless});

ode(m, t)=alpha\_m\*(1{dimensionless}-m)-beta\_m\*m;

enddef;

def **comp sodium\_channel\_h\_gate** as

var V: mV {pub: in};

var t: ms {pub: in};

var h: dimensionless {init: 0.8, pub: out};

var alpha\_h: per\_ms;

var beta\_h: per\_ms;

alpha\_h = 0.17{per\_ms}\*exp(-(V+90{mV})/20{mV});

| beta\_h = 1.00{per\_ms}
|  /(1{dimensionless}+exp(-(V+42{mV})/10{mV}));

ode(h, t) = alpha\_h\*(1{dimensionless}-h)-beta\_h\*h;

**enddef**;

| **def** **map** between **sodium\_channel**
|  and **sodium\_channel\_m\_gate** for

vars V and V;

vars t and t;

vars m and m;

enddef;

| **def** **map** between **sodium\_channel**
|  and **sodium\_channel\_h\_gate** for

vars V and V;

vars t and t;

vars h and h;

**enddef**;

**enddef**;

***Noble62\_K\_channel.xml***

**def model potassium\_ion\_channel** as

**def import** using "Units\_for\_Noble62.xml" for

unit mV using unit mV;

unit ms using unit ms;

unit mM using unit mM;

unit per\_ms using unit per\_ms;

unit per\_mV using unit per\_mV;

unit per\_mV\_ms using unit per\_mV\_ms;

unit microS using unit microS;

unit nanoA using unit nanoA;

**enddef**;

**def** **group** as encapsulation for

comp **potassium\_channel** incl

comp **potassium\_channel\_n\_gate**;

endcomp;

**enddef**;

**def comp potassium\_channel** as

var V: mV {pub: in, priv: out};

var t: ms {pub: in, priv: out};

var n: dimensionless {priv: in};

var Ki: mM {pub: in};

var Ko: mM {pub: in};

var RTF: mV {init: 25};

var E\_K: mV;

var g\_K1: microS;

var g\_K2: microS;

var i\_K: nanoA {pub: out};

E\_K = RTF\*ln(Ko/Ki);

| g\_K1 = 1200{microS}\*exp(-(V+90{mV})/50{mV})
|  +15{microS}\*exp((V+90{mV})/60{mV});

g\_K2 = 1200{microS}\*pow(n, 4{dimensionless});

i\_K = (g\_K1+g\_K2)\*(V-E\_K);

**enddef**;

**def comp potassium\_channel\_n\_gate** as

var V: mV {pub: in};

var t: ms {pub: in};

var n: dimensionless {init: 0.01, pub: out};

var alpha\_n: per\_ms;

var beta\_n: per\_ms;

| alpha\_n = -0.0001{per\_mV\_ms}\*(V+50{mV})
|  /(exp(-(V+50{mV})/10{mV})-1{dimensionless});

beta\_n = 0.0020{per\_ms}\*exp(-(V+90{mV})/80{mV});

ode(n,t)= alpha\_n\*(1{dimensionless}-n)-beta\_n\*n;

**enddef**;

| **def map** between **environment**
|  and **potassium\_channel** for

vars V and V;

vars t and t;

**enddef**;

| **def map** between **potassium\_channel** and
|  **potassium\_channel\_n\_gate** for

vars V and V;

vars t and t;

vars n and n;

**enddef**;

**enddef**;

| **Figure 33**. Output from the Noble62 model. Top panel is
  :math:`V\left( t \right)`, the cardiac action potential. The next
  panel has the two membrane ion channel currents
  :math:`i_{\text{Na}}\left( t \right)` and
  :math:`i_{K}\left( t \right)`. Note that
  :math:`i_{\text{Na}}\left( t \right)` has a very brief downward (i.e.
  inward current) spike that is triggered when the membrane voltage
  reaches about -70mV. This is caused by the huge increase in sodium
  channel conductance :math:`g_{\text{Na}}\left( t \right)` shown in the
  panel below associated with the simultaneous opening of the *m*-gate
  and closing of the *h*-gate (5:sup:`th` panel down). The resting state
  of about
| -80mV in the top panel is set by the potassium equilibrium (Nernst)
  potential via the open potassium channels. As can be seen from the
  4\ :sup:`th` and bottom panels, it is the closing of the
  time-dependent potassium *n*-gate and the corresponding decline of
  potassium conductance that, with a small background leakage current
  :math:`i_{L}\left( t \right)`, leads to the membrane potential rising
  from -80mV to the threshold for activation of the sodium channel (note
  the dotted red line showing the point when *n(t)* reaches a minimum).
  Later cardiac cell models include additional ion channels that
  directly affect the heart rate by controlling this rise.

We have now covered all existing features of CellML and OpenCOR. But,
most importantly, you have learned 'best practice' for building CellML
models, including encapsulation of sub-components and a modular approach
in which units, parameters and model components are defined in separate
files that are imported into a composite model.

