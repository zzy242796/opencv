# import serial

# ser = None  # 初始化ser变量

# try:
#     ser = serial.Serial('COM10', 115200, timeout=1)
#     hex_data = '1A'
#     byte_data = bytes.fromhex(hex_data)
#     ser.write(byte_data)
# except serial.SerialException as e:
#     print(f"Error: {e}")
# # finally:
# #     ser.close()
# incoming_data = ser.readline()
# print(incoming_data)




import serial

try:
    # 配置串口
    ser = serial.Serial('COM9', 115200, timeout=1)
    
    # 发送数据
    # ser.write(b'12')
    ser.write(b' ')
    
    # 接收数据
    incoming_data = ser.readline()
    print(incoming_data)
    
except serial.SerialException as e:
    print(f"串口错误: {e}")
except FileNotFoundError:
    print("指定的串口文件未找到，请检查串口号是否正确。")
except Exception as e:
    print(f"发生错误: {e}")
finally:
    # 确保串口被关闭
    if 'ser' in locals() and ser:
        ser.close()