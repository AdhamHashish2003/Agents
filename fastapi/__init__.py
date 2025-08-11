from typing import Callable, Dict, Tuple, Any


class FastAPI:
    """Minimal FastAPI stub used for offline testing."""

    def __init__(self) -> None:
        self._routes: Dict[Tuple[str, str], Callable[..., Any]] = {}

    def get(self, path: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Register a GET route."""

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._routes[("GET", path)] = func
            return func

        return decorator


__all__ = ["FastAPI"]
