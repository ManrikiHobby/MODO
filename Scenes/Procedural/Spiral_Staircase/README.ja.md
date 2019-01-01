# Spiral_Staircase_Assembly
 階段をプロシージャルに生成するアセンブリ。

# 対応MODOバージョン  
MODO 12.2 v1 以降 

# ファイル概要
|ファイル名|内容|
|:-|:-|
|Spiral_Staircase_Assembly.lxo|アセンブリ作成用のシーンファイル。

# チャンネル一覧
|チャンネル名|意味|
|:-|-|
|Height|階段全体の高さ|
|Inner radius|内半径|
|Turns|巻き数(小数可)|
|Clockwise|右回りにする|
|Count|階段の段数|
|Width|階段の段幅|
|Spacing|蹴上げの隙間|
|Segments|段の側面のポリゴン数(多いほど扇形に近くなる)|
|Rectangulate|矩形度|
|Create center pole|支柱を作成する|
|Side segments|支柱の側面のポリゴン数(多いほど円筒に近くなる)|
|Create inner handrail|手擦り(内側)を作成する|
|Create outer handrail|手擦り(外側)を作成する|
|Handrail height|手擦りの高さ|
|Shaft width|手擦り軸の太さ|
|Shaft side segments|手擦り軸の側面のポリゴン数(多いほど円筒に近くなる)|
|Shaft inner margin (tread)|手擦り軸を内側に寄せる(進行方向)|
|Shaft inner margin (width)|手擦り軸を内側に寄せる(幅方向)|
|Grip width|手擦り握りの幅|
|Grip height|手擦り握りの高さ|

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
