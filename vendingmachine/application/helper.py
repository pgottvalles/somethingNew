import sqlite3


def get_db_conx(db_name='vendinding.machine.db'):
    con = sqlite3.connect(db_name)
    con.row_factory = sqlite3.Row
    return con


def cursor_list_dict(cursor_exe_response):
    list_of_dict_result = [dict(row) for row in cursor_exe_response.fetchall()]
    return list_of_dict_result


def list_of_dict_nice_display(list_dict):
    for i in list_dict:
        print(i)
