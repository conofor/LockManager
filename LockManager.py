import inspect
import asyncio
import threading

class LockManager:
    def __init__(self):
        self.locks = {}
        self.async_locks = {}

    def get_lock(self, name):
        if name not in self.locks:
            self.locks[name] = threading.Lock()
        return self.locks[name]
    
    def get_lock_async(self, name):
        if name not in self.async_locks:
            self.async_locks[name] = asyncio.Lock()
        return self.async_locks[name]

    def this(self):
        stack = inspect.stack()
        name = f"{stack[1].filename}:{stack[1].lineno}"
        if stack[1].frame.f_code.co_flags & 0x80:
            return self.get_lock_async(name)
        else:
            return self.get_lock(name)

lock_manager = LockManager()