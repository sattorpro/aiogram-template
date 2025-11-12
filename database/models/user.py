from tortoise import fields, models

class User(models.Model):
    id = fields.BigIntField(pk=True)
    user_id = fields.BigIntField(unique=True)
    language = fields.CharField(max_length=10, default='en')
    chat_type = fields.CharField(max_length=20, default='private')
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)