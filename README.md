# Poker Spin and Gold Analyzer

這個程式可以分析德州撲克平台 Natural8 的 spin and gold 遊戲結果，計算玩家營利、勝率、機率等情況。

通過這個程式可以分析到在遊戲中需要多少勝率才能營利，每一場遊戲的期望營利等資訊，使玩家了解到自己在這個遊戲的營利程度。

## 輸入使用方法

點開遊戲內戰績按鈕連結到 PokerCraft 戰績分析網站，接著點黃金&轉盤進到畫面如下圖

![image](https://github.com/kenchang890410/poker-spin-and-gold-analyze/blob/203c7d7ecb796474a5723a2e5dba87f717323672/PokerCraft.png)

接著點擊右上角綠色下載遊戲概括信息，放置到自訂資料夾並且把程式內 directory_path 修改成資料夾路徑

## 輸出結果介紹

測試輸入為 input 資料夾下 81 場遊戲資訊

total game :  81 //總局數

win rate : 34 / 81 = 0.41975308641975306 //勝率

total game frequency :  [39, 36, 3, 2, 1] //獎金池出現次數，由左至右為 2倍、3倍、4倍、5倍、10倍

total game prize rate :  [0.48148148148148145, 0.4444444444444444, 0.037037037037037035, 0.024691358024691357, 0.012345679012345678] //獎金池出現頻率

win_type :  [14, 16, 2, 2, 0] //各倍數勝場數

win_type rate:  [0.358974358974359, 0.4444444444444444, 0.6666666666666666, 1.0, 0.0] //各倍數下的勝率

profit : 23.5 - 20.25 = 3.25 //總營利

profit 13.0 buy in //營利的買入數量

per game ev :  0.6728395061728396 //每場遊戲的獎金期望值

per game expected profit :  0.03242645938119193 //每場遊戲的期望利潤

expected profit:  2.626543209876546 //總期望營利

need 0.3715596330275229 win rate to make a profit //盈虧平衡所需的勝率

per game expected profit with 33% win rate:  -0.025720164609053464 //假設 33% 勝率，每場遊戲的期望營利

expected profit with 33% win rate:  -2.0833333333333304 //假設 33% 勝率，總期望營利

