class Counter:
    current = 0
    def __int__(self,start=None,end=None):
        self.start = start
        self.end = end
       # print(self.current)
       # print(self.start)
       # print(self.end)
    def increase(self):# функция по умолчанию ничего не возвращает
        if self.current < self.end:
            self.current += 1
            return self.current # чтобы счетчик работал нужно возвращать значение
        else:
            return 'out of range'
        my_count = Counter(start=0,end=3)
        print(my_count.increase())# 1
        print(my_count.increase())# 2
        print(my_count.increase())# 3
        print(my_count.increase())# 'out of range'