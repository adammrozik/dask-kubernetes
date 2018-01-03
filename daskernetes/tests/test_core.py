from daskernetes import KubeCluster
from dask.distributed import Client
from distributed.utils_test import loop

def test_basic(loop):
    with KubeCluster(loop=loop) as cluster:
        cluster.scale_up(1)
        with Client(cluster) as client:
            assert client.submit(lambda x: x + 1, 10).result() == 11
