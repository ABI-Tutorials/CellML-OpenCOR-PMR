========================
A simple first order ODE
========================

The simplest example of a first order ODE is

:math:`\frac{\text{dy}}{\text{dt}} = - ay + b`

with the solution

:math:`y\left( t \right) = \frac{b}{a} + \left( y\left( 0 \right) - \frac{b}{a} \right).e^{- at}`,

where :math:`y\left( 0 \right)` or :math:`y_{0}`, the value of
:math:`y\left( t \right)` at :math:`t = 0`, is the *initial condition*.
The final steady state solution as :math:`t \rightarrow \infty` is
:math:`y\left( \left. \ t \right|_{\infty} \right) = y_{\infty} = \frac{b}{a}`
(see Figure 6). Note that :math:`t = \tau = \frac{1}{a}` is called the
*time constant* of the exponential decay, and that

:math:`y\left( \tau \right) = \frac{b}{a} + \left( y\left( 0 \right) - \frac{b}{a} \right).e^{- 1}`.

At :math:`t = \tau` , :math:`y\left( t \right)` has therefore fallen to
:math:`\frac{1}{e}` (or about 37%) of the difference between the initial
(:math:`y\left( 0 \right)`) and final steady state (
:math:`y\left( \infty \right)`) values. [22]_

Choosing parameters :math:`a = \tau = 1;b = 2` and
:math:`y\left( 0 \right) = 5`, the *CellML Text* for this model is

    def model first\_order\_model as

    def comp main as

    var t: dimensionless *{init: 0}*;

    var y: dimensionless *{init: 5}*;

    var a: dimensionless *{init: 1}*;

    var b: dimensionless *{init: 2}*;

    ode(y,t)=-a\*y+b;

    enddef;

    enddef;

The solution by OpenCOR is shown in Figure 7(a) for these parameters (a
decaying exponential) and in Figure 7(b) for parameters
:math:`a = 1;b = 5` and :math:`y\left( 0 \right) = 2` (an inverted
decaying exponential). Note the simulation panel with *Ending
point*\ =10, *Point interval*\ =0.1. Try putting :math:`a = - 1`.

(a) (b)

**Figure 7**. OpenCOR output :math:`y\left( t \right)` for the simple
ODE model with parameters (a) :math:`a = 1;b = 2` and
:math:`y\left( 0 \right) = 5`, and (b) :math:`a = 1;b = 5` and
:math:`y\left( 0 \right) = 2`. The **red** **arrow** indicates the point
at which the trace reaches the time constant :math:`\tau`
(:math:`e^{- 1}` or ≈37% of the difference between the initial and final
solution values). The black arrows indicate the initial and final
(steady state) solutions. Note that the parameters on the left have been
reset to their initial values for this figure – normally they would be
at their final solution values.

These two solutions have the same exponential time constant
(:math:`\tau = \frac{1}{a} = 1`) but different initial and final (steady
state) values.

The exponential decay curve shown on the left in Figure 7 is a common
feature of many models and in the case of radioactive decay (for
example) is a statement that the ***rate of decay***
(:math:`- \frac{\text{dy}}{\text{dt}}`) is proportional to the
***current amount of substance*** (:math:`y`). This is illustrated on
the NZ$100 note (should you be lucky enough to possess one), shown in
Figure 8.

**Figure 8.** The **exponential curve** representing the naturally
occurring radioactive decay explained by the New Zealand Noble laureate
Sir Ernest Rutherford - best known for ‘splitting the atom’. This may be
the only bank note depicting the mathematical solution of a first order
ODE.

