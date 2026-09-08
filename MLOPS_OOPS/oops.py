class employee:

    def __init__(self):
        self.name = "John Doe"
        self.age = 30
        self.position = "Software Engineer"

    def travel(self, destination):
        print(f"{self.name} is traveling to {destination}.")

data=employee()

print(data.position)

## Callling the travel method

data.travel("New York")