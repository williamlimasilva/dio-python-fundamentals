class CPU:
    def __init__(self, manufacturer, model, clock_speed):
        self.manufacturer = manufacturer
        self.model = model
        self.clock_speed = clock_speed
    
    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.clock_speed}GHz)"

class Memory:
    def __init__(self, size, type_memory):
        self.size = size
        self.type_memory = type_memory
    
    def __str__(self):
        return f"{self.size}GB {self.type_memory}"

class Storage:
    def __init__(self, type_storage, capacity):
        self.type_storage = type_storage
        self.capacity = capacity
    
    def __str__(self):
        return f"{self.type_storage} {self.capacity}GB"

class GraphicsCard:
    def __init__(self, manufacturer, model, memory):
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
    
    def __str__(self):
        return f"{self.manufacturer} {self.model} ({self.memory}GB)"
class Computer:
    def __init__(self, name):
        self.name = name
        # Composição: Computer é composto por CPU, Memory e Storage
        self.cpu = None
        self.memory = None
        self.storage = None
        self.graphics_card = None

    def add_cpu(self, cpu):
        self.cpu = cpu
    
    def add_memory(self, memory):
        self.memory = memory
    
    def add_storage(self, storage):
        self.storage = storage

    def add_graphics_card(self, graphics_card):
        self.graphics_card = graphics_card

    def specifications(self):
        return f"""
Computer: {self.name}
CPU: {self.cpu}
Memory: {self.memory}
Storage: {self.storage}
Graphics Card: {self.graphics_card}
"""

# Exemplo de uso da composição
if __name__ == "__main__":
    # Criando os componentes
    processor = CPU("Intel", "i7-12700K", 3.6)
    ram = Memory(32, "DDR4")
    ssd = Storage("SSD NVMe", 1000)
    gpu = GraphicsCard("NVIDIA", "RTX 3080", 10)

    # Criando o computador
    my_computer = Computer("Gaming PC")
    
    # Adicionando os componentes ao computador (composição)
    my_computer.add_cpu(processor)
    my_computer.add_memory(ram)
    my_computer.add_storage(ssd)
    my_computer.add_graphics_card(gpu)

    # Mostrando as especificações
    print(my_computer.specifications())