import chardet
import re
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import ctypes

addresses = {
    '31': '[УМ-1]',
    '32': '[УМ-2]',
    '33': '[СУ]',
}

cmd_list = {
    '30': 'Зарезервировано.',
    '31': 'Запрос сводного статуса.',
    '32': 'Зарезервировано.',
    '33': 'Запрос аварии/дополнительного статуса.',
    '34': 'Зарезервировано.',
    '35': 'Зарезервировано.',
    '36': 'Запрос результатов основных измерений.',
    '37': 'Зарезервировано.',
    '38': 'Зарезервировано.',
    '39': 'Зарезервировано.',
    '3A': 'Запрос заданного значения мощности.',

    '40': 'Изм. сост.: Включено.',
    '41': 'Изм. сост.: Дежурный.',
    '42': 'Изм. сост.: Сброс.',
    '43': 'Изм. сост.: Выключено.',
    '44': 'Изм. сост.: Зарезервировано.',
    '45': 'Изм. сост.: Зарезервировано.',
    '46': 'Изм. сост.: Включить АРМ.',
    '47': 'Изм. сост.: Выключить АРМ.',
    '48': 'Изм. сост.: Сброс мощности.',
    '49': 'Изм. сост.: Открыть аттенюатор.',
    '4A': 'Изм. сост.: Зарезервировано.',
    '4B': 'Изм. сост.: Зарезервировано.',
    '4C': 'Изм. сост.: Зарезервировано.',
    '4E': 'Изм. сост.: Установить мощность.',
    '4F': 'Изм. сост.: Мощность +/-/=.',

    '70': 'Зарезервировано.',
    '71': 'Запрос сводного статуса.',
    '72': 'Зарезервировано.',
    '73': 'Запрос аварии/дополнительного статуса.',
    '74': 'Запрос мощностей.',
    '75': 'Запрос положения фазовращателей.',

    '50': 'Изм. сост.: УМ-1 на эквивалент.',
    '51': 'Изм. сост.: УМ-2 на эквивалент.',
    '52': 'Изм. сост.: Зарезервировано.',
    '53': 'Изм. сост.: Зарезервировано.',
    '54': 'Изм. сост.: УМ-1 в антенну.',
    '55': 'Изм. сост.: УМ-2 в антенну.',
    '56': 'Изм. сост.: Сложение на эквивалент.',
    '57': 'Изм. сост.: Зарезервировано.',
    '58': 'Изм. сост.: Зарезервировано.',
    '59': 'Изм. сост.: Сложение в антенну.',
    '5A': 'Изм. сост.: Коммутатор входного сигнала в положение 1.',
    '5B': 'Изм. сост.: Коммутатор входного сигнала в положение 2.',
    '5C': 'Изм. сост.: Сложение автоматическое.',
    '5D': 'Изм. сост.: Сложение ручное.',
    '5E': 'Изм. сост.: Фазовращатель Ф1 +/-.',
    '5F': 'Изм. сост.: Фазовращатель Ф2 +/-.',
    '6A': 'Изм. сост.: Установить резервный УМ.',
    '6B': 'Изм. сост.: Автоматическое резервирование.',
    '6C': 'Изм. сост.: Установить тип резервирования.',
    '6D': 'Изм. сост.: Ослабление -10 дБ.',
    '6E': 'Изм. сост.: Зарезервировано.',
    '6F': 'Изм. сост.: Зарезервировано.'
}

errors_list = {
    '61': 'Код команды не опознан.',
    '62': 'Недопустимый параметр или параметр за пределами диапазона.',
    '63': 'ДУ не разрешено и команда не может быть выполнена.',
    '64': 'Команда не может быть выполнена, т.к. не соблюдены условия выполнения.',
    '65': 'Команда не может быть выполнена из-за наличия аварии.',
    '66': 'Команда не может быть выполнена, т.к. отключено высокое напряжение.',
    '67': 'Команда не может быть выполнена, т.к. закрыт аттенюатор.',
    '68': 'Команда не может быть выполнена, т.к. УМ резервный.',
    '69': 'Зарезервировано.'
}

resp_36 = ('Uк(кВ):', 'Iкол(А):', 'Iа(А):', 'Uн(В):', 'Iн(А):', 'Uвак(кВ):',
           'Iвак(мкА):', 'Uипуп(В):', 'Uипс1(В):', 'Uипс2(В):', 'Pвых(Вт):', 'Pотр(Вт):')
resp_74 = ('Pсум:', 'Pвых:', 'Pотр:')

ENCODING = 'utf-16'

DATA = {'31': [], '32': []}
FAULTS_LIST = {'УМ-1': [], 'УМ-2': []}

PROGRESS = 0


def open_file(path):
    try:
        with open(path, 'rb') as file_in:
            text = file_in.read()
            enc = chardet.detect(text).get('encoding')
            global ENCODING
            ENCODING = str(enc)
            if str(path).endswith('.rpt') or ENCODING == 'None':
                ENCODING = 'utf-16'
            text = text.decode(ENCODING)
            return text
    except Exception:
        return 'Can_not_open'


def save_file(path, text):
    with open(path, 'w', encoding=ENCODING) as file_out:
        file_out.write(text)


def time_filter(text, date_time1, date_time2):
    date_time1 = list(map(int, date_time1.split('-')))
    date_time2 = list(map(int, date_time2.split('-')))
    pattern_datetime = r'\[(\d\d)\.(\d\d)\.(\d\d\d\d), (\d\d):(\d\d):(\d\d)'
    text = text.splitlines()
    filtered_text = []
    for line in text:
        try:
            date_time = list(map(int, re.findall(pattern_datetime, line)[0]))
            date_time = list(reversed(date_time[:3])) + date_time[3:]
            if date_time > date_time2:
                break
            if date_time1 <= date_time <= date_time2:
                filtered_text.append(line)
        except IndexError:
            pass
    return '\n'.join(filtered_text)


def filter_by_word(text, words):
    searched = []
    text = text.splitlines()
    words = words.split(';')
    for line in text:
        for word in words:
            if word.lower().strip() in line.lower():
                searched.append(line)
                break
    return '\n'.join(searched)


def cmd_decoding(text):
    global FAULTS_LIST, DATA, PROGRESS

    decoding_text = []

    PROGRESS = 0

    FAULTS_LIST['УМ-1'] = []
    FAULTS_LIST['УМ-2'] = []

    DATA['31'] = []
    DATA['32'] = []
    text = text.splitlines()

    n_lines = len(text)
    pattern_hex = r'0x(\w{2})'
    pattern_prefix = r'(\[.*(Выдача|Принято).*?:)'
    pattern_addr = r'7B(31|32|33)2F'
    pattern_cmd = r'7B(31|32|33)2F(\w\w)'
    pattern_params = r'7B(31|32|33)2F\w\w(\w*)7D'
    pattern_datetime = r'\[(\d\d)\.(\d\d)\.(\d\d\d\d), (\d\d):(\d\d):(\d\d)'
    pattern_fault = r'\[(УМ-1|УМ-2)\] [OО][КK]\. (.+?): АВАРИЯ'

    for string_num, line in enumerate(text):
        PROGRESS = int(string_num / n_lines * 100)
        try:
            prefix = re.findall(pattern_prefix, line)[0][0]
            req_hex = re.findall(pattern_hex, line)
            req_hex = ''.join(req_hex)
            addr_hex = re.findall(pattern_addr, req_hex)[0]
            cmd_hex = re.findall(pattern_cmd, req_hex)[0][1]
            params_hex = re.findall(pattern_params, req_hex)[0][1]

            if params_hex in errors_list:
                decoding_text.append(prefix + '\t' + '{' + addresses[addr_hex] +
                                     ' ' + cmd_list[cmd_hex] + ' ' + errors_list[params_hex] + '}')
                continue

            params_hex_list = [params_hex[i:i + 2] for i in range(0, len(params_hex), 2)]

            for_hex_list = ['31', '33', '71', '73']
            if cmd_hex in for_hex_list:
                params = params_hex
                # params = bin(int(params_hex, 16))[2:]
            elif cmd_hex == '36':
                measurements_list = ''.join(hex_to_ascii(params_hex_list)).split()
                if measurements_list:
                    date_time = list(map(int, re.findall(pattern_datetime, line)[0]))
                    date_time = [list(reversed(date_time[:3])) + date_time[3:]]
                    # date_time = [mdates.date2num(datetime.datetime(*date_time))]
                    try:
                        DATA[addr_hex].append(date_time + list(map(float, measurements_list)))
                    except ValueError:
                        pass

                params = '; '.join(
                    [a + ' ' + b for a, b in zip(resp_36, measurements_list)])
            elif cmd_hex == '74':
                params = '; '.join(
                    [a + ' ' + b for a, b in zip(resp_74, ''.join(hex_to_ascii(params_hex_list)).split())])
            else:
                params = ''.join(hex_to_ascii(params_hex_list)).strip()

            decoding_text.append(prefix + '\t' + '{' + addresses[addr_hex] +
                                 ' ' + cmd_list[cmd_hex] + ' ' + params + '}')

        except IndexError:
            fault = re.findall(pattern_fault, line)
            if fault:
                date_time = list(map(int, re.findall(pattern_datetime, line)[0]))
                date_time = list(reversed(date_time[:3])) + date_time[3:]
                FAULTS_LIST[fault[0][0]].append([date_time, fault[0][1]])
            decoding_text.append(line)
            continue

    return '\n'.join(decoding_text)


def hex_to_ascii(hex_lst):
    ascii_cmd = []
    for i in hex_lst:
        ascii_cmd.append(bytes.fromhex(i).decode('utf-8'))
    return ascii_cmd


def manually_decoding(text):
    decoding_text = []
    text = text.splitlines()

    pattern_hex = r'0x(\w{2})'
    pattern_addr = r'7B(31|32|33)2F'
    pattern_cmd = r'7B(31|32|33)2F(\w\w)'
    pattern_params = r'7B(31|32|33)2F\w\w(\w*)7D'
    for line in text:
        try:
            req_hex = re.findall(pattern_hex, line)
            req_hex = ''.join(req_hex)
            addr_hex = re.findall(pattern_addr, req_hex)[0]
            cmd_hex = re.findall(pattern_cmd, req_hex)[0][1]
            params_hex = re.findall(pattern_params, req_hex)[0][1]

            if params_hex in errors_list:
                decoding_text.append('{' + addresses[addr_hex] +
                                     ' ' + cmd_list[cmd_hex] + ' ' + errors_list[params_hex] + '}')
                continue

            params_hex_list = [params_hex[i:i + 2] for i in range(0, len(params_hex), 2)]

            for_hex_list = ['31', '33', '71', '73']
            if cmd_hex in for_hex_list:
                params = params_hex
                # params = bin(int(params_hex, 16))[2:]
            elif cmd_hex == '36':
                params = '; '.join(
                    [a + ' ' + b for a, b in zip(resp_36, ''.join(hex_to_ascii(params_hex_list)).split())])
            elif cmd_hex == '74':
                params = '; '.join(
                    [a + ' ' + b for a, b in zip(resp_74, ''.join(hex_to_ascii(params_hex_list)).split())])
            else:
                params = ''.join(hex_to_ascii(params_hex_list)).strip()

            decoding_text.append('{' + addresses[addr_hex] +
                                 ' ' + cmd_list[cmd_hex] + ' ' + params + '}')
        except IndexError:
            decoding_text.append(line)
            continue
    return '\n'.join(decoding_text)


def plot(params, um, one_fig, marker, rationing, time_scope, markersize, faults_flag, koefs):
    time_start = mdates.date2num(datetime.datetime(*time_scope[0]))
    time_finish = mdates.date2num(datetime.datetime(*time_scope[1]))
    rationing_title = ''
    columns = ['Time', 'Uк', 'Iкол', 'Iа', 'Uн', 'Iн', 'Uвак', 'Iвак', 'Uипуп', 'Uипс1', 'Uипс2', 'Pвых', 'Pотр']
    columns_fault = ['Time', 'Param']

    if not rationing:
        ylabels = {'Uк': ['Uк, кВ', 'Напряжение катода'],
                   'Iкол': ['Iкол, А', 'Ток коллектора'],
                   'Iа': ['Iа, А', 'Ток анода'],
                   'Uн': ['Uн, В', 'Напряжение накала'],
                   'Iн': ['Iн, А', 'Ток накала'],
                   'Uвак': ['Uвак, кВ', 'Напряжение вакиона'],
                   'Iвак': ['Iвак, мкА', 'Ток вакиона'],
                   'Uипуп': ['Uипуп, В', 'Напряжение ИП предусилителя'],
                   'Uипс1': ['Uипс1, В', 'Напряжение ИП соленоида'],
                   'Uипс2': ['Uипс2, В', 'Напряжение ИП соленоида'],
                   'Pвых': ['Pвых, Вт', 'Мощность на выходе'],
                   'Pотр': ['Pотр, Вт', 'Отраженная мощность']}
    else:
        ylabels = {'Uк': ['Uк', 'Напряжение катода'],
                   'Iкол': ['Iкол', 'Ток коллектора'],
                   'Iа': ['Iа', 'Ток анода'],
                   'Uн': ['Uн', 'Напряжение накала'],
                   'Iн': ['Iн', 'Ток накала'],
                   'Uвак': ['Uвак', 'Напряжение вакиона'],
                   'Iвак': ['Iвак', 'Ток вакиона'],
                   'Uипуп': ['Uипуп', 'Напряжение ИП предусилителя'],
                   'Uипс1': ['Uипс1', 'Напряжение ИП соленоида'],
                   'Uипс2': ['Uипс2', 'Напряжение ИП соленоида'],
                   'Pвых': ['Pвых', 'Мощность на выходе'],
                   'Pотр': ['Pотр', 'Отраженная мощность']}

    um_f = 'УМ-1'
    if um == '32':
        um_f = 'УМ-2'
    df_faults = pd.DataFrame(data=FAULTS_LIST[um_f], columns=columns_fault)
    df_faults['Time'] = df_faults['Time'].apply(lambda x: mdates.date2num(datetime.datetime(*x)))
    df_faults = df_faults[df_faults['Time'] >= time_start]
    df_faults = df_faults[df_faults['Time'] <= time_finish]
    df_faults = df_faults[df_faults['Param'].str.contains('Рвозб.|Охлаждение') == False]
    df_faults = df_faults.groupby('Param')['Time'].apply(list)

    df = pd.DataFrame(data=DATA[um], columns=columns)
    df['Time'] = df['Time'].apply(lambda x: mdates.date2num(datetime.datetime(*x)))
    df = df[df['Time'] >= time_start]
    df = df[df['Time'] <= time_finish]
    for param in params:
        if param in koefs:
            df[param] = df[param].apply(lambda x: x * koefs[param])
            ylabels[param][0] += f'  x {koefs[param]}'

    if rationing:
        rationing_title = ' (нормированные)'
        max_values = dict()
        for param in params:
            max_values[param] = df[param].max()
        max_value = max(max_values.values())
        for param in params:
            df[param] = df[param].apply(lambda x: (x * max_value / max_values[param]) / max_value)

    my_fmt = mdates.DateFormatter('%H:%M:%S')

    colors_fault = ['m', 'orange', 'r', 'g', 'b', '#CD5C5C', '#C71585', '#FF8C00', '#8B0000', '#FFFF00',
                    '#00FF00', 'c', '#E9967A']

    display_width = ctypes.windll.user32.GetSystemMetrics(0)
    display_heght = ctypes.windll.user32.GetSystemMetrics(1)
    figsize_x = display_width * 0.7 / 100
    figsize_y = display_heght * 0.7 / 100
    position_x = int(display_width / 2 - figsize_x * 100 / 2)
    position_y = int(display_heght / 2 - figsize_y * 100 / 2)

    if not one_fig:
        nparams = len(params)
        if nparams <= 3:
            nrows = 1
            ncols = nparams
        else:
            nrows = 2
            ncols = math.ceil(nparams / 2)

        fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(figsize_x, figsize_y), dpi=100)
        fig.canvas.manager.window.wm_geometry(f'+{position_x}+{position_y}')

        if nrows * ncols == 1:
            ax = [[ax]]
        elif nrows * ncols < 4:
            ax = [ax]
        itr = iter(params)
        for i in range(0, nrows):
            for j in range(0, ncols):
                try:
                    param = next(itr)
                    if faults_flag:
                        for k, faults in enumerate(df_faults.keys()):
                            for m, fault in enumerate(df_faults[faults]):
                                if m == 0:
                                    ax[i][j].axvline(x=fault, color=colors_fault[k], label='Авария: ' + faults,
                                                     linestyle='--', linewidth=1)
                                else:
                                    ax[i][j].axvline(x=fault, color=colors_fault[k], linestyle='--', linewidth=1)

                    ax[i][j].plot_date(x=df['Time'], y=df[param], marker=marker, markersize=markersize)
                    if nrows * ncols > 7:
                        title_size = 9
                    else:
                        title_size = 12
                    text_size = 10, 8
                    ax[i][j].set_title(ylabels[param][1], size=title_size)
                    ax[i][j].xaxis.set_major_formatter(my_fmt)
                    ax[i][j].tick_params(axis='x',  # Применяем параметры к обеим осям(both)
                                         # which='major',  # Применяем параметры к основным делениям
                                         # direction='inout',  # Рисуем деления внутри и снаружи графика
                                         # length=20,  # Длинна делений
                                         # width=4,  # Ширина делений
                                         # color='m',  # Цвет делений
                                         # pad=10,  # Расстояние между черточкой и ее подписью
                                         # labelsize=15,  # Размер подписи
                                         # labelcolor='r',  # Цвет подписи
                                         # bottom=True,  # Рисуем метки снизу
                                         # top=True,  # сверху
                                         # left=True,  # слева
                                         # right=True,  # и справа
                                         # labelbottom=True,  # Рисуем подписи снизу
                                         # labeltop=True,  # сверху
                                         # labelleft=True,  # слева
                                         # labelright=True,  # и справа
                                         labelrotation=20)

                    if nrows * ncols > 9:
                        ax[i][j].set_xlabel('Время', fontsize=6)
                        ax[i][j].set_ylabel(ylabels[param][0], fontsize=6)
                        ax[i][j].tick_params(axis='both', labelsize=6)
                    elif nrows * ncols > 7:
                        ax[i][j].set_xlabel('Время', fontsize=8)
                        ax[i][j].set_ylabel(ylabels[param][0], fontsize=8)
                        ax[i][j].tick_params(axis='both', labelsize=8)
                    else:
                        ax[i][j].set(ylabel=ylabels[param][0], xlabel='Время')

                    ax[i][j].grid(True)
                    if df_faults.count() and faults_flag:
                        legend_size = {1: 10, 2: 9, 3: 9, 4: 9, 5: 8, 6: 8, 7: 7, 8: 7, 9: 7, 10: 7, 11: 6, 12: 6}
                        ax[i][j].legend(prop={'size': legend_size[nrows * ncols]}).set_visible(True)
                except StopIteration:
                    break
        if um == '31':
            fig.suptitle('Параметры УМ-1' + rationing_title)
        elif um == '32':
            fig.suptitle('Параметры УМ-2' + rationing_title)
        # plt.gcf().autofmt_xdate()
        plt.subplots_adjust(hspace=0.4)
        plt.show()
    elif one_fig:
        fig, ax = plt.subplots(figsize=(figsize_x, figsize_y), dpi=100)
        fig.canvas.manager.window.wm_geometry(f'+{position_x}+{position_y}')

        if faults_flag:
            for k, faults in enumerate(df_faults.keys()):
                for m, fault in enumerate(df_faults[faults]):
                    if m == 0:
                        ax.axvline(x=fault, color=colors_fault[k], label='Авария: ' + faults, linestyle='--',
                                   linewidth=1)
                    else:
                        ax.axvline(x=fault, color=colors_fault[k], linestyle='--', linewidth=1)
        colors = {'Uк': 'y',
                  'Iкол': 'g',
                  'Iа': 'orange',
                  'Uн': 'm',
                  'Iн': 'c',
                  'Uвак': '#E9967A',
                  'Iвак': '#FF1493',
                  'Uипуп': '#556B2F',
                  'Uипс1': '#5F9EA0',
                  'Uипс2': '#778899',
                  'Pвых': 'b',
                  'Pотр': 'r'}
        for i, param in enumerate(params):
            ax.plot_date(x=df['Time'], y=df[param], marker=marker, markersize=markersize,
                         color=colors[param], label=ylabels[param][0])
        ax.xaxis.set_major_formatter(my_fmt)
        ax.grid(True)
        ax.set(xlabel='Время')
        ax.tick_params(axis='x',  # Применяем параметры к обеим осям(both)
                       # which='major',  # Применяем параметры к основным делениям
                       # direction='inout',  # Рисуем деления внутри и снаружи графика
                       # length=20,  # Длинна делений
                       # width=4,  # Ширина делений
                       # color='m',  # Цвет делений
                       # pad=10,  # Расстояние между черточкой и ее подписью
                       # labelsize=15,  # Размер подписи
                       # labelcolor='r',  # Цвет подписи
                       # bottom=True,  # Рисуем метки снизу
                       # top=True,  # сверху
                       # left=True,  # слева
                       # right=True,  # и справа
                       # labelbottom=True,  # Рисуем подписи снизу
                       # labeltop=True,  # сверху
                       # labelleft=True,  # слева
                       # labelright=True,  # и справа
                       labelrotation=20)
        if um == '31':
            fig.suptitle('Параметры УМ-1' + rationing_title)
        elif um == '32':
            fig.suptitle('Параметры УМ-2' + rationing_title)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    pass
