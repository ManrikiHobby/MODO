# Straight_Staircase_Assembly
 階段をプロシージャルに生成するアセンブリ。

# 対応MODOバージョン  
MODO 12.2 v1 以降 

# ファイル概要
|ファイル名|内容|
|:-|:-|
|Straight_Staircase_Assembly.lxo|アセンブリ作成用のシーンファイル。

# チャンネル一覧
|チャンネル名|意味|
|:-|-|
|Count |階段の段数|
|Tread |踏み面の奥行き|
|Riser |蹴上げの厚さ|
|Spacing |蹴上げの隙間|
|Overlap |踏み面の重なり(負値可)|
|Create stringers |側板を作成する|
|Stringer width |側板の幅|
|Create handrail |手擦りを作成する|
|Handrail height|手擦りの高さ|
|Grip width|手擦り握りの幅|
|Grip height|手擦り握りの高さ|
|Bar width|手擦り軸の太さ|
|Extension (lower)|手擦り延長(下段)|
|Extension (upper)|手擦り延長(上段)|
|Ground|接地する|
|Flatten|段差を無くす(橋の様な形状になる)|

# アセンブリプリセット作成方法
(1) スケマティックビューでアセンブリを右クリックし、「アセンブリプリセットを保存」を選択。

(2) 警告メッセージが表示されたら[OK]で進み、以下の保存先に任意の名称で保存。

          (コンテンツフォルダ)\Assets\Assemblies

# プロシージャルアイテム(Mesh Operation)作成方法
### [注意] MODO12.2 v1時点 プロシージャルアイテムを使用するとメモリリークが発生します

(1) 以下の手順で、アセンブリ編集用のメッシュを不可視にする。  
アセンブリ中のMesh("Staircase")を選択し、アイテムツリーのプロパティで、以下のように設定する。

       ・メッシュ > レンダー　⇒ 「いいえ」
       ・表示 > 可視　　⇒ 「いいえ(子アイテム非表示)」

(2) スケマティックビューからアセンブリを右クリックし、「アイテムへ折り畳み」を選択。

(3) 「アセンブリをアイテムへ」画面で、以下のように設定し、[OK]。
       
       ・タイプ　⇒ 「Mesh Operation」
       ・ソース　⇒ 「Merge Meshes」

(4) 「ファイル」メニュー > アセンブリプリセットの保存 で、作成したアイテムを保存する。  
       保存先を以下のようにすると、アイテムリストの「アイテム追加」で選べるようになる。

          (コンテンツフォルダ)\Assets\Assemblies\Aliases\Mesh Operations
