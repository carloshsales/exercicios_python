# Faça um programa que peça o tamanho de um arquivo para 
# download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

file_size = float(input("informe o tamanho do arquivo (MB): "))
link_speed = float(input("informe a velocidade do link (Mbps): "))

def download_time(fs, ls):
    speed = ls / 8
    size = 0
    minutes = 0
    seconds = 0
    time = 0
    while size < fs:
        size += speed
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1
    
    time = f"Tempo estimado - {minutes} : {seconds}"

    return time

print(download_time(file_size, link_speed))