class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        import sys
        self.offers = {}
        self.amount = 0
        for i in range(len(needs)):
            self.amount += needs[i]*price[i]
        for i in special:
            if (not tuple(i[:-1]) in self.offers) or (self.offers[tuple(i[:-1])] > i[-1]):
                self.offers[tuple(i[:-1])] = i[-1]
        self.getMinPrice(needs, 0, price)
        return self.amount
            
    def getMinPrice(self, needs, more_sum, price):
        print needs, more_sum
        # apply all the discounts
        if sum(needs) == 0:
            if self.amount > more_sum:
                self.amount = more_sum
            return
        for offer, rate in self.offers.items():
            #print "need %s"%needs
            newneeds = []
            for index in range(len(needs)):   
                if needs[index] - offer[index] >= 0:   # if items do not become less than 0
                    newneeds.append(needs[index] - offer[index])
                else:
                    newneeds = []
                    break
            else:   # offer can be applied
                self.getMinPrice(newneeds, more_sum+rate, price)        
        for index in range(len(needs)):
            more_sum += (needs[index]*price[index])  
        if self.amount > more_sum:
            self.amount = more_sum
        return
            
