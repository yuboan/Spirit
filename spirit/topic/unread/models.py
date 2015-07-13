# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class TopicUnread(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"))
    topic = models.ForeignKey('spirit.Topic')

    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'topic')
        ordering = ['-date', '-pk']
        verbose_name = _("topic unread")
        verbose_name_plural = _("topics unread")
        db_table = 'spirit_unread_topicunread'  # TODO: remove in Spirit 0.4

    def __str__(self):
        return "%s read %s" % (self.user, self.topic)

    def get_absolute_url(self):
        return self.topic.get_absolute_url()