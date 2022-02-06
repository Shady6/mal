class Env():
    def __init__(self, outer=None):
        self.data = {}
        self.outer = outer

    def set(self, k, v):
        self.data[k] = v
        return v

    def find(self, k):
        if self.data.get(k, None):
            return self
        elif self.outer is not None:
            return self.outer.find(k)
        return None

    def get(self, k):
        env = self.find(k)
        if env is not None:
            return env.data[k]
        raise KeyError(f'{k} not found')
