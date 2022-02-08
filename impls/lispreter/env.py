class Env():
    def __init__(self, outer=None, binds=[], exprs=[]):
        self.data = {}
        self.outer = outer
        for i in range(len(binds)):
            if binds[i] == '&':
                self.data[binds[i + 1]] = exprs[i:]
                break
            else:
                self.data[binds[i]] = exprs[i]

    def set(self, k, v):
        self.data[k] = v
        return v

    def find(self, k):
        if self.data.get(k, None) is not None:
            return self
        elif self.outer is not None:
            return self.outer.find(k)
        return None


    def get(self, k):
        env = self.find(k)
        if env is not None:
            return env.data[k]
        raise KeyError(f'{k} not found')
