# -*- coding: utf-8 -*-
class Line:
    def __init__(self,num,line):
        self.num=num
        self.line=line
    
    def setNum(self,num):
        self.num=num
    
    def setLine(self,line):
        self.line=line

    def getNum(self):
        return self.num

    def getLine(self):
        return self.line
    