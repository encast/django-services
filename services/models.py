from datetime import datetime
from django.conf import settings

if 'gis.db' in settings.DATABASES.get('default', {}).get('ENGINE', ''):
    from django.contrib.gis.db import models
else:
    from django.db import models

from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.postgres.fields.jsonb import JSONField


class BaseModel(models.Model):
    created_date = models.DateTimeField(default=datetime.utcnow, db_index=True)
    last_modified = models.DateTimeField(default=datetime.utcnow, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        d = []

        for field in self.__class__._meta.fields:
            field_name = field.name
            if field.primary_key:
                continue
            if field_name in [f.name for f in BaseModel._meta.fields]:
                continue
            if isinstance(field, (TextField, ForeignKey, JSONField)):
                continue
            d.append(getattr(self, field_name))

        return ", ".join([str(val) for val in d])

    @property
    def dict(self):
        ret = self.__dict__
        return dict((k, v) for k, v in ret.items() if not k.startswith('_'))

    def save(self, *args, **kwargs):
        self.last_modified = datetime.utcnow()
        super(BaseModel, self).save(*args, **kwargs)


class ModelDTO(object):

    def save(self, *args, **kwargs):
        m = self.get_model_class()()
        for field in m._meta.fields:
            setattr(m, field.name, getattr(self, field.name, None))
        m.save(*args, **kwargs)
        return m

    def get_model_class(self):
        return self.__class__.__bases__[1]

    class Meta:
        abstract = True
