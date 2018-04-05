from collections import Iterable
import numpy as np

from .form.utils import docval, popargs, call_docval_func, get_docval
from .form import Container
from . import register_class, CORE_NAMESPACE
from .core import NWBContainer, NWBDataInterface


@register_class('BaseTransform', CORE_NAMESPACE)
class BaseTransform(Container):
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
             'doc': 'Reference to the destination coordinate system'})
    def __init__(self, **kwargs):
        transform_type, source_cs, destination_cs = popargs(
            'transform_type', 'source_cs', 'destination_cs', kwargs)
        call_docval_func(super(BaseTransform, self).__init__, kwargs)
        self.source_cs = source_cs
        self.destination_cs = destination_cs


@register_class('STTransform', CORE_NAMESPACE)
class STTransform(BaseTransform):

    @docval({'name': 'scale', 'type': Iterable,
             'doc': 'Parameters'},
            {'name': 'translate', 'type': Iterable,
             'doc': 'Parameters'},
            *get_docval(BaseTransform.__init__))
    def __init__(self, **kwargs):
        print("ST")
        print(kwargs)
        scale, translate = popargs('scale', 'translate', kwargs)
        self.scale = scale
        self.translate = translate
        kwargs["transform_type"] = "STTransform"
        print(kwargs)
        call_docval_func(super(STTransform, self).__init__, kwargs)


    @property
    def parameters(self):
        return np.hstack((self.scale, self.translation))
