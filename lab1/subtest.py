import sub
import unittest

class Test_subscribtion(unittest.TestCase):
    testchannels = {'channel1':['content1'], 'channel2':['content2']}
    testusers = {'user1':['channel1'],'user2':[]}
    testdata = sub.subscribtion(testchannels, testusers)

    def test_sub(self):
        self.testdata.handler(['user1', 'subscribe', 'channel2'])
        self.assertEqual(self.testdata.users['user1'], ['channel1', 'channel2'])

    def test_unsub(self):
        self.testdata.handler(['user1', 'unsubscribe', 'channel2'])
        self.assertEqual(self.testdata.users['user1'], ['channel1'])

    def test_add_content(self):
        self.testdata.handler(['user1', 'addcontent', 'channel1'])
        self.assertEqual(self.testdata.channels['channel1'], ['content1', self.testdata.newcontent])

    def test_delete_content(self):
        self.testdata.handler(['user1', 'deletecontent', 'channel1'])
        self.assertEqual(self.testdata.channels['channel1'], ['content1'])

if __name__ == '__main__':
    unittest.main()