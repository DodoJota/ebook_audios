import decimal
from collections.abc import Callable, Iterable, Iterator, Mapping
from contextlib import AbstractContextManager
from decimal import Decimal
from types import TracebackType
from typing import Any, TypeVar, overload
from typing_extensions import Self

from django.apps.registry import Apps
from django.conf import LazySettings, Settings
from django.core.checks.registry import CheckRegistry
from django.db import DefaultConnectionProxy
from django.test.runner import DiscoverRunner
from django.test.testcases import SimpleTestCase

_TestClass = type[SimpleTestCase]
_DecoratedTest = Callable[..., Any] | _TestClass
_C = TypeVar("_C", bound=Callable[..., Any])
_T = TypeVar("_T")
_U = TypeVar("_U")
_TestClassGeneric = TypeVar("_TestClassGeneric", bound=_TestClass)

TZ_SUPPORT: bool = ...

class Approximate:
    val: decimal.Decimal | float = ...
    places: int = ...
    def __init__(self, val: Decimal | float, places: int = ...) -> None: ...

class ContextList(list[Mapping[str, _T]]):
    def get(self, key: str, default: _U | None = ...) -> _T | _U | None: ...
    def keys(self) -> set[str]: ...

class _TestState: ...

def setup_test_environment(debug: bool | None = ...) -> None: ...
def teardown_test_environment() -> None: ...
def setup_databases(
    verbosity: int,
    interactive: bool,
    *,
    time_keeper: Any | None = ...,
    keepdb: bool = ...,
    debug_sql: bool = ...,
    parallel: int = ...,
    aliases: Iterable[str] | None = ...,
    **kwargs: Any
) -> list[tuple[DefaultConnectionProxy, str, bool]]: ...
def get_runner(
    settings: LazySettings, test_runner_class: str | None = ...
) -> type[DiscoverRunner]: ...

class TestContextDecorator:
    attr_name: str | None = ...
    kwarg_name: str | None = ...
    def __init__(
        self, attr_name: str | None = ..., kwarg_name: str | None = ...
    ) -> None: ...
    def enable(self) -> Any | None: ...
    def disable(self) -> None: ...
    def __enter__(self) -> Any | None: ...
    def __exit__(
        self,
        exc_type: type[Exception] | None,
        exc_value: Exception | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def decorate_class(self, cls: _TestClassGeneric) -> _TestClassGeneric: ...
    def decorate_callable(self, func: _C) -> _C: ...
    @overload
    def __call__(self, decorated: _TestClassGeneric) -> _TestClassGeneric: ...
    @overload
    def __call__(self, decorated: _C) -> _C: ...

class override_settings(TestContextDecorator):
    enable_exception: bool | None = ...
    wrapped: Settings = ...
    options: dict[str, Any] = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def save_options(self, test_func: _DecoratedTest) -> None: ...

class modify_settings(override_settings):
    wrapped: Settings
    operations: list[tuple[str, dict[str, list[str] | str]]] = ...
    options: dict[str, list[tuple[str, str] | str]] = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save_options(self, test_func: _DecoratedTest) -> None: ...

class override_system_checks(TestContextDecorator):
    registry: CheckRegistry = ...
    new_checks: list[Callable[..., Any]] = ...
    deployment_checks: list[Callable[..., Any]] | None = ...
    old_checks: set[Callable[..., Any]] = ...
    old_deployment_checks: set[Callable[..., Any]] = ...
    def __init__(
        self,
        new_checks: list[Callable[..., Any]],
        deployment_checks: list[Callable[..., Any]] | None = ...,
    ) -> None: ...

class CaptureQueriesContext:
    connection: Any = ...
    force_debug_cursor: bool = ...
    initial_queries: int = ...
    final_queries: int | None = ...
    def __init__(self, connection: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, index: int) -> dict[str, str]: ...
    def __len__(self) -> int: ...
    @property
    def captured_queries(self) -> list[dict[str, str]]: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: None, exc_value: None, traceback: None) -> None: ...

class ignore_warnings(TestContextDecorator):
    ignore_kwargs: dict[str, Any] = ...
    filter_func: Callable[..., Any] = ...
    def __init__(self, **kwargs: Any) -> None: ...
    catch_warnings: AbstractContextManager[list[Any] | None] = ...

requires_tz_support: Any

def isolate_lru_cache(lru_cache_object: Callable[..., Any]) -> Iterator[None]: ...

class override_script_prefix(TestContextDecorator):
    prefix: str = ...
    def __init__(self, prefix: str) -> None: ...
    old_prefix: str = ...

class LoggingCaptureMixin:
    logger: Any = ...
    old_stream: Any = ...
    logger_output: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

class isolate_apps(TestContextDecorator):
    installed_apps: tuple[str] = ...
    def __init__(self, *installed_apps: Any, **kwargs: Any) -> None: ...
    old_apps: Apps = ...

def tag(*tags: str) -> Callable[[_T], _T]: ...
