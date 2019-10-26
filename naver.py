from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from config import NAVER_ID, NAVER_PASSWORD


class Naver:
  
  def __init__(self, ID, PASSWORD):
    self.driver = webdriver.Chrome('./chromedriver')
    self.id = "'%s'"%(ID)
    self.password = "'%s'"%(PASSWORD)
    
    self.login()

  def login(self):
    self.driver.get('https://nid.naver.com/nidlogin.login')
    self.driver.execute_script("document.getElementsByName('id')[0].value=" + self.id )
    self.driver.execute_script("document.getElementsByName('pw')[0].value=" + self.password )

    self.driver.find_element_by_id('label_ip_on').click()
    self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
    time.sleep(2)

    self.move_blog_editor()
    print('>>> login complete <<<')

  def setBold(self):
    # self.last_text_line_focus()
    selector = "se-toolbar-button-bold"
    s = "document.getElementsByClassName('%s')[0].click()"%(selector)
    time.sleep(0.3)
    self.driver.execute_script(s)
    time.sleep(1.5)

    print('>>> font weight complete <<<')

  def setFontSize(self, size):
    # self.last_text_line_focus()
    selector = "se-toolbar-button-font-size-code"
    size = str(size)

    s = {
      "11": "se-font-size-code-fs11",
      "13": "se-font-size-code-fs13",
      "15": "se-font-size-code-fs15",
      "16": "se-font-size-code-fs16",
      "19": "se-font-size-code-fs19",
      "24": "se-font-size-code-fs24",
      "28": "se-font-size-code-fs28",
      "30": "se-font-size-code-fs30",
      "34": "se-font-size-code-fs34",
      "38": "se-font-size-code-fs38"
    }

    query = "document.getElementsByClassName('%s')[0].click()"%(selector)
    self.driver.execute_script(query)
    time.sleep(1.0)

    query = "document.getElementsByClassName('%s')[0].click()"%(s[size])

    self.driver.execute_script(query)
    time.sleep(1.0)

    print('>>> font size complete <<<')

  def setCode(self,  text): 
    # 소스코드 추가
    selector = "se-toolbar-button-code" 
    query = "document.getElementsByClassName('%s')[0].click()"%(selector)
    self.driver.execute_script(query)
    time.sleep(0.5)

    # # 추가된 소스코드 클릭
    # code_editors = self.driver.find_elements_by_css_selector('.%s'%(selector))
    # code_editors[-1].click()

    # 포커스 잡힌 부분에 데이터 입력
    actions = ActionChains(self.driver)
    actions.send_keys(text)
    actions.perform()
    time.sleep(1.5)

    print('>>> typing code complete <<<')

  def inputText(self, text):
    self.last_text_line_focus()
  
    actions = ActionChains(self.driver)
    actions.send_keys(text)
    actions.perform()
    time.sleep(0.5)

    print('>>> typing text complete <<<')

  def move_blog_editor(self):
    self.driver.get('https://blog.naver.com/angdnp/postwrite')
    time.sleep(2)
    
  def last_text_line_focus(self):
    selector = '.se-text-paragraph'
    # query = "var componentCnt = document.getElementsByClassName('%s').length; document.getElementsByClassName('%s')[componentCnt - 1].click()"%(selector, selector)
    components = self.driver.find_elements_by_css_selector(selector)
    # self.driver.execute_script(query)
    time.sleep(0.3)
    print(components[-1])
    components[-1].click()
    time.sleep(0.5)

if __name__ == "__main__":

  # 아이디/비밀번호를 입력해준다.
  naver = Naver(NAVER_ID, NAVER_PASSWORD)

  naver.setBold()

  naver.setFontSize(13)

  code1 = 'let a = 10;'
  code2 = '''function test() {
  console.log('hello world');
}'''

  naver.setCode(code1)
  naver.setCode(code2)

  # naver.setBold()
  naver.inputText('안녕하세요\n')
  
  naver.setBold()
  naver.setFontSize(13)
  naver.inputText('안녕하세요1\n')

  naver.setFontSize(15)
  naver.inputText('안녕하세요2\n')

  naver.setFontSize(16)
  naver.inputText('안녕하세요3 ')

  naver.setBold()
  naver.inputText(' 안녕하세요4')