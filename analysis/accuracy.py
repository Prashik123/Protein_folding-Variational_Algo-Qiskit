def accuracy(reference_energy, obtained_energy):
    
    #Accuracy based on relative deviation from benchmark.
   
    return (1 - abs(reference_energy - obtained_energy)
            / abs(reference_energy)) * 100
