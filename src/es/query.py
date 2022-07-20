from elasticsearch_dsl import Q

from logger import Logger

log = Logger(__name__)


class MaterialQuery:
    def build(self, q: str) -> Q:
        title_query = Q("match", title={"query": q, "operator": "and"})
        description_query = Q("match", description={"query": q, "operator": "and"})
        query = title_query | description_query

        category_query = Q("term", categories__group="グループ名") & Q("term", categories__name="カテゴリ名")

        query = query & Q("nested", path="categories", query=category_query)
        log.info(str(query))
        return query
