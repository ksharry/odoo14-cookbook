## 修改自己程式備註的習慣，第四章後程式碼都有備註以下的課程紀錄點。
## 每章的步驟說明:https://alanhou.org/odoo14-cookbook/
## 參考github1:https://github.com/alanhou/odoo14-cookbook/tree/main/
## 參考github2:https://github.com/PacktPublishing/Odoo-14-Development-Cookbook-Fourth-Edition
## 註:如果裝不起來，請重啟伺服器後再安裝。

#### 第一章 安裝ODOO的建置方式

#### 第二章 第三方模組的安裝與第二套環境標準化方式

#### 第三章 第三方模組新增架構說明

#### 第四章 模型的應用調整方式
1. 模型
2. 新增欄位
3. 小數位數
4. 貨幣字段
5. 關聯欄位m2o
6. hierarchy_model
7. constraints
8. compute_fileds
9. related_fields
10. reference_fields
11. 第一種繼承model_inheritance
12. 第二種繼承copy_model
13. 第三種代理繼承delegation_inheritance
14. abstract_models

#### 第五章 CRUD與其他應用服務方式說明
1. 定義模型方法及使用API裝飾器
2. 錯誤的訊息
3. 獲取其他模型的空紀錄
4. 新建紀錄
5. 更新
6. 搜尋紀錄
8. 過濾紀錄
9. 搜尋記錄關聯
10. 搜尋排序
11. 繼承模型中定義的業務邏輯
12. 繼承原生，權限不能修改欄位
13. 自定義搜尋方式
14. read_group
![Alt text](https://imgur.com/KSy3hih.png)
![Alt text](https://imgur.com/MYxPsmH.png)

#### 第六章 管理模組的數據(用4-6續編)
1. 使用命名ID與外部空間
2. 使用XML預載入數據
   + demo.xml 載入DEMO時，才有資料
   + data.xml 一開始安裝就有
3. 使用noupdate和forcecreate標記
   + noupdate 如果為1，載入模組時不更新資料
   + forcecreate 如果為0，刪除後就不更新。
4. 使用CSV載入資料
5. 插件更新與數據遷移(pre,post)
6. 從XML文件中刪除紀錄
7. 在XML文件中使用參數
![Alt text](https://imgur.com/VBt7UDV.png)
![Alt text](https://imgur.com/qmHYwkj.png)

#### 第七章 調適模式
1. --dev=reload,xml 修改python與xml會自動重啟
2. 寫LOG來進行紀錄，擴充--log-web是html:debug --log-level=error
3. 使用Odoo shell來交互調用方法  ./odoo-bin shell -d odoo-test -c myodoo.cfg --log-level=error
   + product = env['product.product']
   + location_stock = env.ref('stock.stock_location_stock')
   + product.export_stock_level(location_stock)  #要先建立目錄並且sudo chown root:wkc -Rf /srv
   + env.cr.commit()
   + cat /srv/exports/stock_level.txt
4. 使用Python調試器來追踪方法執行
   + import pdb; pdb.set_trace()  #debug,設中斷
   + 指令:args,next,list,p product,!fname(給變數),c,step(進入)
   + pdb.runcall(product.export_stock_level, location_stock)   #shell 設定中斷
5. 理解調試模式選項(開發著模式/技術)
![Alt text](https://imgur.com/At8AQXl.png)

#### 第八章 高級服務端開發技巧
1. 新增租借功能-base_suspend_security 可以將追蹤記錄原帳號
2. 新增租借的按鈕
3. 新增SQL執行的按鈕。
4. wizard-編寫批次租借/還書功能  
5. onchange(無程式)
6. 歸還所有的書
7. compute_onchange(無程式)
8. 新增統計圖表
9. 新增設定是否自行租借書籍
   + 在my_library/security/groups.xml文件中添加一個新分組
   + 通過繼承res.config.settings模型來添加新字段：
   + 通過xpath在已有的settings視圖中添加這一字段
   + 為Settings添加一個菜單及一些動作
   + 修改圖書表單視圖中的按鈕燕添加一個my_library.group_self_borrow分組
10. 設定安裝時自動載入資料post_init_hook功能
   + pre_init_hook：這個鉤子會在開始安裝模塊時觸發。它與post_init_hook正好相反，會在當前模塊安裝前觸發。
   + uninstall_hook：這個鉤子會在你卸載該模塊時觸發。它多用於模塊需要垃圾回收機制時
![Alt text](https://imgur.com/ZNqbXf3.png)
![Alt text](https://imgur.com/LNHAEKz.png)
![Alt text](https://imgur.com/8IVdvjc.png)
![Alt text](https://imgur.com/5rfq3OF.png)
![Alt text](https://imgur.com/tGhBxmJ.png)
![Alt text](https://imgur.com/YLSphly.png)

#### 第九章 後端式圖
1. 新增MENU跟窗口動作-act_window or record建立
2. 打開指定視圖動作
3. 表單新增按鈕連接客戶
4. 表單新增按鈕連接標籤
5. 表單動作傳遞-context修改語言
6. 搜尋透過domain
7. list_view
8. 搜尋VIEW
9. 新增側邊攔
10. 繼承
11. 順序調整
12. 動態屬性
13. 內鑲視圖
14. 文件預讀
15. 看板
16. 專案
17. 日曆
18. 圖表
19. COHORT(企業版)
20. 儀錶板(企業版)
21. 甘特(企業版)
22. 活動
23. 地圖(企業版)
![Alt text](https://imgur.com/g8qxF2Z.png)
![Alt text](https://imgur.com/0ZcjFhj.png)
![Alt text](https://imgur.com/LbVVTQo.png)


#### 第十章 訪問權
  >  ODOO12 後新增ACL(訪問權)，僅用於普通模組，非抽象與臨時使用。
1. 創建訪問組.security/group.xml   manager/user
2. 增加訪問權ACL.security/ir.model.access.csv   1,1,1,1
3. 新增欄位訪問，透過group進行  private_note
4. 新增記錄規則,security/security_rules.xml，透過ORM撰寫判定欄位是否能讀取。is_public
5. 透過安全組啟用功能，security/groups.xml，新增透過設定，判斷是否能讀取欄位，release_date
6. 用超級用戶進行訪問，透過按鈕進行sudo.write進行寫入。
7. 根據訪問組來隱藏MENU,在view上寫group進行設定。
![Alt text](https://imgur.com/zGeauns.png)
![Alt text](https://imgur.com/9EMoBXW.png)

#### 第十一章 國際化
1. 安裝語言及配置用戶首選項  Settings > Translations > Load a Translation
2. 配置語言相關設置   Settings > Translations > Languages
3. 通過網頁客戶端在用戶界面翻譯文本  Settings > Users & Companies > Groups
4. 將翻譯字符串導出到文件  Translations > Import/Export > Export Translation
5. 使用gettext工具來簡化翻譯
6. 將翻譯文件導入到Odoo中
7. 對網站修改自定義URL語言代碼 Settings > Translations > Languages

#### 第十二章 自動化、工作留、EMAIL、列印
1. 新增動態紀錄(狀態更新)
2. 管理看板階段
3. 看板新增快速新增樣板
4. 看板新增優線序與顏色
5. 看板新增進度條
6. 新增伺服器動作(odoo/tools/safe_eval.py)，可由專案下自動更新優先與到期日
7. 使用PYTHON代碼進行到期提醒
8. 
![Alt text](https://imgur.com/wRLNQcw.png)
![Alt text](https://imgur.com/eY7P3gU.png)
![Alt text](https://imgur.com/N2lnh4M.png)
![Alt text](https://imgur.com/3OxEH8l.png)

#### 第十三章 WEB服務端開發
  >  Odoo網頁請求都是由Python庫werkzeug來進行處理的，

0. 工作流程:
   + 伺服器建立socket，監聽port，等待client 連線
   + 當請求過來時，server解析client msg放到環境變數environ中，並呼叫繫結的handler來處理
   + handler解析這個http請求，將請求訊息例如method、path等放到environ中
   + wsgi handler再將一些server端訊息也放到environ中，最後server msg，client msg，以及本次請求msg 全部都儲存到了環境變數envrion中；
   + wsgi handler呼叫註冊的wsgi app，並將envrion和回撥函式傳給wsgi app
   + wsgi app將reponse header/status/body回傳給wsgi handler
   + handler 通過socket將response msg返回到client
1. 讓路徑在網絡中可訪問
2. 限制線上路徑的訪問
3. 使用傳遞給handler的參數
4. 修改已有handler
5. 提供對靜態資源的訪問
6. 
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.1.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.21.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.3.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.4.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.5.png?raw=true)

#### 第十四章 CMS網站開發 
  >  odoo12以後使用Bootstrap 4(SCSS)，12以前為Bootstrap 3(LESS)
0. 資源包:任務是將所有JavaScript和CSS合併為一個文件
   + web.assets_common：這個資源包包含對所有應用通用的基本工具文件，如JQurey, Underscore.js, FontAwesome等等。此資源包用於前台（網站）、後台、銷售點（POS）和報表等處。這一通用資源在Odoo的幾乎所有地方加載。它也包含用於Odoo模塊系統的boot.js文件。
   + web.assets_backend：這一資源包在Odoo的後台中使用（ERP部分）。它包含所有與web客戶端、視圖、字段微件、動作管理器等相關的代碼。
   + web.assets_frontend或website.assets_frontend:：這一資源包用於Odoo的前台（網站部分）。它包含所有與網站端應用相關的代碼，如電商、博客、線上活動、論壇和在線聊天等等。注意這個資源包不包含與網站編輯和拖拽功能（網站構造器）相關的代碼。這背後的原因是我們不希望在公眾使用網站時加載編輯器資源。
   + web_editor.assets_editor和web_editor.summernote：這個資源包包含與網站編輯小組件選項及拖拽功能（網站構造器）相關的代碼。它僅在用戶對網站具有編輯權限時才進行加載。也用於批量郵件設計工具。
   + web.report_assets_common：QWeb報表僅僅是通過HTML生成的PDF文件。這一資源在報表佈局中進行加載。
0. Odoo通過AssetsBundle類管理其靜態資源，位於/odoo/addons/base/models/assetsbundle.py。 AssetBundle不僅合併多個文件，也打包了各種功能。以下是其所提供的功能列表：
   + 合併多個JavaScript和CSS文件。
   + 通過從文件內容中刪除註釋、多餘空格及回車換行來最小化JavaScript和CSS文件。刪除這一額外數據會減小靜態資源的大小並提升頁面加載速度。
   + 擁有對CSS預處理器的內置支持，如SASS和LESS。這表示我們可以添加SCSS和LESS文件，它們會自動編譯並添加到資源包中。
1. 管理靜態資源
   + controllers/main.py抓資料
   + views/templates.xml中添加最小化模板
   + website.layout中，通过oe_structure类添加可拖放元素
   + 代码块加入到website.layout中以显示图书的信息
   + website.layout中添加一个不可编辑元素
2. 為網站擴展CSS和JavaScript(進階)
3. 創建或更改模板 – QWeb
   + 在controllers/main.py中添加控制器提供图书列表服务
   + 在views/templates.xml中添加最小化模板
   + 在website.layout中，通过oe_structure类添加可拖放元素
   + 将该代码块加入到website.layout中以显示图书的信息
   + 在website.layout中添加一个不可编辑元素
4. 管理動態路由
   + 在main.py中为图书详情添加一个新路径
   + 在templates.xml中为图书详情添加一个新模板
   + 在图书列表模板中添加一个按钮如下
5. 為用戶提供靜態小組件
   + 添加文件views/snippets.xml
   + 在views/snippets.xml中添加小组
   + 在小组件列表中列出模板
6. 為用戶提供動態小組件
   + 在views/snippets.xml中添加小组件的给定QWeb模板
   + 注册小组件并添加选项来修改小组件的行为
   + 然后在图书小组件中添加组件选项
   + 新增文件/static/src/js/snippets.js并添加代码来渲染动态小组件
   + 添加public微件来动态渲染图书小组件
   + 在模块中添加以上JavaScript文件
7. 獲取網站用戶的輸入
   + **POST是只有送出資訊
   + sudo()權限新增資料
   + csrf_token避免偽照攻擊
8. 管理搜索引擎優化（SEO）選項
   + 每本圖書/main_object傳遞對象
   + 不僅TDK（Title, Description, Keywords）的優化
9. 管理網站的站點地圖
   + Technical > Database Structure > Attachments / sitemap-1.xml  刪除後可再生成
   + slug用于根据记录名生成整洁
   + sitemap_qs2dom用于根据路由和查询字符串生成作用域
10. 獲取訪客的國家信息
    + ./odoo-bin -c config_file --geoip-db=location_of_geoip_DB
    + ./odoo-bin -c main.cfg --geoip-db=~/GeoLite2-Country.mmdb
    + 限制國家讀取資訊。
11. 追踪營銷活動
    + 異常改main.py 的domain
12. 管理多站點
13. 重定向老URL
14. 網站相關記錄的發布管理
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.0.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.2.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.3.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.4.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.5.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.6.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.7.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.8.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch14.9.png?raw=true)

#### 第十五章 網頁客戶端開發
  >  Odoo網頁請求都是由Python庫werkzeug來進行處理的，

0. 文件物件模型（Document Object Model, DOM）是 HTML、XML 和 SVG 文件的程式介面。微件的生命週期:
   + init()：這是微件構造函數。用於進行初始化。在初始化微件時，會先調用該方法。
   + willStart()：這個方法在微件初始化以及在DOM中添加元素的過程中調用。它用於初始化異步數據到微件中。它還會返回一個延遲對象，只需要通過super()方法調用即可獲取。
   + start()：該方法在完成微件渲染且尚未添加到DOM中時調用。這非常有助於渲染後任務，返回一個延遲對象。可以在this.$el中訪問已渲染的元素。
   + destroy()：該方法在微件銷毀時調用。
1. 創建自定義微件
   + static/src/js/field_widget.js，导入了AbstractField和fieldRegistry。
   + static/src/scss/field_widget.scss中添加一些SCSS
   + views/templates.xml后台资源中注册这两个文件
2. 使用客戶端QWeb模板
   + 在js寫的模組化導入web.core并将对qweb的引用提取为一个变量
   + 添加模板文件static/src/xml/qweb_template.xml
3. 向服務端做RPC調用(遠端程序呼叫：Remote Procedure Call)
   + JS添加willStart方法并在RPC调用中设置colorGroupData
   + QWEB上調用內容
4. 新建一個視圖
   + modle:新增ir.ui.view/ir.actions.act_window.view/model
   + /static/src/js/m2m_group_model.js
   + /static/src/js/m2m_group_controller.js
   + /static/src/js/m2m_group_renderer.js
   + /static/src/js/m2m_group_view.js
   + /static/src/xml/qweb_template.xml文件中为视图添加QWeb模板
   + /view/template註冊JavaScript文件
   + /view上添加m2m
5. 調試客戶端代碼(Chromium)
6. 通過引導提升用戶上手體驗
   + /static/src/js/my_library_tour.js
   + 註冊JS
7. 移動應用JavaScript
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch15.1.png?raw=true)
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch15.6.png?raw=true)

#### 第十六章 OWL(ODOO WEB LIBRARY)
  >  javascript全新框架，基於組件的框架，QWEB模板
1. 新增OWL組件(js,qweb)
   + /my_library/static/src/js/component.js
   + /my_library/views/templates.xml file 新增JS組件
   + component.js 文件中定义OWL工具类
   + component.js 文件中添加OWL组件及其基础模板
   + component.js 文件增加到網頁客戶端
2. 新增關閉動作(qweb)
3. 組件左右滑動、響應式(js,qweb)
4. OWL組件的生命週期(js)
   + constructor
   + willstart
   + mounted
   + willpatch
   + willunmounted
5. 在表單增加owl字段(js2,scss)
   + model新增欄位、view給widget
   + static/src/xml/qweb_template.xml 增加QWEB樣板
   + static/src/scss/field_widget.scss
   + static/src/js/field_widget.js
![Alt text](https://imgur.com/vQPEERC.png)

#### 第十七章 ODOO應用內購買
  >  以下是IAP服務每個流程步驟的講解：
  + 客戶向服務提供服務商請求提供服務。通過請求，客戶將提供該帳戶的身份，服務使用它來識別用戶。（注意客戶需要在服務中安裝你的模塊）。
  + 在收到來自客戶的請求後，服務提供者將查詢Odoo 客戶的賬戶裡是否有西方的積分。
  + 在評審積分之後，服務提供者會執行服務。在某些情況下，服務提供者會調用外部服務來執行所請求的服務。
  + 在執行由客戶所請求的服務提供者返回 Odoo 後，在獲取第 2 步中所獲得的積分。的積分。
  + 服務提供者將返回客戶，通知他們所請求的已成功提供。一些可能會返回的結果信息，您可能會得到服務的結果。這些結果信息由客戶根據他們的規格（取決）於服務）來使用。
1. 應用內購買（IAP）的概念
2. 在Odoo中註冊一個IAP服務
3. 創建一個IAP服務模塊
4. 授權並收取IAP積分
5. 創建一個IAP客戶端模塊
6. 在客戶端下載時顯示問題

#### 第十八章自動化測試用例
  >  三種測試方式:
  + Python測試用例：用於測試Python業務邏輯
  + JavaScript QUnit測試：用於測試Odoo中JavaScript的實現
  + 導覽：檢測Python和JavaScript正常人類民族的集成測試
1. Python測試用例-
  + TransactionCas：在一個不同的事務中運行每個測試用例。如果測試用例運行成功，事務會自動回滾
  + SingleTransactionCase：通過類生成的測試用例方法這個實例運行到一個事務中，因此一個測試用例中的修改會在另一個測試用例中可以使用。 在完成最後一個測試用例時結束。
  + SavepointCase：它與SingleTransactionCase相同，但其測試方法在回滾保存點之前運行，而不是將所有測試方法放一個單獨的服務中運行。它用於創建大型測試用例，讓它們只能通過生成數據來實現一次 此處，我們使用setUpClass()方法來生成最終測試數據。
2. 運行打標籤的Python測試用例
3. 為客戶端測試用例設置Headless Chrome
4. 添加客戶端QUnit測試用例
5. 添加導覽測試用例
6. 通過UI（用戶界面）運行客戶端測試用例
7. 調試客戶端測試用例
8. 為失敗的測試用例生成視頻/截圖
9. 為測試生成隨機數據

#### 第十九章 使用Odoo.sh管理、部署和測試
  >   
1. 探討Odoo.sh的一些基本概念
2. 創建一個Odoo.sh賬戶
3. 添加和安裝自定義模塊
4. 管理分支
5. 訪問調試選項
6. 獲取你的實例的備份
7. 查看你的構建的狀態
8. Odoo.sh 的所有選項

#### 第二十章 ODOO中的遠端過程調用
  >  javascript全新框架，基於組件的框架，QWEB模板
1. 通過XML-RPC登錄/連接Odoo
   + python3 odoo_authenticate.py
   + authentication()方法可接收4个参数：数据库名、用户名、密码以及user agent环境。user agent环境是必传的参数
2. 通過XML-RPCSearch/讀取記錄
   + execute_kw (library.book 作为模型名、search作为方法名、domain)
   + search_read
3. 通過XML-RPC創建/更新/刪除記錄(CRUD)
   + create 創建
   + write 更新
   + unlink 刪除
   + check_access_rights
4. 通過XML-RPC調用方法
   + make_available
5. 通過JSON-RPC登錄/連接Odoo
   + JSON-RPC 2.0规范
6. 通過JSON-RPC獲取/搜索記錄
7. 通過JSON-RPC創建/更新/刪除記錄
8. 通過JSON-RPC調用方法
9. OCA odoorpc庫
   + pip install OdooRPC
   + jsonrpc格式
10. 生成API密鑰
    + 双因素认证(2FA) 
    + 除了odoorpc外，都可以使用。
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch20.1.png?raw=true)

#### 第二十一章 性能優化
  >  提升 ORM 級別的性能，而不是客戶端或部署端的性能
1. 記錄集的預提取模式
   + 通过向browse方法传递ID列表
2. 內存內緩存 – ormcache
   + from odoo import tools
   + @tools.ormcache('mode')
3. 生成圖像視圖
   +  image.mixin
4. 訪問狀態數據
   + read_group()
5. 創建或寫入多條記錄
   + self.env['library.book'].create(vals)
   + recordset.flush()
6. 通過數據庫查詢訪問記錄
   + self._cr.execute("SELECT id, name, date_release FROM library_book WHERE name ilike %s", ('%odoo%',))
   + self._cr.dictfetchall()
   + self._cr.fetchall()
   + 通過記錄集有兩種訪問數據庫游標的方式：一種是通過記錄集方法，例如self._cr，另一種是通過環境，例如self.env.cr。
   + self.env.cr.execute('SELECT id, name FROM library_book WHERE name ilike %s ';', (search_keyword,))
7. Python代碼性能分析
   + 	from odoo.tools.profiler import profile
   + 	gprof2dot -f pstats -o /Users/parth/Desktop/prof.xdot /Users/parth/Desktop/make_available.prof
   + 	xdot /Users/parth/Desktop/prof.xdot

#### 第二十二章 POS
  >  不同的架構，因此它可以離線運行
1. 添加自定義JavaScript/SCSS文件
2. 在鍵盤上添加動作按鈕
3. 做RPC調用
4. 修改POS界面UI
5. 修改現有業務邏輯
6. 修改客戶收據

#### 第二十三章 在ODOO管理EMAIL
  >  提升 ORM 級別的性能，而不是客戶端或部署端的性能
1. 配置郵件接收和發送服務器
   + mail.thread
2. 管理文檔中的聊天器
   + mail.activity.mixin
3. 管理文檔中的活動
4. 使用Jinja模板發送郵件
   + Settings > Technical > Email > Templates菜单
5. 使用QWeb模板發送郵件
   + QWeb 模板的内容通过后台Settings > Technical > User Interface > Views
   + QWEB VS JINJA
     + 在邮件模板中没有简单的发送额外参数的方式。需要在对象变量中使用记录集来获取动态数据。另一方面，QWeb邮件模板可以通过values
     + 要管理日期格式、时区和带有货币符号的金额，在Jinja模板中需要使用format_date、format_tz和format_amount函数，而在QWeb模板中则是自动进行管理的。
     + 在Jinja中不能修改其它模块的已有模板，但在QWeb模板中可以通过继承修改邮件模板
     + 可以直接通过消息编辑器选择并使用Jinja模板。在下图中，右下角的下拉菜单用于选择一个Jinja模板
     + 使用QWeb，並不能直接通過消息編輯器來選擇模板。
6. 管理郵件名稱
   + Setting > Technical > Email > Aliases
7. 在聊天器中記錄用戶修改
   + tracking=True
8. 定期發送摘要郵件
   + Settings > Technical > Emails > Digest Emails
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch23.1.png?raw=true)

#### 第二十四章 IOT盒子
  >  企業版-Raspberry Pi 3 Model B+，可通過https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/
1. 對樹莓派（Raspberry Pi）套裝物聯網鏡像
2. 通過網絡連接物聯網盒子
3. 對Odoo添加物聯網盒子
4. 加載驅動及已連接設備
5. 從設備接收輸入
   + 攝影機
   + 卡尺
   + 重量秤
7. 通過SSH訪問物聯網市場
8. 配置POS（銷售點）
9. 直接向打印機發送PDF報表
