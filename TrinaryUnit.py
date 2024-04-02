import random

class TrinaryUnit:
    def __init__(self):
        self.previous_data = None

    def process_data(self, data):
        if data == 0:
            return "Negative"
        elif data == 1:
            return "Positive"
        elif data == "01":
            if self.previous_data is None:
                # If there's no previous data, return a random value between negative and positive
                return random.choice(["Negative", "Positive"])
            else:
                # Otherwise, return the same as the previous data
                return self.previous_data
        else:
            raise ValueError("Invalid input data")

    def run(self, data_stream):
        results = []
        for data in data_stream:
            result = self.process_data(data)
            results.append(result)
            # Update previous data for future "01" inputs
            self.previous_data = result
        return results

# Example usage
if __name__ == "__main__":
    trinary_unit = TrinaryUnit()
    data_stream = ["01", 0, 1, 0, "01", "01", 1, 1, "01"]
    results = trinary_unit.run(data_stream)
    print("Data Stream:", data_stream)
    print("Results:", results)
