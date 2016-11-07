from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm

# Create your models here.
class Position(models.Model):
	security_name = models.CharField(max_length=200)
	security_symbol = models.CharField(max_length=200)
	price_per_contract = models.DecimalField(max_digits=6, decimal_places=2)
	price_underlying = models.DecimalField(max_digits=7, decimal_places=2)
	strike_price = models.DecimalField(max_digits=6, decimal_places=2)
	commission = models.DecimalField(max_digits=6, decimal_places=2)
	created = models.DateTimeField(_('created'), auto_now_add=True)

	def __unicode__(self):
		return u'%s' % self.security_symbol

	def __str__(self):
		return self.security_symbol

class PositionForm(ModelForm):
	class Meta:
		model = Position
		fields = ['security_symbol', 'price_per_contract', 'price_underlying', 'strike_price', 'commission']