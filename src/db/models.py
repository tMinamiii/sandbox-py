from __future__ import annotations

from typing import List

from sqlalchemy import Column, ForeignKey, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, INTEGER, TINYINT, VARCHAR
from sqlalchemy.orm import Query, relationship
from sqlalchemy.orm.relationships import RelationshipProperty

from .session import Base


class MaterialCategory(Base):
    __tablename__ = "materials"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_general_ci",
        "comment": "商品マスタ",
    }
    query: Query

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="主キー")
    material_id = Column(INTEGER, ForeignKey("materials.id"), nullable=False, comment="商品ID")
    group = Column(VARCHAR(255), nullable=False, default="", comment="カテゴリグループ名")
    name = Column(VARCHAR(255), nullable=False, default="", comment="カテゴリ名")

    created_at = Column(DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment="作成日時")
    updated_at = Column(
        DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新日時"
    )

    def __repr__(self) -> str:
        return f"id={self.id} name={self.name} description={self.description} comment={self.comment}"


class Material(Base):
    __tablename__ = "materials"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_general_ci",
        "comment": "商品マスタ",
    }
    query: Query

    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="主キー")
    name = Column(VARCHAR(255), nullable=False, default="", comment="レビューコメント")
    description = Column(VARCHAR(512), nullable=False, default="", comment="レビューコメント")
    released_at = Column(DATETIME, nullable=True, comment="発売日時")
    total_reviews = Column(INTEGER, nullable=False, default=0, comment="レビュー数")
    image_url = Column(VARCHAR(255), nullable=False, default="", comment="画像URL")

    created_at = Column(DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment="作成日時")
    updated_at = Column(
        DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新日時"
    )

    categories: RelationshipProperty[List[MaterialCategory]] = relationship("MaterialCategory", cascade="delete")

    def __repr__(self) -> str:
        return f"id={self.id} name={self.name} description={self.description} comment={self.comment}"


class UserReview(Base):
    __tablename__ = "user_reviews"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_general_ci",
        "comment": "ユーザーレビュー",
    }
    query: Query

    id = Column(BIGINT, primary_key=True, autoincrement=True, comment="主キー")
    user_id = Column(INTEGER, ForeignKey("users.id"), nullable=False, comment="ユーザーのID",)
    star = Column(TINYINT, nullable=False, default=0, comment="レビューコメント")
    comment = Column(VARCHAR(512), nullable=False, default="", comment="レビューコメント")

    created_at = Column(DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment="作成日時")
    updated_at = Column(
        DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新日時"
    )

    def __repr__(self) -> str:
        return f"id={self.id} user_id={self.user_id} star={self.star} comment={self.comment}"


class User(Base):
    __tablename__ = "users"
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_general_ci",
        "comment": "ユーザー",
    }
    query: Query

    # 楽観的な排他制御
    version_id = Column(BIGINT, nullable=False)
    __mapper_args__ = {"version_id_col": version_id}

    # Column
    id = Column(INTEGER, primary_key=True, autoincrement=True, comment="主キー")
    name = Column(VARCHAR(50), nullable=False, default="", comment="名前")

    created_at = Column(DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP"), comment="作成日時")
    updated_at = Column(
        DATETIME, nullable=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment="更新日時"
    )

    user_reviews: RelationshipProperty[List[UserReview]] = relationship("RecipeReview", cascade="delete")

    def __repr__(self) -> str:
        return f"id={self.id} user_id={self.user_id} star={self.star} comment={self.comment}"
