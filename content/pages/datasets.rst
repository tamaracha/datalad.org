Datasets
********
:save_as: datasets.html
:url: /datasets.html

DataLad can create DataLad datasets using any data files published on the web.
But the one-time import of data isn't enough, which is why DataLad can `be
automated </for/data-consumers.html>`_ to monitor such data sources and
incorporate any modifications made to them over time — thus enabling the easy
`publication </for/data-publication.html>`_ and maintenance of entire
distributions of datasets.

Using this automated process, the DataLad team maintains `data trackers
<https://github.com/datalad/datalad-crawler/tree/master/datalad_crawler/pipelines>`__
for a number of popular public data portals. These datasets, some automatically
generated and others manually created and curated, are collated into a `DataLad
super-dataset <http://handbook.datalad.org/glossary.html#term-datalad-superdataset>`_
that is published publicly in its entirety at http://datasets.datalad.org\. This
super-dataset establishes the official DataLad data distribution that is
available via the DataLad resource identifier `///
<http://datasets.datalad.org>`__. Some of these datasets (e.g. `///crcns
<http://datasets.datalad.org/?dir=/crcns>`_) require authentication credentials,
but — other than the supplying of those credentials — access to all resources is
completely uniform regardless of the data's origin. DataLad also aggregates all
relevant `metadata <http://docs.datalad.org/en/latest/metadata.html>`_ for these
datasets — so they can be discovered using DataLad's `search
</for/data-discovery.html>`_.

At present, DataLad's super-dataset offers uniform access to over 10TB of
scientific data. This includes the following datasets, listed by their DataLad
resource identifiers for use with the `datalad clone
<http://docs.datalad.org/en/latest/generated/man/datalad-clone.html>`_
command:

- `OpenFMRI <https://openfmri.org>`_ — `///openfmri <http://datasets.datalad.org/?dir=/openfmri>`__
- `NeuroVault <https://neurovault.org>`_ —
  `///neurovault <http://datasets.datalad.org/?dir=/neurovault>`__
- `International Neuroimaging Data-sharing Initiative (INDI) <http://fcon_1000.projects.nitrc.org>`_ —
  `///indi <http://datasets.datalad.org/?dir=/indi>`__
- `Healthy Brain Network Serial Scanning Initiative (HBN-SSI) <http://fcon_1000.projects.nitrc.org/indi/hbn_ssi/>`_ —
  `///hbnssi <http://datasets.datalad.org/?dir=/hbnssi>`__
- `Data sharing for Collaborative Research in Computational Neuroscience (CRCNS.org) <http://crcns.org>`_ —
  `///crcns <http://datasets.datalad.org/?dir=/crcns>`__
- several individual research labs —
  `///labs <http://datasets.datalad.org/?dir=/labs>`__
- and many more ... — `/// <http://datasets.datalad.org>`__

The `OpenNeuro <https://openneuro.org>`_ portal publishes hosted data as
DataLad datasets on GitHub. The entire collection can be found at:
https://github.com/OpenNeuroDatasets

More datasets are provided in a `collection on GitHub
<https://github.com/datalad-datasets>`__, such as the `Human Connectome
Project's open access dataset
<https://github.com/datalad-datasets/human-connectome-project-openaccess>`__,
the world's `highest resolution brain scan
<https://github.com/datalad-datasets/bmmr-t1w-250um>`__, or podcast
collections.
