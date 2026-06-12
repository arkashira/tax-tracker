class Product:
    def __init__(self, name, demand_score):
        self.name = name
        self.demand_score = demand_score

    def __repr__(self):
        return f"Product('{self.name}', {self.demand_score})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.demand_score == other.demand_score
