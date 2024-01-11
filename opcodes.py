from random import randint
from time import sleep

# Opcodes Fucntion
def opcodes(cpu):

    # Transforms the raw instruction into an opcode
    opcode = (cpu.reg_instruction & 0xFF0000) >> 16
    parameter = (cpu.reg_instruction & 0x00FFFF)

    # The Opcodes
    if opcode == 0x01: #LDA
        cpu.reg_memoryAddress = parameter
        cpu.reg_A = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x02: #LDB
        cpu.reg_memoryAddress = parameter
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x03: #LDC
        cpu.reg_memoryAddress = parameter
        cpu.reg_C = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x04: #LDA_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_A = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x05: #LDB_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x06: #LDC_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_C = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x07: #STA
        cpu.reg_memoryAddress = parameter
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_A

    if opcode == 0x08: #STB
        cpu.reg_memoryAddress = parameter
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_B

    if opcode == 0x09: #STC
        cpu.reg_memoryAddress = parameter
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_C

    if opcode == 0x0a: #STA_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_A

    if opcode == 0x0b: #STB_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_B

    if opcode == 0x0c: #STC_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_C

    if opcode == 0x0d: #STI
        cpu.dataMemory[cpu.reg_memoryAddress] = parameter

    if opcode == 0x0e: #IDA
        cpu.reg_A = parameter

    if opcode == 0x0f: #IDB
        cpu.reg_B = parameter

    if opcode == 0x10: #IDC
        cpu.reg_C = parameter

    if opcode == 0x11: #ATB
        cpu.reg_B = cpu.reg_A

    if opcode == 0x12: #ATC
        cpu.reg_C = cpu.reg_A

    if opcode == 0x13: #BTA
        cpu.reg_A = cpu.reg_B

    if opcode == 0x14: #BTC
        cpu.reg_C = cpu.reg_B

    if opcode == 0x15: #CTA
        cpu.reg_A = cpu.reg_C

    if opcode == 0x16: #CTB
        cpu.reg_B = cpu.reg_C

    if opcode == 0x17: #PCA
        cpu.reg_A = cpu.pc

    if opcode == 0x18: #PCB
        cpu.reg_B = cpu.pc

    if opcode == 0x19: #PCC
        cpu.reg_C = cpu.pc

    if opcode == 0x1a: #PUSHA
        cpu.callStack[cpu.reg_stackPointer] = cpu.reg_A
        cpu.reg_stackPointer += 1

    if opcode == 0x1b: #PUSHB
        cpu.callStack[cpu.reg_stackPointer] = cpu.reg_B
        cpu.reg_stackPointer += 1

    if opcode == 0x1c: #PUSHC
        cpu.callStack[cpu.reg_stackPointer] = cpu.reg_C
        cpu.reg_stackPointer += 1

    if opcode == 0x1d: #PUSHI
        cpu.callStack[cpu.reg_stackPointer] = parameter
        cpu.reg_stackPointer += 1

    if opcode == 0x1e: #PUSHM
        cpu.reg_memoryAddress = parameter
        cpu.callStack[cpu.reg_stackPointer] = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_stackPointer += 1

    if opcode == 0x1f: #PUSHM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.callStack[cpu.reg_stackPointer] = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_stackPointer += 1

    if opcode == 0x20: #POPA
        cpu.reg_stackPointer -= 1
        cpu.reg_A = cpu.callStack[cpu.reg_stackPointer]
        cpu.callStack[cpu.reg_stackPointer] = 0

    if opcode == 0x21: #POPB
        cpu.reg_stackPointer -= 1
        cpu.reg_B = cpu.callStack[cpu.reg_stackPointer]
        cpu.callStack[cpu.reg_stackPointer] = 0

    if opcode == 0x22: #POPC
        cpu.reg_stackPointer -= 1
        cpu.reg_C = cpu.callStack[cpu.reg_stackPointer]
        cpu.callStack[cpu.reg_stackPointer] = 0

    if opcode == 0x23: #POPM
        cpu.reg_memoryAddress = parameter
        cpu.reg_stackPointer -= 1
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.callStack[cpu.reg_stackPointer]
        cpu.callStack[cpu.reg_stackPointer] = 0

    if opcode == 0x24: #POPM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_stackPointer -= 1
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.callStack[cpu.reg_stackPointer]
        cpu.callStack[cpu.reg_stackPointer] = 0

    if opcode == 0x25: #ADD
        cpu.reg_A = cpu.reg_A + cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x26: #SUB
        cpu.reg_A = cpu.reg_A - cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x27: #MUL
        cpu.reg_A = cpu.reg_A * cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x28: #DIV
        cpu.reg_A = cpu.reg_A // cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x29: #MOD
        cpu.reg_A = cpu.reg_A % cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2a: #SHL
        cpu.reg_A = cpu.reg_A << cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2b: #SHR
        cpu.reg_A = cpu.reg_A >> cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2c: #AND
        cpu.reg_A = cpu.reg_A & cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2d: #OR
        cpu.reg_A = cpu.reg_A | cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2e: #XOR
        cpu.reg_A = cpu.reg_A ^ cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x2f: #CMP
        cpu.setFlags(0)

    if opcode == 0x30: #ADDI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A + cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x31: #SUBI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A - cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x32: #MULI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A * cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x33: #DIVI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A // cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x34: #MODI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A % cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x35: #SHLI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A << cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x36: #SHRI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A >> cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x37: #ANDI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A & cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x38: #ORI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A | cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x39: #XORI
        cpu.reg_B = parameter
        cpu.reg_A = cpu.reg_A ^ cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x3a: #CMPI
        cpu.reg_B = parameter
        cpu.setFlags(0)

    if opcode == 0x3b: #ADD_NA
        cpu.reg_C = cpu.reg_A + cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x3c: #SUB_NA
        cpu.reg_C = cpu.reg_A - cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x3d: #MUL_NA
        cpu.reg_C = cpu.reg_A * cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x3e: #DIV_NA
        cpu.reg_C = cpu.reg_A // cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x3f: #MOD_NA
        cpu.reg_C = cpu.reg_A % cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x40: #SHL_NA
        cpu.reg_C = cpu.reg_A << cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x41: #SHR_NA
        cpu.reg_C = cpu.reg_A >> cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x42: #AND_NA
        cpu.reg_C = cpu.reg_A & cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x43: #OR_NA
        cpu.reg_C = cpu.reg_A | cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x44: #XOR_NA
        cpu.reg_C = cpu.reg_A ^ cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x45: #RNG
        cpu.reg_A = randint(0, 0xFFFF)

    if opcode == 0x46: #ADDM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A + cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x47: #SUBM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A - cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x48: #MULM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A * cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x49: #DIVM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A // cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4a: #MODM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A % cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4b: #SHLM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A << cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4c: #SHRM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A >> cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4d: #ANDM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A & cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4e: #ORM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A | cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x4f: #XORM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.reg_A = cpu.reg_A ^ cpu.reg_B
        cpu.setFlags(cpu.reg_A)

    if opcode == 0x50: #CMPM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_B = cpu.dataMemory[cpu.reg_memoryAddress]
        cpu.setFlags(0)

    if opcode == 0x51: #JMP
        cpu.pc = parameter

    if opcode == 0x52 & cpu.flags_zero == True: #JMZ
        cpu.pc = parameter

    if opcode == 0x53 & cpu.flags_carry == True: #JMC
        cpu.pc = parameter

    if opcode == 0x54 & cpu.flags_negative == True: #JMN
        cpu.pc = parameter

    if opcode == 0x55 & cpu.flags_lesser == True: #JML
        cpu.pc = parameter

    if opcode == 0x56 & cpu.flags_equal == True: #JME
        cpu.pc = parameter

    if opcode == 0x57 & cpu.flags_greater == True: #JMG
        cpu.pc = parameter

    if opcode == 0x58: #JMPL
        cpu.reg_B = cpu.pc
        cpu.pc = parameter

    if opcode == 0x59 & cpu.flags_zero == False: #JMNZ
        cpu.pc = parameter

    if opcode == 0x5a & cpu.flags_carry == False: #JMNC
        cpu.pc = parameter

    if opcode == 0x5b & cpu.flags_negative == False: #JMNN
        cpu.pc = parameter

    if opcode == 0x5c & cpu.flags_lesser == False: #JMGE
        cpu.pc = parameter

    if opcode == 0x5d & cpu.flags_equal == False: #JMNE
        cpu.pc = parameter

    if opcode == 0x5e & cpu.flags_greater == False: #JMLE
        cpu.pc = parameter

    if opcode == 0x5f: #JMP_D
        cpu.pc = cpu.reg_C

    if opcode == 0x60 & cpu.flags_zero == True: #JMZ_D
        cpu.pc = cpu.reg_C

    if opcode == 0x61 & cpu.flags_carry == True: #JMC_D
        cpu.pc = cpu.reg_C

    if opcode == 0x62 & cpu.flags_negative == True: #JMN_D
        cpu.pc = cpu.reg_C

    if opcode == 0x63 & cpu.flags_lesser == True: #JML_D
        cpu.pc = cpu.reg_C

    if opcode == 0x64 & cpu.flags_equal == True: #JME_D
        cpu.pc = cpu.reg_C

    if opcode == 0x65 & cpu.flags_greater == True: #JMG_D
        cpu.pc = cpu.reg_C

    if opcode == 0x66: #JMPL_D
        cpu.reg_B = cpu.pc
        cpu.pc = cpu.reg_C

    if opcode == 0x67 & cpu.flags_zero == False: #JMNZ_D
        cpu.pc = cpu.reg_C

    if opcode == 0x68 & cpu.flags_carry == False: #JMNC_D
        cpu.pc = cpu.reg_C

    if opcode == 0x69 & cpu.flags_negative == False: #JMNN_D
        cpu.pc = cpu.reg_C

    if opcode == 0x6a & cpu.flags_lesser == False: #JMGE_D
        cpu.pc = cpu.reg_C

    if opcode == 0x6b & cpu.flags_equal == False: #JMNE_D
        cpu.pc = cpu.reg_C

    if opcode == 0x6c & cpu.flags_greater == False: #JMLE_D
        cpu.pc = cpu.reg_C

    if opcode == 0x6d: #DV0
        cpu.io_device_signal_a = False
        cpu.io_device_signal_b = False

    if opcode == 0x6e: #DV1
        cpu.io_device_signal_a = True
        cpu.io_device_signal_b = False

    if opcode == 0x6f: #DV2
        cpu.io_device_signal_a = False
        cpu.io_device_signal_b = True

    if opcode == 0x70: #DV3
        cpu.io_device_signal_a = True
        cpu.io_device_signal_b = True

    if opcode == 0x71: #OUTA
        cpu.reg_output = cpu.reg_A

    if opcode == 0x72: #OUTB
        cpu.reg_output = cpu.reg_B

    if opcode == 0x73: #OUTA
        cpu.reg_output = cpu.reg_C

    if opcode == 0x74: #OUTM
        cpu.reg_memoryAddress = parameter
        cpu.reg_output = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x75: #OUTM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.reg_output = cpu.dataMemory[cpu.reg_memoryAddress]

    if opcode == 0x76: #DLY
        sleep(parameter / 1000)

    if opcode == 0x77: #INA
        cpu.reg_A = cpu.reg_input

    if opcode == 0x78: #INB
        cpu.reg_B = cpu.reg_input

    if opcode == 0x79: #INA
        cpu.reg_B = cpu.reg_input

    if opcode == 0x7a: #INM
        cpu.reg_memoryAddress = parameter
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_input

    if opcode == 0x7b: #INM_D
        cpu.reg_memoryAddress = cpu.reg_C
        cpu.dataMemory[cpu.reg_memoryAddress] = cpu.reg_input

    if opcode == 0x7c: #DLY_D
        sleep(cpu.reg_C / 1000)

    if opcode == 0x7d: #OUTPS
        if cpu.io_output_port == False:
            cpu.io_output_port = True
        else:
            cpu.io_output_port = False

    if opcode == 0x7e: #INPS
        if cpu.io_input_port == False:
            cpu.io_input_port = True
        else:
            cpu.io_input_port = False

    if opcode == 0x7F: #Halt
        cpu.halt = True