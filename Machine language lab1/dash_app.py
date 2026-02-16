import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc

try:

    # Загружаем данные
    file_path = "C:/Users/shars/Desktop/Python practice/Machine language lab1/Apartments.csv"
    df = pd.read_csv(file_path)

    # Вычисляем статистику и линию тренда
    z = np.polyfit(df['lot area'], df['Price'], 1)

    # Создаем график с plotly
    fig = px.scatter(
        df, 
        x='lot area', 
        y='Price',
        title='Зависимость цены от площади участка',
        labels={'lot area': 'Площадь участка (м²)', 'Price': 'Цена ($)'},
        opacity=0.6
    )

    # Добавляем линию тренда
    x_range = np.linspace(df['lot area'].min(), df['lot area'].max(), 100)
    fig.add_trace(go.Scatter(
        x=x_range,
        y=z[0] * x_range + z[1],
        mode='lines',
        name='Линия тренда',
        line=dict(color='red', dash='dash')
    ))

    # Настройка формата осей
    fig.update_yaxes(tickprefix="$")
    fig.update_layout(plot_bgcolor='white')

    # Dash приложение
    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Анализ рынка недвижимости", 
                style={'textAlign': 'center', 'color': "#000000"}),
        
        html.Div([
            html.Div([
                html.H3(f"Всего домов: {len(df)}"),
                html.H3(f"Средняя цена: ${df['Price'].mean():,.0f}"),
                html.H3(f"Корреляция: {df['lot area'].corr(df['Price']):.3f}"),
            ], style={'display': 'flex', 'justifyContent': 'space-around', 
                    'padding': '20px', 'backgroundColor': '#ecf0f1'})
        ]),
        
        dcc.Graph(figure=fig),
        
        html.Div([
            html.P(f"Уравнение тренда: Цена = {z[0]:.2f} × Площадь + {z[1]:,.0f}",
                style={'textAlign': 'center', 'fontSize': 18, 'margin': '20px'})
        ])
    ])

    if __name__ == '__main__':
        app.run(debug=True)
except FileNotFoundError as e:
    print(f'Ошибка на пути данных: {e}')