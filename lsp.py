class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    pass  # Горобець може літати, тому наслідування правильне

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")  # Порушення LSP