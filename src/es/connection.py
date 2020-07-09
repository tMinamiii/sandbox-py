"""ElaticsearchのRecipeDocument Entity."""
from __future__ import annotations

from elasticsearch_dsl import connections
from utils import env

esclient = "recipeapp"

if "localhost" in env.ELASTICSEARCH_HOST:
    connections.create_connection(
        alias=esclient,
        hosts=[env.ELASTICSEARCH_HOST],
        port=env.ELASTICSEARCH_PORT,
        use_ssl=False,
        verify_certs=False,
        max_retries=3,
        timeout=15,
        retry_on_timeout=True,
        retry_on_status=[409, 429, 500, 501, 502, 503, 504],
    )
else:
    connections.create_connection(
        alias=esclient,
        hosts=[env.ELASTICSEARCH_HOST],
        port=env.ELASTICSEARCH_PORT,
        scheme="https",
        use_ssl=True,
        verify_certs=True,
        max_retries=7,
        timeout=15,
        retry_on_timeout=True,
        retry_on_status=[409, 429, 500, 501, 502, 503, 504],
    )
