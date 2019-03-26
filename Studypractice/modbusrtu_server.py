import sys

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial

PORT = 0


# PORT = '/dev/ptyp5'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

    # Create the server
    server = modbus_rtu.RtuServer(serial.Serial(PORT))  # 建立串口为PORT的从机

    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")

        server.start()

        slave1 = server.add_slave(1)  # 添加地址为1的从机
        slave1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)  # 在从机中添加块名为0的起始地址0，长度100内存块，类型为3(cst.HOLDING_REGISTERS)

        # add 2 blocks of holding registers
        slave1.add_block('a', cst.HOLDING_REGISTERS, 0, 100)  # address 0, length 100
        slave1.add_block('b', cst.HOLDING_REGISTERS, 200, 20)  # address 200, length 20

        # create another slave with id 2
        slave2 = server.add_slave(2)
        slave2.add_block('c', cst.COILS, 0, 100)
        slave2.add_block('d', cst.HOLDING_REGISTERS, 0, 100)

        # set the values of registers at address 0
        slave1.set_values('a', 0, range(100))

        while True:
            cmd = sys.stdin.readline()  # 以下代码是用来输入终端命令：建立从机，建立内存块，设置内存值，读取内存值
            args = cmd.split(' ')

            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break

            elif args[0] == 'add_slave':  # 示例 add_slave 3
                slave_id = int(args[1])
                server.add_slave(slave_id)
                sys.stdout.write('done: slave %d added\r\n' % (slave_id))

            elif args[0] == 'add_block':  # 示例 add_block 3 hold 3 0 3
                slave_id = int(args[1])  # 从机地址
                name = args[2]  # block块名
                block_type = int(args[3])  # 块的寄存器读写类型
                starting_address = int(args[4])  # 内存起始地址
                length = int(args[5])  # 长度
                slave = server.get_slave(slave_id)
                slave.add_block(name, block_type, starting_address, length)
                sys.stdout.write('done: block %s added\r\n' % (name))

            elif args[0] == 'set_values':  # 示例 set_values 3 hold 0 1 2 3
                slave_id = int(args[1])  # 从机地址
                name = args[2]  # block块名
                address = int(args[3])  # 内存地址
                values = []
                for val in args[4:]:  # 设置内存值
                    values.append(int(val))
                slave = server.get_slave(slave_id)
                slave.set_values(name, address, values)
                values = slave.get_values(name, address, len(values))
                sys.stdout.write('done: values written: %s\r\n' % (str(values)))

            elif args[0] == 'get_values':
                slave_id = int(args[1])  # 从机地址
                name = args[2]  # block块名
                address = int(args[3])  # 内存地址
                length = int(args[4])  # 长度
                slave = server.get_slave(slave_id)  # 获取内存值
                values = slave.get_values(name, address, length)
                sys.stdout.write('done: values read: %s\r\n' % (str(values)))

            else:
                sys.stdout.write("unknown command %s\r\n" % (args[0]))
    finally:
        server.stop()


if __name__ == "__main__":
    main()
