import numpy
import pyuipc.constitution
import pyuipc.diff_sim
import pyuipc.geometry
from typing import Callable, ClassVar, overload

Error: SanityCheckResult
Success: SanityCheckResult
Warning: SanityCheckResult

class Animation:
    class UpdateHint:
        def __init__(self, *args, **kwargs) -> None: ...

    class UpdateInfo:
        def __init__(self, *args, **kwargs) -> None: ...
        def dt(self) -> float: ...
        def frame(self) -> int: ...
        def geo_slots(self) -> list: ...
        def hint(self) -> Animation.UpdateHint: ...
        def object(self) -> Object: ...
        def rest_geo_slots(self) -> list: ...
    def __init__(self, *args, **kwargs) -> None: ...

class Animator:
    def __init__(self, *args, **kwargs) -> None: ...
    def erase(self, arg0: int) -> None: ...
    def insert(self, arg0: Object, arg1: Callable) -> None: ...
    @overload
    def substep(self, arg0: int) -> None: ...
    @overload
    def substep(self) -> int: ...

class ConstitutionTabular:
    def __init__(self) -> None: ...
    def insert(self, arg0: pyuipc.constitution.IConstitution) -> None: ...
    def types(self) -> set[str]: ...
    def uids(self) -> numpy.ndarray[numpy.uint64]: ...

class ContactElement:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, id: int, name: str) -> None: ...
    def apply_to(self, arg0: pyuipc.geometry.Geometry) -> pyuipc.geometry.AttributeSlotI32: ...
    def id(self) -> int: ...
    def name(self) -> str: ...

class ContactTabular:
    def __init__(self) -> None: ...
    def create(self, name: str = ...) -> ContactElement: ...
    def default_element(self) -> ContactElement: ...
    def default_model(self, friction_rate: float, resistance: float, config: json = ...) -> None: ...
    def element_count(self) -> int: ...
    def insert(self, L: ContactElement, R: ContactElement, friction_rate: float, resistance: float, enable: bool = ..., config: json = ...) -> None: ...

class DiffSim:
    def __init__(self, *args, **kwargs) -> None: ...
    def H(self) -> pyuipc.diff_sim.SparseCOOView: ...
    def clear(self) -> None: ...
    def pGpP(self) -> pyuipc.diff_sim.SparseCOOView: ...
    def parameters(self) -> pyuipc.diff_sim.ParameterCollection: ...

class Engine:
    def __init__(self, backend_name: str, workspace: str = ..., config: json = ...) -> None: ...
    def backend_name(self) -> str: ...

class Object:
    class Geometries:
        def __init__(self, *args, **kwargs) -> None: ...
        @overload
        def create(self, arg0: pyuipc.geometry.SimplicialComplex) -> tuple[pyuipc.geometry.SimplicialComplexSlot, pyuipc.geometry.SimplicialComplexSlot]: ...
        @overload
        def create(self, arg0: pyuipc.geometry.SimplicialComplex, arg1: pyuipc.geometry.SimplicialComplex) -> tuple[pyuipc.geometry.SimplicialComplexSlot, pyuipc.geometry.SimplicialComplexSlot]: ...
        @overload
        def create(self, arg0: pyuipc.geometry.ImplicitGeometry) -> tuple[pyuipc.geometry.ImplicitGeometrySlot, pyuipc.geometry.ImplicitGeometrySlot]: ...
        @overload
        def create(self, arg0: pyuipc.geometry.ImplicitGeometry, arg1: pyuipc.geometry.ImplicitGeometry) -> tuple[pyuipc.geometry.ImplicitGeometrySlot, pyuipc.geometry.ImplicitGeometrySlot]: ...
        def ids(self) -> numpy.ndarray[numpy.int32]: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def geometries(self) -> Object.Geometries: ...
    def id(self) -> int: ...
    def name(self) -> str: ...

class SanityCheckMessage:
    def __init__(self, *args, **kwargs) -> None: ...
    def geometries(self) -> dict[str, pyuipc.geometry.Geometry]: ...
    def id(self) -> int: ...
    def is_empty(self) -> bool: ...
    def message(self) -> str: ...
    def name(self) -> str: ...
    def result(self) -> SanityCheckResult: ...

class SanityCheckResult:
    __members__: ClassVar[dict] = ...  # read-only
    Error: ClassVar[SanityCheckResult] = ...
    Success: ClassVar[SanityCheckResult] = ...
    Warning: ClassVar[SanityCheckResult] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class SanityChecker:
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, arg0: str) -> SanityCheckResult: ...
    def clear(self) -> None: ...
    def errors(self) -> dict[int, SanityCheckMessage]: ...
    def infos(self) -> dict[int, SanityCheckMessage]: ...
    def report(self) -> None: ...
    def warns(self) -> dict[int, SanityCheckMessage]: ...

class Scene:
    class Geometries:
        def __init__(self, *args, **kwargs) -> None: ...
        def find(self, arg0: int) -> tuple[pyuipc.geometry.GeometrySlot, pyuipc.geometry.GeometrySlot]: ...

    class Objects:
        def __init__(self, *args, **kwargs) -> None: ...
        def create(self, arg0: str) -> Object: ...
        def destroy(self, arg0: int) -> None: ...
        def find(self, arg0: int) -> Object: ...
        def size(self) -> int: ...
    def __init__(self, config: json = ...) -> None: ...
    def animator(self) -> Animator: ...
    def constitution_tabular(self) -> ConstitutionTabular: ...
    def contact_tabular(self) -> ContactTabular: ...
    @staticmethod
    def default_config() -> json: ...
    def diff_sim(self) -> DiffSim: ...
    def geometries(self) -> Scene.Geometries: ...
    def objects(self) -> Scene.Objects: ...
    def sanity_checker(self) -> SanityChecker: ...

class SceneIO:
    def __init__(self, scene: Scene) -> None: ...
    @overload
    def simplicial_surface(self) -> pyuipc.geometry.SimplicialComplex: ...
    @overload
    def simplicial_surface(self, arg0: int) -> pyuipc.geometry.SimplicialComplex: ...
    def write_surface(self, filename: str) -> None: ...

class World:
    def __init__(self, arg0: Engine) -> None: ...
    def advance(self) -> None: ...
    def backward(self) -> None: ...
    def dump(self) -> bool: ...
    def frame(self) -> int: ...
    def init(self, scene: Scene) -> None: ...
    def recover(self, dst_frame: int = ...) -> bool: ...
    def retrieve(self) -> None: ...
    def sync(self) -> None: ...
