# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=missing-module-docstring

from qiskit.circuit.quantumcircuit import QuantumCircuit


def template_nct_9d_9():
    """
    Template 9d_9:

    .. code-block:: text

        q_0: ──■────■────■─────────■────■─────────■────■──
               │    │  ┌─┴─┐       │  ┌─┴─┐       │  ┌─┴─┐
        q_1: ──■────┼──┤ X ├───────■──┤ X ├───────■──┤ X ├
             ┌─┴─┐┌─┴─┐└─┬─┘┌───┐┌─┴─┐└─┬─┘┌───┐┌─┴─┐└─┬─┘
        q_2: ┤ X ├┤ X ├──■──┤ X ├┤ X ├──■──┤ X ├┤ X ├──■──
             └───┘└───┘     └───┘└───┘     └───┘└───┘

    Returns:
        QuantumCircuit: template as a quantum circuit.
    """
    qc = QuantumCircuit(3)
    qc.ccx(0, 1, 2)
    qc.cx(0, 2)
    qc.ccx(0, 2, 1)
    qc.x(2)
    qc.ccx(0, 1, 2)
    qc.ccx(0, 2, 1)
    qc.x(2)
    qc.ccx(0, 1, 2)
    qc.ccx(0, 2, 1)
    return qc
