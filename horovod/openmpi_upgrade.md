# Upgrading to openmpi 3.1.x

## 1. Download latest openmpi 
- [https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.2.tar.gz](https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.2.tar.gz)

## 2. build openmpi

```
gunzip -c openmpi-3.1.2.tar.gz | tar xf -
cd openmpi-3.1.2
./configure --prefix=/usr/local
<...lots of output...>
make all install

export PATH="$PATH:/usr/local/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/lib/"
```

For more information, please refer followings
- [https://www.open-mpi.org/faq/?category=building#easy-build](https://www.open-mpi.org/faq/?category=building#easy-build)
- [http://lsi.ugr.es/jmantas/pdp/ayuda/datos/instalaciones/Install_OpenMPI_en.pdf](http://lsi.ugr.es/jmantas/pdp/ayuda/datos/instalaciones/Install_OpenMPI_en.pdf)


> log out and re-login VM after build. This will make sure configure openmpi libraries/binaries

## 3. reinstall horovod

```
pip uninstall -y horovod
pip install horovod --no-cache-dir
```

> Please refer https://github.com/uber/horovod/issues/56

## 4. run test

```
mpirun -np 1 \
    -H localhost:1 \
    -bind-to none -map-by slot \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
    -mca pml ob1 -mca btl ^openib \
    python ~/work/keras_mnist.py
```

