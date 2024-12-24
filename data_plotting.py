import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go


def create_and_save_plot(data, ticker, start_date, end_date, style, filename=None):
    '''
    Создаёт график, отображающий цены закрытия и скользящие средние.
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    :param data: DataFrame с данными
    :param ticker: Тикер акции
    :param start_date: начало периода
    :param end_date:  конец приода
    :param style: выбор стиля графика
    :param filename: Название файла
    :return: Создаёт график, отображающий цены закрытия и скользящие средние
    '''
    plt.figure(figsize=(10, 6))
    plt.style.use(style)
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.plot(data.index, data['Moving_Average'] + data['stddev_close'], color='orange', alpha=0.5,
                     label='Стандартное отклоение +')
            plt.plot(data.index, data['Moving_Average'] - data['stddev_close'], color='black', alpha=0.5,
                     label='Стандартное отклоение -')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.plot(data.index, data['Moving_Average'] + data['stddev_close'], color='orange', alpha=0.5,
                 label='Стандартное отклоение ' + '')
        plt.plot(data.index, data['Moving_Average'] - data['stddev_close'], color='black', alpha=0.5,
                 label='Стандартное отклоение ' - '')

    plt.title(f"{ticker} Цена акций с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("Цена")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{start_date}-{end_date}-{style}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def calculate_and_display_average_price(data):
    '''
    Вычисляет и выводит среднюю цену закрытия акций за заданный период
    :param data: DataFrame с данными
    :return: Выводит среднюю цену закрытия акций за заданный период
    '''
    if 'Close' in data:
        average_price = data['Close'].mean()
        print(f"Средняя цена закрытия акций за заданный период: {average_price:.2f}")
    else:
        print("Информация о дате отсутствует или не имеет распознаваемого формата.")


def notify_if_strong_fluctuations(data, threshold):
    '''
    Функция анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период
    :param data: DataFrame с данными
    :param threshold: Парог для сравнения с максимальным и минимальными значениями
    :return: Пользователь получает уведомление если превышен парог
    '''
    try:
        max_stock = max([b for b in data['Close'].values])
        min_stock = min([b for b in data['Close'].values])
        if max_stock - min_stock > threshold:
            print(f'User, разница {max_stock - min_stock} превышает порог {threshold}')
        else:
            pass
    except Exception as e:
        print(f'Ошибка {e}')


def export_data_to_csv(data, filename):
    '''
    Cохраняет загруженные данные об акциях в CSV файл.

    :param data:DataFrame с данными
    :param filename: название файла
    :return:Результат сохранения акий в CSV файл
    '''
    df = pd.DataFrame(data)
    try:
        df.to_csv(filename, encoding='utf-8')
        print('Файлы успешно записаны')
    except Exception as e:
        print(f"Произошла ошибка: {e}.")


def plot_data(data, ticker, start_date, end_date, filename=None):
    '''
    Создаёт график, отображающий индикатор RSI
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    :param data: DataFrame с данными
    :param ticker: Тикер акции
    :param start_date: начало периода
    :param end_date:  конец приода
    :param filename: Название файла
    :return: Создаёт график, отображающий индикатор RSI
    '''
    plt.figure(figsize=(10, 6))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['RSI'].values, label='RSI')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['RSI'], label='RSI')

    plt.title(f"{ticker} Индекс относительной силы (RSI)")
    plt.xlabel("Дата")
    plt.ylabel("RSI")
    plt.legend()

    if filename is None:
        filename = f"{ticker}_{start_date}-{end_date}_stock_RSI_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def plot_close_average(data):
    '''
    Функия для рисования интерактивного графика plotly
    :param data: DataFrame с данными
    :return: Выводит plotly график и среднее значение за текущий период закрытия торгов
    '''
    # Проверяем, существует ли колонка 'Close'
    if 'Close' not in data.columns:
        print("Column 'Close' does not exist in the DataFrame.")
        return
        # Создаем интерактивный график
    fig = go.Figure()
    # Вычисляем среднее значение
    mean_close = data['Close'].mean()
    print(f"The average value of 'Close' is: {mean_close}")
    # Добавляем линию графика для 'Close'
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))

    # Добавляем горизонтальную линию для среднего значения
    fig.add_trace(go.Scatter(x=data.index, y=[mean_close] * len(data), mode='lines', name='Average Close Price',
                             line=dict(dash='dash', color='red')))

    # Настраиваем макет графика
    fig.update_layout(title='Close Price and Average Close Price',
                      xaxis_title='Date',
                      yaxis_title='Price',
                      legend=dict(x=0, y=1))

    # Показываем график
    fig.show()
