import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print(
        "Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print(
        "Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    # period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    start_date = input("Введите дату начала (YYYY-MM-DD): ")
    end_date = input("Введите дату окончания (YYYY-MM-DD): ")
    chosen_style = input(
        "Выберите стиль графика (например, 'ggplot', 'fivethirtyeight', 'dark_background', 'default'): ")
    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, start_date, end_date)
    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)
    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, start_date, end_date, chosen_style)
    # Average the data
    dplt.calculate_and_display_average_price(stock_data)
    # Difference the data
    dplt.notify_if_strong_fluctuations(stock_data, 2)
    dplt.export_data_to_csv(stock_data, 'output.csv')
    # Reading indicator
    indicator_data = dd.calculate_indicator('output.csv')
    # Plot the indicator_data
    dplt.plot_data(indicator_data, ticker, start_date, end_date, filename=None)
    dplt.plot_close_average(stock_data)

if __name__ == "__main__":
    main()
