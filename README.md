# Shop API 仕様書

ライブラリを記載した`requirements`ファイルを作成。
```shell
pip freeze > requirements.txt
```

## 概要
シンプルなショップアイテム管理のためのAPI仕様書です。

## ベースURL
```
http://localhost:8000
```

## エンドポイント一覧

### 1. 全アイテムの取得

#### リクエスト
- **メソッド**: GET
- **パス**: `/items`

#### レスポンス
- **ステータスコード**: 200 OK
- **レスポンス形式**: JSON
```json
[
  {
    "id": 1,
    "item": "Apple"
  },
  {
    "id": 2,
    "item": "Banana"
  },
  {
    "id": 3,
    "item": "Orange"
  }
]
```

### 2. 特定アイテムの取得

#### リクエスト
- **メソッド**: GET
- **パス**: `/items/{item_id}`
- **パスパラメータ**:
  - `item_id`: アイテムのID（整数）

#### レスポンス
- **成功時**
  - **ステータスコード**: 200 OK
  - **レスポンス形式**: JSON
```json
{
  "id": 1,
  "item": "Apple"
}
```
- **失敗時**
  - **ステータスコード**: 404 Not Found
  - **レスポンス形式**: JSON
```json
{
  "detail": "Item not found"
}
```

### 3. 新規アイテムの作成

#### リクエスト
- **メソッド**: POST
- **パス**: `/items`
- **Content-Type**: `application/json`
- **リクエストボディ**: 商品名（文字列）
```json
"Grape"
```

#### レスポンス
- **成功時**
  - **ステータスコード**: 200 OK
  - **レスポンス形式**: JSON
```json
{
  "id": 4,
  "item": "Grape"
}
```

### 4. アイテムの削除

#### リクエスト
- **メソッド**: DELETE
- **パス**: `/items/{item_id}`
- **パスパラメータ**:
  - `item_id`: アイテムのID（整数）

#### レスポンス
- **成功時**
  - **ステータスコード**: 200 OK
  - **レスポンス形式**: JSON
```json
{
  "message": "Item 1 deleted"
}
```
- **失敗時**
  - **ステータスコード**: 404 Not Found
  - **レスポンス形式**: JSON
```json
{
  "detail": "Item not found"
}
```

## 備考
- サーバー起動時に3つのデフォルトアイテムが登録されています
- データはメモリ上に保存されるため、サーバー再起動時にリセットされます
- IDは自動的にインクリメントされ、一度削除されたIDは再利用されません

## エラーレスポンス
全てのエンドポイントで、エラー発生時は以下の形式でレスポンスが返されます：
```json
{
  "detail": "エラーメッセージ"
}
```