import h5py

from ...utils import docval, getargs, popargs, call_docval_func
from ...data_utils import RegionSlicer, DataIO


class H5RegionSlicer(RegionSlicer):

    @docval({'name': 'dataset', 'type': h5py.Dataset, 'doc': 'the HDF5 dataset to slice'},
            {'name': 'region', 'type': h5py.RegionReference, 'doc': 'the region reference to use to slice'})
    def __init__(self, **kwargs):
        self.__dataset = getargs('dataset', kwargs)
        self.__regref = getargs('region', kwargs)
        self.__len = self.__dataset.regionref.selection(self.__regref)[0]

    def __read_region(self):
        if self.__region is None:
            self.__region = self.__dataset[self.__regref]

    def __getitem__(self, idx):
        self.__read_region()
        return self.__region[idx]

    def __len__(self):
        return self.__len


class H5DataIO(DataIO):

    @docval({'name': 'data', 'type': 'array_data', 'doc': 'the data to be written'},
            {'name': 'compress', 'type': bool,
             'doc': 'Flag to use gzip compression filter on dataset', 'default': False})
    def __init__(self, **kwargs):
        compress = popargs('compress', kwargs)
        call_docval_func(super(H5DataIO, self).__init__, kwargs)
        self.__compress = compress

    @property
    def compress(self):
        return self.__compress
