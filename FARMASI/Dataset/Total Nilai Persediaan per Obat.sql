SELECT 
  Obat,
  Kode_Obat,
  SUM(Unit) AS Total_Unit,
  SUM(Total_Harga_Pokok) AS Total_Harga_Pokok,
  SUM(Total_Harga_Jual) AS Total_Harga_Jual
FROM 
  `pharmacy_dataset.persediaan_farmasi_2023`
GROUP BY 
  Obat, Kode_Obat
ORDER BY 
  Total_Harga_Pokok DESC;