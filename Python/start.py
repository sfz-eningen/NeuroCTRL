#!/bin/python
import main
from main import *

rp = [20, int(rows)/2 + 10]
rpt = [int(columns)/2 - 20, int(rows)/2]
rp2 = [179/4 - 6,20]
asbt = [0, 0, 0, 0]

def fftprint():
    ffto, addr3 = sock_fft.recvfrom(8192) # buffer size is 1024 bytes
    fch0 = str(str(ffto).split(']')[0])[25:-1].split(',')
    fch1 = str(str(ffto).split(']')[1])[2:-1].split(',')
    fch2 = str(str(ffto).split(']')[2])[2:-1].split(',')
    fch3 = str(str(ffto).split(']')[3])[2:-1].split(',')
    avgfft = []
    for x in range(0, 124):
        avgfft.append(((float(fch0[x]) + float(fch1[x]) + float(fch2[x]) + float(fch3[x]))/4))
    # print(str(fch0) + str(len(fch0)))
    # print(str(fch1) + str(len(fch1)))
    # print(str(fch2) + str(len(fch2)))
    # print(str(fch3) + str(len(fch3)))

    fftt = str(ffto)[25:-8].split(',')
    ffft = [[], [], [], []]
    for x in range(1, len(fch0)):
        ffft[0].append(fch0)
        ffft[1].append(fch1)
        ffft[2].append(fch2)
        ffft[3].append(fch3)
    # sff()
    schr=12
    # print(wlin + str("Signals:" + str(len(fftt))).ljust(int(columns) - 5) + "\x1B[44m  \x1B[0m")
    # sff()
    strln = str(str("\x1B[44m\x1B[34m" + "#".ljust(4) + "\x1B[37mFreq.\x1B[34m" + "#".ljust(2) + "\x1B[37m" + "1 Hz".rjust(8) + "  " + str(str(schr) + " Hz").rjust(8)  + "  " + str(str(schr*2) + " Hz").rjust(8)  + "  " + str(str(schr*3) + " Hz").rjust(8)  + "  " + str(str(schr*4) + " Hz").rjust(8) + "  " + str(str(schr*5) + " Hz").rjust(8) + "  " + str(str(schr*6) + " Hz").rjust(8) + "  " + str(str(schr*7) + " Hz").rjust(8) + "  " + str(str(schr*8) + " Hz").rjust(8)  + "  " + str(str(schr*9) + " Hz").rjust(8) + "  " + str(str(schr*10) + " Hz").rjust(8) + "\x1B[44m\x1B[34m##"))
    # print(str(str("\x1B[44m\x1B[34m" + "#".ljust(11) + "\x1B[37m" + "1 Hz".rjust(8) + "  " + str(str(schr) + " Hz").rjust(8)  + "  " + str(str(schr*2) + " Hz").rjust(8)  + "  " + str(str(schr*3) + " Hz").rjust(8)  + "  " + str(str(schr*4) + " Hz").rjust(8) + "  " + str(str(schr*5) + " Hz").rjust(8) + "  " + str(str(schr*6) + " Hz").rjust(8) + "  " + str(str(schr*7) + " Hz").rjust(8) + "  " + str(str(schr*8) + " Hz").rjust(8)  + "  " + str(str(schr*9) + " Hz").rjust(8) + "  " + str(str(schr*10) + " Hz").rjust(8) + "\x1B[44m\x1B[34m##")).ljust(int(columns ) + 25))
    sgnstr = str(w2 + w2 + w2 + w2 + bb + "FFTs" + "\x1B[44m\x1B[34m###\x1B[0m " + str(ffc(0, avgfft)) + w3 +  str(ffc(1*schr - 1, avgfft)) + w3 +   str(ffc(2*schr - 1, avgfft)) + w3 + str(ffc(3*schr - 1, avgfft)) + w3 + str(ffc(4*schr - 1, avgfft)) + w3 + str(ffc(5*schr - 1, avgfft)) + w3 + str(ffc(6*schr - 1, avgfft))  + w3 + str(ffc(7*schr - 1, avgfft))  + w3 + str(ffc(8*schr - 1, avgfft))  + w3 + str(ffc(9*schr - 1, avgfft)) + w3 + str(ffc(10*schr - 1, avgfft)) + " \x1B[0m")
    # print(sgnstr.ljust(int(columns) + 1))
    bll=0
    for x in range(0, int(rows)):
        for y in range(0, int(columns)):
                pcco(y+1, x+1, "\x1B[44m ")

    dv = "\x1B[37m\x1B[44m\x1B[1m\x1B[2m"
    stfft = [30, 3]
    drawAll()
    wtf = 0
    focs = ""
    asbt = [0, 0, 0, 0]

    while True:
        # DATA WORK #
        ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
        bnd, addr = sock_bnd.recvfrom(1024)
        formf = ts[22:-4]
        ch = str(formf).split(',')
        cu = [time.time(), float(ch[0][2:-4].replace("E-", "")), float(ch[1][0:-1].replace("E-", "")), float(ch[2][0:-1].replace("E-", "")), float(ch[3][0:-2].replace("E-", ""))]
        ffto, addr3 = sock_fft.recvfrom(8192) # buffer size is 1024 bytes
        fch0 = str(str(ffto).split(']')[0])[25:-1].split(',')
        fch1 = str(str(ffto).split(']')[1])[2:-1].split(',')
        fch2 = str(str(ffto).split(']')[2])[2:-1].split(',')
        fch3 = str(str(ffto).split(']')[3])[2:-1].split(',')
        avgfft = []
        for x in range(0, 124):
            avgfft.append(((float(fch0[x]) + float(fch1[x]) + float(fch2[x]) + float(fch3[x]))/4))
        fftt = str(ffto)[25:-8].split(',')
        ffft = [[], [], [], []]
        for x in range(1, len(fch0)):
            ffft[0].append(float(fch0[x-1]))
            ffft[1].append(float(fch1[x-1]))
            ffft[2].append(float(fch2[x-1]))
            ffft[3].append(float(fch3[x-1]))
        # FOCUS #

        inc4 = [[], [], [], []]
        # ALPHA #
        alpha = [[0], [0], [0], [0]]
        lca = inc4
        hca = inc4
        freq = [7, 11]
        bcga = inc4
        asb = inc4
        asa = 0
        alpha[0] = avg(ffft[0][freq[0]:freq[1]])
        alpha[1] = avg(ffft[1][freq[0]:freq[1]])
        alpha[2] = avg(ffft[2][freq[0]:freq[1]])
        alpha[3] = avg(ffft[3][freq[0]:freq[1]])
        lca[0] = avg(ffft[0][freq[0] - 2:freq[0]])
        lca[1] = avg(ffft[1][freq[0] - 2:freq[0]])
        lca[2] = avg(ffft[2][freq[0] - 2:freq[0]])
        lca[3] = avg(ffft[3][freq[0] - 2:freq[0]])
        hca[0] = avg(ffft[0][freq[1]:freq[1] + 2])
        hca[1] = avg(ffft[1][freq[1]:freq[1] + 2])
        hca[2] = avg(ffft[2][freq[1]:freq[1] + 2])
        hca[3] = avg(ffft[3][freq[1]:freq[1] + 2])
        for x in range(0, 124):
            bcga[0] = avg([lca[0], hca[0]])
            bcga[1] = avg([lca[1], hca[1]])
            bcga[2] = avg([lca[2], hca[2]])
            bcga[3] = avg([lca[3], hca[3]])
        asb[0] = alpha[0]/bcga[0]
        asb[1] = alpha[1]/bcga[1]
        asb[2] = alpha[2]/bcga[2]
        asb[3] = alpha[3]/bcga[3]
        asa = avg(alpha) - avg([avg(asb), avg(asbt)])
        asbt = inc4
        asbt[0] = asb[0]
        asbt[1] = asb[1]
        asbt[2] = asb[2]
        asbt[3] = asb[3]
        aous = asa - 0.3
        if aous > 0:
            alpdout = 1
        else:
            alpdout = 0

        # BETA #
        lcb = inc4
        hcb = inc4
        freq = [15, 29]
        bcgb = inc4
        bsb = inc4
        bsa = 0
        beta = [[0], [0], [0], [0]]
        beta[0] = avg(ffft[0][freq[0]:freq[1]])
        beta[1] = avg(ffft[1][freq[0]:freq[1]])
        beta[2] = avg(ffft[2][freq[0]:freq[1]])
        beta[3] = avg(ffft[3][freq[0]:freq[1]])
        lcb[0] = avg(ffft[0][freq[0] - 2:freq[0]])
        lcb[1] = avg(ffft[1][freq[0] - 2:freq[0]])
        lcb[2] = avg(ffft[2][freq[0] - 2:freq[0]])
        lcb[3] = avg(ffft[3][freq[0] - 2:freq[0]])
        hcb[0] = avg(ffft[0][freq[1]:freq[1] + 2])
        hcb[1] = avg(ffft[1][freq[1]:freq[1] + 2])
        hcb[2] = avg(ffft[2][freq[1]:freq[1] + 2])
        hcb[3] = avg(ffft[3][freq[1]:freq[1] + 2])
        for x in range(0, 124):
            bcgb[0] = avg([lcb[0], hcb[0]])
            bcgb[1] = avg([lcb[1], hcb[1]])
            bcgb[2] = avg([lcb[2], hcb[2]])
            bcgb[3] = avg([lcb[3], hcb[3]])
        bsb[0] = beta[0]/bcgb[0]
        bsb[1] = beta[1]/bcgb[1]
        bsb[2] = beta[2]/bcgb[2]
        bsb[3] = beta[3]/bcgb[3]
        bsa = avg(alpha) - avg([avg(asb), avg(asbt)])
        bsbt = inc4
        bsbt[0] = asb[0]
        bsbt[1] = asb[1]
        bsbt[2] = asb[2]
        bsbt[3] = asb[3]
        bous = bsa - 0.3
        if bous > 0:
            blpdout = 1
        else:
            blpdout = 0
        # FOCUS #
        if (asa >= 0.7) and (asa <= 2.0) and (bsa <= 0.7) and (bsa >= 0):
            focout = 1
            focstri = "\x1B[32mFocused!\x1B[36m".rjust(28)
            focPi = "\x1B[32m⏿\x1B[36m"
            drawCaseEff([69, int(int(rows)/2 + 8)], [42, 12], "\x1B[32m\x1B[44m\x1B[1m\x1B[2m")
        else:
            focout = 0
            focstri = "\x1B[31mNot Focused!\x1B[36m".rjust(28)
            focPi = "\x1B[31m⏳\x1B[36m"
            drawCaseEff([69, int(int(rows)/2 + 8)], [42, 12], "\x1B[31m\x1B[44m\x1B[1m\x1B[2m")
        pcco(85, int(int(rows)/2 + 14), focstri + " " + focPi)
        # DES #
        # BAND #
        band0 = []
        band1 = []
        band2 = []
        band3 = []
        band  = []
        bands = str(bnd)[31:-8].split(']')
        band0s = bands[0].split(',')
        band1s = bands[1][2:-1].split(',')
        band2s = bands[2][2:-1].split(',')
        band3s = bands[3][2:-1].split(',')
        for x in range(0, 5):
            band0.append(float(band0s[x]))
            band1.append(float(band1s[x]))
            band2.append(float(band2s[x]))
            band3.append(float(band3s[x]))
        deltab = [band0[0], band1[0], band2[0], band3[0]]
        thetab = [band0[1], band1[1], band2[1], band3[1]]
        alphab = [band0[2], band1[2], band2[2], band3[2]]
        betab  = [band0[3], band1[3], band2[3], band3[3]]
        gammab = [band0[4], band1[4], band2[4], band3[4]]
        deltav = avg(deltab)
        thetav = avg(thetab)
        alphav = avg(alphab)
        betav  = avg(betab)
        gammav = avg(gammab)

        band.append(band0)
        band.append(band1)
        band.append(band2)
        band.append(band3)
        bandavg = [deltav, thetav, alphav, betav, gammav]

        pcco(85, int(int(rows)/2 + 16), str(round(alphav * 100)/100).rjust(20) + " ")
        pcco(85, int(int(rows)/2 + 17), str(round(betav * 100)/100).rjust(20) + " ")
        # DISPLAY #
        if (betav <= 0.7) and (betav >= 0.0) and (alphav <= 2.0) and (alphav >= 0.7):
            focstr = "\x1B[32mFocused!\x1B[36m".rjust(28)
            focP = "\x1B[32m⏿\x1B[36m"
            drawCaseEff([70, int(int(rows)/2 + 9)], [40, 10], "\x1B[32m\x1B[44m\x1B[1m\x1B[2m")
        else:
            focstr = "\x1B[31mNot Focused!\x1B[36m".rjust(28)
            focP = "\x1B[31m⏳\x1B[36m"
            drawCaseEff([70, int(int(rows)/2 + 9)], [40, 10], "\x1B[31m\x1B[44m\x1B[1m\x1B[2m")
        pcco(85, int(int(rows)/2 + 12), focstr + " " + focP)
        # DESIGN WORK #
        pcco(rp2[0] + 1, rp2[1] - 2,str(wlin + red + str(cu[1]).rjust(col_width) + " "  + wlin + hbl + str(cu[2]).rjust(col_width) + " " + wlin + red + str(cu[3]).rjust(col_width) + " "  + wlin + hbl + str(cu[4]).rjust(col_width) + " " + "\x1B[44m"))
        pcco(stfft[0], stfft[1] + 4, strln)
        sgnstr = str(w2 + w2 + w2 + w2 + bb + "FFTs" + "\x1B[44m\x1B[34m###\x1B[0m " + str(ffc(0, avgfft)) + w3 +  str(ffc(1*schr - 1, avgfft)) + w3 +   str(ffc(2*schr - 1, avgfft)) + w3 + str(ffc(3*schr - 1, avgfft)) + w3 + str(ffc(4*schr - 1, avgfft)) + w3 + str(ffc(5*schr - 1, avgfft)) + w3 + str(ffc(6*schr - 1, avgfft))  + w3 + str(ffc(7*schr - 1, avgfft))  + w3 + str(ffc(8*schr - 1, avgfft))  + w3 + str(ffc(9*schr - 1, avgfft)) + w3 + str(ffc(10*schr - 1, avgfft)) + " \x1B[44m")
        pcco(stfft[0], stfft[1]+5, sgnstr)
        wtf = wtf + 1
        #if wtf>30:
        #    drawAll()
        #    wtf = 0
        #pcco(2, 20, " \n \n \n ")
        pcco(5, 20, "          ")
        pcco(5, 20, "")


fftprint()
