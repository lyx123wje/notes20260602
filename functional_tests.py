from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # 每次测试前，启动浏览器
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # 测试结束后，自动关闭浏览器（清扫战场）
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #张三听说有一个在线待办事项的应用
        #他去看了这个应用的首页
        self.browser.get('http://localhost:8000')
        #他注意到网页里面包含“To-Do”这个词
        self.assertIn('To-Do', self.browser.title, "Browser title was: " + self.browser.title)
    #应用有一个待办事项的文本输入框
        self.fail('Finish the test!')
    #他在文本输入框中输入了“Buy flowers”

#他按了回车键键后，页面更新了
#待办事项表格中显示了“1：Buy flowers”
#页面中又显示一个本文输入框，可以输入其他待办事项
#他输入了“Send a gift to List”

#页面再次更新，他的清单中显示了这连个待办事项

#张三象只打这个网站是否会记住他的清单
#他看到网站为他生成了一个唯一的URL

#他访问那个URL，法宣他的待办事项列表还在
#他满意的离开了
 
if __name__ == '__main__':
    unittest.main()
