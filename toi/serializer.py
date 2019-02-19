from rest_framework import serializers

from toi.models import Level1


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Level1
		fields = (
			'id',
			'menu',
		)


