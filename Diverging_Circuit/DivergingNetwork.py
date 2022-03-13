from Neuron_Essentials import Neuron, SignalType, NeuronType

def run_sim(runtime):
    
    inp_nrn = Neuron(NeuronType.INPUT, runTime)

    # Create a Diverging Neuron Graph
    layer1_nrn = [Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime)]
    layer2_nrn = [Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime)]
    layer3_nrn = [Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime), Neuron(NeuronType.EXCITATORY, runTime)]

    # Connect the input to the first layer
    for nrn in layer1_nrn:
        inp_nrn.addSynapse(nrn)
    
    # Connect the first layer to the second layer
    for nrn in layer1_nrn:
        for nrn2 in layer2_nrn:
            nrn.addSynapse(nrn2)
    
    


    