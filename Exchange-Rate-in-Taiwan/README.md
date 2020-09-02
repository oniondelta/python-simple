# Exchange-Rate-in-Taiwan（臺灣銀行匯率轉換）

### 資料來源：
- 臺灣銀行網站：https://rate.bot.com.tw/xrt?Lang=zh-TW

### 說明：
- 匯率轉換有方向性，例如：現時匯率為 30 元整新台幣兌換 1 元整美金，但當你拿 1 元整美金，會換匯到少於 30 元整新台幣。

- 以此寫一個 Python 程式，從臺灣銀行爬蟲每日匯率，然後計算各方向的匯兌金額。

- 打包好的 App (Mac Os)：https://www.dropbox.com/s/ld3ztpwgytzt25c/Exchange_Rate_in_Taiwan.app.zip?dl=0

- 使用 pyinstaller 打包，在別台 Mac 上會出現「無法打開『 xxx 』因為無法驗證開發者」，故附上原始碼，可直接用 Python 執行，或自行封裝。

### 注意：

- 須開啟網路連線！

- 點擊「數字」可直接複製該數字

### 圖示：
![介紹1](https://raw.githubusercontent.com/oniondelta/python-simple/master/Exchange-Rate-in-Taiwan/Exchange%20Rate%20in%20Taiwan.png)
