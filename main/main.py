from class_members import Processor

if __name__ == "__main__":
    p = Processor('var1.csv')
    print(f"Удалено повторяющихся строк: {~p}")
