from time import sleep

# 定義 windowScroll 的 method
def windowScroll(driver, scrollToPos, n, sleepSec):
    for x in range(n):
    #為了符合臉書的動態頁面載入，讓scrollBar移動到 特定的位置(不是最下，這樣臉書載入時會出錯)
    # 這邊還要再細調整一下
        driver.execute_script(f"window.scrollTo(0,{scrollToPos})")
        # print("scroll")
        sleep(sleepSec)

def scrollCollection(time, driver):
    windowScroll(driver, "document.body.scrollHeight*3/4", n= 10, sleepSec= 1)
    windowScroll(driver, "document.body.scrollHeight*10/11", n= 20, sleepSec= 0.5)
    windowScroll(driver, "document.body.scrollHeight*50/51", n= 20, sleepSec= 0.5)
    for i in range(time):
        windowScroll(driver, "document.body.scrollHeight*100/101", n= 10, sleepSec= 1)