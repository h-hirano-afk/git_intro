import datetime
import const
import json

def type_format(db_responce):
    # フォーマットを整え、1行のデータを全体に追加
    result = [format(rows) for rows in db_responce]
    # 検索数カウント
    result_count = len(result)
    # 結果をjson化
    data_list = [dict(zip(const.db_col, row)) for row in result]
    print(f"検索件数：{result_count}")
    
    # レスポンスデータ作成
    res = mkresponse(data_list)
    return res


def format(rows):
    result_row = [
        ""
        if row == "NULL"
        else [""]
        if row is None and (index == 7 or index == 8)
        else ""
        if row is None
        else str(row)
        if isinstance(row, int)
        else row.strftime("%Y/%m/%d")
        if isinstance(row, datetime.datetime)
        else list(dict.fromkeys(row.split(",")))
        if (index == 7 or index == 8) and isinstance(row, str)
        else row
        for index, row in enumerate(rows)
    ]
    return result_row
    
    
# 引数にJsonデータを入れると、APIレスポンスに変換して返す
def mkresponse(json_data):
    response = {
        "statuscode": 200,
        "statusdescription": "200 OK",
        "headers": {"Content-Type": "application/json; charset=utf-8"},
    }
    response["body"] = json.dumps(json_data, ensure_ascii=False)

    return response