class Item:
    def to_json(self):
        item = vars(self)
        for k, v in item.items():
            if isinstance(v, list):
                item[k] = [i.to_json() for i in v]
        return item


class Process(Item):
    
    def __init__(self, process):
        self.username: str = process.username
        self.command: str = process.command
        self.gpu_memory_usage: int = process.gpu_memory_usage
        self.pid: int = process.pid


class Card(Item):
    
    def __init__(self, card, ip, time):
        self.gpu_name: str = card.gpu_name
        self.ip: str = ip
        self.index: int = card.index
        self.temperature: int = card.temperature
        self.fan_speed: int = card.fan_speed
        self.memory_used: int = card.memory_used
        self.memory_total: int = card.memory_total
        self.utilization: int = card.utilization
        self.uuid: str = card.uuid
        self.process = [Process(p) for p in card.process]
        self.time = time
    
    def __repr__(self):
        return "%s %s %d" % (self.gpu_name, self.ip, self.index)
