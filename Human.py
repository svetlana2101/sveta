class Human:

    default_name = "no name"
    default_age = 0

    def__init__(self,name=default_name,age=default_age):
        seif.name = name
        self.age = age
        self.__money = 0
        self.__house = None

  #  @property
   # def money(self):
    #    return self.__money

    #@property
 #   def house(self):
 #       return self.__house

  #  @money.setter
  #  def money(self,value):
   #     self.__money=value

  #  @house.setter
   # def house(self,value):
    #    self.__house=value
    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money:{self.money}")
        print(f"House:{self.house}")

    @staticmethod                      #5 punkt
    def default_info():
        print(f"Default Name:{Human,default_name}")
        print(f"Default Age:{Human,default_age}")

     def__make_deal(self,house,price):
        self.__money = price
        self.__house = house

     def earn_money(self,total):
         self.__money += total
         print(f"Y:{total}")

    def buy_house(self,house,discount):
        price = house.finel_price(discount)
        if self.__money >= price
            self.__make_deal(house, price)
        else:
            print("nedostatochno sredstv"){finel_price}")
        return finel_price





