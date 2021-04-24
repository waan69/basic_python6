nilai_teori = int(input('Masukan Nilai Teori: '))
nilai_praktek = int(input('Masukan Nilai Praktek: '))

if nilai_teori >= 70:
  if (nilai_praktek >= 70):
        print('Selamat Anda Lulus')
  else:
        print('Anda Harus Mengulang Ujian Praktek')
else:
  if nilai_praktek >= 70:
    if (nilai_teori >= 70):
        print('Selamat ANda Lulus')
    else:
        print('Anda Harus Mengulang Ujian Teori')

