# Script for Horovod with DSVM

## environment variables

```
rg='<add here>'
location='westus2'
vnet='<add here>'
storacc='<add here>'
azfile='<add here>'
user='user'
pwd=<strong pwd>
```

## create a vnet

```
az group create -l "westus2" -n $rg

az network vnet create -g $rg -n $vnet --address-prefix 10.4.0.0/16 \
    --subnet-name default --subnet-prefix 10.4.0.0/24

az network vnet subnet create -g $rg --vnet-name $vnet -n jumpnet \
    --address-prefix 10.4.1.0/24

az network vnet subnet create -g $rg --vnet-name $vnet -n batchai \
    --address-prefix 10.4.2.0/24
```

##  create a vm (ai training)

create 2 NC6 vm

```
az vm create -n ${vmname}1 -g $rg -l "westus2" \
 --image microsoft-dsvm:linux-data-science-vm-ubuntu:linuxdsvmubuntu:latest --size Standard_NC6 \
 --vnet-name $vnet --subnet default \
 --admin-username $user --ssh-key-value  ./sshkey.pub \
 --verbose

az vm create -n ${vmname}2 -g $rg -l "westus2" \
 --image microsoft-dsvm:linux-data-science-vm-ubuntu:linuxdsvmubuntu:latest --size Standard_NC6 \
 --vnet-name $vnet --subnet default \
 --admin-username $user --ssh-key-value  ./sshkey.pub \
 --verbose
```

## optional gpu monitor vm

create a monitor vm

```
az vm create -n gpumon -g $rg -l "westus2" \
 --image microsoft-dsvm:linux-data-science-vm-ubuntu:linuxdsvmubuntu:latest --size Standard_D2s_v3 \
 --vnet-name $vnet --subnet  default \
 --admin-username $user --ssh-key-value  ./sshkey.pub \
 --verbose
```

### Configure and run monitor app

Install package for running monitor app (grafana, influxdb) on docker container

```
https://github.com/msalvaris/gpu_monitor.git
pip install -r gpu_monitor/requirements.txt
cd gpu_monitor/scripts
sudo apt install docker-compose
make run
```

## run horovod

get tensorflow benchmark source

```
git clone https://github.com/tensorflow/benchmarks
cd benchmarks
git checkout cnn_tf_v1.10_compatible
```

run mpi

```
mpirun -np 2 \
    -H 10.4.0.4,10.4.0.5 \
    -bind-to none -map-by slot \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
    -mca pml ob1 -mca btl ^openib \
    -mca btl_tcp_if_exclude lo,docker0 \
    \
    python ~/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py \
        --model resnet50 \
        --batch_size 64 \
        --variable_update horovod
```

```
mpirun -np 2 \
    -H 10.4.0.4,10.4.0.5 \
    -bind-to none -map-by slot \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
    -mca pml ob1 -mca btl ^openib \
    -mca btl_tcp_if_exclude lo,docker0 \
    \
    python ~/benchmarks/scripts/tf_cnn_benchmarks/tf_cnn_benchmarks_gpumon.py \
        --model resnet50 \
        --batch_size 64 \
        --variable_update horovod
```

