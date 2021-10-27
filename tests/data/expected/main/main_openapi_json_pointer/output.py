# generated by datamodel-codegen:
#   filename:  json_pointer.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class TestNestedNested(BaseModel):
    test_nested_nested_string: Optional[str] = None


class TestNested(BaseModel):
    test_string: Optional[str] = None
    nested_nested: Optional[TestNestedNested] = None


class Test(TestNested):
    pass


class Foo(Test):
    pass