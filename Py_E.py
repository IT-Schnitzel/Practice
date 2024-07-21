import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
import urllib.request
import xml.dom.minidom

plt.rcParams.update({'font.size': 12})
current_date = datetime.today().date()

weeks = []
current_date_str = current_date.strftime('%d.%m.%Y')
prev_date = current_date - timedelta(weeks=1)
weeks.append(f"{prev_date.strftime('%d.%m.%Y')} - {current_date_str}")
for _ in range(3):
    new_date = prev_date - timedelta(weeks=1)
    weeks.append(f"{new_date.strftime('%d.%m.%Y')} - {(prev_date - timedelta(days=1)).strftime('%d.%m.%Y')}")
    prev_date = new_date

months = []
current_date_str = current_date.strftime('%b %Y')
prev_date = current_date
months.append(current_date_str)
for _ in range(3):
    prev_date -= timedelta(weeks=4)
    months.append(prev_date.strftime('%b %Y'))

quarters = []
current_date_str = current_date.strftime('%d.%m.%Y')
prev_date = current_date - timedelta(weeks=12)
quarters.append(f"{prev_date.strftime('%d.%m.%Y')} - {current_date_str}")
for _ in range(3):
    new_date = prev_date
    prev_date -= timedelta(weeks=12)
    quarters.append(f"{prev_date.strftime('%d.%m.%Y')} - {new_date.strftime('%d.%m.%Y')}")

years = []
current_date = current_date
years.append(current_date.strftime('%Y'))
for _ in range(3):
    current_date -= timedelta(weeks=52)
    years.append(current_date.strftime('%Y'))

def update_date_box():
    period_choice = date.get()
    if period_choice == 1:
        graph_date_box.config(values=weeks)
    elif period_choice == 2:
        graph_date_box.config(values=months)
    elif period_choice == 3:
        graph_date_box.config(values=quarters)
    elif period_choice == 4:
        graph_date_box.config(values=years)
    graph_date_box.current(0)
    graph_date_box.grid(column=2, row=period_choice)

def convert_currency():
    amount = float(currency_input.get())
    first_currency = first_currency_box.get()
    second_currency = second_currency_box.get()
    first_value = currency_values[currency_keys.index(first_currency)]
    second_value = currency_values[currency_keys.index(second_currency)]
    converted_value = amount * first_value / second_value
    converted_currency_label.config(text=converted_value)

month_mapping = {
    "Jan": 1, "Feb": 2, "Mar": 3,
    "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9,
    "Oct": 10, "Nov": 11, "Dec": 12,
    1: "янв", 2: "фев", 3: "март",
    4: "апр", 5: "май", 6: "июнь",
    7: "июль", 8: "авг", 9: "сен",
    10: "окт", 11: "ноя", 12: "дек"
}

def create_graph():
    period_choice = date.get()
    dates = []
    data_points = []
    currency = third_currency_box.get()

    if period_choice == 1:
        start_date = datetime.strptime(graph_date_box.get().split()[0], '%d.%m.%Y')
        for _ in range(7):
            dates.append(start_date.strftime('%d'))
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={start_date.strftime('%d/%m/%Y')}"
            data_points.append(fetch_data(url)[currency])
            start_date += timedelta(days=1)
    elif period_choice == 2:
        month, year = graph_date_box.get().split()
        first_date = datetime(year=int(year), month=month_mapping[month], day=1)
        day = 1
        month_num = month_mapping[month]
        if month_num < 10:
            month_str = f'0{month_num}'
        else:
            month_str = str(month_num)
        if month != current_date.strftime('%b'):
            while first_date.strftime('%m') == month_str:
                dates.append(day)
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={first_date.strftime('%d.%m.%Y')}"
                data_points.append(fetch_data(url)[currency])
                first_date += timedelta(days=1)
                day += 1
        else:
            while day != int(current_date.strftime('%d')):
                dates.append(day)
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={first_date.strftime('%d.%m.%Y')}"
                data_points.append(fetch_data(url)[currency])
                first_date += timedelta(days=1)
                day += 1
    elif period_choice == 3:
        start_date = datetime.strptime(graph_date_box.get().split()[0], '%d.%m.%Y')
        for _ in range(13):
            dates.append(start_date.strftime('%d.%m'))
            url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={start_date.strftime('%d/%m/%Y')}"
            data_points.append(fetch_data(url)[currency])
            start_date += timedelta(weeks=1)
    elif period_choice == 4:
        year = graph_date_box.get()
        year_diff = int(year) - int(current_date.strftime('%Y'))
        if year_diff == 0:
            month_count = int(current_date.strftime('%m'))
        else:
            month_count = 12
        for i in range(month_count):
            dates.append(month_mapping[i+1])
            if i < 9:
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/0{i+1}/{year}"
            else:
                url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{i+1}/{year}"
            data_points.append(fetch_data(url)[currency])

    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=second_tab)
    plot_widget = canvas.get_tk_widget()
    fig.clear()

    plt.plot(dates, data_points)
    plt.grid()
    plot_widget.grid(row=10, column=10)

def fetch_data(url):
    response = urllib.request.urlopen(url)
    xml_string = response.read().decode('windows-1251')
    dom = xml.dom.minidom.parseString(xml_string)
    data = {}
    for valute in dom.getElementsByTagName('Valute'):
        name = valute.getElementsByTagName('Name')[0].childNodes[0].nodeValue
        value = float(valute.getElementsByTagName('Value')[0].childNodes[0].nodeValue.replace(',', '.')) / int(
            valute.getElementsByTagName('Nominal')[0].childNodes[0].nodeValue)
        data[name] = value
    data["Российский рубль"] = 1.0
    return data

url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date.strftime('%d/%m/%Y')}"
initial_data = fetch_data(url)
currency_keys = list(initial_data.keys())
currency_values = list(initial_data.values())

window = tk.Tk()
window.title("Конвертер валют")
window.geometry("1280x800")

notebook = ttk.Notebook(window)
first_tab = ttk.Frame(notebook)
second_tab = ttk.Frame(notebook)
notebook.add(first_tab, text="Калькулятор валют")
notebook.add(second_tab, text="Динамика курса")

first_tab.grid_columnconfigure(0, minsize=200)
first_tab.grid_columnconfigure(1, minsize=150)
first_tab.grid_rowconfigure(0, minsize=100)

first_currency_box = ttk.Combobox(first_tab, values=currency_keys)
first_currency_box.current(0)
first_currency_box.grid(row=0, column=0)
second_currency_box = ttk.Combobox(first_tab, values=currency_keys)
second_currency_box.current(0)
second_currency_box.grid(row=3, column=0)

currency_input = tk.Entry(first_tab)
currency_input.grid(row=0, column=1)
convert_button = tk.Button(first_tab, text="Конвертировать", command=convert_currency)
convert_button.grid(row=0, column=2)
converted_currency_label = tk.Label(first_tab, text="")
converted_currency_label.grid(row=3, column=1)

second_tab.grid_columnconfigure(0, minsize=200)
second_tab.grid_columnconfigure(1, minsize=200)

currency_label = tk.Label(second_tab, text="Валюта")
currency_label.grid(row=0, column=0)
third_currency_box = ttk.Combobox(second_tab, values=currency_keys)
third_currency_box.current(0)
third_currency_box.grid(row=1, column=0)

date_label = tk.Label(second_tab, text="Период")
date_label.grid(row=0, column=1)
date = tk.IntVar()
tk.Radiobutton(second_tab, text='Неделя', variable=date, value=1, command=update_date_box).grid(row=1, column=1)
tk.Radiobutton(second_tab, text='Месяц', variable=date, value=2, command=update_date_box).grid(row=2, column=1)
tk.Radiobutton(second_tab, text='Квартал', variable=date, value=3, command=update_date_box).grid(row=3, column=1)
tk.Radiobutton(second_tab, text='Год', variable=date, value=4, command=update_date_box).grid(row=4, column=1)

date_choice_label = tk.Label(second_tab, text="Выбор периода")
date_choice_label.grid(row=0, column=2)
graph_date_box = ttk.Combobox(second_tab)
graph_creator_button = tk.Button(second_tab, text="Построить график", command=create_graph)
graph_creator_button.grid(row=4, column=0)

notebook.pack(expand=1, fill='both')
window.mainloop()
