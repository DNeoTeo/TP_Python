class SyracuseFile(object):

    def __init__(self, InFileName, OutFileName):
        self.InFileName = InFileName
        self.OutFileName = OutFileName
        self.nbIteration = 0
        self.ListValue = []
        with open(InFileName, 'r') as f_i:
            for line in f_i.readlines():
                self.Uzero = int(line)  
                print(line)

    def calcul_syracuse(self):
        u = self.Uzero
        n=0
        self.ListValue =[self.Uzero]
        while(u!=1): # pour i allant de 1 à n
            if u%2==0: # u%2: reste de la division euclidienne de u par 2
                u = u//2 # u//2: quotient de la division euclidienne de u par 2
            else:
                u = 3*u+1
            n += 1
            self.ListValue.append(u)  
        self.nbIteration =  n

    def WriteFile(self):
        if(self.ListValue != []):
            with open(self.OutFileName, 'w') as f_o:
                f_o.write("Uo = "+str(self.Uzero)+" Nombre d'iteration "+str(self.nbIteration)+"\n")
                for val in self.ListValue :
                    f_o.write(str(val)+" ")
        else:
            print("Error calcul_syracuse is missing")






