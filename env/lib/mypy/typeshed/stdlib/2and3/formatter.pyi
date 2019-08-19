# Source: https://hg.python.org/cpython/file/2.7/Lib/formatter.py
# and https://github.com/python/cpython/blob/master/Lib/formatter.py
from typing import Any, IO, List, Optional, Tuple

AS_IS = None
_FontType = Tuple[str, bool, bool, bool]
_StylesType = Tuple[Any, ...]

class NullFormatter:
    writer = ...  # type: Optional[NullWriter]
    def __init__(self, writer: Optional[NullWriter] = ...) -> None: ...
    def end_paragraph(self, blankline: int) -> None: ...
    def add_line_break(self) -> None: ...
    def add_hor_rule(self, *args, **kw) -> None: ...
    def add_label_data(self, format, counter: int, blankline: Optional[int] = ...) -> None: ...
    def add_flowing_data(self, data: str) -> None: ...
    def add_literal_data(self, data: str) -> None: ...
    def flush_softspace(self) -> None: ...
    def push_alignment(self, align: Optional[str]) -> None: ...
    def pop_alignment(self) -> None: ...
    def push_font(self, x: _FontType) -> None: ...
    def pop_font(self) -> None: ...
    def push_margin(self, margin: int) -> None: ...
    def pop_margin(self) -> None: ...
    def set_spacing(self, spacing: Optional[str]) -> None: ...
    def push_style(self, *styles: _StylesType) -> None: ...
    def pop_style(self, n: int = ...) -> None: ...
    def assert_line_data(self, flag: int = ...) -> None: ...

class AbstractFormatter:
    writer = ...  # type: NullWriter
    align = ...  # type: Optional[str]
    align_stack = ...  # type: List[Optional[str]]
    font_stack = ...  # type: List[_FontType]
    margin_stack = ...  # type: List[int]
    spacing = ...  # type: Optional[str]
    style_stack = ...  # type: Any
    nospace = ...  # type: int
    softspace = ...  # type: int
    para_end = ...  # type: int
    parskip = ...  # type: int
    hard_break = ...  # type: int
    have_label = ...  # type: int
    def __init__(self, writer: NullWriter) -> None: ...
    def end_paragraph(self, blankline: int) -> None: ...
    def add_line_break(self) -> None: ...
    def add_hor_rule(self, *args, **kw) -> None: ...
    def add_label_data(self, format, counter: int, blankline: Optional[int] = ...) -> None: ...
    def format_counter(self, format, counter: int) -> str: ...
    def format_letter(self, case: str, counter: int) -> str: ...
    def format_roman(self, case: str, counter: int) -> str: ...
    def add_flowing_data(self, data: str) -> None: ...
    def add_literal_data(self, data: str) -> None: ...
    def flush_softspace(self) -> None: ...
    def push_alignment(self, align: Optional[str]) -> None: ...
    def pop_alignment(self) -> None: ...
    def push_font(self, font: _FontType) -> None: ...
    def pop_font(self) -> None: ...
    def push_margin(self, margin: int) -> None: ...
    def pop_margin(self) -> None: ...
    def set_spacing(self, spacing: Optional[str]) -> None: ...
    def push_style(self, *styles: _StylesType) -> None: ...
    def pop_style(self, n: int = ...) -> None: ...
    def assert_line_data(self, flag: int = ...) -> None: ...

class NullWriter:
    def __init__(self) -> None: ...
    def flush(self) -> None: ...
    def new_alignment(self, align: Optional[str]) -> None: ...
    def new_font(self, font: _FontType) -> None: ...
    def new_margin(self, margin: int, level: int) -> None: ...
    def new_spacing(self, spacing: Optional[str]) -> None: ...
    def new_styles(self, styles) -> None: ...
    def send_paragraph(self, blankline: int) -> None: ...
    def send_line_break(self) -> None: ...
    def send_hor_rule(self, *args, **kw) -> None: ...
    def send_label_data(self, data: str) -> None: ...
    def send_flowing_data(self, data: str) -> None: ...
    def send_literal_data(self, data: str) -> None: ...

class AbstractWriter(NullWriter):
    def new_alignment(self, align: Optional[str]) -> None: ...
    def new_font(self, font: _FontType) -> None: ...
    def new_margin(self, margin: int, level: int) -> None: ...
    def new_spacing(self, spacing: Optional[str]) -> None: ...
    def new_styles(self, styles) -> None: ...
    def send_paragraph(self, blankline: int) -> None: ...
    def send_line_break(self) -> None: ...
    def send_hor_rule(self, *args, **kw) -> None: ...
    def send_label_data(self, data: str) -> None: ...
    def send_flowing_data(self, data: str) -> None: ...
    def send_literal_data(self, data: str) -> None: ...

class DumbWriter(NullWriter):
    file = ...  # type: IO
    maxcol = ...  # type: int
    def __init__(self, file: Optional[IO] = ..., maxcol: int = ...) -> None: ...
    def reset(self) -> None: ...
    def send_paragraph(self, blankline: int) -> None: ...
    def send_line_break(self) -> None: ...
    def send_hor_rule(self, *args, **kw) -> None: ...
    def send_literal_data(self, data: str) -> None: ...
    def send_flowing_data(self, data: str) -> None: ...

def test(file: Optional[str] = ...) -> None: ...
