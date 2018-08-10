# coding=utf-8
import unittest, doctest
import HTMLTestRunner
import time
# 相对路径
test_dir ='./test_case'
test_dir1 ='./report'
# 绝对路径
# test_dir='C:\\Users\\Anne\\Desktop\\SeleniumPython_Test\\Web_case\\test_case'
# test_dir1='C:\\Users\\Anne\\Desktop\\SeleniumPython_Test\\Web_case\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# 定义带有当前测试时间的报告，防止前一次报告被覆盖
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = test_dir1 + '/' + now + 'result.html'
# 定义测试报告存放路径
# filename = 'C:\\Users\\Anne\\Desktop\\SeleniumPython_Test\\Web_case\\report\\result.html'
# 二进制打开，准备写入文件
fp = file(filename, 'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
runner.run(discover)

# if __name__=='__main__':
#   runner=unittest.TextTestRunner()
#   runner.run(discover)