from dataclasses import dataclass, field
from cloudquery.sdk.scheduler import Client as ClientABC

from plugin.tarot.client import TarotClient

DEFAULT_CONCURRENCY = 100
DEFAULT_QUEUE_SIZE = 10000


@dataclass
class Spec:
    randomness_seed: int = field(default=None)
    concurrency: int = field(default=DEFAULT_CONCURRENCY)
    queue_size: int = field(default=DEFAULT_QUEUE_SIZE)

    def validate(self):
        pass
        # No strict validation needed - randomness_seed is optional


class Client(ClientABC):
    def __init__(self, spec: Spec) -> None:
        self._spec = spec
        self._client = TarotClient(spec.randomness_seed)

    def id(self):
        return "tarot-cards"

    @property
    def client(self) -> TarotClient:
        return self._client
