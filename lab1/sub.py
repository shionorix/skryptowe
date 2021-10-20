import sys

class subscribtion(object):
    allowedactions = ['subscribe', 'unsubscribe', 'addcontent', 'deletecontent', 'info', 'mylist']
    oldcontent = ''
    newcontent = ''
    def __init__(self, channels, users):
        self.channels = channels
        self.users = users
        pass
    
    def handler(self, action):
        if action[1] in self.allowedactions:
            if action[1] == 'subscribe':
                self.subscribe(action[0], action[2])
            if action[1] == 'unsubscribe':
                self.unsubscribe(action[0], action[2])
            if action[1] == 'addcontent':
                self.addcontent(action[2])
            if action[1] == 'deletecontent':
                self.deletecontent(action[2])
            if action[1] == 'info':
                self.printinfo(action[2])
            if action[1] == 'mylist':
                self.printSubscribedChannels(action[0])
        else:
            print("Invalid action, operation failed.")

    def addcontent(self, channel):
        if channel in self.channels:
            self.newcontent = input("Input content to add: \n")
            self.channels[channel].append(self.newcontent) 
            print('Success')
        else:
            print('There is no such channel. Operation failed.')

    def deletecontent(self, channel):
        if channel in self.channels:
            self.oldcontent = input(f"Input content to delete. Current content: \n{';'.join(self.channels[channel])}\n")
            if self.oldcontent in self.channels[channel]:
                self.channels[channel].remove(self.oldcontent)
                print('Success')
            else:
                print('There is no such content in this channel. Operation failed.')
        else:
            print('There is no such channel. Operation failed.')

    def printinfo(self, channel):
        if channel in self.channels:
            print('; '.join(self.channels[channel]))
        else:
            print('There is no such channel. Operation failed.')

    def printSubscribedChannels(self, user):
        if user in self.users:
            print("; ".join(self.users[user]))
        else:
            print('There is no such user. Operation failed.')
   

    def subscribe(self, user, channel):
        if user in self.users:
            if channel in self.channels:
                self.users[user].append(channel)
                print('Success')
            else:
                print('There is no such channel. Operation failed.')
        else:
            print('There is no such user. Operation failed.')

    def unsubscribe(self, user, channel):
        if user in self.users:
            if channel in self.users[user]:
                self.users[user].remove(channel) 
                print('Success')
            else:
                print('User does not subscribe this channel. Operation failed.')
        else:
            print('There is no such user. Operation failed.')

if __name__ == '__main__':
    channels = {'channel1':['content1'], 'channel2':['content2'],'channel3':['content3']}
    users = {'user1':[],'user2':[]}
    data = subscribtion(channels, users)    
    print(f"Input action in following order: user action channel.\nActions allowed: {', '.join(subscribtion.allowedactions)}")
    while True:
        line = sys.stdin.readline()    
        if line:
            line = line[:-1]
            action = line.split(" ")
            data.handler(action)
        else:                          
            break