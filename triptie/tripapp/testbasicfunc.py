# 测试模块基本功能
from django.test import TestCase
from tripapp.templatetags.tripapp_template_tags import your_custom_tag_function

class TemplateTagsTests(TestCase):
    def test_your_custom_tag_function(self):
        # 假设 your_custom_tag_function 是一个将数字加倍的简单函数
        input_value = 5
        expected_output = 10
        self.assertEqual(your_custom_tag_function(input_value), expected_output)

class PopulateTripAppTests(TestCase):
    def test_populate_script(self):
        # 这里假设 populate_tripapp.py 脚本填充了数据库
        # 您可以编写测试来检查数据库中是否存在预期的数据
        self.assertTrue(YourModel.objects.exists())
