import random
import time


def ringLength(x):
    return int(pow(2, x))


class Node:
    """ Node Definition """

    def __init__(self, ip, m):
        self.id = self.generateId(ip=ip, m=m)
        self.fingerTable = self.generateFT(m=m)
        self.predecessor = self
        self.sucessor = self

    def generateId(self, ip, m):
        result = 0
        # random.seed(time.time())
        # print(type(ip))
        for ch in ip:
            # result = (result + ord(ch) + random.randint(1, 99)) % length
            result = (result + ord(ch)) % ringLength(m)
        return result

    def generateFT(self, m):
        result = {}
        for i in range(m):
            result[int(pow(2, i))] = self
        return result

    def updateFT(self, m, dht):
        for item in self.fingerTable:
            pointer = (item + self.id) % ringLength(m)
            for node in dht.getNodes():
                if node.isInBound(pointer, m):
                    self.fingerTable[item] = node
                    break

    def isInBound(self, pointer, m):
        # 每个节点负责的标识符范围，有三种情况
        # case 1 环中只有一个节点时
        if self.id == self.predecessor.getId():
            return True
        # case 2 前驱节点标识符较小
        elif self.id > self.predecessor.getId():
            if self.predecessor.getId() < pointer <= self.id:
                return True
        # case 3 前驱节点标识符较大
        elif self.id < self.predecessor.getId():
            if self.predecessor.getId() < pointer < ringLength(m):
                return True
            if pointer < self.id:
                return True
        else:
            return False

    def getSucessor(self):
        return self.sucessor

    def getPredecessor(self):
        return self.predecessor

    def setSuceesor(self, node):
        self.sucessor = node

    def setPredecessor(self, node):
        self.predecessor = node

    def getId(self):
        return self.id

    def getFT(self):
        return self.fingerTable


class DHT:
    """ 哈希表数据结构 """

    def __init__(self, fileName, m):
        self.nodeSet = {}
        firstNode = None
        for ip in open(fileName, 'r').readlines():
            node = Node(ip, m)
            if firstNode is None:
                firstNode = node
            self.joinToRing(firstNode, node, m)

    def joinToRing(self, curNode, wnode, m):
        if len(self.nodeSet) != 0:
            sucessor = self.searchSucessor(curNode, wnode, m)
            predecessor = sucessor.getPredecessor()

            wnode.setPredecessor(predecessor)
            wnode.setSuceesor(sucessor)
            sucessor.setPredecessor(wnode)
            predecessor.setSuceesor(wnode)

        self.nodeSet[wnode.getId()] = wnode
        self.updateNodesFT(m)

    def searchSucessor(self, curNode, wnode, m):
        if curNode.isInBound(wnode.getId(), m):
            return curNode
        else:
            dis = (wnode.getId() - curNode.getId() + ringLength(m)) % ringLength(m)
            # 寻找最大的 k 使得 2^k <= dis
            maxk = 0
            while ((2 ** maxk) <= dis): maxk += 1
            maxk -= 1
            return self.searchSucessor(curNode.getFT()[2 ** maxk], wnode, m)

    def updateNodesFT(self, m):
        for node in self.nodeSet:
            self.nodeSet[node].updateFT(m, self)

    def getNodes(self):
        return self.nodeSet.values()


class Test:
    """ 测试哈希表是否运行正常 """

    def __init__(self, fileName, m):
        self.dht = DHT(fileName, m)
        for node in self.dht.getNodes():
            print("I am node %d, My predecessor is node %d, and My sucessor is node %d"
                  % (node.getId(), node.getPredecessor().getId(), node.getSucessor().getId()))


if __name__ == "__main__":
    test = Test("data/IPAddressList.txt", 5)
