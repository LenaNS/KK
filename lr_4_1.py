
class TreatmentData:
    def __init__(self, chain):
        self.chain = chain
        self.tokens = ""

    def divide_tokens(self):
        self.list_tokens = self.chain
        print(f"tokens: {self.list_tokens}")
        return self.list_tokens

class Control_table:
    stack_tokens = ""
    def proverka(self, list_tokens):
            for i in range(len(list_tokens)):
                if "n"  == list_tokens[i]:
                    self.stack_tokens += "T"
                    print(self.stack_tokens, "свёртка по правилу (3)")

                    

                    if "E+T" in self.stack_tokens:
                        self.stack_tokens = self.stack_tokens.replace("E+T", "E")
                        print(self.stack_tokens, "свёртка по правилу (1)")

                else:
                    self.stack_tokens += list_tokens[i]
                    print(self.stack_tokens, "перенос")
                    if "(E)" in self.stack_tokens:
                        self.stack_tokens = self.stack_tokens.replace("(E)", "T")
                        print(self.stack_tokens, "свёртка по правилу (4)")
                    if "T" in self.stack_tokens and "E+T" not in self.stack_tokens :
                        self.stack_tokens =  self.stack_tokens.replace("T", "E")
                        print(self.stack_tokens, "свёртка по правилу (2)")
            print(self.stack_tokens)
                 
class Analyzer:
    treatment_data = TreatmentData( chain = input("Enter the chain: "))
    treatment_data.divide_tokens()
    control_table = Control_table()
    control_table.proverka(treatment_data.list_tokens)
