from qiskit_nature.second_q.drivers import PySCFDriver
from qiskit_nature.units import DistanceUnit


def build_gly_ile():
    """
    Builds a minimal Gly–Ile peptide fragment
    using ab initio electronic structure.
    """

    geometry = """
    N  0.000  0.000  0.000
    C  1.458  0.000  0.000
    C  2.028  1.410  0.000
    N  3.486  1.410  0.000
    C  4.056  2.820  0.000
    """

    driver = PySCFDriver(
        atom=geometry,
        basis="sto3g",
        unit=DistanceUnit.ANGSTROM,
        charge=0,
        spin=0,
    )

    return driver.run()
