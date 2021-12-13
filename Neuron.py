from NeuronType import *
from SignalType import *
import math

class Neuron():

    def __init__(self, type, runtime):
        self.type = type
        self.runtime = runtime
        self.connectedTo = []
        self.voltagePotentialHistory = []
        self.counter = 0

    def sendSynapseSignal(self, signal):
        pos = SignalType.POSITIVE
        neg = SignalType.NEGATIVE

        if(self.type == NeuronType.INPUT):
            self.helper(signal)

        elif(self.type == NeuronType.EXCITATORY):            
            self.helper(pos) if signal == pos else self.helper(neg)

        elif(self.type == NeuronType.INHIBITORY):
            cond = self.counter % 2 == 0
            if(signal == pos):
                self.helper(pos) if cond else self.helper(neg)

            else:
                self.helper(pos) if cond else self.helper(neg)
            
        elif(self.type == NeuronType.OUTPUT):
            raise ValueError("Output neurons cannot receive synapse signals.")
    
    def helper(self, signal):
        for neuron in self.connectedTo:
            neuron.receiveSynapseSignal(signal)
    
    def receiveSynapseSignal(self, signal):
        
        self.simulateChargeTransfer(signal)
        
        if self.type != NeuronType.OUTPUT and self.counter < self.runtime/2:
            self.counter+=1
            self.sendSynapseSignal(signal)
            

    def simulateChargeTransfer(self, signal):
        
        dt = 0.1 #time step in ms
        counter = 0

        if signal == SignalType.POSITIVE:
            while counter < self.runtime:
                self.voltagePotentialHistory.append(self.potentialChargeModel(counter))
                counter += dt
        else:
           while counter < self.runtime:
                self.voltagePotentialHistory.append(self.potentialChargeModel(-40))
                counter += dt
    
    def potentialChargeModel(self, t):
        
        return 0.110*math.exp(-(math.pow(1.5*t-2.8,2)))-0.04
    
    def addSynapse(self, neuron):
        self.connectedTo.append(neuron)
    
    def getConnectedTo(self):
        return self.connectedTo