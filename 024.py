cidade = input('Em qual cidade você nasceu? ').strip()
if cidade[:5].upper() == 'SANTO':
    print(True)
else:
    print(False)