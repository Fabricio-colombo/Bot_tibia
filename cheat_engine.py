import ctypes

# PID do processo do jogo
pid = 15708

# Endereço de memória da vida
address = 0x015112D8

# Novo valor de vida
new_health = 1000

# Obtém um handle para o processo do jogo
process_handle = ctypes.windll.kernel32.OpenProcess(0x10, False, pid)  # 0x10 é o acesso de leitura no Windows

# Cria um objeto ctypes.c_int com o novo valor de vida
new_health_ctypes = ctypes.c_int(new_health)

# Escreve o novo valor na memória do processo
ctypes.windll.kernel32.WriteProcessMemory(process_handle, address, ctypes.byref(new_health_ctypes), ctypes.sizeof(new_health_ctypes), None)

# Fecha o handle do processo
ctypes.windll.kernel32.CloseHandle(process_handle)
