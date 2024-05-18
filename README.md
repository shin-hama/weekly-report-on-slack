# Weekly Report Bot

Slack に流れてくるアクティビティを要約して週報を作成する Bot

## 作り方ノート

### Slack App を作成する

1. [Slack API](https://api.slack.com/) にアクセスして、新しい App を作成する
2. App に必要な権限を設定する
3. App のトークンを取得する
4. App をチャンネルに追加する
   1. メッセージ履歴を取得するためには、チャンネルに追加する必要があったため
5. メッセージを取得して要約する部分を実装する

### 権限の設定

#### Channel 情報の取得

メッセージ履歴を取得するのには Channel ID が必要。
bot で Channel 一覧を取得するために以下の API と権限が必要。

- api: [conversations.list](https://api.slack.com/methods/conversations.list)
- permission: `channels:read`, `groups:read`, `im:read`, `mpim:read`

#### メッセージ履歴の取得

要約するためのメッセージ履歴を取得するために以下の API と権限が必要。

- api: [conversations.history](https://api.slack.com/methods/conversations.history)
- permission: `channels:history`, `groups:history`, `im:history`, `mpim:history`
