from dataclasses import dataclass, field
from typing import TypeVar, Generic

T = TypeVar("T")

@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, x: T) -> None:
        self.items.append(x)

    def pop(self) -> T:
        return self.items.pop()

@dataclass
class Queue(Generic[T]):
    items: list[T] = field(default_factory=list)

    def enqueue(self, x: T) -> None:
        self.items.append(x)

    def dequeue(self) -> T:
        return self.items.pop(0)

s = Stack[int]()
s.push(10)
print(s.pop())

q = Queue[int]()
q.enqueue(20)
print(q.dequeue())