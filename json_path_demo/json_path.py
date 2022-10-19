# --------------------------------------------------
# -*- coding: utf-8 -*-
# !/usr/bin/python
# PN: interface_test
# FN: json_path
# Author: xiaxu
# DATA: 2022/9/30
# Description:jsonpath的使用方法
# ---------------------------------------------------
"""https://github.com/masukomi/jsonpath-perl/tree/master json的xpath"""
"""
JSONPath表达式总是引用JSON结构，就像XPath表达式与XML文档结合使用一样。
由于JSON结构通常是匿名的，不一定有“根成员对象”，
因此JSONPath假定分配给外层对象的抽象名称为$。
"""
data={ "store": {
	"book": [
	  { "category": "reference",
		"author": "Nigel Rees",
		"title": "Sayings of the Century",
		"price": 8.95
	  },
	  { "category": "fiction",
		"author": "Evelyn Waugh",
		"title": "Sword of Honour",
		"price": 12.99
	  },
	  { "category": "fiction",
		"author": "Herman Melville",
		"title": "Moby Dick",
		"isbn": "0-553-21311-3",
		"price": 8.99
	  },
	  { "category": "fiction",
		"author": "J. R. R. Tolkien",
		"title": "The Lord of the Rings",
		"isbn": "0-395-19395-8",
		"price": 22.99
	  }
	],
	"bicycle": {
	  "color": "red",
	  "price": 19.95
	}
  }
}
"""
    jsonpath表达式的基本格式规范：
        $ 表示根节点，也是所有jsonpath表达式的开始
        . 表示获取子节点
        .. 表示获取所有符合条件的内容
        *  代表所有的元素节点
        [] 表示迭代器的标示（可以用于处理下标等情况）
        [,] 表示多个结果的选择
        ?() 表示过滤操作
        @ 表示当前节点
    JsonPath要么返回False，要么返回list
"""
import jsonpath

# bicycle = jsonpath.jsonpath(data,'$.store.bicycle')#获取bicycle的内容
# print(bicycle,type(bicycle))
# print(bicycle[0]['price'])
# print(jsonpath.jsonpath(data,'$.store..price'))#获取所有price内容
# print(jsonpath.jsonpath(data,'$.store.*')) #获取子节点下的所有内容
# print(jsonpath.jsonpath(data,'$.store.book[1].author')) #获取book下第二个类容的auther类容
# print(jsonpath.jsonpath(data,'$.store.book[?(@.price>10)].title')) #获取book下价格大于10的所有title
print(jsonpath.jsonpath(data, '$..a'))
