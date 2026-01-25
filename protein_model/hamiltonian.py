from qiskit_nature.second_q.mappers import ParityMapper
from qiskit_nature.second_q.transformers import ActiveSpaceTransformer


def get_qubit_hamiltonian(problem):
    
    #Active-space reduction + fermion-to-qubit mapping.
    

    transformer = ActiveSpaceTransformer(
        num_electrons=2,
        num_spatial_orbitals=2
    )

    reduced_problem = transformer.transform(problem)
    mapper = ParityMapper()

    return mapper.map(
        reduced_problem.hamiltonian.second_q_op()
    )
