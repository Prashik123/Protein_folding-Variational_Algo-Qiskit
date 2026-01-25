from qiskit.circuit.library import TwoLocal


def protein_ansatz(num_qubits):
    #Hardware-efficient ansatz for protein Hamiltonians.
    
    return TwoLocal(
        num_qubits=num_qubits,
        rotation_blocks=["ry", "rz"],
        entanglement_blocks="cx",
        entanglement="linear",
        reps=2
    )
