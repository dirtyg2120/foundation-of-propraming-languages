import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    # ================Test Random================

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_random_00(self):
        """Name"""
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_random_01(self):
        input = """ Var: x;
                    Function: fact
                        Parameter: n
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return n * fact (n - 1);
                            EndIf.
                        EndBody.

                    Function: main
                        Body:
                            x = 10;
                            fact (x);
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_random_02(self):
        """If statement"""
        input = """ Function: main
                        Body:
                            If n == 0 Then
                                Return 1;
                            Else
                                Return 2;
                            EndIf.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_random_03(self):
        """For statement"""
        input = """ Function: main
                        Body:
                            For (i = 0, i < 10, 2) Do
                                println(i);
                            EndFor.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_random_04(self):
        """While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            While (i < 10) Do
                                println(x);
                                i = i + 1;
                            EndWhile.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_random_05(self):
        """Do While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            Do
                                println(x);
                                i = i + 1;
                            While (i < 10) EndDo.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_random_06(self):
        """Continue statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            While (i < 10) Do
                                println(x);
                                i = i + 1;
                                Continue;
                            EndWhile.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_random_07(self):
        """For and If statement"""
        input = """ Function: main
                        Body:
                            For (i = 0, i < 10, 2) Do
                                If (i % 2 == 0) Then
                                    println("Chan");
                                ElseIf (i % 2 != 0) Then
                                    println("Le");
                                EndIf.
                            EndFor.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_random_08(self):
        """COntinue in While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            While (i < 10) Do
                                If (i % 2 == 0) Then
                                    Continue;
                                EndIf.
                                println(x);
                                i = i + 1;
                            EndWhile.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_random_09(self):
        """Break in Do While statement"""
        input = """ Var: i=0, x;
                    Function: main
                        Body:
                            x = 100;
                            Do
                                println(x);
                                i = i + 1;
                                If (i == 8) Then
                                    Break;
                                EndIf.
                            While (i < 10) EndDo.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_random_10(self):
        """Var array"""
        input = """ Var: i=0, x;
                    Var: a[5] = {1,4,3,2,0};
                    Var: b[2][3]={{1,2,3},{4,5,6}};
                    Function: main
                        Body:
                            x = 100;
                            Do
                                println(x);
                                i = i + 1;
                                If (i == 8) Then
                                    Break;
                                EndIf.
                            While (i < 10) EndDo.
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_random_11(self):
        """Var Boolean"""
        input = """ Var: tmp0 = True, tmp1 = False, tmp2;
                    Function: main
                        Body:
                            tmp2 = tmp0;
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_random_12(self):
        """Working with Boolean"""
        input = """ Var: tmp0 = True, tmp1 = False, tmp2;
                    Function: main
                        Body:
                            tmp0 = !tmp0;
                            tmp2 = tmp0 || !tmp1;
                            tmp1 = tmp2 && !tmp2;
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_random_13(self):
        """Working with String"""
        input = """ Var: s;
                    Function: main
                        Body:
                            s = "This is a string containing tab \t";
                        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_random_14(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4];
                Body:
                    
                EndBody.
        """
        expect = "Error on line 3 col 50: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_random_15(self):
        input = """
            Function: foo
                Parameter: a , v
                Body:
                    x++;
                EndBody.
        """
        expect = "Error on line 5 col 21: +"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_random_16(self):
        input = """
            Function: foo
                Parameter: a , v
                Body:
                    Return foo;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_random_17(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i + a = 123;
                EndBody.
        """
        expect = "Error on line 5 col 27: +"
        self.assertTrue(TestParser.checkParser(input, expect, 219))


# ================Test Variable================

    def test_var_00(self):
        input = """
            Var: a = 5;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_var_01(self):
        input = """
            Var: b[2][3] = {{2,3,4},{4,5,6}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_var_02(self):
        input = """
            Var: c, d = 6, e, f;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_var_03(self):
        input = """
            Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_var_04(self):
        input = """
            Var: a = 5;
            Var: b[2][3] = {{2,3,4},{4,5,6}};
            Var: c, d = 6, e, f;
            Var: m, n[10];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_var_05(self):
        input = """
            Var: a[5] = {1,4,3,2,0};
            Var: b[2][3]={{1,2,3},{4,5,6}};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_var_06(self):
        input = """
            Var: a=1, b= 6, c= 7, d=a+b-c;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_var_07(self):
        input = """
            Var: v , a[1][2][4] , b = 6 ;
            Var: b = 7, v;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_var_08(self):
        input = """
            Var: a = 4 * 4;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_var_10(self):
        input = """
            Var: lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at."
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

# ================Test Assignment================
    def test_assignment_00(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    i = 0;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_assignment_01(self):
        input = """
            Var: a, c, d, m;
            Function: foo
                Parameter: a, c, d, m
                Body:
                    Var: b[2][3], n[10];
                    a = 5;
                    b[2][3] = {{2,3,4},{4,5,6}};
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_assignment_02(self):
        input = """
            Function: foo
                Body:
                    Var: boo;
                    boo = !!!True + False;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_assignment_03(self):
        input = """
            Function: foo
                Parameter: a , v , lst[10]
                Body:
                    Var: i = 10;
                    lst[i * a + v] = a;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_assignment_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2
                Body:
                    Var: boo;
                    boo = !(tmp1 || !!tmp2) && tmp0;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_assignment_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = tmp1 + lst[tmp1 - 2 * tmp1];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_assignment_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    lst[0] = tmp0;
                    lst[2] = tmp1;
                    lst[4] = lst[0 % tmp0]
                EndBody.
        """
        expect = "Error on line 8 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_assignment_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = p[];
                EndBody.
        """
        expect = "Error on line 5 col 29: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_assignment_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 == tmp1;
                EndBody.
        """
        expect = "Error on line 5 col 25: =="
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_assignment_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, lst[10]
                Body:
                    tmp0 = tmp1 = lst[0];
                EndBody.
        """
        expect = "Error on line 5 col 32: ="
        self.assertTrue(TestParser.checkParser(input, expect, 239))

# ================Test If statement================
    def test_if_00(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_if_01(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_if_02(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_if_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If (tmp0 == 1) || (tmp0 == 2) Then println("tmp0 = 1 or 2");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_if_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    If (tmp0 == 1) && (tmp1 != 1) Then println("tmp0 == 1 & tmp1 != 1");
                    ElseIf (tmp0 != 1) && (tmp1 == 1) Then println("tmp0 != 1 & tmp1 = 1");
                    Else println("IDK");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_if_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 = 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = "Error on line 5 col 28: ="
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_if_07(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1")
                    Else println("tmp0 != 1 & tmp1 != 1");
                    EndIf.
                EndBody.
        """
        expect = "Error on line 7 col 20: Else"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_if_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If tmp0 == 1 Then println("tmp0 = 1");
                    Else println("tmp0 != 1 & tmp1 != 1");
                    ElseIf tmp1 == 1 Then println("tmp1 = 1")
                    EndIf.
                EndBody.
        """
        expect = "Error on line 7 col 20: ElseIf"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_if_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    If (tmp0 == 1) && (tmp1 != 1) Then println("tmp0 == 1 & tmp1 != 1");
                    ElseIf (tmp0 != 1) && (tmp1 <> 1) Then println("tmp0 != 1 & tmp1 = 1");
                    Else println("IDK");
                    EndIf.
                EndBody.
        """
        expect = "Error on line 6 col 49: >"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

# ================Test For statement================

    def test_for_00(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_for_01(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_for_02(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, 2) Do
                        For (j = 0, j < 10, 2) Do
                            writeln(i + j);
                        EndFor.
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_for_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , i < tmp0 * tmp1 , tmp2[4]) Do
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_for_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_for_05(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        If i % 2 == 0 Then Continue;EndIf.
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_for_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[10]
                Body:
                    Var: i, tmp = 1;
                    For(i = tmp0 + tmp1 , (i < tmp0 * tmp1) || (i != tmp0 * tmp0), tmp2[4]) Do
                        If i % 2 == 0 Then Continue;
                        ElseIf (i == tmp0 * 2) || (i == tmp1 * 2) Then Break; 
                        EndIf.
                        tmp = tmp * i;
                    EndFor.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_for_07(self):
        input = """
            Function: foo
                Body:
                    For (i = 0, i < 10, 2)
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = "Error on line 5 col 24: writeln"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_for_08(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i = 0, i < 10, i = i + 1) Do
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = "Error on line 5 col 42: ="
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_for_09(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    For (i == 0, i < 10, 2) Do
                        writeln(i);
                    EndFor.
                EndBody.
        """
        expect = "Error on line 5 col 27: =="
        self.assertTrue(TestParser.checkParser(input, expect, 259))

# ================Test while statement================

    def test_while_00(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        writeln(i);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_while_01(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0, j;
                    While i < 10 Do
                        For (j = i, j < 10, i) Do
                            writeln(j);
                        EndFor.
                        i = i + 1;
                   EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_while_02(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    While (i < 10) Do
                        Var: tmp = i * i;
                        writeln(tmp);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_while_03(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    While (i < 10) && i % 2 > 3 Do
                        Var: tmp = i * i;
                        writeln(tmp);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_while_04(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10)
                        writeln(i);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 5 col 20: While"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_while_05(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While Do
                        writeln(i);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 5 col 20: While"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_while_06(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        If i % 2 != 0 Then writeln(i);EndIf.
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_while_07(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        ;
                        writeln(i);
                        i = i + 1;
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 6 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_while_08(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        writeln(i);
                        Do
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 8 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_while_09(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    While (i < 10) Do
                        writeln(i);
                        EndWhile.
                    EndWhile.
                EndBody.
        """
        expect = "Error on line 8 col 20: EndWhile"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

# ================Test do while statement================

    def test_do_while_00(self):
        input = """
            Function: foo
                Body:
                    Var: i = 0;
                    Do
                        writeln(i);
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_do_while_01(self):
        input = """
            Function: foo
                Parameter: tmp0
                Body:
                    Var: i = 0;
                    Do
                        writeln(i);
                        If i == tmp0 Then Break;EndIf.
                        i = i + 1;
                    While i < 10 EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_do_while_02(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i,j;
                    Do 
                        writeln(i);
                        For(j = 2 , j < 10 , 1) Do
                            tmp = tmp + j;
                        EndFor.
                    While !True EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_do_while_03(self):
        input = """
            Function: foo
                Body:
                    Do some_thing();
                    While(!condition())
                    EndDo.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_do_while_04(self):
        input = """
            Function: foo
                Body:
                    Do func()
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = "Error on line 5 col 20: While"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_do_while_05(self):
        input = """
            Function: foo
                Body:
                    Do func();
                    While condition();
                    EndDo.
                EndBody.
        """
        expect = "Error on line 5 col 37: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_do_while_06(self):
        input = """
            Function: foo
                Body:
                    Do func();
                    condition()
                    EndDo.
                EndBody.
        """
        expect = "Error on line 6 col 20: EndDo"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_do_while_07(self):
        input = """
            Function: foo
                Body:
                    Do func();
                    While condition()
                EndBody.
        """
        expect = "Error on line 6 col 16: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_do_while_08(self):
        input = """
            Function: foo
                Body:
                    Do ;
                    While condition()
                    EndDo.
                EndBody.
        """
        expect = "Error on line 4 col 23: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_do_while_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    Do func();
                    While tmp0 = tmp1;
                    EndDo.
                EndBody.
        """
        expect = "Error on line 6 col 31: ="
        self.assertTrue(TestParser.checkParser(input, expect, 279))

# ================Test expression statement================

    def test_expression_00(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1[10]
                Body:
                    tmp0 = tmp0 + tmp1[9];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_expression_01(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    Var: tmp;
                    tmp = tmp0 + tmp1 - tmp0 * tmp1 + 1321312;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_expression_02(self):
        input = """
            Function: foo
                Parameter: a, b
                Body:
                    a[3 + foo(2)] = a[b[2][3]] + 4;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_expression_03(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1
                Body:
                    tmp0 = tmp1 && tmp0;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_expression_04(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    tmp0 = tmp1 || !tmp2[2];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_expression_05(self):
        input = """
            Function: foo
                Parameter: tmp[200]
                Body:
                    tmp [[ [][][]][];
                EndBody.
        """
        expect = "Error on line 5 col 25: ["
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_expression_06(self):
        input = """
            Function: foo
                Parameter: tmp
                Body:
                    Var: i           = .tmp;
                EndBody.
        """
        expect = "Error on line 5 col 39: ."
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_expression_07(self):
        input = """
            Function: foo
                Parameter: tmp
                Body:
                    Var: i;
                    i = .- tmp;
                    return i;
                EndBody.
        """
        expect = "Error on line 6 col 24: ."
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_expression_08(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i;
                    tmp0 = tmp2[0] * tmp1 + tmp2[1];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_expression_09(self):
        input = """
            Function: foo
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: tmp_0, tmp_1, tmp_2;
                    tmp_0 = tmp0;
                    tmp_1 = !(tmp1+tmp2[tmp0][tmp_0 * 3]);
                    tmp_2 = tmp_1 + tmp_0 * tmp2[tmp1][tmp0];
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))


# ================Test completed program================

    def test_program_00(self):
        input = """
            Var: x;
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
            Function: main
                Body:
                    x = 10;
                    fact (x);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_program_01(self):
        input = """
            Function: square
                Parameter: n
                Body:
                    Return n * n;
                EndBody.
            Function: main
                Body:
                    writeln(square(3));
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_program_02(self):
        input = """
            Function: fact
                Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else Return n * fact(n-1); 
                    EndIf.                   
                EndBody.
            ** This is a single-line comment. **
            ** This is a
            * multi-line
            * comment.
            **
            Function: main
                Body:
                    Var: fact_4;
                    fact_4 = fact(4);
                    printLn(a);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_program_03(self):
        input = """
            Function: sum
                Parameter: n
                Body:
                    Var: i , sum = 0;
                    For(i = 1 , i <= n , 1) Do
                        sum = sum + i;
                    EndFor.
                    Return sum;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_program_04(self):
        input = """
            Function: result
                Parameter: tmp0, tmp1, tmp2[12][4]
                Body:
                    Var: i = 1, result;
                    While i <= n Do
                        result = result * i;
                        i = i + 1;
                    EndWhile.
                    Return result;
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_program_05(self):
        input = """
            Function: foo
                Parameter: a 
                Body:
                    Var: i;
                    Return a*i;
                EndBody.
            Function: main
                Body:
                    Var: a = foo(z);
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_program_06(self):
        input = """
            Function: foo
                Parameter: a[5] , n
                Body:
                    Var: i, sum = 0;
                    For(i = 0 , i <= n, 1) Do
                        sum = sum + a[i];
                    EndFor.
                    Return sum;
                EndBody.
            Function: main
                Body
                    Var: a = 10;
                    xx = foo(a);
                    printLn(xx);
                EndBody.
        """
        expect = "Error on line 13 col 20: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_program_07(self):
        input = """
            Function: foo
                Body:
                    Var: i;
                    Return foo(i);
                EndBody.
            Function: main
                Body
                    Return foo(z)[123];
                EndBody.
        """
        expect = "Error on line 9 col 20: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_program_08(self):
        input = """
            Function: foo
                Parameter: n , a[expression]
                Body:
                    Return "Foo";
                EndBody.
        """
        expect = "Error on line 3 col 33: expression"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_program_09(self):
        input = """
            Function: foo
                Parameter: a[5] , n
                Body:
                    Var: i, result = 0;
                    For(i = 0, i < n , 1) Do
                        If(a[i] % 2 == 0) Then 
                            result = result + a[i];
                        EndIf.
                    EndFor.
                EndBody.
            Function: main
                Body:
                    Var: a[5] = {1,2,3,4,5} , result;
                    result = foo(a[5]);
                    printLn(x);
                EndBody.
                
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
