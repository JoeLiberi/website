from django.forms import ModelForm
from .models import Position

class PositionForm(ModelForm):
	class Meta:
		model = Position
		#fields = ['security_symbol', 'price_per_contract', 'price_underlying', 'strike_price', 'commission']
		exclude = ['security_name', 'created']

	def __str__(self):
		return self.security