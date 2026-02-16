import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

try:

    # Загружаем данные
    file_path = "C:/Users/shars/Desktop/Python practice/Machine language lab1/Apartments.csv"
    df = pd.read_csv(file_path)


    # Создаем точечную диаграмму
    plt.figure(figsize=(14, 8))

    # Используем seaborn для красивого графика с линией тренда
    sns.set_style("whitegrid")
    scatter = sns.scatterplot(
        data=df, 
        x='lot area', 
        y='Price',
        alpha=0.6,
        s=50,
        color='blue',
        edgecolor='black',
        linewidth=0.5
    )

    # Добавляем линию регрессии
    sns.regplot(x='lot area', y='Price', data=df, scatter=False, color='red', 
                line_kws={'linestyle': '--', 'linewidth': 2, 'alpha': 0.8, 'label': 'Линия тренда'})

    # Настройка подписей осей с правильными единицами измерения
    plt.xlabel('Площадь участка (м²)', fontsize=12, fontweight='bold')
    plt.ylabel('Цена ($)', fontsize=12, fontweight='bold')
    plt.title('Зависимость цены от площади участка', fontsize=14, fontweight='bold')

    # Форматирование осей с добавлением символов валюты и единиц измерения
    def price_formatter(x, p):
        return f'${x:,.0f}'

    def area_formatter(x, p):
        return f'{x:,.0f} м²'

    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(price_formatter))
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(area_formatter))

    # Поворачиваем подписи на оси X для лучшей читаемости
    plt.xticks(rotation=45)

    plt.legend()
    plt.tight_layout()
    plt.show()

    # Вычисляем коэффициенты линии тренда
    z = np.polyfit(df['lot area'], df['Price'], 1)
    print("=" * 40)
    print("СТАТИСТИКА ПО ДАННЫМ")
    print("=" * 40)
    print(f"Всего домов: {len(df)}")
    print(f"Диапазон цен: ${df['Price'].min():,.0f} - ${df['Price'].max():,.0f}")
    print(f"Диапазон площадей: {df['lot area'].min():,.0f} м² - {df['lot area'].max():,.0f} м²")
    print(f"Средняя цена: ${df['Price'].mean():,.0f}")
    print(f"Средняя площадь участка: {df['lot area'].mean():,.0f} м²")
    print(f"\nУравнение линии тренда: Цена = {z[0]:.2f} × Площадь + {z[1]:,.0f}")
    print(f"Корреляция: {df['lot area'].corr(df['Price']):.3f}")

    '''average_price = df["Price"].mean()
    total_area = df["lot area"].sum()

    # Форматированный вывод результатов
    print("=" * 40)
    print("АНАЛИЗ ДАННЫХ О КВАРТИРАХ")
    print("=" * 40)
    print(f"Средняя цена квартиры: {average_price:,.2f} $.")
    print(f"Суммарная площадь всех квартир: {total_area:,.2f} кв.м")
    print("=" * 40)

    # Дополнительная информация (по желанию)
    print(f"\nКоличество квартир: {len(df)}")
    print(f"Минимальная цена: {df['Price'].min():,.2f} $.")
    print(f"Максимальная цена: {df['Price'].max():,.2f} $.")'''
except FileNotFoundError as e:
    print(f'Ошибка на пути данных: {e}')