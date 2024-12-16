import yfinance as yf
import pandas as pd
import pandas_ta as ta


def fetch_stock_data(ticker, period='1mo'):
    '''
    Получает исторические данные об акциях для указанного тикера и временного периода.
    :param ticker: name ticker
    :param period:  date period
    :return: Возвращает DataFrame с данными.
    '''
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=7):
    '''
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    :param data: Данные торгов
    :param window_size: размер окна
    :return: DataFrame с данными
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_indicator(filename):
    '''
    Функция для расчета индикатора RSI
    :param filename: Файл с DataFrame
    :return: DataFrame с данными
    '''
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df.set_index('Date', inplace=True)  # Установка даты в качестве индекса
    df['RSI'] = ta.rsi(df['Close'], length=14)

    return df
