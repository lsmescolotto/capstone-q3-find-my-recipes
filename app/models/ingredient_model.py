from marshmallow import Schema, fields
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String


class IngredientSchema(Schema):
    ingredient_id = fields.Int()
    title = fields.Str()


class IngredientModel(db.Model):
    ingredient_id = int
    title = str

    __tablename__ = "ingredient"

    ingredient_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
