

class TreatmentData:
    def __init__(self, chain):
        self.chain = chain
        self.list_tokens = []

    def divide_tokens(self):
        self.list_tokens = self.chain.split(" ")
        print(f"tokens: {self.list_tokens}")
        return self.list_tokens

class Control_table:
    pravilo = ["E+T","T","n", "(E)"]

class Main:
   
    treatment_data = TreatmentData( chain = input("Enter the chain: "))
    treatment_data.divide_tokens()


#start = Main()