list1=["0","1","2",["3","4"],"5"]
"2" in list1 //True
"3" in list1 //False
“3” in list1[3]//True
list1[3][0]  //'3'在第三个数组元素里

list1=[123]
list2=[234]
list1>list2 //False

list1=[123,456]
list2=[234,123]
list3=list1+list2
list3  //[123,456,234,123]
