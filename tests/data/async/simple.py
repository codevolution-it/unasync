class TestImplementation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.s = "UTF-8: ❄"

    async def get_a_b(self):
        return f"a is {self.a} b is {self.b}"

    async def f(self):
        return await 1


async def f():
    return await 1
