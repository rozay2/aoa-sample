# tensorflow benchmark

## Test environment & Summary

Test environment :West US2, NC12 (K80x2), Azure Files/Local

### Result Summary

test | node | gpu | images/sec | images/sec/gpu | note
--   | --   | --  | --         | --             | --
1    | 1    | 1   | 56.57      | 56.57          | DSVM (python3) + local
2    | 1    | 2   | 109.34     | 54.67          | DSVM (python3) + local
3    | 2    | 1   | 109.72     | 54.86          | DSVM (python3) + local
4    | 2    | 2   | 209.87     | 52.47          | DSVM (python3) + local
5    | 2    | 1   | 106.38     | 53.19          | BatchAI (tensorflow/tensorflow:latest-gpu-py3)/lowpriority + azure files
6    | 2    | 2   | 205.18     | 51.30          | BatchAI (tensorflow/tensorflow:latest-gpu-py3)/lowpriority + azure files
7    | 2    | 2   | 211.02     | 52.76          | BatchAI (tensorflow/tensorflow:latest-gpu-py3)/dedicated + azure files

## Results

### test 1: dsvm, 1 node (NC6) x 1 gpu

```
Step    Img/sec total_loss
1       images/sec: 57.0 +/- 0.0 (jitter = 0.0) 7.876
10      images/sec: 56.9 +/- 0.1 (jitter = 0.2) 7.848
20      images/sec: 56.8 +/- 0.0 (jitter = 0.2) 7.942
30      images/sec: 56.8 +/- 0.0 (jitter = 0.2) 7.829
40      images/sec: 56.8 +/- 0.0 (jitter = 0.2) 7.871
50      images/sec: 56.7 +/- 0.0 (jitter = 0.2) 7.846
60      images/sec: 56.7 +/- 0.0 (jitter = 0.3) 7.846
70      images/sec: 56.7 +/- 0.0 (jitter = 0.2) 7.887
80      images/sec: 56.6 +/- 0.0 (jitter = 0.3) 7.975
90      images/sec: 56.6 +/- 0.0 (jitter = 0.3) 7.942
100     images/sec: 56.6 +/- 0.0 (jitter = 0.3) 7.951
----------------------------------------------------------------
total images/sec: 56.57
----------------------------------------------------------------
```

### test 2: dsvm, 1 node (NC12) x 2 gpus

```
1       images/sec: 55.2 +/- 0.0 (jitter = 0.0) 7.876
1       images/sec: 55.2 +/- 0.0 (jitter = 0.0) 7.835
10      images/sec: 55.1 +/- 0.1 (jitter = 0.1) 7.896
10      images/sec: 55.1 +/- 0.1 (jitter = 0.2) 7.849
20      images/sec: 54.9 +/- 0.1 (jitter = 0.3) 7.943
20      images/sec: 54.9 +/- 0.1 (jitter = 0.3) 7.887
30      images/sec: 54.8 +/- 0.1 (jitter = 0.3) 7.825
30      images/sec: 54.8 +/- 0.1 (jitter = 0.3) 7.832
40      images/sec: 54.8 +/- 0.0 (jitter = 0.3) 7.829
40      images/sec: 54.8 +/- 0.0 (jitter = 0.2) 7.872
50      images/sec: 54.8 +/- 0.0 (jitter = 0.2) 7.848
50      images/sec: 54.8 +/- 0.0 (jitter = 0.2) 7.955
60      images/sec: 54.8 +/- 0.0 (jitter = 0.2) 7.843
60      images/sec: 54.8 +/- 0.0 (jitter = 0.2) 7.922
70      images/sec: 54.7 +/- 0.0 (jitter = 0.2) 7.890
70      images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.858
80      images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.838
80      images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.978
90      images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.935
90      images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.889
100     images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.809
----------------------------------------------------------------
total images/sec: 109.34
----------------------------------------------------------------
100     images/sec: 54.7 +/- 0.0 (jitter = 0.3) 7.948
----------------------------------------------------------------
total images/sec: 109.34
----------------------------------------------------------------
```

### test 3:  dsvm, 2 nodes (NC6) x 1 gpu

```
1       images/sec: 55.2 +/- 0.0 (jitter = 0.0) 7.876
1       images/sec: 55.3 +/- 0.0 (jitter = 0.0) 7.835
10      images/sec: 55.1 +/- 0.1 (jitter = 0.3) 7.848
10      images/sec: 55.1 +/- 0.1 (jitter = 0.1) 7.896
20      images/sec: 55.0 +/- 0.1 (jitter = 0.3) 7.944
20      images/sec: 55.0 +/- 0.1 (jitter = 0.3) 7.886
30      images/sec: 55.0 +/- 0.1 (jitter = 0.3) 7.830
30      images/sec: 55.0 +/- 0.1 (jitter = 0.2) 7.828
40      images/sec: 55.0 +/- 0.1 (jitter = 0.3) 7.871
40      images/sec: 55.0 +/- 0.0 (jitter = 0.3) 7.830
50      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.847
50      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.944
60      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.845
60      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.935
70      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.889
70      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.855
80      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.985
80      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.835
90      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.953
90      images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.895
100     images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.952
----------------------------------------------------------------
total images/sec: 109.72
----------------------------------------------------------------
100     images/sec: 54.9 +/- 0.0 (jitter = 0.3) 7.811
----------------------------------------------------------------
total images/sec: 109.72
----------------------------------------------------------------
```

### test 4: dsvm, 2 nodes (NC12) x 2 gpus

```
1       images/sec: 53.9 +/- 0.0 (jitter = 0.0) 7.839
1       images/sec: 54.1 +/- 0.0 (jitter = 0.0) 7.877
1       images/sec: 53.9 +/- 0.0 (jitter = 0.0) 7.773
1       images/sec: 54.0 +/- 0.0 (jitter = 0.0) 7.892
10      images/sec: 53.0 +/- 0.4 (jitter = 0.8) 7.900
10      images/sec: 53.1 +/- 0.4 (jitter = 0.8) 7.839
10      images/sec: 53.0 +/- 0.4 (jitter = 0.8) 7.862
10      images/sec: 53.1 +/- 0.4 (jitter = 0.7) 7.906
20      images/sec: 53.1 +/- 0.3 (jitter = 0.6) 7.886
20      images/sec: 53.1 +/- 0.3 (jitter = 0.8) 7.884
20      images/sec: 53.1 +/- 0.3 (jitter = 0.6) 7.942
20      images/sec: 53.1 +/- 0.3 (jitter = 0.5) 7.864
30      images/sec: 52.3 +/- 0.5 (jitter = 0.6) 7.902
30      images/sec: 52.3 +/- 0.5 (jitter = 0.8) 7.832
30      images/sec: 52.3 +/- 0.5 (jitter = 0.7) 7.830
30      images/sec: 52.3 +/- 0.5 (jitter = 1.0) 7.933
40      images/sec: 52.4 +/- 0.5 (jitter = 0.8) 7.892
40      images/sec: 52.4 +/- 0.4 (jitter = 0.7) 7.831
40      images/sec: 52.4 +/- 0.4 (jitter = 0.6) 8.008
40      images/sec: 52.4 +/- 0.4 (jitter = 0.5) 7.875
50      images/sec: 52.3 +/- 0.4 (jitter = 0.8) 7.953
50      images/sec: 52.3 +/- 0.4 (jitter = 0.8) 7.867
50      images/sec: 52.3 +/- 0.4 (jitter = 0.5) 7.913
50      images/sec: 52.3 +/- 0.4 (jitter = 0.5) 7.848
60      images/sec: 52.4 +/- 0.3 (jitter = 0.6) 7.847
60      images/sec: 52.4 +/- 0.3 (jitter = 0.8) 7.946
60      images/sec: 52.4 +/- 0.3 (jitter = 0.8) 7.874
60      images/sec: 52.4 +/- 0.3 (jitter = 0.5) 7.916
70      images/sec: 52.4 +/- 0.3 (jitter = 0.6) 7.886
70      images/sec: 52.4 +/- 0.3 (jitter = 0.7) 7.838
70      images/sec: 52.4 +/- 0.3 (jitter = 0.5) 7.836
70      images/sec: 52.4 +/- 0.3 (jitter = 0.8) 7.925
80      images/sec: 52.5 +/- 0.3 (jitter = 0.6) 7.974
80      images/sec: 52.5 +/- 0.3 (jitter = 0.8) 7.848
80      images/sec: 52.5 +/- 0.3 (jitter = 0.8) 7.900
80      images/sec: 52.5 +/- 0.3 (jitter = 0.5) 7.903
90      images/sec: 52.5 +/- 0.2 (jitter = 0.8) 7.896
90      images/sec: 52.5 +/- 0.2 (jitter = 0.5) 7.823
90      images/sec: 52.5 +/- 0.3 (jitter = 0.9) 7.875
90      images/sec: 52.5 +/- 0.3 (jitter = 0.6) 7.954
100     images/sec: 52.5 +/- 0.2 (jitter = 0.8) 7.826
----------------------------------------------------------------
total images/sec: 209.86
----------------------------------------------------------------
100     images/sec: 52.5 +/- 0.2 (jitter = 0.9) 7.896
----------------------------------------------------------------
total images/sec: 209.86
----------------------------------------------------------------
100     images/sec: 52.5 +/- 0.2 (jitter = 0.6) 7.856
100     images/sec: 52.5 +/- 0.2 (jitter = 0.6) 7.942
----------------------------------------------------------------
----------------------------------------------------------------
total images/sec: 209.87
----------------------------------------------------------------
total images/sec: 209.86
----------------------------------------------------------------
```

### test 5: batchai(lowpriority), az files, tensorflow/tensorflow:latest-gpu-py3, 1 node x 2 gpu

```
1	images/sec: 53.1 +/- 0.0 (jitter = 0.0)	7.876
1	images/sec: 53.1 +/- 0.0 (jitter = 0.0)	7.835
10	images/sec: 53.4 +/- 0.1 (jitter = 0.3)	7.896
10	images/sec: 53.4 +/- 0.1 (jitter = 0.3)	7.849
20	images/sec: 53.5 +/- 0.1 (jitter = 0.2)	7.886
20	images/sec: 53.5 +/- 0.1 (jitter = 0.2)	7.944
30	images/sec: 53.4 +/- 0.1 (jitter = 0.3)	7.829
30	images/sec: 53.4 +/- 0.1 (jitter = 0.2)	7.825
40	images/sec: 53.3 +/- 0.0 (jitter = 0.3)	7.826
40	images/sec: 53.3 +/- 0.0 (jitter = 0.3)	7.874
50	images/sec: 53.3 +/- 0.1 (jitter = 0.2)	7.952
50	images/sec: 53.3 +/- 0.1 (jitter = 0.2)	7.847
60	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.928
60	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.854
70	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.863
70	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.889
80	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.838
80	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.976
90	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.877
90	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.939
100	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.945
100	images/sec: 53.2 +/- 0.0 (jitter = 0.2)	7.805
----------------------------------------------------------------
total images/sec: 106.38
----------------------------------------------------------------
----------------------------------------------------------------
total images/sec: 106.38
----------------------------------------------------------------
```

### test 6: batchai(lowpriority), az files, tensorflow/tensorflow:latest-gpu-py3, 2 node x 2 gpu

after several warm-up try

```
1	images/sec: 52.0 +/- 0.0 (jitter = 0.0)	7.877
1	images/sec: 51.9 +/- 0.0 (jitter = 0.0)	7.839
1	images/sec: 52.0 +/- 0.0 (jitter = 0.0)	7.774
1	images/sec: 51.6 +/- 0.0 (jitter = 0.0)	7.893
10	images/sec: 51.9 +/- 0.1 (jitter = 0.2)	7.838
10	images/sec: 51.9 +/- 0.1 (jitter = 0.1)	7.891
10	images/sec: 51.9 +/- 0.1 (jitter = 0.2)	7.868
10	images/sec: 51.9 +/- 0.1 (jitter = 0.2)	7.905
20	images/sec: 51.6 +/- 0.1 (jitter = 0.2)	7.889
20	images/sec: 51.7 +/- 0.1 (jitter = 0.2)	7.938
20	images/sec: 51.7 +/- 0.1 (jitter = 0.3)	7.892
20	images/sec: 51.6 +/- 0.1 (jitter = 0.2)	7.868
30	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.840
30	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.819
30	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.929
30	images/sec: 51.6 +/- 0.1 (jitter = 0.2)	7.901
40	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.835
40	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.871
40	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.888
40	images/sec: 51.6 +/- 0.1 (jitter = 0.2)	8.006
50	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.952
50	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.849
50	images/sec: 51.6 +/- 0.1 (jitter = 0.3)	7.866
50	images/sec: 51.5 +/- 0.1 (jitter = 0.3)	7.916
60	images/sec: 51.4 +/- 0.1 (jitter = 0.4)	7.928
60	images/sec: 51.4 +/- 0.1 (jitter = 0.4)	7.845
60	images/sec: 51.4 +/- 0.1 (jitter = 0.4)	7.852
60	images/sec: 51.4 +/- 0.1 (jitter = 0.4)	7.913
70	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.896
70	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.837
70	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.915
70	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.837
80	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.838
80	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.977
80	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.891
80	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.895
90	images/sec: 51.3 +/- 0.1 (jitter = 0.5)	7.868
90	images/sec: 51.3 +/- 0.1 (jitter = 0.5)	7.940
90	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.886
90	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.834
100	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.812
----------------------------------------------------------------
total images/sec: 205.17
----------------------------------------------------------------
100	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.957
----------------------------------------------------------------
total images/sec: 205.18
----------------------------------------------------------------
100	images/sec: 51.3 +/- 0.1 (jitter = 0.5)	7.910
----------------------------------------------------------------
100	images/sec: 51.3 +/- 0.1 (jitter = 0.4)	7.887
----------------------------------------------------------------
total images/sec: 205.18
----------------------------------------------------------------
total images/sec: 205.18
----------------------------------------------------------------
```

### test 7:  batchai(dedicated), az files, tensorflow/tensorflow:latest-gpu-py3, 2 node x 2 gpu

```
1	images/sec: 53.3 +/- 0.0 (jitter = 0.0)	7.838
1	images/sec: 53.3 +/- 0.0 (jitter = 0.0)	7.773
1	images/sec: 53.3 +/- 0.0 (jitter = 0.0)	7.893
1	images/sec: 53.4 +/- 0.0 (jitter = 0.0)	7.877
10	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.894
10	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.860
10	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.898
10	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.844
20	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.896
20	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.889
20	images/sec: 53.1 +/- 0.1 (jitter = 0.2)	7.865
20	images/sec: 53.1 +/- 0.0 (jitter = 0.2)	7.939
30	images/sec: 53.0 +/- 0.0 (jitter = 0.3)	7.816
30	images/sec: 53.0 +/- 0.0 (jitter = 0.3)	7.939
30	images/sec: 53.0 +/- 0.0 (jitter = 0.3)	7.902
30	images/sec: 53.0 +/- 0.0 (jitter = 0.3)	7.831
40	images/sec: 53.0 +/- 0.0 (jitter = 0.2)	7.833
40	images/sec: 53.0 +/- 0.0 (jitter = 0.2)	7.909
40	images/sec: 53.0 +/- 0.0 (jitter = 0.2)	8.005
40	images/sec: 53.0 +/- 0.0 (jitter = 0.3)	7.874
50	images/sec: 52.9 +/- 0.0 (jitter = 0.2)	7.949
50	images/sec: 52.9 +/- 0.0 (jitter = 0.2)	7.881
50	images/sec: 52.9 +/- 0.0 (jitter = 0.2)	7.916
50	images/sec: 52.9 +/- 0.0 (jitter = 0.3)	7.844
60	images/sec: 52.9 +/- 0.0 (jitter = 0.3)	7.930
60	images/sec: 52.9 +/- 0.0 (jitter = 0.3)	7.868
60	images/sec: 52.9 +/- 0.0 (jitter = 0.3)	7.930
60	images/sec: 52.9 +/- 0.0 (jitter = 0.3)	7.860
70	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.840
70	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.913
70	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.815
70	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.876
80	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.849
80	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.892
80	images/sec: 52.8 +/- 0.0 (jitter = 0.3)	7.898
80	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.966
90	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.892
90	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.817
90	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.874
90	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.964
100	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.789
----------------------------------------------------------------
total images/sec: 211.03
----------------------------------------------------------------
100	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.843
100	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.914
----------------------------------------------------------------
total images/sec: 211.02
----------------------------------------------------------------
----------------------------------------------------------------
total images/sec: 211.02
----------------------------------------------------------------
100	images/sec: 52.8 +/- 0.0 (jitter = 0.4)	7.972
----------------------------------------------------------------
total images/sec: 211.02
----------------------------------------------------------------
```