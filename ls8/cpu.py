"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.running = True

        self.branch_table = {
            0b10000010: self.LDI,
            0b01000111: self.PRN,
            0b00000001: self.HLT,
            0b10100010: self.MUL
        }

    # Should accept the address to read and return the value
    def ram_read(self, address):
        return self.ram[address]

    # Should accept an address and value and store the value at that address
    def ram_write(self, address, value):
        self.ram[address] = value

    def LDI(self):
        index = self.ram[self.pc + 1]
        value = self.ram[self.pc + 2]
        self.reg[index] = value
        self.pc += 3

    def PRN(self):
        value = self.reg[self.ram[self.pc + 1]]
        print(value)
        self.pc += 2

    def HLT(self):
        self.running = False

    def MUL(self):
        reg_a = self.ram[self.pc + 1]
        reg_b = self.ram[self.pc + 2]
        self.alu('MUL', reg_a, reg_b)

    def load(self, fileName):
        """Load a program into memory."""
        address = 0
        with open(fileName) as file:
            for line in file:
                line = line.split('#')
                try:
                    instruction = int(line[0], 2)
                    self.ram[address] = instruction
                    address += 1
                except ValueError:
                    continue
                    
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
            self.pc += 3
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
            self.pc += 3
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while self.running:
            ir = self.ram[self.pc]
            try:
                self.branch_table[ir]()
            except:
                raise Exception(f"Unknown instruction: {self.ram[self.pc]}")
            # if self.ram[self.pc] == HLT:
            #     running = False
            # elif self.ram[self.pc] == PRN:
            #     value = self.reg[self.ram[self.pc + 1]]
            #     print(value)
            #     self.pc += 2
            # elif self.ram[self.pc] == LDI:
            #     index = self.ram[self.pc + 1]
            #     value = self.ram[self.pc + 2]
            #     self.reg[index] = value
            #     self.pc += 3
            # else:
            #     raise Exception(f"Unknown instruction: {self.ram[self.pc]}")
            


        
