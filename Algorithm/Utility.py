
class Utility:

    def annagram(self,var_str1,var_str2):
        var_nospace_str1=var_str1.replace(" ","")
        var_nospace_str2=var_str2.replace(" ","")
        if(len(var_nospace_str1) != len(var_nospace_str2)):
            return False
        else:
            var_lower_str1=var_nospace_str1.lower()
            var_lower_str2=var_nospace_str2.lower()

            char_array_1=list(var_lower_str1)
            char_array_2=list(var_lower_str2)

            char_array_1.sort()
            char_array_2.sort()

            for x in range(0,len(char_array_1)):
                if(char_array_1[x]!= char_array_2[x]):
                    return False

            return True

    def primenumber(self,var_range):
        my_array=[None]*var_range
        j=0
        for x in range(1,var_range+1):
            count=0
            for num in range(1,x+1):
                if(x%num==0):
                    count=count+1
            if(count==2):
                my_array[j]=x
                j=j+1
        return my_array

    def extend_annagram(self,prime_array):
        var_size=0
        var_j=0
        for x in  range(0,len(prime_array)):
            if(prime_array[x]!=None):
                var_size=var_size+1

        my_array=[None]*var_size
        for x in range(0,len(prime_array)):
            if (prime_array[x] != None):
                my_array[var_j]=prime_array[x]
                var_j=var_j+1
                print(str(prime_array[x])+" "),
        print ("\n")
        var_str1=""
        var_str2=""
        for x in range(0,len(my_array)-1):
            for y in range(x+1,len(my_array)):
                var_str1=my_array[x]
                var_str2=my_array[y]
                flag=self.annagram(str(var_str1),str(var_str2))
                if(flag):
                    print(str(my_array[x])+" "+str(my_array[y]))

    def palindrome(self,prime_array):
        var_size = 0
        var_j = 0
        for x in range(0, len(prime_array)):
            if (prime_array[x] != None):
                var_size = var_size + 1

        my_array = [None] * var_size
        for x in range(0, len(prime_array)):
            if (prime_array[x] != None):
                my_array[var_j] = prime_array[x]
                var_j = var_j + 1
                print(str(my_array[x]) + " "),
        print ("\n")

        for x in range(0,len(my_array)):
            # var_remainder=0
            # var_sum=0
            # var_temp=my_array[x]
            # while(my_array[x]>0):
            #     var_remainder == my_array[x]%10
            #     print(var_remainder)
            #     var_sum = (var_sum * 10) + var_remainder
            #     print(var_sum)
            #     my_array[x] = my_array[x]/10
            #     print(my_array[x])
            var_temp=str(my_array[x])
            if(var_temp == var_temp[::-1]):
                print(str(var_temp)+" palindrome")
            else:
                print(str(var_temp)+" is not a palindrome")