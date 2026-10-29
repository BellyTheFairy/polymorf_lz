#var1
import pandas as pd

class Processor:
    def __init__(self, filepath):
        try:
            self.df = pd.read_csv(filepath, encoding='utf-8-sig')
            print(f"Загружено строк: {len(self.df)}")
        except FileNotFoundError:
            print(f"Файл {filepath} не найден")
            self.df = pd.DataFrame()

    def split_and_save(self):
        if self.df.empty:
            print("Данных нет.")
            return

        col = 'Участники гражданского оборота'
        phys = self.df[self.df[col] == 'физ. лицо']
        legal = self.df[self.df[col] == 'юр. лицо']

        phys.to_csv('phys_persons.csv', index=False, encoding='utf-8-sig')
        legal.to_csv('legal_entities.csv', index=False, encoding='utf-8-sig')

        print(f"физ. лиц: {len(phys)}, юр. лиц: {len(legal)}")

    def __invert__(self):
        if self.df.empty:
            return 0

        before = len(self.df)
        self.df = self.df.drop_duplicates()
        removed = before - len(self.df)

        print(f"Удалено дубликатов: {removed}")
        self.split_and_save()

        return removed
