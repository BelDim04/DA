import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str = "cat_exam_data.csv"):  # task0
        self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
        return self.df.head(5)

    def task2(self) -> tp.List[str]:
        return list(self.df.columns[self.df.isna().any()].values)

    def task3(self) -> pd.DataFrame:
        self.df = self.df.dropna()
        return self.df

    def task4(self) -> pd.DataFrame:
        return self.df.describe()

    def task5(self) -> int:
        return len(self.df[self.df.test_score == 100])

    def task6(self) -> pd.DataFrame:
        return self.df[self.df.test_score == 100].groupby(['school', 'number_of_students'])[
            'test_score'].count().reset_index().rename(columns={'test_score': 'cnt_100'}).sort_values(
            by=['cnt_100', 'school'], ascending=False).reset_index().drop(['index'], axis='columns')

    def task7(self) -> pd.DataFrame:
        return self.df.groupby(['school', 'number_of_students'])[
            'test_score'].mean().reset_index().sort_values(
            by='test_score', ascending=False
        )[['school', 'test_score', 'number_of_students']].head(10).reset_index().drop(['index'], axis='columns')

    def task8(self) -> pd.DataFrame:
        return self.df.groupby(['school', 'number_of_students'])[
            'test_score'].mean().reset_index().sort_values(
            by='test_score', ascending=False
        )[['school', 'test_score', 'number_of_students']].tail(10).reset_index().drop(['index'], axis='columns')

    def task9(self) -> Axes:
        small = self.df[self.df.number_of_students <= 1000]
        big = self.df[self.df.number_of_students > 1000]
        plt.hist(small['test_score'], bins=10, alpha=0.5, color='red', label='small schools')
        plt.hist(big['test_score'], bins=10, alpha=0.5, color='grey', label='big schools')
        plt.ylabel('students')
        plt.xlabel('test_score')
        plt.title('Test scores for big and small schools')
        plt.legend()
        #plt.savefig("mygraph.png")
        return plt.gca()
