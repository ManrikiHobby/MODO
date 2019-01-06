# Spiral_Staircase
 らせん階段をプロシージャルに生成するアセンブリ。

# 対応MODOバージョン  
MODO 12.2 v1 以降 

# ファイル一覧
|ファイル名|内容|
|:-|:-|
|Spiral_Staircase.lxp|アセンブリファイル

# 使用方法
(1) [こちら](https://github.com/ManrikiHobby/MODOAssets/raw/master/Assemblies/Procedural/Spiral_Staircase/Spiral_Staircase.lxp)からアセンブリファイル(*.lxp)をダウンロードし、  MODOのコンテンツフォルダに保存する。 保存先は以下を推奨。  

        (コンテンツフォルダ)\Assets\Assemblies


(2) MODOを起動し、アイテムツリーの「アイテム追加」ボタンを押下する。

(3) メニューから、(1)のアセンブリをスケマティックビューにドラッグ＆ドロップする。

(4) アイテムツリーに"Staircase"アイテムが追加されるので、プロパティの「アセンブリチャンネル」で数値を調整する。

**※注意 作成したメッシュをダイレクトモデリングで編集したり、アイテムモードで動かすには、  
「メッシュのフリーズ（確定）」が必要になります。  詳細は[メッシュの確定方法](#メッシュの確定方法)を参照。**

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
|Rectangulate|段の矩形度(%)|
|Start angle offset|段の扇形の開始角度オフセット|
|End angle offset|段の扇形の終了角度オフセット|
|Create center pole|支柱を作成する|
|Side segments|支柱の側面のポリゴン数(多いほど円筒に近くなる)|
|Create inner handrail|手擦り(内側)を作成する|
|Create outer handrail|手擦り(外側)を作成する|
|Handrail height|手擦りの高さ|
|Grip width|手擦り握りの幅|
|Grip height|手擦り握りの高さ|
|Shaft width|手擦り軸の太さ|
|Shaft side segments|手擦り軸の側面のポリゴン数(多いほど円筒に近くなる)|
|Shaft inner margin (tread)|手擦り軸を内側に寄せる(進行方向)|
|Shaft inner margin (width)|手擦り軸を内側に寄せる(幅方向)|
|Ground the 1st floor|接地する(1階分)|

# 作例
(1) デフォルト    
![spiralstairs_default](https://user-images.githubusercontent.com/40119223/50734592-acc02500-11e4-11e9-9145-c8014def5228.jpg)

(2) 支柱無し／両手擦り (聖ヨゼフの階段)  
![spiralstairs_stjoseph1](https://user-images.githubusercontent.com/40119223/50734605-cb262080-11e4-11e9-9aac-c0321d465465.jpg)
![spiralstairs_stjoseph2](https://user-images.githubusercontent.com/40119223/50734622-f446b100-11e4-11e9-8a2f-ef9ae78a2549.jpg)

* Create center pole = OFF  
* Create inner handrail = ON

(3) 回り階段  
![spiralstairs_quarter](https://user-images.githubusercontent.com/40119223/50734634-150f0680-11e5-11e9-8c70-405353c7fd46.jpg)
* Inner radius = 3m
* Turns = 0.25
* Clockwise = ON
* Count = 12
* Width = 4m
* Segments = 8
* Start angle offset = 2°
* Grip width = 20cm
* Grip height = 20cm
* Shaft width = 15cm
* Shaft side segments = 16
* Shaft inner margin (tread) = 2.5°
* Shaft inner margin (width) = 25cm
* Ground the 1st floor = ON

(4) 塔の外階段  
![spiralstairs_tower](https://user-images.githubusercontent.com/40119223/50734649-42f44b00-11e5-11e9-9e4d-d759f6168667.jpg)
* Height = 30m
* Inner radius = 8m
* Turns = 5
* Count = 96
* Width = 1m
* Spacing = 1mm(最小)
* End angle offset = -2.4°

# メッシュの確定方法
(1) アイテムツリーでメッシュアイテム("Staircase")を右クリックし、コンテキストメニューから以下を実行。

        メッシュオペレーションのフリーズ > フリーズ

**※ (2)以降は必須ではありません。 不要なチャンネルが残って気持ち悪いようでしたら実施して下さい。**

(2) スケマティックビューでアセンブリ("Spiral staircase")をダブルクリックして中に入る。

(3) スケマティックビュー上で右ドラッグし、すべてのノードを選択する。

(4) 右クリックし、コンテキストメニューから「ノードの除去」を実行し、すべてのノードを削除。

(5) 残った"アセンブリ入力"ノードを右クリックし、コンテキストメニューから「削除」を実行。
