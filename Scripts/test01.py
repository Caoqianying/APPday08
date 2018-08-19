import allure
import pytest


class Test01:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是第一个测试方法")
    def test01_01(self):
        allure.attach("test01_01", "这是test01_01的步骤描述")  # 第一个引号相当于report中生成的txt文件的名字，在allure报告中的测试套件中是步骤标题
                                                             # 第二个引号是文件中的具体内容，在allure报告中的测试套件中是步骤描述
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是第二个测试方法")
    def test01_02(self):
        allure.attach("test01_02", "这是test01_02的步骤描述")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是第三个测试方法")
    def test01_03(self):
        allure.attach("test01_03", "这是test01_03的步骤描述")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是第四个测试方法")
    def test01_04(self):
        allure.attach("test01_04", "这是test01_04的步骤描述")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是第五个测试方法")
    def test01_05(self):
        allure.attach("test01_05", "这是test01_05的步骤描述")
        assert 1