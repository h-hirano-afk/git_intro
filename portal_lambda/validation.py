# listかどうかチェック
def list_check(value):
    if not isinstance(value, list):
        raise ValueError


def str_check(tags,keys):
    check_tag = [
        tag for tag in tags if not isinstance(tag, str) or len(tag) > 30 or tag == ""
    ]
    check_key = [
        key for key in keys if not isinstance(key, str) or len(key) > 40 or key == ""
    ]
    if check_tag or check_key:
        raise ValueError


def validation_check(tags, keys):
    # listかチェック
    list_check(tags)
    list_check(keys)

    # strかチェック
    str_check(tags,keys)
