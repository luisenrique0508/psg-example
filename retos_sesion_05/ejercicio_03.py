# convertir 1000000 segundos en semanas, días, horas, minutos y segundos

seg_total = 1000000

seg_sem = 7 * 24 * 60 * 60
num_sem = seg_total // seg_sem
resto_seg = seg_total - (num_sem * seg_sem)

seg_dia = 24 * 60 * 60
num_dia = resto_seg // seg_dia
resto_seg = resto_seg - (num_dia * seg_dia)

seg_hr = 60 * 60
num_hr = resto_seg // seg_hr
resto_seg = resto_seg - (num_hr * seg_hr)

seg_min = 60
num_min = resto_seg // seg_min
seg_fin = resto_seg - (num_min * seg_min)
print(f"Los {seg_total} segundos son:")
print(f"{num_sem} semanas, {num_dia} días, {num_hr} horas, {num_min} minutos y {seg_fin} segundos")
