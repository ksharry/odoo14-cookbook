## 修改自己程式備註的習慣與修復BUG，第四章後程式碼都有備註以下的課程紀錄點。
## 每章的步驟說明:https://alanhou.org/odoo14-cookbook/
## 參考github:https://github.com/alanhou/odoo14-cookbook/tree/main/

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
