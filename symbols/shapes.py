class SimpleRect():
    "Simple rectangle"

    def __init__(self, location, size):
        self.location = location
        self.size = size

    def draw(self, ctx):
        ctx.rectangle(
        self.location[0], self.location[1],
        self.size[0], self.size[1])
