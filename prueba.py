from datetime import datetime


ahora = datetime.now()

print(f"\nAño => {ahora.year}")
print(f"Mes => {ahora.month:02}")
print(f"Día => {ahora.day:02}")

print("\ndd/mm/yy hh:mm:ss\n"\
      "{0:02}/{1:02}/{2} {3:02}:{4:02}:{5:02}\n"\
        .format(ahora.day, ahora.month, ahora.year,
                ahora.hour % 12, ahora.minute, ahora.second))

if (ahora.second % 2):
    print("\n\tSEGUNDO IMPAR!! D:\n")
    print(f"{ahora.second} % 2 = {ahora.second % 2}")
else:
    print("\n\tSEGUNDO PAR!! :D\n")
    print(f"{ahora.second} % 2 = {ahora.second % 2}")