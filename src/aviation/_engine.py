import collections.abc
import typing

from aviation._model import Transform


class SystemsModel:
    def __init__(self, transforms: collections.abc.Sequence[Transform[typing.Any, ...]]) -> None:
        self.transforms = set(transforms)

    def evaluate(self, inputs: dict[str, typing.Any], output: str) -> typing.Any:  # noqa: ANN401
        # If the requested output has already been supplied as an input then this can just be
        # returned directly without any need for computation
        # If transform not found in self.transforms there must be an error

        if output in inputs:
            return inputs[output]
        for transform in self.transforms:
            if transform.name == output:
                break
        else:
            message = f"No transform with name '{output}'"
            raise ValueError(message)
        for parameter in transform.parameters:
            if parameter not in inputs:
                inputs[parameter] = self.evaluate(inputs, parameter)
        arguments = {parameter: inputs[parameter] for parameter in transform.parameters}
        return transform(**arguments)
