from opcodes import opcodes

# CPU16 Class
class CPU16:
    # Initializes all the variables
    def __init__(self):
        # Data Registers
        self.reg_A = 0
        self.reg_B = 0
        self.reg_C = 0

        # Memory
        self.instructionMemory = [0] * 65536
        self.dataMemory = [0] * 65536
        self.callStack = [0] * 256

        # Counters
        self.pc = 0

        # Other Registers
        self.reg_instruction = 0
        self.reg_memoryAddress = 0
        self.reg_input = 0
        self.reg_output = 0
        self.reg_stackPointer = 0

        # Flags
        self.flags_zero = False
        self.flags_carry = False
        self.flags_negative = False
        self.flags_lesser = False
        self.flags_equal = False
        self.flags_greater = False

        # States
        self.halt = False

        #I/O
        self.io_device_signal_a = False
        self.io_device_signal_b = False
        self.io_output_port = False #False = Port 1; True = Port 2
        self.io_input_port = False #False = Port 1; True = Port 2

    # Sets the flags
    def setFlags(self, result):
        self.flags_zero = (result == 0)
        self.flags_carry = (result == 0x10000)
        self.flags_negative = (result & 0x8000) != 0

        self.flags_lesser = self.reg_A < self.reg_B
        self.flags_equal = self.reg_A == self.reg_B
        self.flags_greater = self.reg_A > self.reg_B

    # Fetch Cycle Fucntion
    def fetch_cycle(self):
        self.reg_instruction = self.instructionMemory[self.pc]

        if self.pc == 0xFFFF:
            self.pc = 0
        else:
            self.pc += 1

    # Execution Cycle Function
    def execute_cycle(self):
        opcodes(self)
        
        self.constrain()

    # Contrains all registers to their correspoinding bit size
    def constrain(self):
        self.reg_A = self.reg_A & 0xFFFF #16 bits
        self.reg_B = self.reg_B & 0xFFFF #16 bits
        self.reg_C = self.reg_C & 0xFFFF #16 bits
        self.reg_instruction = self.reg_instruction & 0xFFFFFF #24 bits
        self.reg_memoryAddress = self.reg_memoryAddress & 0xFFFF #16 bits
        self.reg_input = self.reg_input & 0xFFFF #16 bits
        self.reg_output = self.reg_output & 0xFFFF #16 bits
        self.reg_stackPointer = self.reg_stackPointer & 0xFF #8 bits

    # Updates the CPU
    def update(self):
        self.fetch_cycle()
        self.execute_cycle()