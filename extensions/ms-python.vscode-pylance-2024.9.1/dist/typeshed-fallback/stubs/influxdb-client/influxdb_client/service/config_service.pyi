from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class ConfigService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def get_config(self, **kwargs): ...
    def get_config_with_http_info(self, **kwargs): ...
    async def get_config_async(self, **kwargs): ...
    def get_flags(self, **kwargs): ...
    def get_flags_with_http_info(self, **kwargs): ...
    async def get_flags_async(self, **kwargs): ...
