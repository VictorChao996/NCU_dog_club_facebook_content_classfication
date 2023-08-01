# NCU 汪汪社-臉書社團文章分析
## 事先準備
- python 安裝
- 瀏覽器
- 瀏覽器 Driver (ChromeDriver、Microsoft Edge Driver等)

### python package installation
`pip install ...`
- selenium
- dotenv
## 介紹

### 使用
1. 新增 .env file，內容包含
```
USER=
PASSWORD=
URL=
```
2. `python main.py` 執行程式

### 功能
1. 爬臉書社團文章
2. 根據貼文的關鍵字做簡單的一個貼文分類

### 輸出檔案
- 中午班貼文
- 下午班貼文
- 環校班貼文
- 個人請假貼文
- 醫療相關貼文
- 其他
> 可自行增加新的分類
### 檔案說明
- v1
  - 主程式: [NCU_dog_club_facebook_context.ipynb](./NCU_dog_club_facebook_context.ipynb)
- v2: 
  - `main.py`: 主程式
  - `utils/files.py`: 檔案處理相關函數
  - `utils/manipulate.py`: 自動化相關操作函數
  - records_example: 輸出範例


## 其他備註

### 時間紀錄
- 2022/1/24 : 新增 v1
- 2023/8/1 : 新增 v2，重新撰寫程式架構
### 未來預計
- 做UI並打包成執行檔，讓不會程式的社員也可以使用，特別是對需要觀看排班紀錄的幹部。
### 相關資源
- 瀏覽器必須使用最新版本的
    - [ChromeDriver 下載網站](https://chromedriver.chromium.org/)
    - [Edge Driver 下載網站](https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/)

