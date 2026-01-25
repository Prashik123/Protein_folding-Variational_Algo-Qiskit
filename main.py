import os
from protein_model import build_gly_ile, get_qubit_hamiltonian
from algorithms import run_vqe, run_qaoa
from analysis import efficiency, accuracy

# Ensure results directory exists
RESULTS_DIR = os.path.join(os.getcwd(), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

# Build electronic structure
problem = build_gly_ile()

# Map to qubit Hamiltonian
qubit_op = get_qubit_hamiltonian(problem)

# Run quantum algorithms
vqe_energy = run_vqe(qubit_op)
qaoa_energy = run_qaoa(qubit_op)

# Classical benchmark (small Gly–Ile fragment, STO-3G)
reference_energy = -1.137

# Metrics
vqe_eff = efficiency(reference_energy, vqe_energy)
vqe_acc = accuracy(reference_energy, vqe_energy)

# Save metrics using os
metrics_path = os.path.join(RESULTS_DIR, "metrics.txt")
with open(metrics_path, "w") as f:
    f.write(f"Protein Fragment : Gly–Ile\n")
    f.write(f"Reference Energy : {reference_energy}\n")
    f.write(f"VQE Energy       : {vqe_energy}\n")
    f.write(f"QAOA Energy      : {qaoa_energy}\n")
    f.write(f"Efficiency (%)   : {vqe_eff:.2f}\n")
    f.write(f"Accuracy (%)     : {vqe_acc:.2f}\n")

print("===== QWorld Protein Folding Results =====")
print(f"VQE Energy      : {vqe_energy:.6f} Ha")
print(f"QAOA Energy     : {qaoa_energy:.6f} Ha")
print(f"Efficiency (%)  : {vqe_eff:.2f}")
print(f"Accuracy (%)    : {vqe_acc:.2f}")
print(f"Saved to        : {metrics_path}")
