from _typeshed import Incomplete

from influxdb_client.domain.expression import Expression

class ObjectExpression(Expression):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, type: Incomplete | None = None, properties: Incomplete | None = None) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def properties(self): ...
    @properties.setter
    def properties(self, properties) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
