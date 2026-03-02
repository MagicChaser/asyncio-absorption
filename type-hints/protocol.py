from collections.abc import Iterable, Iterator
from typing import TYPE_CHECKING, TypeVar, Protocol, Any
import pytest # type: ignore


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:      
        ...   # protocol仅用省略号,表示接口签名

    
LT = TypeVar('LT', bound=SupportsLessThan)    

def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]

def test_top_tuple() -> None:
    fruits = 'Mango Pear Apple Kiwi Banana'.split(" ")
    series: Iterator[tuple[int, str]] = ((len(s), s) for s in fruits)
    
    length = 3
    expected = [(6, 'Banana'), (5, 'Mango'), (5, 'Apple')]
    res = top(series, length) # type: ignore
    if TYPE_CHECKING:
        reveal_type(series)
        reveal_type(expected)
        reveal_type(res)
    assert res == expected
    
def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)
    with pytest.raises(TypeError) as excinfo:
        top(series, 3) # type: ignore
    assert "'<' not supported" in str(excinfo.value)
    
        
    
    