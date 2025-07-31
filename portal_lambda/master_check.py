import os
import oracledb
import const
import logic
import exception

# username、passwordなどを設定する
password = os.environ["PYTHON_PASSWORD"]
username = os.environ["PYTHON_USERNAME"]
tns = os.environ["PYTHON_CONNECTSTRING"]


def master_check(tags):
    with oracledb.connect(user=username, password=password, dsn=tns) as connection:
        with connection.cursor() as cursor:
            for tag in tags:
                sql_sentence = const.master_sql + logic.create_sql_tag(tag)
                cursor.execute(sql_sentence)
                # 結果を格納
                if not cursor.fetchall():
                    raise exception.NotFoundException 
                    
                    
                    