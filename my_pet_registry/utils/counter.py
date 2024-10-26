class Counter:
    def __init__(self):
        self.count = 0
        self.resource_open = False

    def __enter__(self):
        if self.resource_open:
            raise Exception("Resource already open!")
        self.resource_open = True
        print("Counter resource opened.")
        return self

    def add(self):
        if not self.resource_open:
            raise Exception("Resource must be open to use Counter.")
        self.count += 1
        print(f"Counter incremented. Current count: {self.count}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource_open = False
        print("Counter resource closed.")
        if exc_type:
            print(f"An error occurred: {exc_val}")
