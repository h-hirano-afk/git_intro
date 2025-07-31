import validation
import logic
import fsportal_utils
import oracledb
import const
import master_check
import exception
import json
# .NotFoundException as NotFoundException


def lambda_handler(event, context):
    try:
        event = json.loads(event["body"])
        tags = event["tag"]
        keys = event["key"]
        # バリデーションチェック
        validation.validation_check(tags, keys)
        # マスターチェック
        master_check.master_check(tags)
    
        # 検索
        result = logic.search(tags, keys)
        # # フォーマット
        formated_result = fsportal_utils.type_format(result)
    
        return formated_result

    except ValueError:
        return const.error_result400_1
    except exception.NotFoundException:
        return const.error_result400_2
    except oracledb.Error:
        return const.error_result500_1
    except Exception:
        return const.error_result500_2