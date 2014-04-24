from collections import namedtuple

import nose.tools as n

from download_ckan.download import dataset_ids

Response = namedtuple('Response', ['text'])

def test_dataset_ids():
    fake_get = lambda _: Response('{"results":[{"a":3}]}')
    observed = dataset_ids(fake_get, 'https://foo-catalog.sh', 2)
    n.assert_list_equal(observed, [{'a': 3}])
