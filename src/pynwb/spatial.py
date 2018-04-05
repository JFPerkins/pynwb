from collections import Iterable
import numpy as np

from .form.utils import docval, popargs, call_docval_func, get_docval
from . import register_class, CORE_NAMESPACE
from .core import NWBDataInterface


@register_class('BaseTransform', CORE_NAMESPACE)
class BaseTransform(NWBDataInterface):
    """A generic base class for representing spatial transform data"""
    __nwbfields__ = ('transform_type',
                     'source_cs',
                     'destination_cs')

    @docval({'name': 'transform_type', 'type': str,
             'doc': 'Type of the transform',
             'default': None},
            {'name': 'source_cs', 'type': str,
             'doc': 'Reference to the source coordinate system',
             'default': None},
            {'name': 'destination_cs', 'type': str,
             'doc': 'Reference to the destination coordinate system'},
            *get_docval(NWBDataInterface.__init__))
    def __init__(self, **kwargs):
        transform_type, source_cs, destination_cs = popargs(
            'transform_type', 'source_cs', 'destination_cs', kwargs)
        call_docval_func(super(BaseTransform, self).__init__, kwargs)
        self.source_cs = source_cs
        self.destination_cs = destination_cs
        self.transform_type = transform_type


@register_class('STTransform', CORE_NAMESPACE)
class STTransform(BaseTransform):
    __nwbfields__ = ('scale',
                     'translate')

    @docval({'name': 'scale', 'type': Iterable,
             'doc': 'Parameters'},
            {'name': 'translate', 'type': Iterable,
             'doc': 'Parameters'},
            *get_docval(BaseTransform.__init__))
    def __init__(self, **kwargs):
        scale, translate = popargs('scale', 'translate', kwargs)
        kwargs["transform_type"] = "STTransform"
        call_docval_func(super(STTransform, self).__init__, kwargs)
        self.scale = scale
        self.translate = translate
        
