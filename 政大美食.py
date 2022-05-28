import tkinter as tk
from tkinter import Button, Menubutton,Menu
top = tk.Tk()  
top.geometry("300x350") 
top.title("政大美食") 

menubutton1 = Menubutton(top, text = "早餐")  
  
menubutton1.grid()  
  
menubutton1.menu = Menu(menubutton1)  
  
menubutton1["menu"]=menubutton1.menu  
  
menubutton1.menu.add_checkbutton(label = "brunch first 早餐店/評價:?/大門/價位:100元以下")
  
menubutton1.menu.add_checkbutton(label = "德合香/評價:4/大門/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "美味派/評價:3.1/麥側/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "傳香飯團/評價:3.7/大門/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "古早味豆漿店/評價:4.4/大門/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "小貓咪早餐/評價:3.6/大門/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "口福豆漿/評價:4.1/大門/價位:100元以下")  

menubutton1.menu.add_checkbutton(label = "李白Breakfast X coffee/評價:4.4/大門/價位:100元以下")  

menubutton2 = Menubutton(top, text = "義式")  
  
menubutton2.grid()  
  
menubutton2.menu = Menu(menubutton2)  
  
menubutton2["menu"]=menubutton2.menu  
  
menubutton2.menu.add_checkbutton(label = "首思義義式餐坊so sweet/評價:4.3/麥側/價位:100-300元")

menubutton2.menu.add_checkbutton(label = "提洛斯/評價:3.8/西側門/價位:100-300元")

menubutton2.menu.add_checkbutton(label = "LAZY PASTA/評價:4.2/西側門/價位:100-300元")

menubutton2.menu.add_checkbutton(label = "Pasta Kitchen/評價:4.1/大門/價位:100-300元")

menubutton2.menu.add_checkbutton(label = "里克德義廚房/評價:4.4/大門/價位:100-300元")

menubutton2.menu.add_checkbutton(label = "豔陽下義大利小餐館/評價:4.6/大門/價位:100-300元")

menubutton3 = Menubutton(top, text = "日式")  
  
menubutton3.grid()  
  
menubutton3.menu = Menu(menubutton3)  
  
menubutton3["menu"]=menubutton3.menu  
  
menubutton3.menu.add_checkbutton(label = "吉野家/評價:3/大門/價位:100-300元")
  
menubutton3.menu.add_checkbutton(label = "湯饌/評價:3.5/麥側/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "鬼匠拉麵/評價:4/麥側/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "加賀日式料理/評價:3.5/麥側/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "金鰭/評價:3.9/西側門/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "東京小城/評價:?/西側門/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "浪速食鋪/評價:4.8/大門/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "原丼力/評價:4.2/大門/價位:100-300元")

menubutton3.menu.add_checkbutton(label = "樂山食堂/評價:4.2/大門/價位:100-300元")

menubutton4 = Menubutton(top, text = "點心")  
  
menubutton4.grid()  
  
menubutton4.menu = Menu(menubutton4)  
  
menubutton4["menu"]=menubutton4.menu  
  
menubutton4.menu.add_checkbutton(label = "紅豆餅/評價:?/大門/價位:100元以下")
  
menubutton4.menu.add_checkbutton(label = "明池豆花/評價:4/大門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "壹合冰品湯圓甜品/評價:3.8/麥側/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "小木屋/評價:4/大門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "老麵水煎包/評價:3.7/西側門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "TDB傳統甜點麵包店/評價:4.4/西側門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "可麗餅/評價:4.4/大門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "Mr. 葱/評價:?/大門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "囂張吃翅/評價:4.9/大門/價位:100-300元")

menubutton4.menu.add_checkbutton(label = "派克雞排/評價:3.1/大門/價位:100元以下")

menubutton4.menu.add_checkbutton(label = "龐舍炸物/評價:4.1/大門/價位:100元以下")

menubutton5 = Menubutton(top, text = "咖啡廳")  

menubutton5.grid()  
  
menubutton5.menu = Menu(menubutton5)  
  
menubutton5["menu"]=menubutton5.menu  
  
menubutton5.menu.add_checkbutton(label = "小公寓Apt.cafe/評價:4.3/大門/價位:100-300元")

menubutton6 = Menubutton(top, text = "台式")  

menubutton6.grid()  

menubutton6.menu = Menu(menubutton6)  
  
menubutton6["menu"]=menubutton6.menu  
  
menubutton6.menu.add_checkbutton(label = "美香味快餐/評價:4.1/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "廢墟/評價:4/麥側/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "丐幫滷味/評價:3.5/麥側/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "私房麵/評價:3.9/麥側/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "八方雲集鍋貼水餃專賣店/評價:3.5/麥側/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "梁社漢排骨/評價:4/大門/價位:100-300元")

menubutton6.menu.add_checkbutton(label = "健康滷味/評價:3.8/西側門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "焿大王/評價:3.7/西側門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "大呼過癮/評價:?/西側門/價位:100-300元")

menubutton6.menu.add_checkbutton(label = "大汗麻辣鴨血臭豆腐/評價:4.2/西側門/價位:100-300元")

menubutton6.menu.add_checkbutton(label = "阿義師牛肉麵/評價:3.8/西側門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "小農食堂/評價:4.1/西側門/價位:100-300元")

menubutton6.menu.add_checkbutton(label = "愛心滷味/評價:?/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "舅媽的店/評價:3.6/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "季旭小吃/評價:4.3/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "排骨王/評價:4.1/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "左撇子/評價:4/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "季旭小吃/評價:4.3/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "來來快餐/評價:4.2/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "3號小吃部/評價:?/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "飽飽食府/評價:4.1/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "悅來牛肉麵/評價:4.4/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "食鼎鵝肉/評價:4.5/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "楊記小吃/評價:4.1/大門/價位:100元以下")

menubutton6.menu.add_checkbutton(label = "政大赤肉羹魯肉飯/評價:4/大門/價位:100元以下")

menubutton7 = Menubutton(top, text = "東南亞式")  

menubutton7.grid()  

menubutton7.menu = Menu(menubutton7)  
  
menubutton7["menu"]=menubutton7.menu  
  
menubutton7.menu.add_checkbutton(label = "波波恰恰/評價:4/大門/價位:100-300元")

menubutton7.menu.add_checkbutton(label = "小曼谷泰國雲南料理/評價:4.1/麥側/價位:100-300元")

menubutton7.menu.add_checkbutton(label = "滇味廚房/評價:3.9/西側門/價位:100元以下")

menubutton7.menu.add_checkbutton(label = "華越美食/評價:4/西側門/價位:100元以下")

menubutton7.menu.add_checkbutton(label = "珍妹麵店/評價:4.9/麥側/價位:100元以下")

menubutton7.menu.add_checkbutton(label = "小曼谷泰國雲南料理/評價:4.1/大門/價位:300元以上")

menubutton8 = Menubutton(top, text = "韓式")  

menubutton8.grid()  

menubutton8.menu = Menu(menubutton8)  
  
menubutton8["menu"]=menubutton8.menu  
  
menubutton8.menu.add_checkbutton(label = "石鍋軒/評價:3.2/麥側/價位:100-300元")

menubutton8.menu.add_checkbutton(label = "阿里郎/評價:3.7/麥側/價位:100-300元")

menubutton8.menu.add_checkbutton(label = "高句麗/評價:4.3/西側門/價位:100-300元")

menubutton8.menu.add_checkbutton(label = "弘大歐巴（韓國紫菜飯捲專賣店）/評價:4/西側門/價位:100元以下")

menubutton8.menu.add_checkbutton(label = "韓大佬/評價:4.2/大門/價位:100-300元")

menubutton9 = Menubutton(top, text = "美式")  

menubutton9.grid()  

menubutton9.menu = Menu(menubutton9)  
  
menubutton9["menu"]=menubutton9.menu  
  
menubutton9.menu.add_checkbutton(label = "湘湘牛排館/評價:4/麥側/價位:100-300元")

menubutton9.menu.add_checkbutton(label = "Come See Pizza 牽絲披薩/評價:4.4/麥側/價位:100-300元")

menubutton9.menu.add_checkbutton(label = "Juicy Bun/評價:4.4/大門/價位:100-300元")

menubutton9.menu.add_checkbutton(label = "SUBWAY/評價:3.5/大門/價位:100元以下")

menubutton10 = Menubutton(top, text = "自助餐")  

menubutton10.grid()  

menubutton10.menu = Menu(menubutton10)  
  
menubutton10["menu"]=menubutton10.menu  
  
menubutton10.menu.add_checkbutton(label = "素還真/評價:4.5/麥側/價位:100元以下")

menubutton10.menu.add_checkbutton(label = "菁英食堂自助餐/評價:3.6/麥側/價位:100元以下")

menubutton10.menu.add_checkbutton(label = "佳味自助餐/評價:3.8/大門/價位:100元以下")

menubutton11 = Menubutton(top, text = "中式")  

menubutton11.grid()  

menubutton11.menu = Menu(menubutton11)  
  
menubutton11["menu"]=menubutton11.menu  
  
menubutton11.menu.add_checkbutton(label = "敏忠餐廳/評價:4/麥側/價位:100-300元")

menubutton11.menu.add_checkbutton(label = "四川飯館/評價:4.2/麥側/價位:300元以上")

menubutton11.menu.add_checkbutton(label = "喜記港式燒臘/評價:5/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "廣東粥/評價:2.8/西側門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "餛飩超人/評價:4/西側門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "阿寶早午餐/評價:3.9/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "甘泉魚麵/評價:3.7/大門/價位:100-300元")

menubutton11.menu.add_checkbutton(label = "蘭亭池上便當/評價:4.1/大門/價位:100-300元")

menubutton11.menu.add_checkbutton(label = "早安找點/評價:4.5/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "蔬福創意蔬食料理/評價:3.9/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "來來豆漿/評價:4.6/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "新光小吃店/評價:3.9/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "米粉湯滷肉飯/評價:4/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "漢堡寶活力早餐/評價:3.4/大門/價位:100元以下")

menubutton11.menu.add_checkbutton(label = "味新飲食店/評價:4.1/大門/價位:100元以下")

menubutton12 = Menubutton(top, text = "餐酒館")  

menubutton12.grid()  

menubutton12.menu = Menu(menubutton12)  
  
menubutton12["menu"]=menubutton12.menu  
  
menubutton12.menu.add_checkbutton(label = "隱 Bistro/評價:4.6/西側門/價位:300元以上")
 
menubutton12.menu.add_checkbutton(label = "李氏兄弟44號餐酒館/評價:4.8/大門/價位:100-300元")

top.mainloop()  