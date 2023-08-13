import qiskit
import math

def print_state_vector(state_vector):
    binary_length = math.floor(math.log2(len(state_vector) + 1))
    for i in range(len(state_vector)):
        i_prob = math.pow(abs(state_vector[i]),2)
        print(f'{i:0{binary_length}b} {i_prob:.2f}% {state_vector[i]:12.2f}')

def run_circuit(qcircuit):
    backend = qiskit.Aer.get_backend('statevector_simulator')
    job = backend.run(qcircuit)
    result = job.result()
    return(result)