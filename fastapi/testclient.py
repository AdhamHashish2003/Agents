from typing import Any


class Response:
    def __init__(self, status_code: int, payload: Any) -> None:
        self.status_code = status_code
        self._payload = payload

    def json(self) -> Any:
        return self._payload


class TestClient:
    __test__ = False

    def __init__(self, app: Any) -> None:
        self.app = app

    def get(self, path: str) -> "Response":
        handler = self.app._routes.get(("GET", path))
        if not handler:
            return Response(404, {"detail": "Not Found"})
        payload = handler()
        return Response(200, payload)


__all__ = ["TestClient"]
