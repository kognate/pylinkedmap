class LinkedMap:

    def __init__(self, startv=None):
        self.__head = None
        self.__tail = None
        self.__map = {}

        if startv is not None:
            if isinstance(startv, list):
                for pair in startv:
                    self[pair[0]] = pair[1]
            else:
                print(type(startv))
                error = "Argument {} is not a list of pairs".format(startv)
                raise ValueError(error)

    def first(self):
        return (self.__head, self.__map[self.__head]['v'])

    def last(self):
        return (self.__tail, self.__map[self.__tail]['v'])

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__map.clear()

    def __setitem__(self, key, item):
        if self.__head is None:
            self.__head = key
            self.__tail = key
            self.__map[key] = dict(v=item, next=None, prev=None)
        elif key in self.__map:
            oldv = self.__map[key]
            oldv['v'] = item
            self.__map[key] = oldv
        else:
            old_tail = self.__tail
            self.__map[key] = dict(v=item, next=None, prev=old_tail)
            self.__map[old_tail]['next']=key
            self.__tail = key

    def __getitem__(self, key):

        if key in self.__map:
            return self.__map[key]['v']
        else:
            return None

    def __iter__(self):
        k = self.__head
        while k:
            f = self.__map[k]
            yield (k, f['v'])
            k = f['next']

    def __reversed__(self):
        k = self.__tail
        while k:
            f = self.__map[k]
            yield (k, f['v'])
            k = f['prev']
            
    def next_for(self, key):
        if key in self.__map:
            return self.__map[key]['next']

    def prev_for(self, key):
        if key in self.__map:
            return self.__map[key]['prev']

    def __delitem__(self, key):
        if key in self.__map:
            old_item = self.__map[key]
            del self.__map[key]
            if self.__head == key:
                self.__head = old_item['next']
            if self.__tail == key:
                self.__tail = old_item['prev']

            if old_item['next'] == None:
                self.__map[old_item['prev']]['next'] = None
            else:
                self.__map[old_item['prev']]['next'] = old_item['next']
                self.__map[old_item['next']]['prev'] = old_item['prev']
        
    def __len__(self):
        return len(self.__map)
