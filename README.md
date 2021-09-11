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
  >  javascript全新框架，基於組件的框架，QWEB模板
1. 管理靜態資源
2. 為網站擴展CSS和JavaScript
3. 創建或更改模板 – QWeb
4. 管理動態路由
5. 為用戶提供靜態小組件
6. 為用戶提供動態小組件
7. 獲取網站用戶的輸入
8. 管理搜索引擎優化（SEO）選項
9. 管理網站的站點地圖
10. 獲取訪客的國家信息
11. 追踪營銷活動
12. 管理多站點
13. 重定向老URL
14. 網站相關記錄的發布管理
15. 
![Alt text](https://github.com/ksharry/odoo14-cookbook/blob/main/png/ch13.1.png?raw=true)

#### 第十六章 OWL(ODOO WEB LIBRARY)
  >  javascript全新框架，基於組件的框架，QWEB模板
1. 新增OWL組件(js,qweb)
2. 新增關閉動作(qweb)
3. 組件左右滑動、響應式(js,qweb)
4. 組件的生命週期(js->constructor、willstart、mounted、willpatch、willunmounted)
5. 在表單增加owl字段(js2,scss)
![Alt text](https://imgur.com/vQPEERC.png)
