N = input("Please enter your name: ")
HW = int(input("Please enter your hours worked: "))
HR = int(input("Please enter your hourly rate: "))

print("")
print("P A Y S L I P")
print("Name: " + N)
print("Hours worked: " + str(HW) + " hours")
print("Hourly rate: ₱" + "{:.2f}".format(HR))

def BasicPay(HW, HR):
    if HW >= 160:
        BP= HR * 160
    else:
        BP= HR * HW
    return BP
BP1 = BasicPay(HW, HR)
print("Basic Pay: ₱" + "{:.2f}".format(BP1))

def Overtime(HW):
    print("")
    print("Note: Regular work hours are 160 per month. Any hours beyond this are automatically counted as overtime.")

    if HW > 160:
        OT= HW - 160
    else:
        OT= 0
    return OT

OT1 = Overtime(HW)
print("")
print("Overtime: " + str(OT1))

def OvertimePay(HR, OT1):
    if OT1 > 0:
        OTP= (HR * 1.25) * OT1
    else:
        OTP = 0
    return OTP

OTP1 = OvertimePay(HR, OT1)
print("Overtime Pay: ₱" + "{:.2f}".format(OTP1))

def PhHealth(BP1):
    PH = BP1 * 0.025
    return PH

PH1 = PhHealth(BP1)
print("")
print("CONTRIBUTIONS")
print("PhilHealth: ₱" + "{:.2f}".format(PH1))

def HDMF(BP1):
    if BP1 <= 1500:
        H= BP1 * 0.01
    elif BP1 <= 5000 and BP1 > 1500:
        H= BP1 * 0.02
    else:
        H= 100
    return H

H1 = HDMF(BP1)
print("HDMF: ₱" + "{:.2f}".format(H1))

def SSS(BP1):
    if BP1 < 4250:
        MSC = 4250
    elif BP1 > 35000:
        MSC = 35000
    else:
        MSC = BP1
    SS = MSC * 0.045
    return SS

SS1 = SSS(BP1)
print("SSS: ₱" + "{:.2f}".format(SS1))

def TotalDeduct(PH1, H1, SS1):
    TD = PH1 + H1 + SS1
    return TD

print("Total Contribution: ₱" + "{:.2f}".format(TotalDeduct(PH1, H1, SS1)))

def GrossPay(BP1, PH1, H1, SS1):
    GP = BP1 - PH1 - H1 - SS1 + OTP1
    return GP

GP1 = GrossPay(BP1, PH1, H1, SS1)
print("")
print("Gross Pay: ₱" + "{:.2f}".format(GP1))

def WithTax(GP1):
    if GP1 <= 20832:
        T = 0
    elif GP1 >= 20833 and GP1 <= 33332:
        T = (GP1 - 20833) * 0.2
    elif GP1 >= 33333 and GP1 <= 66666:
        T = ((GP1 - 33333) * 0.25) + 2500
    elif GP1 >= 66667 and GP1 <= 166666:
        T = ((GP1 - 66667) * 0.3) + 10833.33
    elif GP1 >= 166667 and GP1 <= 666666:
        T = ((GP1 - 166667) * 0.32) + 40833.33
    else:
        T = ((GP1 - 666667) * 0.35) + 200833.33
    return T

T1 = WithTax(GP1)
print("Withholding Tax: ₱" + "{:.2f}".format(T1))

def NetPay(GP1, T1):
    NP = GP1 - T1
    return NP

print()
print("NET PAY: ₱" + "{:.2f}".format(NetPay(GP1, T1)))
