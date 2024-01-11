Hello. THis is my 16 bit computer project.
This is a project created in Visual Studio Code, and i advise to use it to run the code.
But if you want to use this project with another text editor or IDE. Then remove the .vscode, and only run the main.py file if that is possible.
The specifications of the CPU are:
16 bit data.
16 bit address (Data Memory and Instruction Memory).
24 bit or 3 byte Instructions with this format: 0xOOPPPP O = opcode p = parameter.
Is multi cycle.
C Register is mainly for Dynamic Memory, where the register is the address.
A and B Register are hard wired to the ALU
Has a total of 128 opcodes
Has a Call Stack seperate to the Data Memory, of which the Call Stack is 256 levels deep.
The Opcodes.py file is where the Opcodes function resides. The Opcodes were put into their seperate file due to the need for a clean way of doing the code.
The Opcodes function basically just checks which opcode to run, and runs it.
Program.py is where the program, is stored. Was modularized also for clean appearance.
Memory.py is the initial Data Memory. It is basically what values you want in your Data Memory when starting the computer.
cpu_log.txt is how you can see what the CPU is doing. it records every state of the CPU after every instruction. Making it useful to debug.
But if you chose to disable the log. It will instead print the final state of the Computer, aka halt state to the terminal.
opcodes.txt is where you will find all the opcodes and their corresponding opcode number.
otherDevices.py was an attempt to create a screen, external drive, and keyboard I/O devices. But ultimetly left out due to the need to have a working CPU first.