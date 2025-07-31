from fastapi import FastAPI
from typing import List
import json
app = FastAPI()
# JSONファイルからレスポンスデータを読み込む
with open('responses.json', 'r', encoding='utf-8') as f:
    responses = json.load(f)
@app.get("/fsportal_dev_apistage/detail")
async def detail(key: List[str] = None, tag: List[str] = None):
    # リクエストパラメータに基づいてレスポンスを選択
    if key == ["FS Portal"] and tag == ["テスト", "こんにちは"]:
        response = responses["test_case_1"]
    elif key == ["Another Key"] and tag == ["サンプル", "デモ"]:
        response = responses["test_case_2"]
    else:
        response = {"message": "No matching test case found"}
    return response
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)