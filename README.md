# 🧬 Quantum Protein Folding using VQE & QAOA  
### QWorld Project | Qiskit Nature | Quantum Optimization Algorithms

---

## 📌 Introduction

Protein folding determines biological function, but simulating it **classically becomes intractable** as system size grows.  
This repository demonstrates a **quantum optimization approach** to protein folding using **Variational Quantum Algorithms**.

📍 **Project Context**  
- Program: **QWorld Quantum Project**
- Protein Fragment: **Gly–Ile (Insulin chain fragment)**
- Framework: **Qiskit 2.3.0 + Qiskit Nature**
- Algorithms: **VQE & QAOA**
- Result: **~85% efficiency vs classical benchmark**

---

## 🎯 Problem Statement

The task is to determine the **most stable folded configuration** of a protein fragment by **minimizing its electronic ground-state energy**.

This is formulated as a quantum eigenvalue problem:

$$
H_{\text{protein}} \;|\psi_0\rangle = E_0 \;|\psi_0\rangle
$$

Where:
- $H_{\text{protein}}$ → Electronic structure Hamiltonian  
- $E_0$ → Ground-state (minimum) energy  
- $|\psi_0\rangle$ → Stable folded protein configuration  

---

## 🧠 Key Concepts Used

- Quantum Chemistry (Electronic Structure)
- Second Quantization
- Fermion-to-Qubit Mapping (Parity Mapping)
- Active Space Approximation
- Variational Quantum Algorithms
- Classical Optimization (COBYLA)

---

## 🔬 Mathematical Background (GitHub-friendly)

### 1️⃣ Electronic Hamiltonian (Second Quantization)

$$
H = \sum_{p,q} h_{pq} a_p^\dagger a_q
+ \frac{1}{2} \sum_{p,q,r,s} h_{pqrs} a_p^\dagger a_q^\dagger a_r a_s
$$

This Hamiltonian captures:
- One-electron interactions
- Two-electron Coulomb interactions

---

### 2️⃣ Active Space Reduction

To make the problem feasible on NISQ hardware:
- Number of electrons = **2**
- Number of spatial orbitals = **2**

This drastically reduces the required number of qubits.

---

### 3️⃣ Fermion → Qubit Mapping

Using **Parity Mapping**, the Hamiltonian is converted to a qubit operator:

$$
H_{\text{qubit}} = \sum_i c_i P_i
$$

Where:
- $P_i$ are Pauli strings (`I`, `X`, `Y`, `Z`)
- $c_i$ are real coefficients

---

## ⚙️ Algorithms Used

### 🔹 Variational Quantum Eigensolver (VQE)

- Uses a **parameterized quantum circuit (ansatz)**
- Classical optimizer minimizes expectation value:

$$
E(\theta) = \langle \psi(\theta) | H | \psi(\theta) \rangle
$$

- Optimizer used: **COBYLA**
- Ansatz: **TwoLocal (hardware-efficient)**

---

### 🔹 Quantum Approximate Optimization Algorithm (QAOA)

- Alternates between:
  - Cost Hamiltonian ($H_C$)
  - Mixer Hamiltonian ($H_M$)

$$
|\psi(\gamma, \beta)\rangle =
e^{-i \beta H_M} e^{-i \gamma H_C} |+\rangle^{\otimes n}
$$

- Optimized to approximate the ground-state energy

---

## 🔁 Repository Workflow

```mermaid
flowchart TD
    A[Define Gly–Ile Geometry] --> B[Electronic Structure via PySCF]
    B --> C[Active Space Reduction]
    C --> D[Fermion to Qubit Mapping]
    D --> E{Quantum Algorithm}
    E -->|VQE| F[Parameterized Ansatz]
    E -->|QAOA| G[Cost + Mixer Hamiltonians]
    F --> H[Energy Minimization]
    G --> H
    H --> I[Ground-State Energy]
    I --> J[Accuracy & Efficiency Analysis]
