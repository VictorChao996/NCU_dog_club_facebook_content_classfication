# NCU 汪汪社-臉書社團文章分析
## 功能
1. 爬臉書社團文章
2. 根據貼文的關鍵字做簡單的一個貼文分類

## 輸出檔案
- 中午班貼文
- 下午班貼文
- 環校班貼文
- 個人請假貼文
- 醫療相關貼文
- 其他
> 可自行增加新的分類
## 檔案說明
- 主程式: [NCU_dog_club_facebook_context.ipynb](./NCU_dog_club_facebook_context.ipynb)
- 瀏覽器Driver: [ChromeDriver](./chromedriver.exe)、[Microsoft edge driver](./msedgedriver.exe) 

## 目前階段
- 執行 python 程式檔，結果會輸出到新增的txt file 中

## 未來預計
- 做UI並打包成執行檔，讓不會程式的社員也可以使用，特別是對需要觀看排班紀錄的幹部。
## 備註
- 瀏覽器Driver最好使用最新版本的
    - [ChromeDriver 下載網站](https://chromedriver.chromium.org/)
    - [Edge Driver 下載網站](https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/)
- 主程式內預設google瀏覽器
- 要在網路良好的情況下使用
