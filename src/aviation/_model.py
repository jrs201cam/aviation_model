"""Decorate functions as transforms."""

__all__ = ("Transform", "transform")

import collections.abc
import inspect
import typing


class Transform[R, **P](typing.Protocol):
    name: str
    parameters: tuple[str, ...]

    def __call__(*args: P.args, **kwargs: P.kwargs) -> R: ...


def transform[R, **P](
    function: collections.abc.Callable[P, R],
) -> Transform[R, P]:
    transform = typing.cast("Transform[R,P]", function)
    transform.name = function.__name__
    transform.parameters = tuple(inspect.signature(transform).parameters.keys())
    return transform
