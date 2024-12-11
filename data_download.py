import yfinance as yf


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
    :param data:
    :param window_size:
    :return:
    '''
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data
