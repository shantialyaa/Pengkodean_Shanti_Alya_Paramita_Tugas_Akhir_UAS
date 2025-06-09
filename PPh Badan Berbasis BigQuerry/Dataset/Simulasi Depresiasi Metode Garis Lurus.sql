SELECT
  aset_id,
  kategori,
  nilai_perolehan,
  umur_ekonomis,
  metode,
  nilai_perolehan / umur_ekonomis AS depresiasi_tahunan
FROM PPh_Badan_Berbasis_BigQuerry.Aset_Tetap
WHERE metode = 'garis_lurus';