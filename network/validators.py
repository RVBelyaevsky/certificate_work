from rest_framework import serializers


class CannotUpdateFieldValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if dict(value).get(self.field):
            raise serializers.ValidationError(
                "Запрещено обновлять это поле."
            )
