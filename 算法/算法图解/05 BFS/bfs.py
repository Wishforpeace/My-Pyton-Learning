from collections import deque

def person_is_seller(name):
    return name[-1]=='m'

graph={}
graph["you"]=["alice","bob","claire"]
graph["alice"]=["peggy"]
graph["bob"]=["anuj"]
graph["claire"]=["thom","jonny"]
graph["peggy"]=[]
graph["anuj"]=[]
graph["thom"]=[]
graph["jonny"]=[]

def bfs(name):
    search_queue = deque()
    search_queue += [name]

    searched = set()
    while search_queue:
        person = search_queue.popleft()

        if person in searched:
            continue
        if person_is_seller(person):
            print(person+" is a mango seller")
            return True

        search_queue += graph[person]

        searched.add(person)
    return False

bfs("you")
