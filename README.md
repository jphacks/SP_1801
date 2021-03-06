 # 共同貯金箱アプリ「チョキンシ.アイ」

[![Product Name](TyokinAI.png)](https://youtu.be/81z42RVCK9k)

## 製品概要
### 貯金箱☓Tech
  
### 背景（製品開発のきっかけ、課題等）
####  お金がらみでトラブルに
ゼミやオフィスなど複数人で利用する場所において、共同で使用しているものは誰が購入するか、その配分はどうするかなどで言い争いが起こることがあります。そこで、チームで共同で貯めたお金を管理をしてくれるアプリ「チョキンシ.アイ」を作成しました。
  
#### 開発のきっかけ
私の研究室にはバリスタが置いてあります。バリスタの横には貯金箱が設置してあり、バリスタでコーヒーを飲む際は「お気持ち」と称して貯金箱に好きなだけお金を投げます。そして、週末に貯金箱を開封し、担当の者がそのお金でバリスタに使う豆を買い足しに行きます。買い足す豆の種類は貯金箱に入っていた金額に応じて変化し、多めにお金が入っているとミルクや砂糖なども購入します。しかし、貯金箱に入ったお金の集計や、購入などの処理を手動で行う必要があり、毎週となるとそれなりに時間を浪費します。そこで私達は考えました。購入も集計も自動で行う方法はないかと。その解決策が「チョキンシ.アイ」なのです。  
  
### 製品説明（具体的な製品の説明）
#### 貯金・集計・購入
ゼミやオフィス、サークルなどのコミュニティでの使用を想定している共同貯金箱アプリ。各々好きな額を投じ、一定期間ごとに集計。あらかじめ設定しておいた皆で使えるもの（コーヒー豆など）を通販で自動購入してくれる。
  
#### あらゆる小規模コミュニティで日常的に利用可能
チョキンシ.アイの使用場所は研究室に留まりません。サークルでの物品購入、友達同士での約束など、様々なコミュニティにおける日常的なイベントで利用することが可能です。
  
### 特長
#### 1. 投じた額の大きさによって優待（配分の変化など）がある
#### 2. 貯金額に応じて購入するもののグレードが変化
#### 3. 定期的に集計して、設定した商品を自動で購入してくれる（デモでは週一）
  
### 解決出来ること
#### チョキンシ.アイはあなたを口約束から開放する
チョキンシ.アイは投じた金額や得られる配分などの情報が見ることができます。商品を自動購入してくれるため、買い忘れを防ぐことができます。もう、お金絡みで友達と揉めることはありません。
  
### 今後の展望
* APIとの連携改善
* 実際に運用できるように改善（購入品の選択や自動購入の値をクライアント側から設定できるようにする）
* 友人との金銭の貸し借りを円滑に管理できるように改良

## 開発内容・開発技術
### 活用した技術
#### API・データ
今回スポンサーから提供されたAPI、製品などの外部技術があれば記述をして下さい。

* 不使用

#### フレームワーク・ライブラリ・モジュール
* Python3
* Swift4
* selenium
* Flask

#### デバイス
* MAC
* iPhone

### 研究内容・事前開発プロダクト（任意）
ご自身やチームの研究内容や、事前に持ち込みをしたプロダクトがある場合は、こちらに実績なども含め記載をして下さい。

* 事前開発なし


### 独自開発技術（Hack Dayで開発したもの）
#### 2日間に開発した独自の機能・技術
* [Swift Project](https://github.com/jphacks/SP_1801/tree/Swift)
：クライアントサイド
* [Python Project](https://github.com/jphacks/SP_1801/tree/tamai_python)
：サーバサイド
