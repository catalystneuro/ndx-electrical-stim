# -*- coding: utf-8 -*-
# Standard libraries
import os.path

# Third party libraries
from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, \
    NWBAttributeSpec, NWBDatasetSpec


# TODO: import the following spec classes as needed
# from pynwb.spec import NWBDatasetSpec, NWBLinkSpec, NWBDtypeSpec, NWBRefSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='stores electrical stimulation waveforms',
        name='ndx-electrical-stim',
        version='0.1.0',
        author=list(map(str.strip, 'Jessie R. Liu'.split(','))),
        contact=list(map(str.strip, 'jrliu95@gmail.com'.split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    ns_builder.include_type('TimeSeries', namespace='core')
    ns_builder.include_type('DynamicTableRegion', namespace='hdmf-common')

    # TODO: define your new data types
    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb
    # for more information

    stim_series = NWBGroupSpec(
        neurodata_type_def='StimSeries',
        neurodata_type_inc='TimeSeries',
        doc=('An extension of TimeSeries to include stimulation waveforms '
             'used during electrical stimulation.'),
    )
    stim_series.add_dataset(name='electrodes',
                            neurodata_type_inc='DynamicTableRegion',
                            doc='DynamicTableRegion pointer to the '
                                'bipolar electrode pairs corresponding to the '
                                'stimulation waveforms.')
    stim_series.add_dataset(name='metadata',
                            doc='JSON serialized metadata for creating the '
                                'recorded stimulation waveform.',
                            dtype='text')

    # TODO: add all of your new data types to this list
    new_data_types = [stim_series]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
