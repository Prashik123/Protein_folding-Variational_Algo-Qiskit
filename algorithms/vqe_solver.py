from qiskit_algorithms import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import Estimator
from algorithms.ansatz import protein_ansatz


def run_vqe(qubit_op):
    
    #Variational Quantum Eigensolver for protein folding.
    

    ansatz = protein_ansatz(qubit_op.num_qubits)
    optimizer = COBYLA(maxiter=200)

    vqe = VQE(
        estimator=Estimator(),
        ansatz=ansatz,
        optimizer=optimizer
    )

    result = vqe.compute_minimum_eigenvalue(qubit_op)
    return result.eigenvalue.real
