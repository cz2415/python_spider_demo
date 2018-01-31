# # -*- coding:utf-8 -*-
import requests
import urllib3
from prettytable import PrettyTable

urllib3.disable_warnings()

from stations import stations_dict

code_dict = {v: k for k, v in stations_dict.items()}


def get_query_url(from_station, to_station, date):
    url = (
        'https://kyfw.12306.cn/otn/leftTicket/queryZ?'
        'leftTicketDTO.train_date={}&'
        'leftTicketDTO.from_station={}&'
        'leftTicketDTO.to_station={}&'
        'purpose_codes=ADULT'
    ).format(date, stations_dict[from_station], stations_dict[to_station])
    return url


def query_train_info(url):
    info_list = []
    r = requests.get(url, verify=False)
    raw_trains = r.json()['data']['result']
    table = PrettyTable(
        ["车次", "出发站/到达站", "出发时间/到达时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座"])
    table.align["车次"] = "1"  # 以姓名字段左对齐
    table.padding_width = 1  # 填充宽度
    for raw_train in raw_trains:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')
        # 车次号码
        train_no = data_list[3]
        # 出发站
        from_station_code = data_list[6]
        from_station_name = code_dict[from_station_code]
        # 终点站
        to_station_code = data_list[7]
        to_station_name = code_dict[to_station_code]
        # 出发时间
        start_time = data_list[8]
        # 到达时间
        arrive_time = data_list[9]
        # 总耗时
        time_fucked_up = data_list[10]
        # 商务座
        commerce_class_seat = data_list[32] or data_list[32] or '--'
        # 一等座
        first_class_seat = data_list[31] or '--'
        # 二等座
        second_class_seat = data_list[30] or '--'
        # 高级软卧
        first_class_soft_sleep = data_list[21] or '--'
        # 软卧
        soft_sleep = data_list[23] or '--'
        # 动卧
        chr_soft_sleep = data_list[27] or '--'
        # 硬卧
        hard_sleep = data_list[28] or '--'
        # 软座
        soft_seat = data_list[24] or '--'
        # 硬座
        hard_seat = data_list[29] or '--'
        # 无座
        no_seat = data_list[26] or '--'
        # "车次", "出发站/到达站", "出发时间/到达时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座"
        table.add_row([train_no, from_station_name + "/" + to_station_name,
                       start_time + "/" + arrive_time, time_fucked_up, commerce_class_seat,
                       first_class_seat, second_class_seat, first_class_soft_sleep, soft_sleep,
                       chr_soft_sleep, hard_sleep, soft_seat, hard_seat, no_seat])
    print(table)


url = get_query_url('北京', '沈阳', '2018-01-31')
query_train_info(url)
