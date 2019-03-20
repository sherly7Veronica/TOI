from rest_framework import serializers

from toi.models import Level1, Level2, Level3


class Level1serializer(serializers.ModelSerializer):

	class Meta:
		model = Level1
		fields = (
			'id',
			'name',
		)


class Level2serializer(serializers.ModelSerializer):

	class Meta:
		model = Level2
		fields = (
			'id',
			'name',
			'submenu'
		)


class Level3serializer(serializers.ModelSerializer):

	class Meta:
		model = Level3
		fields = (
			'__all__'
		)



