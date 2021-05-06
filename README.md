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
