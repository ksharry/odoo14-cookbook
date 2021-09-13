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

0.工作流程:
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
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.1.png?raw=true)

#### 第十六章 OWL(ODOO WEB LIBRARY)
  >  javascript全新框架，基於組件的框架，QWEB模板
1. 新增OWL組件(js,qweb)
2. 新增關閉動作(qweb)
3. 組件左右滑動、響應式(js,qweb)
4. 組件的生命週期(js->constructor、willstart、mounted、willpatch、willunmounted)
5. 在表單增加owl字段(js2,scss)
![Alt text](https://imgur.com/vQPEERC.png)
