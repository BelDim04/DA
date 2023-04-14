import json
import typing as tp

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime
from matplotlib.figure import Figure


class YouTube2:
    def __init__(  # task0
            self,
            trends_df_path: str = "RUvideos_short.csv",
            categories_df_path: str = "RU_category_id.json"
    ):
        self.trends_df = pd.read_csv(trends_df_path)
        self.trends_df["trending_date"] = pd.to_datetime(self.trends_df["trending_date"], format="%y.%d.%m")

        with open(categories_df_path) as json_file:
            json_data = json.load(json_file)

        self.categories_df = pd.DataFrame(columns=['id', 'name'])

        for item in json_data['items']:
            self.categories_df = self.categories_df.append(
                {'id': int(item['id']),
                 'name': item['snippet']['title']},
                ignore_index=True
            )

        self.categories_df['id'] = self.categories_df['id'].astype(int)

    def task1(self) -> pd.DataFrame:
        self.trends_df = self.trends_df.merge(self.categories_df, how='inner', left_on='category_id', right_on='id')
        return self.trends_df

    def task2(self) -> pd.DataFrame:
        return pd.pivot_table(self.trends_df, values='views', index=['name'], columns=['trending_date'], aggfunc=np.sum)

    def task3(self) -> Figure:
        sns.heatmap(self.task2() / 1e6, annot=True)
        plt.ylabel('category')
        plt.title("Views per day for categories")
        plt.tight_layout()
        # plt.savefig("mygraph.png")
        return plt.gcf()

    def task4(self) -> pd.DataFrame:
        data = self.task2()
        data.loc[:, 'Всего просмотров'] = data.sum(axis=1)
        data.loc['Всего просмотров'] = data.sum(axis=0)
        return data

    def task5(self) -> Figure:
        data = self.task4()
        dates = list(data.columns.values)
        rename_helper = {d: d.day for d in dates[:-1]}
        sns.heatmap(data.rename(columns=rename_helper) / 1e6, annot=True, vmin=0, vmax=10)
        plt.ylabel('category')
        plt.title("Views per day for categories")
        plt.tight_layout()
        plt.savefig("mygraph.png")
        return plt.gcf()


t = YouTube2()
t.task1()
t.task2()
# t.task3()
t.task4()
t.task5()
