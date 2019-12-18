from ..argument import Argument as Argument
from ..field import Field as Field
from ..inputfield import InputField as InputField
from ..inputobjecttype import InputObjectType as InputObjectType
from ..objecttype import ObjectType as ObjectType
from ..scalars import Boolean as Boolean, String as String
from ..schema import Schema as Schema
from ..unmountedtype import UnmountedType as UnmountedType

class MyType: ...

class MyScalar(UnmountedType):
    def get_type(self) -> Any: ...

def test_generate_inputobjecttype() -> None: ...
def test_generate_inputobjecttype_with_meta() -> None: ...
def test_generate_inputobjecttype_with_fields() -> None: ...
def test_ordered_fields_in_inputobjecttype() -> None: ...
def test_generate_inputobjecttype_unmountedtype() -> None: ...
def test_generate_inputobjecttype_as_argument() -> None: ...
def test_generate_inputobjecttype_inherit_abstracttype() -> None: ...
def test_generate_inputobjecttype_inherit_abstracttype_reversed() -> None: ...
def test_inputobjecttype_of_input() -> Any: ...
