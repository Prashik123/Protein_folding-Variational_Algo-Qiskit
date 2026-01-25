from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Sampler


def run_qaoa(qubit_op):
   
  #QAOA-based energy minimization for protein folding.
    qaoa = QAOA(
        sampler=Sampler(),
        optimizer=COBYLA(maxiter=150),
        reps=2
    )

    result = qaoa.compute_minimum_eigenvalue(qubit_op)
    return result.eigenvalue.real
