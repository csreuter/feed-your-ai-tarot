from typing import Any, Generator

import pyarrow as pa
from cloudquery.sdk.scheduler import TableResolver
from cloudquery.sdk.schema import Column
from cloudquery.sdk.schema import Table
from cloudquery.sdk.schema.resource import Resource

from plugin.client import Client


class TarotCards(Table):
    def __init__(self) -> None:
        super().__init__(
            name="tarot_cards",
            title="Tarot Cards",
            columns=[
                Column("card_number", pa.uint64(), primary_key=True),
                Column("card_name", pa.string()),
                Column("description", pa.string()),
                Column("front_image_base64", pa.string()),
                Column("back_image_base64", pa.string()),
                Column("special_instructions", pa.string()),
                Column("sync_time", pa.timestamp("ms")),
            ],
        )

    @property
    def resolver(self):
        return TarotCardResolver(table=self)


class TarotCardResolver(TableResolver):
    def __init__(self, table) -> None:
        super().__init__(table=table)

    def resolve(
        self, client: Client, parent_resource: Resource
    ) -> Generator[Any, None, None]:
        for card_response in client.client.get_random_card():
            yield card_response
