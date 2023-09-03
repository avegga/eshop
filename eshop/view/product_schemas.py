from marshmallow import Schema, fields


class ProductHttpDto(Schema):
    class Meta:
        fields = ["id", "name", "price"]

    id = fields.Str()
    name = fields.Str()
    price = fields.Int()


class ProductCreateDtoSchema(Schema):
    id = fields.String()
    name = fields.Str()
    price = fields.Float()


class ProductSchema(Schema):
    id = fields.String()
    name = fields.Str()
    price = fields.Float()


class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)