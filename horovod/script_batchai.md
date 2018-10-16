# Script for running Horovod with BatchAI

## environment variables

```
rg='<add here>'
location='westus2'
vnet='<add here>'
storacc='<add here>'
azfile='<add here>'
vnet_subnet_id='<add here>'
user='user'
pwd=<strong pwd>

workspace='<add here>'
cluster='<add here>'
benchmark='<add here>'
```

## create azure files

Create a Azure files with `$azfile` name and get access key for azure files

```
az storage account create -n $storacc -g $rg -l $location --sku Standard_LRS
az storage share create -n $azfile --account-name $storacc --quota 100

export AZURE_STORAGE_KEY="$(az storage account keys list -g $rg --account-name $storacc -o tsv --query [0].value)"
```

## batchai setup

create workspace & cluster, ...

```
az batchai workspace create -g $rg -n $workspace

az batchai cluster create --name $cluster --workspace $workspace --resource-group $rg \
 --vm-size STANDARD_NC12 --image UbuntuLTS --min 2 --max 2 \
 --afs-name $azfile --afs-mount-path azurefileshare \
 --storage-account-name $storacc \
 --storage-account-key $AZURE_STORAGE_KEY \
 --vm-priority lowpriority \
 --subnet $vnet_subnet_id \
 -u $user --password $pwd

az batchai cluster node list \
  --cluster $cluster \
  --workspace $workspace \
  --resource-group $rg -o tsv

az batchai experiment create --name $benchmark \
  --workspace $workspace \
  --resource-group $rg
```

Sample output
```
13.66.212.87    tvm-2748522322_1-20180927t053632z-p     50000.0
13.66.212.87    tvm-2748522322_2-20180927t053632z-p     50001.0
```

## show cluster status

```
az batchai cluster show -n $cluster \
  --workspace $workspace \
  --resource-group $rg -o tsv

watch -n10 az batchai cluster show -n $cluster  --workspace $workspace  \
 --resource-group $rg --query '["nodeStateCounts"]' -o tsv
```

##  login to one of vm

```
ssh -p 50000 iljoong@<ip>
```

> cd /mnt/batch/tasks/shared/LS_root/jobs/$workspace/tfbenchmark/job01/mounts/$azfile


## submit new job

> upload `benchmarks` folder to fileshare and create `logs` folder and update `LOGGER_URL` ip address in `tf_cnn_benchmarks_gpumon.py`.

```
az batchai job create --name job01 \
  --cluster $cluster \
  --experiment $benchmark \
  --workspace $workspace\
  --resource-group $rg \
  --config-file job-gpumon.json
```

# monitoring

```
az batchai job file list --experiment tfbenchmark --job job01 --resource-group $rg --workspace $workspace --output table
```
