import random  

class TrinaryUnit:     
    def __init__(self):         
        self.previous_data = None      

    def process_data(self, data):         
        if data in ["10", "01", "11", "00"]:  # Neutral cases
            new_data = random.choice([0, 1])  
            
            # Ensure the new data is not the same as the last result to avoid repetition
            while new_data == self.previous_data:
                new_data = random.choice([0, 1])
                
            data = new_data
        
        if data == 0:             
            result = "Positive"         
        elif data == 1:             
            result = "Negative"         
        else:             
            raise ValueError("Invalid input data")      
        
        self.previous_data = data  # Store the last processed value
        return result

    def run(self, data_stream):         
        results = []         
        for data in data_stream:             
            result = self.process_data(data)
            results.append(result)       
        return results  

# Example usage
if __name__ == "__main__":     
    trinary_unit = TrinaryUnit()     
    data_stream = ["10", 0, 1, "00", "01", "11", 1, 0, "10"]     
    results = trinary_unit.run(data_stream)     
    print("Data Stream:", data_stream)     
    print("Results:", results)
