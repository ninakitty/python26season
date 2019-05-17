#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 21:47
# @Author  : Abel
# @File    : staff_info.py
# @Software: PyCharm
import os
import user_login


# Decorator
@user_login.login_index
def staff_info_index():
    """
    Employee Information System Home Function
    :return: No return
    """
    while True:
        function_name, ret = staff_info_input()
        if function_name == "Q":
            break
        if function_name == "select":
            if ret:
                for info in ret:
                    print(info)
            else:
                print("No corresponding data found")

        elif function_name == "insert":
            if ret:
                print("Insert data successfully , The inserted data is '%s' " % ret)

        elif function_name == "delete" or function_name == "update":
            if ret:
                print(ret)
        else:
            print("Syntax error, please enter the correct syntax")


def staff_info_input():
    """
    Employee information query statement input
    :return:Return value of subsequent function
    """
    user_input = input("请输入操作语句,[Q=quit]>>>").strip()
    if user_input.upper() == "Q":
        return "Q", None
    func_name, func = routing_method(user_input)
    if not func:
        return False
    info = user_input.split(maxsplit=1)
    return func_name, func(*info)


def routing_method(info):
    """
    Invoke related methods according to the title information input by the user
    :param info:User input information, need to be a string
    :return:select/update/insert/delete function memory id  or False
    """
    if info.startswith("select"):
        return "select", select
    elif info.startswith("update"):
        return "update", update
    elif info.startswith("insert"):
        return "insert", insert
    elif info.startswith("delete"):
        return "delete", delete
    else:
        return False, None


def select(*args):
    """
    Query matching user information based on criteria
    :param args:user entered string content
    :return:matched_staff_info_list ["content1","content2","content3",...]
    """
    info = args[1].split("where")
    # user entered column name
    display_content = info[0].split(",")
    temp_matched_staff_info_list = operator(info[1])
    matched_staff_info_list = []

    # Processing * query
    if display_content[0].strip() == "*":
        # Get the dictionary in the list info
        for line_staff_dict in temp_matched_staff_info_list:
            line_staff_info_temp_list = []
            # line_staff_dict == All columns
            for column_info in line_staff_dict:
                # dict --> list
                line_staff_info_temp_list.append(line_staff_dict[column_info])
            # list --> str
            matched_staff_info_list.append(",".join(line_staff_info_temp_list))
        return matched_staff_info_list

    else:
        # Get the dictionary in the list info
        for line_staff_dict in temp_matched_staff_info_list:
            line_staff_info_temp_list = []
            # display_content == The column the user wants to query
            for column_info in display_content:
                column_info = column_info.strip()
                # dict --> list
                line_staff_info_temp_list.append(line_staff_dict[column_info])
            # list --> str
            matched_staff_info_list.append(",".join(line_staff_info_temp_list))
        return matched_staff_info_list


def update(*args):
    """
    Update matching user information based on criteria
    :param args:user entered string content
    :return:
    """
    info = args[1].split("where")

    if "=" in info[0] and "=" in info[1]:
        # user entered column name and  new value
        data = info[0].strip().split("=")
        # user entered condition
        condition = info[1].strip().split("=")
        return update_staff_information(data, condition)
    else:
        return False


def insert(*args):
    """
    Insert user information based on criteria
    :param args:user entered string content
    :return:
    """
    info_list = args[1].split(",")
    info_dict = {}
    for info_ in info_list:
        k = info_.strip().split("=")[0]
        v = info_.strip().split("=")[1]
        # user input k=v str --> dict
        info_dict[k] = v
    return insert_staff_information(**info_dict)


def delete(*args):
    if "=" in args[1]:
        # user entered condition
        condition = args[1].strip().split("=")
        return delete_staff_information(*condition)
    else:
        return False


def operator(operational_content):
    """
    Call different functions based on user input
    :param operational_content: a string containing an operator  'a>b' or 'a<b' or 'a=b'
    :return:Contains a list of dictionaries  [{"key","value"},{"key","value"},...] or False
    """
    if ">" in operational_content:
        opr_list = operational_content.strip().split(">")
        column_name = opr_list[0].strip()
        opr = opr_list[1].strip()
        return select_greater_than_operation(column_name, opr)

    elif "<" in operational_content:
        opr_list = operational_content.strip().split("<")
        column_name = opr_list[0].strip()
        opr = opr_list[1].strip()
        return select_less_than_operation(column_name, opr)

    elif "=" in operational_content:
        opr_list = operational_content.strip().split("=")
        column_name = opr_list[0].strip()
        opr = opr_list[1].strip()
        return select_equal_than_operation(column_name, opr)
    elif "like" in operational_content:
        opr_list = operational_content.strip().split("like")
        column_name = opr_list[0].strip()
        opr = opr_list[1].strip()
        return select_like_than_operation(column_name, opr)
    else:
        return False


def select_greater_than_operation(column, benchmark):
    """
    Query data greater than the condition
    :param column: Existing column name
    :param benchmark: operation benchmark
    :return:Contains a list of dictionaries  [{"key","value"},{"key","value"},...]
    """
    matched_staff_info_temp_list = []
    with open("staff_info") as info_file:
        for line in info_file:
            line = line.strip().split(",")
            staff_line_dict = {"id": line[0], "name": line[1], "age": line[2], "phone": line[3], "job": line[4]}

            if int(staff_line_dict[column]) > int(benchmark):
                matched_staff_info_temp_list.append(staff_line_dict)
        info_file.close()
    return matched_staff_info_temp_list


def select_less_than_operation(column, benchmark):
    """
    Query data less than the condition
    :param column: Existing column name
    :param benchmark: operation benchmark
    :return:Contains a list of dictionaries  [{"key","value"},{"key","value"},...]
    """
    matched_staff_info_temp_list = []
    with open("staff_info") as info_file:
        for line in info_file:
            line = line.strip().split(",")
            staff_line_dict = {"id": line[0], "name": line[1], "age": line[2], "phone": line[3], "job": line[4]}

            if int(staff_line_dict[column]) < int(benchmark):
                matched_staff_info_temp_list.append(staff_line_dict)
        info_file.close()
    return matched_staff_info_temp_list


def select_equal_than_operation(column, benchmark):
    """
    Query data equal than the condition
    :param column: Existing column name
    :param benchmark: operation benchmark
    :return: Contains a list of dictionaries  [{"key","value"},{"key","value"},...]
    """
    matched_staff_info_temp_list = []
    with open("staff_info") as info_file:
        for line in info_file:
            line = line.strip().split(",")
            staff_line_dict = {"id": line[0], "name": line[1], "age": line[2], "phone": line[3], "job": line[4]}

            if staff_line_dict[column] == benchmark:
                matched_staff_info_temp_list.append(staff_line_dict)
        info_file.close()
    return matched_staff_info_temp_list


def select_like_than_operation(column, benchmark):
    """
    Fuzzy query based on like condition
    :param column: Existing column name
    :param benchmark: operation benchmark
    :return: Contains a list of dictionaries  [{"key","value"},{"key","value"},...]
    """
    matched_staff_info_temp_list = []
    with open("staff_info") as info_file:
        for line in info_file:
            line = line.strip().split(",")
            staff_line_dict = {"id": line[0], "name": line[1], "age": line[2], "phone": line[3], "job": line[4]}
            # Determine if the character exists in the string
            if benchmark in staff_line_dict[column]:
                matched_staff_info_temp_list.append(staff_line_dict)
        info_file.close()
    return matched_staff_info_temp_list


def update_staff_information(data, benchmark):
    """
    Update staff information
    :param data:
    :param benchmark:
    :return: Operation completed,%d Affected data
    """
    column_name = data[0].strip()
    new_value = data[1].strip()
    benchmark_name = benchmark[0].strip()
    benchmark_value = benchmark[1].strip()
    with open("staff_info") as info_file, open("staff_info_temp", "w") as info_file_temp:
            number = 0
            for line in info_file:
                new_line = line.strip().split(",")
                # line_file --> list --> dict
                staff_line_dict = {"id": new_line[0], "name": new_line[1], "age": new_line[2],
                                   "phone": new_line[3], "job": new_line[4]}
                if staff_line_dict[benchmark_name] == benchmark_value:
                    # update dict data
                    staff_line_dict[column_name] = new_value
                    staff_line_list = []
                    for column in staff_line_dict:
                        # dict --> list
                        staff_line_list.append(staff_line_dict[column])
                    # list --> str
                    info_file_temp.write(",".join(staff_line_list)+"\n")
                    number += 1
                    continue
                else:
                    info_file_temp.write(line)
            else:
                info_file.close()
                info_file_temp.close()
                os.remove("staff_info")
                os.rename("staff_info_temp", "staff_info")
                context = "Operation completed,%d Affected data " %(number)
                return context


def insert_staff_information(**kwargs):
    """
    Insert staff information
    :param kwargs: staff dict ,{name:v,age:v1,phone:v2,job:v3}
    :return: Insert staff str
    """
    with open("staff_id", "r") as r_id_file:
        # Get staff id,and add one  str(int(str)+1)
        staff_id = str(int(r_id_file.readline().strip().split(",")[-1])+1)
        r_id_file.close()
        # dict add staff_id
        kwargs["id"] = staff_id
    with open("staff_info", "a") as a_staff_file, open("staff_id", "a") as a_id_file:
        staff_info = "{id},{name},{age},{phone},{job}\n".format(**kwargs)
        a_id_file.write(",{id}".format(id=staff_id))
        # Additional write to staff_info.txt
        a_staff_file.write(staff_info)
        # Additional write to staff_id.txt
        a_id_file.close()
        a_staff_file.close()
        # returning remove spaces, line breaks
        return staff_info.strip()


def delete_staff_information(*args):
    """
    Delete staff information
    :param args: benchmark_list [name,value]
    :return:
    """
    benchmark_name = args[0].strip()
    benchmark_value = args[1].strip()
    with open("staff_info") as info_file, open("staff_info_temp", "w") as info_file_temp:
            number = 0
            for line in info_file:
                new_line = line.strip().split(",")
                # line_file --> list --> dict
                staff_line_dict = {"id": new_line[0], "name": new_line[1], "age": new_line[2],
                                   "phone": new_line[3], "job": new_line[4]}
                if staff_line_dict[benchmark_name] == benchmark_value:
                    continue
                else:
                    info_file_temp.write(line)
            else:
                info_file.close()
                info_file_temp.close()
                os.remove("staff_info")
                os.rename("staff_info_temp", "staff_info")
                context = "Operation completed,%d Affected data " %(number)
                return context


if __name__ == '__main__':
    staff_info_index()
