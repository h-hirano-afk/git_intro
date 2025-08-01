import const
import os
import oracledb

# username、passwordなどを設定する
password = os.environ["PYTHON_PASSWORD"]
username = os.environ["PYTHON_USERNAME"]
tns = os.environ["PYTHON_CONNECTSTRING"]


def search_type_check(tags, keys):
    # key×tag検索
    if keys and tags:
        return 1
    # tagのみ検索
    elif tags:
        return 2
    # keyのみ検索
    elif keys:
        return 3
    # 全件検索
    else:
        return 4


def search(tags, keys):
    with oracledb.connect(user=username, password=password, dsn=tns) as connection:
        with connection.cursor() as cursor:
            search_type = search_type_check(tags, keys)
            default_sql = const.default_sql
            match search_type:
                case 1:
                    sql_sentence = (
                        default_sql
                        + "WHERE ("
                        + create_sql_tag(tags)
                        + ") AND ("
                        + create_sql_key(keys)
                        + ")"
                    )
                case 2:
                    sql_sentence = default_sql + "WHERE " + create_sql_tag(tags)
                case 3:
                    sql_sentence = default_sql + "WHERE " + create_sql_key(keys)
                case 4:
                    sql_sentence = default_sql

            # SQLの実行
            cursor.execute(sql_sentence)
            # 結果を格納
            result = cursor.fetchall()
            return result


# 複数検索を行うSQLを作成
def create_sql_tag(tags):
    conditions = [
        f"""(custom_translate_like(hankaku_to_zenkaku(tag),hankaku_to_zenkaku('{tag}')) = 1)"""
        for tag in tags
    ]
    sql = " AND ".join(conditions)
    return sql


# 複数検索を行うSQLを作成
def create_sql_key(keys):
    conditions = [
        f"""(custom_translate_like(hankaku_to_zenkaku(notice_id),hankaku_to_zenkaku('{key}')) = 1
        OR custom_translate_like(hankaku_to_zenkaku(title),hankaku_to_zenkaku('{key}')) = 1
        OR custom_translate_like(hankaku_to_zenkaku(content),hankaku_to_zenkaku('{key}')) = 1
        OR custom_translate_like(hankaku_to_zenkaku(user_name),hankaku_to_zenkaku('{key}')) = 1
        OR custom_translate_like(hankaku_to_zenkaku(tag),hankaku_to_zenkaku('{key}')) = 1)"""
        for key in keys
    ]
    sql = " AND ".join(conditions)
    return sql