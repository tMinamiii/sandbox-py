"""ElaticsearchのRecipeDocument Entity."""
from __future__ import annotations

from typing import Any

from elasticsearch_dsl import Date, Document, InnerDoc, Integer, Keyword, Long, Nested, Text, analyzer

from context import exception_handler
from es.connection import esclient
from utils import env

INDEX_SETTINGS = (
    {"number_of_shards": 5, "number_of_replicas": 1}
    if env.IS_PROD
    else {"number_of_shards": 1, "number_of_replicas": 0}
)

recipe_app_analyzer = analyzer(
    "sandbox",
    tokenizer="kuromoji_tokenizer",
    filter=[{"type": "synonym", "synonyms_path": env.ELASTICSEARCH_REFERENCE_PATH}],
)

recipe_anaylzer = "sandbox" if env.ELASTICSEARCH_REFERENCE_PATH else "kuromoji"


class CategoryInnerDoc(InnerDoc):
    group = Keyword()  # グループ名
    name = Keyword()  # カテゴリ名


class MaterialDocument(Document):
    class Index:
        name = "materials"
        using = esclient
        settings = INDEX_SETTINGS
        analyzer = recipe_app_analyzer

    material_id = Long()
    name = Text(analyzer=recipe_anaylzer)
    description = Text(analyzer=recipe_anaylzer)  # レシピの説明文
    total_reviews = Integer()  # レビュー件数
    released_at = Date()  # 公開日
    image_url = Keyword()  # レシピの画像URL
    categories = Nested(CategoryInnerDoc)

    created_at = Date()
    updated_at = Date()

    def save(self, **kwargs: Any) -> Any:
        with exception_handler():
            return super().save(**kwargs)

    def delete(self, **kwargs: Any) -> Any:
        with exception_handler():
            return super().delete(**kwargs)
