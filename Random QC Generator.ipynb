from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit import Aer, execute
from qiskit.circuit.library import XGate, YGate, ZGate, HGate, CXGate, UGate
import random

def random_quantum_circuit(qubit_count, depth, base_gates):
    
    circuit = QuantumCircuit(qubit_count)
    # If 1 qubit circuit 
    if qubit_count == 1:
        for i in range(depth):
            gate = random.choice(base_gates["1q"])
            circuit.append(gate, [0])
    else:
    # Generate random gates for each depth
        for i in range(depth):
            for j in range(qubit_count):
                # Generate random single-qubit gate
                if random.random() < 0.5:
                    gate = random.choice(base_gates["1q"])
                    circuit.append(gate, [j])

                # Generate random two-qubit gate
                else:
                    qubit_choices = list(range(qubit_count))
                    q1, q2 = random.sample(qubit_choices, k=2)
                    gate = random.choice(base_gates["2q"])
                    circuit.append(gate, [q1, q2])

    return circuit

#Example


# Define the number of qubits, depth, and base gates
qubit_count = 5
depth = 2
base_gates = {"1q": [XGate(), YGate(), ZGate(), HGate()], "2q": [CXGate()]}

# Generate the random quantum circuit
circuit = random_quantum_circuit(qubit_count, depth, base_gates)
circuit.draw()
