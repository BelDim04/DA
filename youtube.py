from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.figure import Figure
import typing as tp

class YouTube:
    def __init__(self, path_to_df: str = "RUvideos_short.csv"):
        self.df = pd.read_csv(path_to_df)
        print(self.df[self.df.category_id == 10].sort_values(by=['views'], ascending=False)[['trending_date', 'views']].head(10))

    def task1(self) -> pd.DataFrame:
        self.df["trending_date"] = pd.to_datetime(self.df["trending_date"], format="%y.%d.%m")
        return self.df

    def task2(self) -> pd.DataFrame:
        self.df = self.df[["trending_date", "category_id", "views", "likes", "dislikes", "comment_count"]]
        self.df["trending_date"] = self.df["trending_date"].apply(lambda x: x.day)
        return self.df

    def task3(self) -> Figure:
        sns.boxplot(x="trending_date", y="views", data=self.df)
        plt.title("Views by Day")
        plt.xlabel("Day")
        plt.ylabel("Views")
        plt.savefig("mygraph.png")
        return plt.gcf()

    def task4(self) -> Figure:
        sns.boxplot(x="trending_date", y="views", data=self.df)
        plt.title("Views by Day")
        plt.xlabel("date")
        plt.ylabel("views")
        plt.ylim(0, 12e5)
        plt.tight_layout()
        plt.savefig("mygraph.png")
        return plt.gcf()

    def task5(self) -> Figure:
        sns.jointplot(x="views", y="likes", data=self.df, joint_kws={'alpha': 0.5})
        plt.title("Likes by Views")
        plt.xlabel('views')
        plt.ylabel('likes')
        #plt.tight_layout()
        #plt.savefig("mygraph.png")
        return plt.gcf()

    def task6(self) -> Figure:
        sns.jointplot(x="views", y="likes", data=self.df[
            (self.df.views <= 2e5) & (self.df.likes <= 8e3)
        ], joint_kws={'alpha': 0.3})
        plt.ylim(-500, 8.5e3)
        plt.xlim(-10000, 2e5)
        plt.title("Likes by Views")
        plt.xlabel('views')
        plt.ylabel('likes')
        plt.xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3, 150e3, 175e3, 200e3],
                   ['0', '25k', '50k', '75k', '100k', '125k', '150k', '175k', '200k'])
        plt.tight_layout()
        #plt.savefig("mygraph.png")
        return plt.gcf()

t = YouTube()
t.task1()
t.task2()
t.task3()
t.task4()
t.task5()
t.task6()