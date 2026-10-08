import pandas as pd
import matplotlib.pyplot as plt
answers = pd.read_excel('var127683 (1).xlsx')
to_plot = pd.DataFrame(answers['Choice_1'].value_counts())
to_plot.columns = ['Amount']
to_plot = to_plot.sort_index()
# plt.bar(to_plot.index, to_plot['Amount'])
# plt.xticks(rotation = 'vertical')
# plt.show()


#Соответствует графику 9 из файла
#За Big Data 55 респондентов
#За Машинное обучение 44 респондентов
#За Статистика 75 респондентов
full_to_plot = pd.DataFrame(pd.DataFrame(answers.values.reshape(-1))[0].value_counts())
full_to_plot.columns = ['Amount']
full_to_plot = full_to_plot.sort_index()
plt.pie(full_to_plot['Amount'], labels = full_to_plot.index)
plt.show()
#Соответствует графику 4 из файла
#За Big Data 55 респондентов
#За Машинное обучение 44 респондентов
#За Статистика 75 респондентов