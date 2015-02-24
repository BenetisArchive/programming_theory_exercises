__author__ = 'Tautvydas Vaitieku\'nas IFF-2/7'
import datetime
import array

class UglyNumbers:
    def getUglyNumberSlow(self, position ):
        pradzia=datetime.datetime.utcnow();
        current = 0;
        counter = 0;
        while counter < position:
            current = current + 1
            tmp = current
            while tmp % 2 == 0:
                tmp = tmp / 2
            while tmp % 3 == 0:
               tmp = tmp / 3
            while tmp % 5 == 0:
               tmp = tmp / 5
            if tmp == 1:
                counter = counter + 1
        pabaiga=datetime.datetime.utcnow();
        print pabaiga-pradzia;
        print "Slow number ", current;
        return 1;

    def getUglyNumberFast(self, input ):
        pradzia=datetime.datetime.utcnow();
        sk1 = 2
        sk2 = 3
        sk3 = 5
        a = 0
        b = 0
        c = 0
        uglyNo = array.array('i',(0 for i in range(0,input)))
        input = input - 1;
        uglyNo[input] = 0
        uglyNo[0] = 1
        index = 1

        while uglyNo[input] == 0:
            if sk1 < sk2 and sk1 < sk3:
                uglyNo[index] = sk1
                a = a + 1;
                sk1 = uglyNo[a]*2
                index = index + 1
            elif sk2 < sk1 and sk2 < sk3:
                uglyNo[index] = sk2
                b = b + 1
                sk2 = uglyNo[b]*3
                index = index + 1
            elif sk3 < sk1 and sk3 < sk2:
                uglyNo[index] = sk3;
                c = c + 1
                sk3=uglyNo[c]*5;
                index = index + 1
            if sk1 == sk2:
                a = a + 1
                sk1 = uglyNo[a]*2
            elif sk2 == sk3:
                b = b + 1
                sk2 = uglyNo[b]*3;
            elif sk3 == sk1:
                c = c + 1
                sk3 = uglyNo[c]*5;

        pabaiga=datetime.datetime.utcnow()
        print "The", input + 1, "'th ugly number is", uglyNo[input], "."
        print pabaiga-pradzia
        return 1

Rezultatas = UglyNumbers();
Rezultatas.getUglyNumberFast(1500);
