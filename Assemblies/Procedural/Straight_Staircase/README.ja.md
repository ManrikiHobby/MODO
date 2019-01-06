# Straight_Staircase
 直進階段をプロシージャルに生成するアセンブリ。

# 対応MODOバージョン  
MODO 12.2 v1 以降 

# ファイル一覧
|ファイル名|内容|
|:-|:-|
|Straight_Staircase.lxp|アセンブリファイル

# 使用方法
(1) [こちら](https://github.com/ManrikiHobby/MODOAssets/raw/master/Assemblies/Procedural/Straight_Staircase/Straight_Staircase.lxp)からアセンブリファイル(*.lxp)をダウンロードし、MODOのコンテンツフォルダに保存する。 保存先は以下を推奨。  

          (コンテンツフォルダ)\Assets\Assemblies


(2) MODOを起動し、アイテムツリーの「アイテム追加」ボタンを押下する。

(3) メニューから、(1)のアセンブリをスケマティックビューにドラッグ＆ドロップする。

(4) アイテムツリーに"Staircase"アイテムが追加されるので、プロパティの「アセンブリチャンネル」で数値を調整する。

**※注意 作成したメッシュをダイレクトモデリングで編集したり、アイテムモードで動かすには、  
「メッシュのフリーズ（確定）」が必要になります。  詳細は[メッシュの確定方法](#メッシュの確定方法)を参照。**

# チャンネル一覧
|チャンネル名|意味|
|:-|-|
|Count |階段の段数|
|Tread |踏み面の奥行き|
|Riser |蹴上げの厚さ|
|Width|段幅|
|Overlap |踏み面の重なり(負値可)|
|Spacing |蹴上げの隙間|
|Create stringers |側板を作成する|
|Stringer width |側板の幅|
|Create handrail |手擦りを作成する|
|Handrail height|手擦りの高さ|
|Grip width|手擦り握りの幅|
|Grip height|手擦り握りの高さ|
|Bar width|手擦り軸の太さ|
|Bar spacing (by step)|何段おきに手擦り軸を配置するか|
|Extension (lower)|手擦り延長(下段)|
|Extension (upper)|手擦り延長(上段)|
|Ground|接地する|
|Flatten|段差を無くす(橋の様な形状になる)|

# 作例
(1) デフォルト    
![straightstairs_default](https://user-images.githubusercontent.com/40119223/50732404-0fea9100-11be-11e9-8758-4fe83829a13e.jpg)

(2) 手擦り付き  
![straightstairs_handrail](https://user-images.githubusercontent.com/40119223/50732337-85556200-11bc-11e9-8bbe-c3e8f042cb88.jpg)
* Create handrail = ON  

(3) 接地  
![StraightStairs_Grounded](https://user-images.githubusercontent.com/40119223/50732986-17af3300-11c8-11e9-987c-7badea799136.jpg)

* Ground = ON

(4) 橋状  
![straightstairs_flattened](https://user-images.githubusercontent.com/40119223/50732991-2a296c80-11c8-11e9-8a89-af0a07c712df.jpg)
* Flatten = ON
* Spacing = -2cm (負値)

# メッシュの確定方法
(1) アイテムツリーでメッシュアイテム("Staircase")を右クリックし、コンテキストメニューから以下を実行。

        メッシュオペレーションのフリーズ > フリーズ

**※ (2)以降は必須ではありません。 不要なチャンネルが残って気持ち悪いようでしたら実施して下さい。**

(2) スケマティックビューでアセンブリ("Straight staircase")をダブルクリックして中に入る。

(3) スケマティックビュー上で右ドラッグし、すべてのノードを選択する。

(4) 右クリックし、コンテキストメニューから「ノードの除去」を実行し、すべてのノードを削除。

(5) 残った"アセンブリ入力"ノードを右クリックし、コンテキストメニューから「削除」を実行。
