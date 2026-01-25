from protein_model import build_gly_ile, get_qubit_hamiltonian
from algorithms import run_vqe, run_qaoa
from analysis import efficiency, accuracy

# Step 1: Build electronic structure of Gly–Ile fragment
problem = build_gly_ile()

# Step 2: Map fermionic Hamiltonian to qubits
qubit_op = get_qubit_hamiltonian(problem)

# Step 3: Run quantum algorithms
vqe_energy = run_vqe(qubit_op)
qaoa_energy = run_qaoa(qubit_op)

# Classical reference (FCI benchmark for reduced system)
reference_energy = -1.137

# Step 4: Compute metrics
vqe_eff = efficiency(reference_energy, vqe_energy)
vqe_acc = accuracy(reference_energy, vqe_energy)

print("QWorld Protein Folding Results: ")
print(f"VQE Energy      : {vqe_energy:.6f} Ha")
print(f"QAOA Energy     : {qaoa_energy:.6f} Ha")
print(f"Reference Energy: {reference_energy:.6f} Ha")
print(f"Efficiency (%)  : {vqe_eff:.2f}")
print(f"Accuracy (%)    : {vqe_acc:.2f}")
