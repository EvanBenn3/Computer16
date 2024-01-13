from program import program
from memory import memory
from cpu16 import CPU16
from otherDevices import Screen
import time

# Initializes CPU and other devices
cpu = CPU16()
cpu.instructionMemory[:len(program)] = program
cpu.dataMemory[:len(memory)] = memory

display = Screen()

log = True
logDataMemoryRange = (0, 10)
logCallStackRange = (0, 10)
simSpeed = 100 # Speed that simulation runs at in iterations per second

executedInstructions = 0

with open("cpu_log.txt", "w") as log_file:

# Simulation Loop
    while cpu.halt == False:
        # Actual Simulation v
        cpu.update()
        executedInstructions += 1

        if cpu.io_output_port == False:
            if (cpu.io_device_signal_a == True) and (cpu.io_device_signal_b == False):
                display.pos = cpu.reg_output
            if (cpu.io_device_signal_a == False) and (cpu.io_device_signal_b == True):
                display.color = cpu.reg_output
            if (cpu.io_device_signal_a == True) and (cpu.io_device_signal_b == True):
                display.update()

        # print(cpu.io_device_signal_a, cpu.io_device_signal_b)
        
        display.root.update_idletasks()
        display.root.update()

        # Actual Simulation ^

        if log:
            # Logs
            log_file.write("Data Registers: A = {} | B = {} | C = {}\n".format(cpu.reg_A, cpu.reg_B, cpu.reg_C))
            log_file.write("Instruction Registers: Instructon = {} | Memory Address = {} | Stack Pointer = {}\n".format(hex(cpu.reg_instruction), cpu.reg_memoryAddress, cpu.reg_stackPointer))
            log_file.write("I/O Registers: Input = {} | Output = {}\n".format(cpu.reg_input, cpu.reg_output))
            log_file.write("Program Counter = {}\n".format(cpu.pc))
            log_file.write("Flags: Zero = {} | Carry = {} | Negative = {} | Lesser = {} | Equal = {} | Greater = {}\n".format(cpu.flags_zero, cpu.flags_carry, cpu.flags_negative, cpu.flags_lesser, cpu.flags_equal, cpu.flags_greater))
            log_file.write("Data Memory Addresses {}\n".format(logDataMemoryRange))
            for address in range(logDataMemoryRange[0], logDataMemoryRange[1] + 1):
                log_file.write(f"{cpu.dataMemory[address]}, ")
            log_file.seek(log_file.tell() - 2)
            log_file.truncate()
            log_file.write("\nCall Stack Levels {}\n".format(logCallStackRange))
            for level in range(logCallStackRange[0], logCallStackRange[1] + 1):
                log_file.write(f"{cpu.callStack[level]}, ")
            log_file.seek(log_file.tell() - 2)
            log_file.truncate()
            log_file.write("\n\n")

        #for simulation speed
        time.sleep(1 / simSpeed)

if log == False:
    print("Data Registers: A = {} | B = {} | C = {}".format(cpu.reg_A, cpu.reg_B, cpu.reg_C))
    print("Instruction Registers: Instructon = {} | Memory Address = {} | Stack Pointer = {}".format(hex(cpu.reg_instruction), cpu.reg_memoryAddress, cpu.reg_stackPointer))
    print("I/O Registers: Input = {} | Output = {}".format(cpu.reg_input, cpu.reg_output))
    print("Program Counter = {}".format(cpu.pc))
    print("Flags: Zero = {} | Carry = {} | Negative = {} | Lesser = {} | Equal = {} | Greater = {}".format(cpu.flags_zero, cpu.flags_carry, cpu.flags_negative, cpu.flags_lesser, cpu.flags_equal, cpu.flags_greater))
    print("Data Memory Addresses {}".format(logDataMemoryRange))
    for address in range(logDataMemoryRange[0], logDataMemoryRange[1] + 1):
        print(f"{cpu.dataMemory[address]}, ", end="")
    print("\nCall Stack Levels {}".format(logCallStackRange))
    for level in range(logCallStackRange[0], logCallStackRange[1] + 1):
        print(f"{cpu.callStack[level]}, ", end="")
    print("\n")

print(f"Computer halted after executing {executedInstructions} instructions with no issues.")

print("Computer Halted With No Issues")
