import sub
import unittest

class Test_subscribtion(unittest.TestCase):
    testchannels = {'channel1':['content1'], 'channel2':['content2']}
    testusers = {'user1':['channel1'],'user2':[]}
    testdata = sub.subscribtion(testchannels, testusers)

    def test_sub(self):
        self.testdata.handler(['user1', 'subscribe', 'channel2'])
        self.assertEqual(self.testdata.users['user1'], ['channel1', 'channel2'])
        self.assertEqual(self.testdata.subscribe('user3','channel2'), None)
        self.assertEqual(self.testdata.subscribe('user1', 'channel3'), None)

    def test_unsub(self):
        self.testdata.handler(['user1', 'unsubscribe', 'channel2'])
        self.assertEqual(self.testdata.users['user1'], ['channel1'])
        self.assertEqual(self.testdata.unsubscribe('user3','channel2'), None)
        self.assertEqual(self.testdata.unsubscribe('user1', 'channel2'), None)

    def test_add_content(self):
        self.testdata.handler(['user1', 'addcontent', 'channel1'])
        self.assertEqual(self.testdata.channels['channel1'], ['content1', self.testdata.newcontent])
        self.assertEqual(self.testdata.addcontent('channel3'), None)

    def test_delete_content(self):
        self.testdata.handler(['user1', 'deletecontent', 'channel1'])
        self.assertEqual(self.testdata.channels['channel1'], ['content1'])
        self.assertEqual(self.testdata.deletecontent('channel3'), None)

if __name__ == '__main__':
    unittest.main()