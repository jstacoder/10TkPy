import unittest
from views import MyViews

class SendToViewTest(unittest.TestCase):
    
    def setUp(self):
        #global testCount
        self.testView = MyViews()
        #testCount += 1
    def tearDown(self):
        self.testView = ''

    def testMenuView(self):
        self.assertIsNone(self.testView.print_menu_view())

if __name__ == "__main__":
    unittest.main()
