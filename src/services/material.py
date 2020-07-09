from typing import List

from db.models import Material, MaterialCategory
from es.document import CategoryInnerDoc, MaterialDocument


class MaterialService:
    @staticmethod
    def model_to_doc(material: Material) -> MaterialDocument:
        doc = MaterialDocument()
        doc.meta.id = material.id
        doc.material_id = material.id
        doc.title = material.title
        doc.total_reviews = material.total_reviews
        doc.released_at = material.released_at
        doc.image_url = material.image_url
        doc.updated_at = material.updated_at
        doc.created_at = material.created_at

        categories: List[MaterialCategory] = material.categories
        for c in categories:
            group = c.material_category_group.name
            cat_doc = CategoryInnerDoc()
            cat_doc.group = group
            cat_doc.name = c.name
            doc.categories.append(cat_doc)

        return doc
