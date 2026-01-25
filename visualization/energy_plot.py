import os
import matplotlib.pyplot as plt


def plot_energy(vqe_energy, qaoa_energy, reference_energy):
    energies = [vqe_energy, qaoa_energy, reference_energy]
    labels = ["VQE", "QAOA", "Reference"]

    plt.bar(labels, energies)
    plt.ylabel("Energy (Hartree)")
    plt.title("Protein Folding Energy Comparison")

    os.makedirs("results", exist_ok=True)
    plot_path = os.path.join("results", "energy_comparison.png")
    plt.savefig(plot_path)
    plt.close()

    return plot_path
