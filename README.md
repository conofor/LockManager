from .LockManager import lock_manager

class Test:
  def __init__(self) -> None:
    self.obj = {}
  
  async def set_obj(self, name:str):
    async with lock_manager.this():
      self.obj["name"] = name

t = Test()

asyncio.run(t.set_obj("a"))
asyncio.run(t.set_obj("b"))
