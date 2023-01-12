class BinarySearch():

    def search_iterative(self,list,item):

        low = 0
        high = len(list)-1

        while low <= high:
            mid = (low+high)//2
            guess = list[mid]

            if guess == item:
                return mid
            if guess < item:
                    low = mid+1
            if guess > item:
                    high = mid-1
        return Non


    def search_recursive(self,list,low,high,item):
        if high >= low:
            mid = (low+high)//2
            guess = list[mid]
            if guess == item:
                return mid
            elif guess > item:
                return self.search_recursive(list,low,mid-1,item)
            else:
                return self.search_recursive(list,mid+1,high,item)
            
        else:
            return None

if __name__ == "__main__":
    bs = BinarySearch()
    my_list = [1,3,5,7,9]

    print(bs.search_iterative(my_list,3))

    print(bs.search_recursive(my_list,0,len(my_list)-1,7))
