SELECT
  aset_id,
  kategori,
  nilai_perolehan,
  umur_ekonomis,
  metode,
  ROUND(nilai_perolehan * 0.25, 2) AS depresiasi_tahun_pertama
FROM `PPh_Badan_Berbasis_BigQuerry.Aset_Tetap`
WHERE metode = 'saldo_menurun';