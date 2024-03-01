import pandas as pd
import numpy as np
import datetime as dt
import dask.dataframe as dd
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor as tp


cpu = mp.cpu_count()
print("Số CPU có sẵn trong hệ thống: ",cpu)


df = pd.DataFrame({'X':np.random.randint(1000, size=10000000),'Y':np.random.randint(1000, size=10000000)})


#df['add_squares'] = 0 


def add_squares(df):
    return df.X**2+df.Y**2


# Tính với apply()
start_time = dt.datetime.now()
df['add_squares']=df.apply(add_squares,axis=1)
print("Kết quả: ",df)
end_time = dt.datetime.now()
execution_time = (end_time - start_time).total_seconds()
print("Thời gian thực hiện tính toán thông thường: {} giây".format(execution_time))


# Tính với xử lý song song
ddf = dd.from_pandas(df, npartitions=cpu)

start_time = dt.datetime.now()
ddf ['z'] = ddf.map_partitions(add_squares,meta=(None, 'int64')).compute()
print("Kết quả: ",ddf)
end_time = dt.datetime.now()
execution_time = (end_time - start_time).total_seconds()
print("Thời gian thực hiện tính toán xử lý bằng Dask: {} giây".format(execution_time))


start_time = dt.datetime.now()
with tp(max_workers=cpu) as executor:
    futures = [executor.submit(add_squares, df[i:i+100000]) for i in range(0, len(df), 100000)]
end_time = dt.datetime.now()
execution_time = (end_time - start_time).total_seconds()
print("Thời gian thực hiện tính toán xử lý bằng ThreadPool: {} giây".format(execution_time))