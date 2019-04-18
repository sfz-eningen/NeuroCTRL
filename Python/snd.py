 
UDP_IP = "192.168.178.108"
UDP_PORT_TSS = 56571
UDP_PORT_FOC = 56572
UDP_PORT_FFT = 56573
sock_tss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_foc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_fft = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_tss.bind((UDP_IP, UDP_PORT_TSS))
sock_foc.bind((UDP_IP, UDP_PORT_FOC))
sock_fft.bind((UDP_IP, UDP_PORT_FFT))

ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
foc, addr2 = sock_foc.recvfrom(1024)
formf = ts[22:-4]
ch = str(formf).split(',')
cu = [time.time(), float(ch[0][2:-1]), float(ch[1]), float(ch[2]), float(ch[3][0:-1])]
sleep(.004)
sys.stdout.write(wlin + red + str(cu[1]).ljust(col_width) + wlin + hbl + str(cu[2]).ljust(col_width) + wlin + red + str(cu[3]).ljust(col_width) + wlin + hbl + str(cu[4]).ljust(col_width) + wlin + str(str(foc)[25:-7]).ljust(4) + wlin + "\n")
