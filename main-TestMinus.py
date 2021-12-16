import unittest
from HTMLTestRunner import HTMLTestRunner #生成测试运行器，才能生成测试报告

#1.首先要加载出自己写的用例，并一个变量去接收他
tests = unittest.defaultTestLoader.discover(r"D:\测试项目\PythonProject\day12【单元测试】\day12单元测试",pattern="Test*.py")

#2.创建用例运行器

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是计算器测试",
    description = "算法报告",
    verbosity=1,
    stream = open(file="../test/Calcater.html", mode="w+", encoding="utf-8")
)

#3.运行该程序

runner.run(tests)

#4.在生成报告后发送给指定邮箱
