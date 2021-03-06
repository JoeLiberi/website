from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.conf import settings
from tinymce.models import HTMLField

import datetime

# Create your models here.
class Post(models.Model):
	 # Post Model

	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	title = models.CharField(_('title'), max_length=200)
	# body = models.TextField(_('body'), )
	body = HTMLField(_('body'), )
	tease = models.TextField(_('tease'), blank=True, help_text=_('Concise text suggested. Does not appear in RSS feed.'))
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
	allow_comments = models.BooleanField(_('allow comments'), default=True)
	publish = models.DateTimeField(_('publish'), default=datetime.datetime.now)
	created = models.DateTimeField(_('created'), auto_now_add=True)
	modified = models.DateTimeField(_('modified'), auto_now=True)

	class Meta:
		verbose_name = _('post')
		verbose_name_plural = _('posts')
		db_table  = 'blog_posts'
		ordering  = ('-publish',)
		get_latest_by = 'publish'

	def __unicode__(self):
		return u'%s' % self.title

	def __str__(self):
		return self.title

	@permalink
	def get_absolute_url(self):
		return ('blog_detail', None, {
			'year': self.publish.year,
			'month': self.publish.strftime('%b').lower(),
			'day': self.publish.day
		})

	def get_previous_post(self):
		return self.get_previous_by_publish(status__gte=2)

	def get_next_post(self):
		return self.get_next_by_publish(status__gte=2)