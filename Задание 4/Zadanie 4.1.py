import pandas as pd
pulsar_stars = pd.read_csv('asset-v1_ITMOUniversity+DATSC+summer_2022_1+type@asset+block@pulsar_stars_new (1).csv',
                       delimiter=',',
                       decimal='.')
pulsar_stars = pulsar_stars.drop(['STDIP','EKIP','SIP','MC','STDC','EKC','SC'], axis = 1)
sample_pulsar = pulsar_stars[((pulsar_stars.TG == 0) & (pulsar_stars.MIP >= 96.921875)
                               & (pulsar_stars.MIP <= 97.4140625)) | ((pulsar_stars.TG == 1) & (pulsar_stars.MIP >= 41.8828125)
                               & (pulsar_stars.MIP <= 47.4140625))]

print('Количество строк в полученной выборке = ', len(sample_pulsar))
print(f'Среднее выборочное для столбца MIP = {sample_pulsar.MIP.mean():.3f}')
