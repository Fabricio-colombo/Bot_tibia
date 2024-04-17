import ctypes

# Define o PID (identificador do processo) do processo alvo
pid = 16324  # Substitua pelo PID do processo alvo

# Obtém um handle para o processo alvo
process_handle = ctypes.windll.kernel32.OpenProcess(0x10, False, pid)  # 0x10 é o acesso de leitura no Windows

# Define o endereço de memória que queremos ler/escrever
address = 0x01234567  # Substitua pelo endereço de memória desejado no processo alvo

# Define o buffer para armazenar os dados lidos da memória
buffer = ctypes.create_string_buffer(4)  # 4 bytes para ler um inteiro (32 bits)

# Função para ler a memória do processo
def read_process_memory(address):
    bytes_read = ctypes.c_ulong(0)
    ctypes.windll.kernel32.ReadProcessMemory(process_handle, address, buffer, ctypes.sizeof(buffer), ctypes.byref(bytes_read))
    value = ctypes.c_int.from_buffer(buffer)
    return value.value

# Função para escrever na memória do processo
def write_process_memory(address, value):
    value_to_write = ctypes.c_int(value)
    ctypes.windll.kernel32.WriteProcessMemory(process_handle, address, ctypes.byref(value_to_write), ctypes.sizeof(value_to_write), None)

# Lê um valor na memória do processo
value_read = read_process_memory(address)
print("Valor lido na memória:", value_read)

# Escreve um novo valor na memória do processo
new_value = 9999  # Valor a ser escrito na memória
write_process_memory(address, new_value)
print("Novo valor escrito na memória")

# Fecha o handle do processo
ctypes.windll.kernel32.CloseHandle(process_handle)
