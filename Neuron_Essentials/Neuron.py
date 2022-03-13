from Neuron_Essentials import Neuron, SignalType, NeuronType
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

    #     # Values for I is calculated from the average resistance of a
    #     # neuron and the resting potential. 
    #     # I = V/R, where V = -0.04 and R = 0.15 ohm
    #     # Source: https://www.sciencedirect.com/science/article/pii/B9780123972651001337
    #     # Value for C is 9.E-7 Farads. From: https://www.sciencedirect.com/science/article/pii/S000634950076293X
        
    #     Vrest = -0.04
    #     R = 0.15
    #     Irest = Vrest/R
    #     C = 9.E-7
    #     dt = 0.01
    #     Vthresh = 0.07
        
    #     # Calculate the voltage potential of the neuron
    #     if(signal == SignalType.POSITIVE):
    #         for i in range(0, self.runtime, ):
    #             if(self.voltagePotentialHistory[i] < Vthresh):
    #                 Vcurr = self.voltagePotentialHistory[i]
    #                 self.voltagePotentialHistory.append(Vcurr + dt*(Irest - Vcurr)/C)
    #             else:
    #                 break
    #     else:
    #         for i in range(0, self.runtime):
    #             if(self.voltagePotentialHistory[i] > Vthresh):
    #                 Vcurr = self.voltagePotentialHistory[i]
    #                 self.voltagePotentialHistory.append(Vcurr - dt*(Irest - Vcurr)/C)
    #             else:
    #                 break

        dt = 0.2 #time step in ms
        counter = 0

        if signal == SignalType.POSITIVE:
            while counter < self.runtime*0.99:
                self.voltagePotentialHistory.append(self.potentialChargeModel(counter))
                counter += dt
        else:
           while counter < self.runtime*0.99:
                self.voltagePotentialHistory.append(-0.04) #-0.04 is the resting potential
                counter += dt
    
    def potentialChargeModel(self, t):
        
        return 0.110*math.exp(-(math.pow(1.5*t-2.8,2)))-0.04
    
    def addSynapse(self, neuron):
        self.connectedTo.append(neuron)
    
    def getConnectedTo(self):
        return self.connectedTo