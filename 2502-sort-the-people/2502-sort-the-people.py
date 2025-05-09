class Solution(object):
    def sortPeople(self, names, heights):
        people=[]
        person={}
        for i in range(len(names)):
            person[heights[i]]=names[i]
        for i in sorted(person,reverse=True):
            people.append(person[i])
        return people