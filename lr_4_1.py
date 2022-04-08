class TreatmentData:
    def __init__(self, chain):
        self.chain = chain
        self.tokens = ""

    def divide_tokens(self):
        # здесь должна быть нормальная обработка через регулярные выражения
        self.list_tokens = self.chain
        print(f"tokens: {self.list_tokens}")
        return self.list_tokens

class Control_table:
    stack_tokens = ""
    def proverka(self, list_tokens):

        #while list_tokens != "E":
            for i in range(len(list_tokens)):
                if "n"  == list_tokens[i]:
                    #list_tokens = list_tokens.replace(list_tokens[i], "T")
                    self.stack_tokens += "T"
                    print(self.stack_tokens)
                    if "T" in self.stack_tokens:
                        list_tokens = list_tokens.replace("T", "E")
                        print(self.stack_tokens)
                    if "E+T" in list_tokens:
                        self.stack_tokens = self.stack_tokens.replace("E+T", "E")
                        print(self.stack_tokens)
                    if "(E)" in list_tokens:
                        self.stack_tokens = self.stack_tokens.replace("(E)", "T")
                        print(self.stack_tokens)
                else:
                    self.stack_tokens += list_tokens[i]

                    print(self.stack_tokens)


            print(self.stack_tokens)
                 
class Analyzer:
   
    treatment_data = TreatmentData( chain = input("Enter the chain: "))
    treatment_data.divide_tokens()
    control_table = Control_table()
    control_table.proverka(treatment_data.list_tokens)
