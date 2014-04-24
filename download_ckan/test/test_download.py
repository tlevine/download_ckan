from collections import namedtuple

import nose.tools as n

import download_ckan.download as dl

Response = namedtuple('Response', ['text'])

def test_dataset_ids():
    fake_get = lambda _: Response('{"results":[{"a":3}]}')
    observed = dl.dataset_ids(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])

def test_dataset():
    fake_get = lambda _: Response('[{}]')
    observed = dl.dataset(fake_get, 'bar-catalog', 'whatever')
    n.assert_dict_equal(observed, {'catalog': 'bar-catalog'})
