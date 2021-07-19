#!/usr/bin/env python3
'''   duck-typing function
'''

from typing import List, Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A duck-typed function.
    """
    if lst:
        return lst[0]
    else:
        return None
