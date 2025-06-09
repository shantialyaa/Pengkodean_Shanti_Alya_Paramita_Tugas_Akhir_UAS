SELECT 
  j.Obat,
  j.Kode_Obat,
  SUM(j.Unit) AS Total_Unit_Terjual,
  SUM(j.Total_Harga_Jual) AS Total_Harga_Jual,
  SUM(j.Unit * p.Harga_Pokok_Pembelian) AS Total_Harga_Pokok,
  SUM(j.Total_Harga_Jual - (j.Unit * p.Harga_Pokok_Pembelian)) AS Margin_Keuntungan
FROM 
  `pharmacy_dataset.penjualan_obat_rawat_jalan_2023` j
JOIN 
  `pharmacy_dataset.persediaan_farmasi_2023` p
ON 
  j.Kode_Obat = p.Kode_Obat
GROUP BY 
  j.Obat, j.Kode_Obat
ORDER BY 
  Margin_Keuntungan DESC;