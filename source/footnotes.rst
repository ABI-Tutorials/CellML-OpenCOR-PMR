=========
Footnotes
=========

.. [31]
   The original expression in the HH paper used
   :math:`\alpha_{n} = \frac{0.01\left( v + 10 \right)}{e^{\frac{\left( v + 10 \right)}{10}} - 1}`
   and :math:`\beta_{n} = 0.125e^{\frac{v}{80}}` , where :math:`v` is
   defined relative to the resting potential (-75mV) with +ve :math:`v`
   corresponding to +ve *inward* current and
   :math:`v = - \left( V + 75 \right)`.

.. [32]
   From here on we use a coloured background to identify code blocks
   that relate to a particular CellML construct: **units**,
   **components**, **mappings** and **encapsulation groups** and later
   **imports**.

.. [33]
   Note that a later version of CellML will remove the terms *in* and
   *out* since it is now thought that the *direction* of information
   flow should not be constrained.

.. [34]
   The HH paper used
   :math:`\alpha_{m} = \frac{0.1\left( v + 25 \right)}{e^{\frac{\left( v + 25 \right)}{10}} - 1}`;
   :math:`\beta_{m} = 4e^{\frac{v}{18}}`;
   :math:`\alpha_{h} = 0.07e^{\frac{v}{20}}`;
   :math:`\beta_{h} = \frac{1}{e^{\frac{\left( v + 30 \right)}{10}} + 1}`
   (see footnote on page 16).

.. [35]
   http://en.wikipedia.org/wiki/Cable\_theory

.. [36]
   This term is needed when determining the propagation of the action
   potential, including its wave speed.

.. [37]
   The second inwardly rectifying channel model was later replaced with
   two currents :math:`i_{\text{Kr}}` and :math:`i_{\text{Ks}}`, so that
   modern cardiac cell models do not include :math:`g_{K2}` but they do
   include the inward rectifier :math:`g_{K1}` (see later section).

.. [38]
   The Purkinje fibre membrane capacitance :math:`C_{m}` is 12 times
   higher than that found for squid axon. The use of µF ensures unit
   consistency with ms, mV and µA since F is equivalent to
   C.V\ :sup:`-1` or s.A.V\ :sup:`-1` and therefore µA/µF or µA/(ms.µA.
   mV\ :sup:`-1`) on the RHS matches mV/ms on the LHS).

.. [39]
   Referred to as W3C – see `www.w3.org <media/image14.tif>`__

.. [40]
   `www.w3.org/RDF <media/image15.png>`__

.. [41]
   For details on the annotation plugin see
   `opencor.ws/user/plugins/editing/CellMLAnnotationView.html <media/image16.png>`__

.. [42]
   See `www.cellml.org/specifications/metadata/ <media/image17.png>`__
   and
   `www.cellml.org/specifications/metadata/mcdraft <media/image18.png>`__

.. [43]
   `http://co.mbine.org/standards/qualifiers <media/image19.png>`__

.. [44]
   `http://en.wikipedia.org/wiki/Uniform\_resource\_identifier <media/image20.png>`__

.. [45]
   `http://en.wikipedia.org/wiki/Regular\_expression <media/image21.png>`__

.. [46]
   This is a project being carried out at the University of Washington,
   Seattle, using an annotation tool called SEMGEN (…).

.. [47]
   These are currently hand drawn SVG diagrams but the plan is to
   automatically generate them from the model annotation and also (at
   some stage!) to animate them as the model is executed.

.. [48]
   https://creativecommons.org/licenses/by/3.0/

.. [49]
   `www.mathworks.com/products/matlab <media/image22.png>`__

.. [50]
   `https://github.com/opencor/speedcomparison <media/image23.png>`__.
   These tests were carried out by Alan Garny.

.. |image0| image:: media/image14.tif
.. |image1| image:: media/image15.png
.. |image2| image:: media/image16.png
.. |image3| image:: media/image17.png
.. |image4| image:: media/image18.png
.. |image5| image:: media/image19.png
.. |image6| image:: media/image19.png
.. |image7| image:: media/image19.png
.. |image8| image:: media/image19.png
.. |image9| image:: media/image19.png
.. |image10| image:: media/image19.png
.. |image11| image:: media/image19.png
.. |image12| image:: media/image19.png
.. |image13| image:: media/image19.png
.. |image14| image:: media/image19.png
.. |image15| image:: media/image19.png
.. |image16| image:: media/image22.png
.. |image17| image:: media/image23.png
.. |image18| image:: media/image46.png
.. |image19| image:: media/image49.png
.. |image20| image:: media/image56.png
.. |image21| image:: media/image57.png
.. |image22| image:: media/image58.png
.. |image23| image:: media/image59.png
.. |image24| image:: media/image60.png
.. |image25| image:: media/image61.png
.. |image26| image:: media/image60.png
.. |image27| image:: media/image68.png
