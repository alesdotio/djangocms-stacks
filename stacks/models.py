import uuid
from django.db import models
from cms.models.fields import PlaceholderField
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings


class Stack(models.Model):
    name = models.CharField(max_length=255, blank=True, default='', verbose_name=_("name"))
    code = models.CharField(max_length=255, unique=True, blank=True)
    content = PlaceholderField(slotname='stack_content', verbose_name=_('content'), related_name='stacks_contents')

    class Meta:
        verbose_name = _('stack')
        verbose_name_plural = _('stacks')
        unique_together = ('code',)

    def __unicode__(self):
        return self.name

    def clean(self):
        # TODO: check for clashes if the random code is already taken
        if not self.code:
            self.code = u"stack-%s" % uuid.uuid4()


class StackLink(CMSPlugin):
    stack = models.ForeignKey(Stack, verbose_name=_("stack"))

    def __unicode__(self):
        return self.stack.name
